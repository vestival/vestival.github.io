# vestival.es

Source for https://vestival.es. Hand-written static HTML and one stylesheet. No framework, no build step. Hosted on Netlify behind Cloudflare.

## Files

- `index.html`: home (hero, about with the Now line, latest writing and projects, experience, skills, contact)
- `portfolio.html`: everything else, grouped by topic, served at `/portfolio`
- `writing/index.html`: the writing index, served at `/writing/`
- `writing/_template.html`: the template for a post hosted on this site
- `feed.xml`: RSS feed for posts hosted on this site
- `sitemap.xml`, `robots.txt`
- `style.css`, `favicon.svg`, `victor.png` (hero portrait), `logos/` (experience and writing logos), `og.jpg` (social preview image)
- Each page carries the same header, nav, footer and inline script (theme toggle and font size). Copy them from an existing page.

## Preview locally

```bash
npx serve .
```

Then open http://localhost:3000. `serve` maps `/portfolio` to `portfolio.html` the way Netlify does. `python3 -m http.server` works too, but then open `/portfolio.html` by hand.

## How to add a post

Posts live at `/writing/<slug>/`. Pick a short slug, for example `orca-two-weeks`.

1. Copy the template: `mkdir writing/<slug>` and `cp writing/_template.html writing/<slug>/index.html`.
2. In the copy, replace every placeholder: `SLUG`, `POST TITLE`, `ONE-SENTENCE SUMMARY`, the ISO date (`2026-12-07`) and the display date (`7 Dec 2026`). Write the body in plain HTML. Delete the `<meta name="robots" content="noindex" />` line and the comment at the top.
3. Add it to the index: in `writing/index.html`, uncomment the "On this site" section the first time, then add one `other-card` per post, newest first.
4. Add it to the feed: in `feed.xml`, copy the commented `<item>`, fill it in, uncomment it, and update `lastBuildDate`.
5. Add it to the sitemap: in `sitemap.xml`, copy the commented `<url>`, fill it in and uncomment it.
6. Optional: add it to "Latest writing and projects" on `index.html` and drop the oldest entry there.
7. Publish here first. Syndicate to dev.to or DZone a few days later, with the canonical URL set to `https://vestival.es/writing/<slug>/`. When the copies are live, add them as "Also on" links in the post and in the index.

The first slot is reserved for the Orca article planned for 7 Dec 2026.

## How to add a portfolio item

Copy an existing card in the right section of `portfolio.html` and reuse the components already there: `project-card` for main items (title, date and outlet, one line, pill, links), `other-card` for compact lists, `conf-card` for talks, `writing-group` with `article-list` for series. Copies of a piece go in as extra `project-link` "Also on" links. Only add items with a public URL.

## Decisions

- Typography: Sora for headings, Inter for body text. Intentional, kept from the earlier version of the site. Do not swap it.
- Design: the original layout, components and stylesheet are kept as they were. New content reuses existing components. The only CSS added is the rule for the collapsed Earlier work section.
- Assets: `logos/` and `victor.png` stay in place because the design uses them. `_archive/` is for assets that fall out of use, so they are kept rather than deleted.
- Analytics: Umami at umami.vestival.es, with its own site ID for the apex domain. The script tag is in the `<head>` of every page, including the post template.

## Rules for copy on this site

Write in the first person, in plain words. No em dashes, semicolons, hashtags or `<hr>`. SUSE can be named as the current role. No other employer or client is named as current.
