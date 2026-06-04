# OCH Email Guidelines

These rules apply to every OCH email. Always read `brand/OCH_brand.md` first.

---

## Brand Colors (Email-Safe)

| Role | Hex | Use |
|------|-----|-----|
| Background (body) | `#1C1C1C` | Page and section backgrounds |
| Background (container) | `#111111` | Email card |
| Background (footer) | `#161616` | Footer band |
| Amber Gold (primary accent) | `#C8860A` | CTAs, rules, labels, links, chips |
| Cream / Off-white | `#F2EBD9` | Headline text on dark |
| Body text | `#C8C2B4` | Paragraph copy on dark backgrounds |
| Muted text | `#888888` | Subheadings, meta, legal |
| Dark text (on amber CTA) | `#111111` | Button labels |
| Decorative rule | `#2E2E2E` | Subtle section dividers |

---

## Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Eyebrow label | Arial, Helvetica | 11–12px | Normal | `#C8860A` — ALL CAPS, letter-spacing: 3–4px |
| H1 / Beer name | Georgia, Times New Roman | 36–42px | Normal (use `<em>` for name) | `#F2EBD9` / name in `#C8860A` |
| H2 / Section head | Georgia | 20–24px | Normal | `#F2EBD9` |
| Body copy | Arial, Helvetica | 15–16px | Normal | `#C8C2B4`, line-height: 26px |
| CTA button | Arial, Helvetica | 14px | Bold | `#111111` — ALL CAPS, letter-spacing: 2px |
| Footer / legal | Arial | 11px | Normal | `#444444` |

**Stack order for fallbacks:** `Georgia, 'Times New Roman', serif` for display; `Arial, Helvetica, sans-serif` for body.

---

## Email Types

### 1. Beer Announcement (`beer_announcement.html`)
Use when dropping a new tap or seasonal release.

**Required variables to fill before sending:**

| Variable | Description | Example |
|----------|-------------|---------|
| `{{BEER_NAME}}` | Name of the beer | Canal Street Amber |
| `{{BEER_STYLE}}` | Style | American Amber Ale |
| `{{ABV}}` | ABV number only | 5.4 |
| `{{OPENING_COPY}}` | 2–3 sentence hook, OCH voice | "We've been sitting on this one…" |
| `{{TASTING_NOTES_COPY}}` | 1–2 sentences on flavor | "Toasty caramel malt upfront…" |
| `{{TASTING_NOTE_1–3}}` | Single flavor/aroma words | Caramel, Citrus Peel, Toasted Oak |
| `{{FOOD_PAIRING_COPY}}` | Short BBQ pairing line | "Our smoked brisket, a rack of ribs…" |
| `{{CTA_TEASER_LINE}}` | 1-sentence urgency line | "It's on tap now. Limited keg." |
| `{{CTA_URL}}` | Destination link | https://oldcityhallbbq.com/taplist |
| `{{CTA_BUTTON_LABEL}}` | Button text (≤4 words) | See the Tap List |
| `{{RESTAURANT_ADDRESS}}` | Street address | 238 W First St |
| `{{HOURS_SHORT}}` | Hours summary | Mon–Thu 11am–10pm · Fri–Sat 11am–11pm |
| `{{FACEBOOK_URL}}` | Facebook page URL | — |
| `{{INSTAGRAM_URL}}` | Instagram profile URL | — |
| `{{UNSUBSCRIBE_URL}}` | ESP unsubscribe link | — |
| `{{PRIVACY_URL}}` | Privacy policy URL | — |
| `{{YEAR}}` | Current year | 2026 |

**Hero image:** Replace the placeholder `src` with a hosted photo. Ideal: close-up of the filled pint glass or tap handle. Min width 1200px source, displayed at 600px.

**Logo:** Replace the placeholder `src` in the header with the hosted logo file URL.

---

## Voice Rules for Beer Emails

- Lead with the **story or setting**, not the spec sheet (ABV comes second, experience comes first).
- Write like Jim Walter would want to read it — no craft-beer pretension, no jargon.
- Short sentences. White space does the work.
- Never use the word "artisanal." Never say "we're excited to announce."
- One CTA per email. Don't dilute it.
- Pair the beer to food in every beer email — this is OCH, not a taproom-only operation.

### Example opening copy (use or adapt):
> "We brewed this one for the kind of night where the work week finally lets go. Light enough to drink two. Interesting enough that you'll want to."

### Example CTA teaser lines:
> "It's on tap now. Limited keg, no promises on how long it lasts."
> "Come grab a pint. We'll keep the fire going."
> "This one won't wait around. The tap list doesn't."

---

## Layout Rules

- Max container width: **600px**
- Side padding (desktop): **48px** | (mobile): **20px**
- Amber top rule: `6px` solid `#C8860A` directly below header
- Amber bottom rule: `4px` solid `#C8860A` above footer block
- Section dividers: `1px` dashed or solid `#2E2E2E`
- CTA button: `border-radius: 4px`, background `#C8860A`, padding `16px 36px`

---

## Image Specs

| Slot | Dimensions | Format | Notes |
|------|-----------|--------|-------|
| Logo | 260 × 60px | PNG (transparent) | Dark background version |
| Hero / beer photo | 1200 × 680px source | JPG | Displays at 600 × 340 |
| Secondary inline | 600 × 400px source | JPG | Optional, for event tie-ins |

All images must have descriptive `alt` text. Never rely on images alone to convey key info — Outlook will block them by default.

---

## ESP / Send Checklist

- [ ] All `{{VARIABLES}}` replaced — search for `{{` before sending
- [ ] Subject line written (≤50 chars, no emoji unless tested)
- [ ] Preview text set in ESP (do not leave blank — the `<div>` preheader is a fallback)
- [ ] Logo and hero image URLs live and load over HTTPS
- [ ] CTA URL tested and tracking params applied
- [ ] Unsubscribe link verified
- [ ] Sent a test to hammad@albertsgroup.net before deploy
- [ ] Mobile preview checked (Gmail app, Apple Mail)
