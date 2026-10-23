# NBA Pinpoint

> Verified game note.

![NBA Pinpoint screenshot](https://raw.githubusercontent.com/fwdmove/nba-pinpoint/main/assets/thumbnail.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.5/10 ([manually reviewed image](https://github.com/fwdmove/nba-pinpoint/blob/main/assets/thumbnail.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/fwdmove/nba-pinpoint](https://github.com/fwdmove/nba-pinpoint)
- **Evidence:** [direct model evidence](https://github.com/fwdmove/nba-pinpoint/commit/78ac20bc4fb8e99fa8f8fd407e9d9126d1b6bc85)
- **Live demo:** [open demo](https://nba-pinpoint.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/fwdmove/nba-pinpoint/blob/main/assets/thumbnail.png) — 📸 5.5/10 · manual visual review · Use this frame for the game-level score. Bold NBA guessing promo card with leaderboard slots.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A stat-leaderboard guessing game. You get a random NBA category, like Most dunks in 2015-16, Most career playoff steals, or Highest usage rate in 2022-23. Name as many of its top 100 players as you can. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/fwdmove/nba-pinpoint/blob/main/components/Game.tsx](https://github.com/fwdmove/nba-pinpoint/blob/main/components/Game.tsx)
- [https://github.com/fwdmove/nba-pinpoint/commit/78ac20bc4fb8e99fa8f8fd407e9d9126d1b6bc85](https://github.com/fwdmove/nba-pinpoint/commit/78ac20bc4fb8e99fa8f8fd407e9d9126d1b6bc85)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/fwdmove/nba-pinpoint

[Back to the awesome list](../../README.md)
