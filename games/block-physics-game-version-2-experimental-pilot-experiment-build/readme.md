# Block physics game - Version 2 (experimental): pilot experiment build

> Verified game note.

![Block physics game - Version 2 (experimental): pilot experiment build screenshot placeholder](block-physics-game-version-2-experimental-pilot-experiment-build-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/marlenercohen/block-game-v2](https://github.com/marlenercohen/block-game-v2)
- **Evidence:** [direct model evidence](https://github.com/marlenercohen/block-game-v2/commit/12f4d97ffe719d04b364010cb389301f0dbcdcff)
- **Live demo:** [open demo](https://marlenercohen.github.io/block-game-v2/)
- **Additional live link:** [open demo](https://marlenercohen.github.io/block-game-v2/?kiosk=1)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Block game with color and memory rules. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/marlenercohen/block-game-v2/blob/main/tools/v2_checks.mjs](https://github.com/marlenercohen/block-game-v2/blob/main/tools/v2_checks.mjs)
- [https://github.com/marlenercohen/block-game-v2/commit/12f4d97ffe719d04b364010cb389301f0dbcdcff](https://github.com/marlenercohen/block-game-v2/commit/12f4d97ffe719d04b364010cb389301f0dbcdcff)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/marlenercohen/block-game-v2

[Back to the awesome list](../../README.md)
