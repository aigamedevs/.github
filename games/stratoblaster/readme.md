# Stratoblaster

> Verified game note.

![Stratoblaster screenshot placeholder](stratoblaster-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/rguillon/stratoblaster](https://github.com/rguillon/stratoblaster)
- **Evidence:** [direct model evidence](https://github.com/rguillon/stratoblaster/commit/f7791c61a0cbf95249d9fb487e50bf60a9ac28fb)
- **Live demo:** [open demo](https://rguillon.github.io/stratoblaster/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An old-school vertical shoot 'em up with modern 3D graphics, running entirely in the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/rguillon/stratoblaster/blob/main/src/core/scenery/prop-placement.ts](https://github.com/rguillon/stratoblaster/blob/main/src/core/scenery/prop-placement.ts)
- [https://github.com/rguillon/stratoblaster/commit/f7791c61a0cbf95249d9fb487e50bf60a9ac28fb](https://github.com/rguillon/stratoblaster/commit/f7791c61a0cbf95249d9fb487e50bf60a9ac28fb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/rguillon/stratoblaster

[Back to the awesome list](../../README.md)
