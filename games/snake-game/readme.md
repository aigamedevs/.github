# Snake Game

> Verified game note.

![Snake Game screenshot placeholder](snake-game-placeholder.svg)

## At a glance

- **Score:** 6.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/VAHTKA/snake-game](https://github.com/VAHTKA/snake-game)
- **Evidence:** [direct model evidence](https://github.com/VAHTKA/snake-game/commit/870075fe8289d80c8e5adc888729030c9dcfc4a1)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Classic Snake game in Python (tkinter) with levels, obstacles, bonus food and high scores. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/VAHTKA/snake-game/blob/main/snake-game.py](https://github.com/VAHTKA/snake-game/blob/main/snake-game.py)
- [https://github.com/VAHTKA/snake-game/commit/870075fe8289d80c8e5adc888729030c9dcfc4a1](https://github.com/VAHTKA/snake-game/commit/870075fe8289d80c8e5adc888729030c9dcfc4a1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/VAHTKA/snake-game

[Back to the awesome list](../../README.md)
