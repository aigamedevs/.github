# SECTOR

> Verified game note.

![SECTOR screenshot](https://raw.githubusercontent.com/Blacksheep909/sector/main/docs/img/board.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 6.6/10 ([manually reviewed image](https://github.com/Blacksheep909/sector/blob/main/docs/img/board.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Blacksheep909/sector](https://github.com/Blacksheep909/sector)
- **Evidence:** [direct model evidence](https://github.com/Blacksheep909/sector/commit/d87ffda7c26325160fde9556733b2391fe08b55f)
- **Live demo:** [open demo](https://github.com/Blacksheep909/sector/releases/latest)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Blacksheep909/sector/blob/main/docs/img/board.png) — 📸 6.6/10 · manual visual review · Use this frame for the game-level score. Hex conquest map with coloured territories, unit tokens and a card hand; rich board-game layout.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Turn-based hex conquest for 2–6 players on the same Wi-Fi. Procedural maps, card drafting, naval warfare, Balatro-style dice combat. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Blacksheep909/sector/blob/main/public/main.js](https://github.com/Blacksheep909/sector/blob/main/public/main.js)
- [https://github.com/Blacksheep909/sector/commit/d87ffda7c26325160fde9556733b2391fe08b55f](https://github.com/Blacksheep909/sector/commit/d87ffda7c26325160fde9556733b2391fe08b55f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Blacksheep909/sector

[Back to the awesome list](../../README.md)
