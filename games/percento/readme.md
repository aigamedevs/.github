# PERCENTO

> Verified game note.

![PERCENTO screenshot placeholder](percento-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/jacoposta21-ux/Percento](https://github.com/jacoposta21-ux/Percento)
- **Evidence:** [direct model evidence](https://github.com/jacoposta21-ux/Percento/commit/285998b0af92e4fd762e4a02516262bd7c31f148)
- **Live demo:** [open demo](https://percento-virid.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Plain HTML, CSS and ES modules. The only runtime library is supabase-js (vendored in vendor/, loaded in the background); if it or the server is unreachable, the game keeps working as a guest. Node ≥ 20 for the tooling. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jacoposta21-ux/Percento/blob/claude/keen-edison-0s02ip/src/app.js](https://github.com/jacoposta21-ux/Percento/blob/claude/keen-edison-0s02ip/src/app.js)
- [https://github.com/jacoposta21-ux/Percento/commit/285998b0af92e4fd762e4a02516262bd7c31f148](https://github.com/jacoposta21-ux/Percento/commit/285998b0af92e4fd762e4a02516262bd7c31f148)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/jacoposta21-ux/Percento

[Back to the awesome list](../../README.md)
