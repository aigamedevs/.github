# DuneCraft & Conquer

> Verified game note.

![DuneCraft & Conquer screenshot](https://raw.githubusercontent.com/AndreyBelyy/dunecraft-conquer/main/docs/screenshots/battle.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/AndreyBelyy/dunecraft-conquer/blob/main/docs/screenshots/battle.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/AndreyBelyy/dunecraft-conquer](https://github.com/AndreyBelyy/dunecraft-conquer)
- **Evidence:** [direct model evidence](https://github.com/AndreyBelyy/dunecraft-conquer/commit/24b0e5616021fc5c67320980d2a7061537112652)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/AndreyBelyy/dunecraft-conquer/blob/main/docs/screenshots/battle.jpg) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. Desert RTS battle with many units, bases, explosions, minimap and build sidebar; busy and detailed.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser RTS mash-up of Command & Conquer, Dune 2000 and StarCraft: 9 factions, multiplayer, WebGL. Converters build the art from your own game copies; no game files included. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AndreyBelyy/dunecraft-conquer/blob/main/game/public/js/game.js](https://github.com/AndreyBelyy/dunecraft-conquer/blob/main/game/public/js/game.js)
- [https://github.com/AndreyBelyy/dunecraft-conquer/commit/24b0e5616021fc5c67320980d2a7061537112652](https://github.com/AndreyBelyy/dunecraft-conquer/commit/24b0e5616021fc5c67320980d2a7061537112652)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/AndreyBelyy/dunecraft-conquer

[Back to the awesome list](../../README.md)
