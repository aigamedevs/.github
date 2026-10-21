# Monster Arena

> Verified game note.

![Monster Arena screenshot placeholder](monster-arena-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/curiomindsinc/pokemonarena](https://github.com/curiomindsinc/pokemonarena)
- **Evidence:** [direct model evidence](https://github.com/curiomindsinc/pokemonarena/commit/47f72b2cb3d5730c0ba36d5b8b62141e69ffdb3e)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Top-down monster fighting game in the browser (canvas, no build step). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/curiomindsinc/pokemonarena/blob/main/src/world.js](https://github.com/curiomindsinc/pokemonarena/blob/main/src/world.js)
- [https://github.com/curiomindsinc/pokemonarena/commit/47f72b2cb3d5730c0ba36d5b8b62141e69ffdb3e](https://github.com/curiomindsinc/pokemonarena/commit/47f72b2cb3d5730c0ba36d5b8b62141e69ffdb3e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/curiomindsinc/pokemonarena

[Back to the awesome list](../../README.md)
