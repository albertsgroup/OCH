# OCH Weekly Backlink Scout

An automated weekly research task for **Old City Hall Barbecue & Brewery** (159 Water Street, Oswego, NY) — the only brewery and only BBQ restaurant in downtown Oswego.

## What it does

Every Monday, this automation:

1. **Researches** 8–12 realistic backlink opportunities for the week, prioritizing:
   - Oswego County Chamber of Commerce and business directories
   - Central New York tourism sites (I Love NY CNY region, Syracuse.com, Visit Oswego County)
   - SUNY Oswego community, alumni, or visitor-facing pages
   - Local news outlets covering Oswego (Palladium-Times, Oswego County Business, CNY Central)
   - Craft beer directories and blogs (Untappd venue listings, CNY craft beer trail guides, BeerAdvocate)
   - BBQ and food blogs covering Central New York or the Northeast
   - Wedding and event vendor directories (OCH caters private parties)
   - Local nonprofit or community event sponsor pages
   - "Best restaurants in Oswego" / "things to do in Oswego" roundup articles that don't yet mention OCH

2. **Vets each opportunity** for relevance (High / Medium / Low) and identifies the best contact method (email, contact form, or social handle).

3. **Drafts outreach messages** in the voice of Jim Walter, OCH's brand avatar — approachable, clever, a wink of Oswego humor, locally grounded, no em-dashes, no corporate language.

4. **Saves a dated report** to `/reports/backlink-report-[YYYY-MM-DD].md` with a table of opportunities sorted by relevance.

5. **Notifies** michelle@albertsgroup.net and hammad@albertsgroup.net by email with a summary and a link to the new report.

## What it does NOT do

- It does **not** send any outreach messages on OCH's behalf.
- It does **not** merge this branch into `main` (or the repo's default branch).

All reports are for manual human review — Michelle and Hammad decide which outreach to send and when.

## Folder structure

```
automation/backlink-scout/
├── README.md
└── reports/
    └── backlink-report-YYYY-MM-DD.md   (one per week)
```

## Schedule

- **Name:** OCH Weekly Backlink Scout
- **Repo:** albertsgroup/OCH
- **Branch:** automation/backlink-scout
- **Schedule:** Weekly, Monday
- **Notify:** michelle@albertsgroup.net, hammad@albertsgroup.net
