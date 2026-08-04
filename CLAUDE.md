# Samscaped

Static site for a lawn care company in Akron/Canton, OH. Cloudflare Pages, branch main,
build output directory public/, no build command.

## Rules
- Never hand-edit files in public/. All copy, CSS, and markup live in build_site.py.
  Edit that, run `python3 build_site.py`, commit both.
- Never change title tags, meta descriptions, H1s, canonicals, JSON-LD, or URL slugs
  unless asked. The SEO layer is load-bearing.
- Footer NAP must match the GBP exactly: Samscaped / (330) 578-5085 / samscaped@outlook.com
- No frameworks, no npm, no CI build step. Python 3 stdlib and vanilla CSS/JS only.
- Keep CSS under 15KB and JS under 40 lines.
- Open TODOs are in README.md. Do not silently resolve them.
