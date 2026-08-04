# Samscaped

Static marketing site for Samscaped, a lawn care company serving the Akron/Canton, OH area.
Built and maintained by Veraa Technology.

## Structure

```
build_site.py    Python generator. All page copy, SEO metadata, and CSS live here.
public/          Generated output. This is what Cloudflare Pages serves.
public/assets/   Logo and photo assets.
public/_headers  Cloudflare Pages security + cache headers.
```

Do not hand-edit files in `public/`. They are overwritten on every build.
Edit `build_site.py`, then run:

```bash
python3 build_site.py
```

No dependencies. Python 3 standard library only.

## Deploy (Cloudflare Pages)

1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git
2. Select this repo, branch `main`
3. Framework preset: **None**
4. Build command: leave **empty**
5. Build output directory: `public`
6. Save and deploy

`public/` is committed, so Pages does not need a build step. Every push to `main` redeploys.

Custom domain: Pages project → Custom domains → add the apex and `www`, then set `www` to redirect to apex.

## Pages (16)

Home, Services hub, 6 service pages, Service Areas hub, 4 city pages, Pricing, About, Contact.
Plus `sitemap.xml` and `robots.txt`.

City pages target Akron, Canton, North Canton, and Green. Uniontown, Jackson Township, and Massillon
are covered as mentions.

## Before launch

- [ ] **GHL form ID** — three pages (index, pricing, contact) embed a LeadConnector iframe with the
      placeholder `YOUR_FORM_ID`. Create the form in the Samscaped GHL sub-account and replace it in
      `build_site.py`, then rebuild.
- [ ] **Domain** — `DOMAIN` in `build_site.py` is set to `https://samscaped.com`. Update if different.
      It drives canonicals, schema, and the sitemap.
- [ ] **Pricing** — ranges in the pricing table are typical Akron/Canton market rates. Confirm with Sam.
- [ ] **"Licensed & insured"** — appears in the hero trust row. Confirm before publishing.
- [ ] **Hours** — footer says "Mon–Sat, seasonal hours". Confirm.
- [ ] **Logo** — the header wordmark is an inline SVG rebuild because the only supplied asset was a
      ~150px PNG. Swap in Sam's original vector file if it exists.
- [ ] **Photos** — replace the gradient placeholders. Phone photos of real jobs beat stock.
      Paths: `assets/hero.jpg`, `svc-mowing.jpg`, `svc-landscaping.jpg`, `svc-mulch.jpg`,
      `svc-cleanup.jpg`, `svc-trimming.jpg`, `svc-leaf.jpg`, `city-akron.jpg`, `city-canton.jpg`,
      `city-north-canton.jpg`, `city-green.jpg`
- [ ] **Reviews** — two placeholder testimonials on the homepage. Swap in real Google reviews.

## After launch

- [ ] Google Search Console: add a Domain property, submit `sitemap.xml`, confirm 16 pages discovered
- [ ] Confirm the GBP website link points to the homepage
- [ ] Confirm NAP matches the GBP exactly: Samscaped / (330) 578-5085 / samscaped@outlook.com
- [ ] Set up a review request process for Sam. Review count moves the map pack faster than the site will.
