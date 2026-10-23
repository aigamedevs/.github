# Portalsweeper

> Verified game note.

![Portalsweeper screenshot placeholder](portalsweeper-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Sireadell/portalsweeper](https://github.com/Sireadell/portalsweeper)
- **Evidence:** [direct model evidence](https://github.com/Sireadell/portalsweeper/commit/af26cdc4c4dd73a99569daefa8ad29eb1ccf6739)
- **Live demo:** [open demo](https://portalsweeper.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Portalsweeper is a daily puzzle game on Portaldot V3. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Sireadell/portalsweeper/blob/main/scripts/gen-portals.mjs](https://github.com/Sireadell/portalsweeper/blob/main/scripts/gen-portals.mjs)
- [https://github.com/Sireadell/portalsweeper/commit/af26cdc4c4dd73a99569daefa8ad29eb1ccf6739](https://github.com/Sireadell/portalsweeper/commit/af26cdc4c4dd73a99569daefa8ad29eb1ccf6739)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Sireadell/portalsweeper

[Back to the awesome list](../../README.md)
