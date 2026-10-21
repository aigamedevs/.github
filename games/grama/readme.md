# Grama

> Verified game note.

![Grama screenshot placeholder](grama-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ewajs/grama](https://github.com/ewajs/grama)
- **Evidence:** [direct model evidence](https://github.com/ewajs/grama/commit/d48fa2c11473513be142d0e1dd34d34768d15c1b)
- **Live demo:** [open demo](https://ewajs.github.io/grama/)
- **Additional live link:** [open demo](https://ewajs.github.io/grama/guia/)
- **Additional live link:** [open demo](https://ewajs.github.io/grama/docs/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A calm, fast word game: connect the letters on the wheel to find every word in the level. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ewajs/grama/blob/main/src/app/game.svelte.ts](https://github.com/ewajs/grama/blob/main/src/app/game.svelte.ts)
- [https://github.com/ewajs/grama/commit/d48fa2c11473513be142d0e1dd34d34768d15c1b](https://github.com/ewajs/grama/commit/d48fa2c11473513be142d0e1dd34d34768d15c1b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ewajs/grama

[Back to the awesome list](../../README.md)
