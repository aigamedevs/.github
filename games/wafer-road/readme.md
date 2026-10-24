# 晶圓之路 Wafer Road

> Verified game note.

![晶圓之路 Wafer Road screenshot](https://raw.githubusercontent.com/boenchen1112/wafer-road/main/docs/screenshot.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 5.2/10 ([manually reviewed image](https://github.com/boenchen1112/wafer-road/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/boenchen1112/wafer-road](https://github.com/boenchen1112/wafer-road)
- **Evidence:** [direct model evidence](https://github.com/boenchen1112/wafer-road/commit/60e42fe10bb0bc3dbb2c0817d7ca71508cbd26a4)
- **Live demo:** [open demo](https://boenchen1112.github.io/wafer-road/)
- **Additional live link:** [open demo](https://boenchen1112.github.io/wafer-road/?room=ABCD`），朋友開連結即可加入，不需要帳號。房主可設定)
- **Additional live link:** [open demo](https://boenchen1112.github.io/wafer-road/?room=ABCD)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/boenchen1112/wafer-road/blob/main/docs/screenshot.png) — 📸 5.2/10 · manual visual review · Use this frame for the game-level score. Dark card-based management UI with upgrade slots; tidy but text-heavy with little scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

繁體中文 · English. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/boenchen1112/wafer-road/blob/main/server/src/room.ts](https://github.com/boenchen1112/wafer-road/blob/main/server/src/room.ts)
- [https://github.com/boenchen1112/wafer-road/commit/60e42fe10bb0bc3dbb2c0817d7ca71508cbd26a4](https://github.com/boenchen1112/wafer-road/commit/60e42fe10bb0bc3dbb2c0817d7ca71508cbd26a4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/boenchen1112/wafer-road

[Back to the awesome list](../../README.md)
