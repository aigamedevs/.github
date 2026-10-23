# 21 點

> Verified game note.

![21 點 screenshot](https://raw.githubusercontent.com/SodaCK87/Game---Blackjack/main/docs/img/play.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/SodaCK87/Game---Blackjack/blob/main/docs/img/play.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/SodaCK87/Game---Blackjack](https://github.com/SodaCK87/Game---Blackjack)
- **Evidence:** [direct model evidence](https://github.com/SodaCK87/Game---Blackjack/commit/8c5a6058baa903f61bea53fb79da6bd5e04dbf8d)
- **Live demo:** [open demo](https://sodack87.github.io/Game---Blackjack/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/SodaCK87/Game---Blackjack/blob/main/docs/img/play.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. 3D blackjack table with illustrated dealer and chips

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

給同事玩的網頁 21 點：3D 牌桌、插畫荷官、三位電腦同桌. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/SodaCK87/Game---Blackjack/blob/main/app/lib/three.js](https://github.com/SodaCK87/Game---Blackjack/blob/main/app/lib/three.js)
- [https://github.com/SodaCK87/Game---Blackjack/commit/8c5a6058baa903f61bea53fb79da6bd5e04dbf8d](https://github.com/SodaCK87/Game---Blackjack/commit/8c5a6058baa903f61bea53fb79da6bd5e04dbf8d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/SodaCK87/Game---Blackjack

[Back to the awesome list](../../README.md)
