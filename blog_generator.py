#!/usr/bin/env python3
"""Generate a .docx from a blog post JSON payload. No third-party deps.

Usage:
    python blog_generator.py --json '{"slug": "...", "title": "...", "meta_description": "...", "body": "..."}'

`body` is markdown: paragraphs separated by blank lines, supporting
**bold** spans and [link text](https://...) links. Writes "<slug>.docx"
to the current directory and prints its path.
"""

import argparse
import json
import re
import zipfile
from xml.sax.saxutils import escape

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

INLINE_PATTERN = re.compile(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)|([^\[*]+|\*)")


def inline_runs(text, extra_rpr=""):
    runs = []
    for m in INLINE_PATTERN.finditer(text):
        bold, link_text, link_url, plain = m.groups()
        if bold is not None:
            runs.append(("text", bold, extra_rpr + "<w:b/>"))
        elif link_text is not None:
            runs.append(("link", link_text, link_url))
        elif plain:
            runs.append(("text", plain, extra_rpr))
    return runs


def run_xml(text, rpr):
    rpr_xml = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    return f'<w:r>{rpr_xml}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def paragraph_xml(text, rels, extra_rpr="", ppr=""):
    parts = []
    for kind, content, meta in inline_runs(text, extra_rpr):
        if kind == "text":
            parts.append(run_xml(content, meta))
        else:
            rid = f"rId{len(rels) + 2}"
            rels.append((rid, meta))
            parts.append(
                f'<w:hyperlink r:id="{rid}"><w:r><w:rPr><w:rStyle w:val="Hyperlink"/></w:rPr>'
                f'<w:t xml:space="preserve">{escape(content)}</w:t></w:r></w:hyperlink>'
            )
    return f"<w:p>{ppr}{''.join(parts)}</w:p>"


def heading_xml(text, level=1):
    size = {1: 32, 2: 28, 3: 24}.get(level, 24)
    return (
        f'<w:p><w:pPr><w:spacing w:after="200"/></w:pPr>'
        f'<w:r><w:rPr><w:b/><w:sz w:val="{size}"/></w:rPr>'
        f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'
    )


def body_paragraphs(markdown_body, rels):
    blocks = re.split(r"\n\s*\n", markdown_body.strip())
    xml_parts = []
    for block in blocks:
        block = block.strip()
        if not block or block == "---":
            continue
        heading_match = re.match(r"^(#{1,3})\s+(.*)$", block)
        if heading_match:
            xml_parts.append(heading_xml(heading_match.group(2), len(heading_match.group(1))))
        else:
            ppr = '<w:pPr><w:spacing w:after="200"/></w:pPr>'
            xml_parts.append(paragraph_xml(block, rels, ppr=ppr))
    return xml_parts


def build_document_xml(title, meta_description, body_md, rels):
    parts = [heading_xml(title, level=1)]
    meta_ppr = '<w:pPr><w:spacing w:after="300"/></w:pPr>'
    meta_text = f"Meta description: {meta_description}"
    parts.append(paragraph_xml(meta_text, rels, extra_rpr="<w:i/>", ppr=meta_ppr))
    parts.extend(body_paragraphs(body_md, rels))
    body_xml = "".join(parts)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
    {body_xml}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


def build_document_rels(rels):
    rel_xml = "".join(
        f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" Target="{escape(url)}" TargetMode="External"/>'
        for rid, url in rels
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {rel_xml}
</Relationships>
"""


STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="character" w:styleId="Hyperlink">
    <w:name w:val="Hyperlink"/>
    <w:rPr>
      <w:color w:val="0563C1"/>
      <w:u w:val="single"/>
    </w:rPr>
  </w:style>
</w:styles>
"""


def generate_docx(slug, title, meta_description, body_md, out_path):
    rels = []
    document_xml = build_document_xml(title, meta_description, body_md, rels)
    document_rels_xml = build_document_rels(rels)

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", ROOT_RELS)
        z.writestr("word/document.xml", document_xml)
        z.writestr("word/styles.xml", STYLES_XML)
        z.writestr("word/_rels/document.xml.rels", document_rels_xml)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    args = parser.parse_args()

    payload = json.loads(args.json)
    slug = payload["slug"]
    out_path = f"{slug}.docx"
    generate_docx(slug, payload["title"], payload["meta_description"], payload["body"], out_path)
    print(out_path)


if __name__ == "__main__":
    main()
