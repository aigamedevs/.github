# hypercaz

> Verified game note.

![hypercaz screenshot placeholder](hypercaz-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/hobsojam/hypercaz](https://github.com/hobsojam/hypercaz)
- **Evidence:** [direct model evidence](https://github.com/hobsojam/hypercaz/commit/c6e5dd11b9411177985ae62f17fa027609591124)
- **Live demo:** [open demo](https://hobsojam.github.io/hypercaz/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Simple, ad-free hyper-casual browser games. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hobsojam/hypercaz/blob/main/games/squad/render/draw.ts](https://github.com/hobsojam/hypercaz/blob/main/games/squad/render/draw.ts)
- [https://github.com/hobsojam/hypercaz/commit/c6e5dd11b9411177985ae62f17fa027609591124](https://github.com/hobsojam/hypercaz/commit/c6e5dd11b9411177985ae62f17fa027609591124)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/hobsojam/hypercaz

[Back to the awesome list](../../README.md)
