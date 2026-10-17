# TUX 64 — The Kernel Castle Adventure

> Verified game note.

![TUX 64 — The Kernel Castle Adventure screenshot](https://raw.githubusercontent.com/hubstacksea/tux64/main/docs/screenshots/grounds.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.5/10 ([manually reviewed image](https://github.com/hubstacksea/tux64/blob/main/docs/screenshots/grounds.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/hubstacksea/tux64](https://github.com/hubstacksea/tux64)
- **Evidence:** [direct model evidence](https://github.com/hubstacksea/tux64/commit/7e3f55f28d812689412f92393dfc61ec9b39c123)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hubstacksea/tux64/blob/main/docs/screenshots/grounds.png) — 📸 6.5/10 · manual visual review · Use this frame for the game-level score. Snowy 3D platformer level with Tux, trees, snowmen and collectible HUD; cheerful, simple shapes.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D game featuring Tux, the Linux mascot. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hubstacksea/tux64/blob/main/src/font_ja.h](https://github.com/hubstacksea/tux64/blob/main/src/font_ja.h)
- [https://github.com/hubstacksea/tux64/commit/7e3f55f28d812689412f92393dfc61ec9b39c123](https://github.com/hubstacksea/tux64/commit/7e3f55f28d812689412f92393dfc61ec9b39c123)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/hubstacksea/tux64

[Back to the awesome list](../../README.md)
