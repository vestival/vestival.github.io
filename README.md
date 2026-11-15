# vestival.es

Source for https://vestival.es. Hand-written static HTML and one stylesheet. No framework, no build step. Hosted on Netlify behind Cloudflare.

## Files

- `index.html`: home (bio, now line, selected work, latest writing, links)
- `portfolio.html`: everything else, grouped by topic, served at `/portfolio`
- `writing/index.html`: the writing index, served at `/writing/`
- `writing/_template.html`: the template for a post hosted on this site
- `feed.xml`: RSS feed for posts hosted on this site
- `sitemap.xml`, `robots.txt`
- `style.css`, `site.js` (theme toggle and font size), `favicon.svg`, `avatar.jpg`, `og.jpg` (social preview image)

## Preview locally

```bash
npx serve .
```

Then open http://localhost:3000. `serve` maps `/portfolio` to `portfolio.html` the way Netlify does. `python3 -m http.server` works too, but then open `/portfolio.html` by hand.

## How to add a post

Posts live at `/writing/<slug>/`. Pick a short slug, for example `orca-two-weeks`.

1. Copy the template: `mkdir writing/<slug>` and `cp writing/_template.html writing/<slug>/index.html`.
2. In the copy, replace every placeholder: `SLUG`, `POST TITLE`, `ONE-SENTENCE SUMMARY`, the ISO date (`2026-12-07`) and the display date (`7 Dec 2026`). Write the body in plain HTML. Delete the `<meta name="robots" content="noindex" />` line and the comment at the top.
3. Add it to the index: in `writing/index.html`, uncomment the "On this site" section the first time, then add one `<li>` per post, newest first.
4. Add it to the feed: in `feed.xml`, copy the commented `<item>`, fill it in, uncomment it, and update `lastBuildDate`.
5. Add it to the sitemap: in `sitemap.xml`, copy the commented `<url>`, fill it in and uncomment it.
6. Optional: add it to "Latest writing" on `index.html` and drop the oldest entry there.
7. Publish here first. Syndicate to dev.to or DZone a few days later, with the canonical URL set to `https://vestival.es/writing/<slug>/`. When the copies are live, add them as "Also on" links in the post and in the index.

The first slot is reserved for the Orca article planned for 7 Dec 2026.

## How to add a portfolio item

Copy an existing `<li>` in the right section of `portfolio.html`. Every item has a title link, a date, one line, and "Also on" links for its copies. Only add items with a public URL.

## Decisions

- Typography: Sora for headings, Inter for body text. Intentional, kept from the earlier version of the site. Do not swap it.
- `_archive/` holds assets the site no longer uses (company logos, the old `victor.png` portrait). Kept for reference, not linked from any page.
- Analytics: Umami at umami.vestival.es, with its own site ID for the apex domain. The script tag is in the `<head>` of every page, including the post template.

## Rules for copy on this site

Write in the first person, in plain words. No em dashes, semicolons, hashtags or `<hr>`. SUSE can be named as the current role. No other employer or client is named as current.
