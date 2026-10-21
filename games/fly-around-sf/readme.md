# Fly Around SF

> Verified game note.

![Fly Around SF screenshot placeholder](fly-around-sf-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ayaangazali/fly-around-sf](https://github.com/ayaangazali/fly-around-sf)
- **Evidence:** [direct model evidence](https://github.com/ayaangazali/fly-around-sf/commit/c8b48eb5ecbd7b13921a6263d9bc3bcc526df1b3)
- **Live demo:** [open demo](https://ayaangazali.github.io/fly-around-sf/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Fly a drone around all 172,000 buildings of a 3D San Francisco. Collect landmarks, solve clues, fly with friends. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ayaangazali/fly-around-sf/blob/main/src/ui/card-art.ts](https://github.com/ayaangazali/fly-around-sf/blob/main/src/ui/card-art.ts)
- [https://github.com/ayaangazali/fly-around-sf/commit/c8b48eb5ecbd7b13921a6263d9bc3bcc526df1b3](https://github.com/ayaangazali/fly-around-sf/commit/c8b48eb5ecbd7b13921a6263d9bc3bcc526df1b3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ayaangazali/fly-around-sf

[Back to the awesome list](../../README.md)
