# TapkoTyper

> Verified game note.

![TapkoTyper screenshot](https://raw.githubusercontent.com/atiris/tapkotyper/main/docs/meadow.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/atiris/tapkotyper/blob/main/docs/meadow.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/atiris/tapkotyper](https://github.com/atiris/tapkotyper)
- **Evidence:** [direct model evidence](https://github.com/atiris/tapkotyper/commit/93d77b702df3609da3fcebce1dce1c9b620c9094)
- **Live demo:** [open demo](https://atiris.github.io/tapkotyper/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/atiris/tapkotyper/blob/main/docs/meadow.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Sunny meadow scene with on-screen keyboard and hand guide

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A peaceful, story-driven touch-typing adventure for children (about 10-15 years). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/atiris/tapkotyper/blob/main/src/game/runtime.ts](https://github.com/atiris/tapkotyper/blob/main/src/game/runtime.ts)
- [https://github.com/atiris/tapkotyper/commit/93d77b702df3609da3fcebce1dce1c9b620c9094](https://github.com/atiris/tapkotyper/commit/93d77b702df3609da3fcebce1dce1c9b620c9094)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/atiris/tapkotyper

[Back to the awesome list](../../README.md)
