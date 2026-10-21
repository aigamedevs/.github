# HMB Arena

> Verified game note.

![HMB Arena screenshot placeholder](hmb-arena-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/CborgX/HMB_ARENA](https://github.com/CborgX/HMB_ARENA)
- **Evidence:** [direct model evidence](https://github.com/CborgX/HMB_ARENA/commit/e6818e7343c8b15aef1d2cb45277b61b1912c8d1)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

FPS game that autonomously betters itself as per user feedback. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/CborgX/HMB_ARENA/blob/main/public/draco/draco_decoder.js](https://github.com/CborgX/HMB_ARENA/blob/main/public/draco/draco_decoder.js)
- [https://github.com/CborgX/HMB_ARENA/commit/e6818e7343c8b15aef1d2cb45277b61b1912c8d1](https://github.com/CborgX/HMB_ARENA/commit/e6818e7343c8b15aef1d2cb45277b61b1912c8d1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/CborgX/HMB_ARENA

[Back to the awesome list](../../README.md)
