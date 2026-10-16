# Gecko

> Verified game note.

![Gecko screenshot placeholder](gecko-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/alecoschwartz/gekko](https://github.com/alecoschwartz/gekko)
- **Evidence:** [direct model evidence](https://github.com/alecoschwartz/gekko/commit/bf89493d66d314d8ab1d22a08769f829e9654c20)
- **Live demo:** [open demo](https://alecoschwartz.github.io/gekko/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Phone party word game with room codes: everyone but the Gecko gets the secret word; answer questions and vote. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/alecoschwartz/gekko/blob/main/js/game.js](https://github.com/alecoschwartz/gekko/blob/main/js/game.js)
- [https://github.com/alecoschwartz/gekko/commit/bf89493d66d314d8ab1d22a08769f829e9654c20](https://github.com/alecoschwartz/gekko/commit/bf89493d66d314d8ab1d22a08769f829e9654c20)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/alecoschwartz/gekko

[Back to the awesome list](../../README.md)
