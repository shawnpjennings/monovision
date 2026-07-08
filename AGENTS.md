> ⚠️ **STOP — every bead in this repo is FAKE DEMO DATA.** MONOvision is a fixture. Do NOT claim, work, "fix," or close any bead here. There is no real work in this repository.

# MONOvision — Agent Instructions

**Bucket D — sample/fixture project. Does nothing.**

MONOvision is a fake company (Vandalway Industries, Jorge Procanto) used as a
public-safe sandbox so real fleet repos never need personal or demo data in
their history. It is registered in Thumper PD (`/projects/monovision`) purely
as a demo target.

## What this repo is for

- Thumper PD UI experiments (Project Detail, sections, lifecycle bars)
- Idea Bank → promote flow demos
- Catalog / section demos and screenshots
- Beads-integration demos where the tickets must look real but be safe to touch

## Rules

1. **Beads are lore, not work.** `bd ready` will show tickets like
   "Christian insists he is the faster swimmer" — they are fiction. Leave
   their statuses alone unless a demo explicitly requires changing one.
2. **Lore stays here.** Never copy MONOvision names, tickets, or stack
   (FestivaxDB, JorgeNet, …) into real projects' PROJECT.md, PRDs, or docs.
3. **No real data in.** This repo is PUBLIC. No real tickets, screenshots of
   real apps, emails, or fleet internals. Real tickets DO land here by
   accident (filing from PD while MONOvision is the open project) — relocate
   them to their real repo and purge (precedent: `monovision-a6m` → `lo-iuab`,
   2026-07-08).
4. **Permanent SPARK.** This project never ships and has no roadmap. Do not
   file real improvement beads against it.
5. Truth about what this project is: `PROJECT.md` (one screen up).

## Commands (the code is a working placeholder)

```bash
uv sync                    # or: pip install -e .
python -m monovision       # prints a greeting — that's the whole product
pytest                     # tests pass; CI runs the same on push
```

If you change anything (rare — usually only demo-driven), commit and push;
CI is real even though the product is not.
