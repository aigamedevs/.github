# Cavern of Code

> Verified game note.

![Cavern of Code screenshot placeholder](cavern-of-code-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/bipinjr/Treasure-Hunt](https://github.com/bipinjr/Treasure-Hunt)
- **Evidence:** [direct model evidence](https://github.com/bipinjr/Treasure-Hunt/commit/c1cbcecae1794eb7b3b38e947917477606fd84fb)
- **Live demo:** [open demo](https://treasure-hunt-seven-sigma.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Static site (repo root) + Supabase project rbaibnntcgpdeybvtool (already set up). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bipinjr/Treasure-Hunt/blob/main/js/game.js](https://github.com/bipinjr/Treasure-Hunt/blob/main/js/game.js)
- [https://github.com/bipinjr/Treasure-Hunt/commit/c1cbcecae1794eb7b3b38e947917477606fd84fb](https://github.com/bipinjr/Treasure-Hunt/commit/c1cbcecae1794eb7b3b38e947917477606fd84fb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/bipinjr/Treasure-Hunt

[Back to the awesome list](../../README.md)
