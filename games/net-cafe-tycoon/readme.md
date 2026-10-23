# Net Cafe Tycoon

> Verified game note.

![Net Cafe Tycoon screenshot placeholder](net-cafe-tycoon-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Sonnet 5.5
- **Technology:** C#, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/bilgehandk/internet-cafe-simulator](https://github.com/bilgehandk/internet-cafe-simulator)
- **Evidence:** [direct model evidence](https://github.com/bilgehandk/internet-cafe-simulator/commit/d08d97e80a1a0a90e759bb168cab44d8f1b6acc9)
- **Live demo:** [open demo](https://bilgehandk.github.io/net-cafe-tycoon/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Blender --background --python blender/scripts/buildassets.py sonra FBX'leri Game/Assets/Models'e kopyala. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bilgehandk/internet-cafe-simulator/blob/master/docs/Build/WebBuild.framework.js](https://github.com/bilgehandk/internet-cafe-simulator/blob/master/docs/Build/WebBuild.framework.js)
- [https://github.com/bilgehandk/internet-cafe-simulator/commit/d08d97e80a1a0a90e759bb168cab44d8f1b6acc9](https://github.com/bilgehandk/internet-cafe-simulator/commit/d08d97e80a1a0a90e759bb168cab44d8f1b6acc9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/bilgehandk/internet-cafe-simulator

[Back to the awesome list](../../README.md)
