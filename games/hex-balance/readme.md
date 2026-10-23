# Hex Balance

> Verified game note.

![Hex Balance screenshot](https://raw.githubusercontent.com/Zach-Shirley/hex-balance/main/docs/screenshot.jpg)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/Zach-Shirley/hex-balance/blob/main/docs/screenshot.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Zach-Shirley/hex-balance](https://github.com/Zach-Shirley/hex-balance)
- **Evidence:** [direct model evidence](https://github.com/Zach-Shirley/hex-balance/commit/315bd591d166d3d3a2a9d4d5e0a9beebc6fb0e43)
- **Live demo:** [open demo](https://hex-balance.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Zach-Shirley/hex-balance/blob/main/docs/screenshot.jpg) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Hexagonal balance board with clean dark UI panels

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser recreation of a steel hexagonal balance game built in high school: dice, stacks, torque, online play and bots. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Zach-Shirley/hex-balance/blob/main/src/main.ts](https://github.com/Zach-Shirley/hex-balance/blob/main/src/main.ts)
- [https://github.com/Zach-Shirley/hex-balance/commit/315bd591d166d3d3a2a9d4d5e0a9beebc6fb0e43](https://github.com/Zach-Shirley/hex-balance/commit/315bd591d166d3d3a2a9d4d5e0a9beebc6fb0e43)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Zach-Shirley/hex-balance

[Back to the awesome list](../../README.md)
