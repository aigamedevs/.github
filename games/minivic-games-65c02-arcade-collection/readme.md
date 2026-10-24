# miniVIC Games: 65C02 Arcade Collection

> Verified game note.

![miniVIC Games: 65C02 Arcade Collection screenshot](https://raw.githubusercontent.com/Boogs77/miniVIC_games/main/screenshots/tank_game.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/Boogs77/miniVIC_games/blob/main/screenshots/tank_game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Assembly
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/Boogs77/miniVIC_games](https://github.com/Boogs77/miniVIC_games)
- **Evidence:** [direct model evidence](https://github.com/Boogs77/miniVIC_games/commit/bf04f1280c01018edd575141fd1b700909b6d60e)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Boogs77/miniVIC_games/blob/main/screenshots/tank_game.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Green maze tank battle screen in 8-bit style; authentic but very simple.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

65C02 assembly arcade games for the miniVIC (TMS9918A + AY-3-8910). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Boogs77/miniVIC_games/blob/main/the_warriors.asm](https://github.com/Boogs77/miniVIC_games/blob/main/the_warriors.asm)
- [https://github.com/Boogs77/miniVIC_games/commit/bf04f1280c01018edd575141fd1b700909b6d60e](https://github.com/Boogs77/miniVIC_games/commit/bf04f1280c01018edd575141fd1b700909b6d60e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/Boogs77/miniVIC_games

[Back to the awesome list](../../README.md)
