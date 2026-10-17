# Игра-детектив (браузер, three.js)

> Verified game note.

![Игра-детектив (браузер, three.js) screenshot placeholder](three-js-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/rysev-a/game](https://github.com/rysev-a/game)
- **Evidence:** [direct model evidence](https://github.com/rysev-a/game/commit/76f2ebcdee4b422c95419151a26c092ae6e4ecc6)
- **Live demo:** [open demo](https://rysev-a.github.io/game/)
- **Additional live link:** [open demo](https://rysev-a.github.io/game/demo/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

На телефоне и планшете игра включает сенсорное управление сама и играется только горизонтально. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/rysev-a/game/blob/main/src/demo/race.js](https://github.com/rysev-a/game/blob/main/src/demo/race.js)
- [https://github.com/rysev-a/game/commit/76f2ebcdee4b422c95419151a26c092ae6e4ecc6](https://github.com/rysev-a/game/commit/76f2ebcdee4b422c95419151a26c092ae6e4ecc6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/rysev-a/game

[Back to the awesome list](../../README.md)
