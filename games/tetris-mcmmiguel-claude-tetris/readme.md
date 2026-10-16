# Tetris

> Verified game note.

![Tetris screenshot placeholder](tetris-mcmmiguel-claude-tetris-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/mcmmiguel/claude-tetris](https://github.com/mcmmiguel/claude-tetris)
- **Evidence:** [direct model evidence](https://github.com/mcmmiguel/claude-tetris/commit/ad5d4a1b7d98b723b682c3da4e60be7ca65a7b73)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Vanilla JavaScript canvas Tetris built during a Claude course; game loop and game-over handling in game.js. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/mcmmiguel/claude-tetris/blob/main/game.js](https://github.com/mcmmiguel/claude-tetris/blob/main/game.js)
- [https://github.com/mcmmiguel/claude-tetris/commit/ad5d4a1b7d98b723b682c3da4e60be7ca65a7b73](https://github.com/mcmmiguel/claude-tetris/commit/ad5d4a1b7d98b723b682c3da4e60be7ca65a7b73)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/mcmmiguel/claude-tetris

[Back to the awesome list](../../README.md)
