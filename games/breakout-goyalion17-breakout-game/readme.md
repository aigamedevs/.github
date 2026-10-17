# Breakout

> Verified game note.

![Breakout screenshot](https://raw.githubusercontent.com/goyalion17/breakout-game/main/screenshot.png)

## At a glance

- **Score:** 6.4/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/goyalion17/breakout-game/blob/main/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/goyalion17/breakout-game](https://github.com/goyalion17/breakout-game)
- **Evidence:** [direct model evidence](https://github.com/goyalion17/breakout-game/commit/cad21d5cdbe7d8ced8c4fc8f18e6b0b1302bb941)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/goyalion17/breakout-game/blob/main/screenshot.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Turtle-graphics Breakout with brick rows on a game-over screen; very basic.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Classic Breakout arcade game in Python (turtle): levels, lives, high score, sound effects. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/goyalion17/breakout-game/blob/main/main.py](https://github.com/goyalion17/breakout-game/blob/main/main.py)
- [https://github.com/goyalion17/breakout-game/commit/cad21d5cdbe7d8ced8c4fc8f18e6b0b1302bb941](https://github.com/goyalion17/breakout-game/commit/cad21d5cdbe7d8ced8c4fc8f18e6b0b1302bb941)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/goyalion17/breakout-game

[Back to the awesome list](../../README.md)
