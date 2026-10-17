# OLESHKY — Humanitarian Access

Independent editorial pilot about humanitarian conditions in Oleshky, Ukraine. **Snapshot verified against linked reporting on 17 October 2026; not a live situation feed.** Not affiliated with UN, ICRC or government bodies. No donations collected.

## Publish free on GitHub Pages
1. Create a public GitHub repository named `oleshky-aid`.
2. Upload **the contents of this folder** (including `.github/`, `index.html`, `assets/`, `data/`, `scripts/`), not the enclosing folder.
3. Go to repository **Settings → Pages → Build and deployment → Deploy from a branch**, select `main` and `/ (root)`, save.
4. Wait for the Pages deployment. Your URL will be `https://YOUR-USERNAME.github.io/oleshky-aid/`.
5. Check all 8 languages and all links on a phone and desktop.
6. The site uses `fetch`, so to test locally run `python -m http.server 8000` from this directory and open `http://localhost:8000/`. Do not double-click index.html as a file.

## Content updates
- Edit `data/updates.json` with a dated, attributed, independently written summary and HTTPS source URL.
- Write translations for all eight languages or the site will fall back to English for missing entries. Review translations with a fluent speaker.
- Change the editorial-review date in `index.html` **only after actual review**, and change the stale-date constant in `assets/app.js` accordingly.
- Use a Pull Request and require another human reviewer for disputed or high-risk claims.
- `check-links.yml` runs every six hours but **only validates the structure of local data**, not the truth of news or whether links remain reachable. There is deliberately no automatic publication of scraped news.
- If a story is disputed, attribute the claim to the source; do not represent allegations as established facts. Keep a public correction log when updating published material.

## Editorial and safety policy
Prioritize official statements and established newsrooms; check original publication dates; corroborate contested claims; separate estimates from independently confirmed facts. Never disclose operational evacuation routes, civilian locations, personal identifiers or aid logistics. Do not scrape copyrighted article bodies or reuse photographs without permission. No impersonation, spam bots, automated comments or misleading coordinated activity. Never suggest that a safe route exists unless confirmed by a competent humanitarian body.

## Current sources (17 October 2026)
- Associated Press: https://apnews.com/article/dc2ee1a9c31707f61674c598820a5900
- Reuters (16 October): https://www.reuters.com/world/europe/kremlin-says-putin-told-pope-leo-he-backs-vatican-idea-help-civilians-in-oleshky-2026-10-16/
- Reuters (8 October): https://www.reuters.com/world/europe/people-russian-occupied-ukrainian-town-risk-road-death-get-food-2026-10-08/
- European Commission: https://civil-protection-humanitarian-aid.ec.europa.eu/news-stories/news/statement-commissioner-lahbib-siege-oleshky-ukraine-2026-10-02_en
- Council of Europe: https://www.coe.int/en/web/commissioner/

## Scope / limitations
No server, analytics, cookies, user registration, API keys or donations. Language selector translates site interface; news summaries are currently hand-written in English and Slovak, with English fallback in the other six languages until editorially reviewed translations are added. The validator is not an autonomous news monitor. GitHub Pages service availability and quotas follow GitHub's current terms.


## Hero photography / Fotografia v hlavičke
The page currently contains a custom architectural illustration, **not a real photograph**.
The authentic aerial image discussed is published at:
https://nikvesti.com/news/politics/324455-ukraina-vymahaie-uvahy-osce-sytuatsii-okupovanykh-oleshkakh
We have **not verified reuse permission**, so the copyrighted photo is not copied into this ZIP.
To replace the illustration once you obtain permission: save the licensed image as
`assets/oleshky-hero.jpg`, open `assets/style.css`, find the line beginning
`/* After permission:` and uncomment the `.hero-art` background-image rule.
Provide attribution according to the license/permission and document the capture date.
Do not label historical footage as showing the current crisis.
