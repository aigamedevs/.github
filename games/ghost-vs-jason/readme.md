# Ghost vs Jason

> Verified game note.

![Ghost vs Jason screenshot placeholder](ghost-vs-jason-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/Ander-tsx/horror-game](https://github.com/Ander-tsx/horror-game)
- **Evidence:** [direct model evidence](https://github.com/Ander-tsx/horror-game/commit/9b9e58c992298528b12d0e8135b9dc5659f5dcd2)
- **Live demo:** [open demo](https://ander-tsx.github.io/horror-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ghost vs Jason: juego de peleas retro pixel art de Halloween (Unity). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ander-tsx/horror-game/blob/main/Tools/pixelart/codex_char.py](https://github.com/Ander-tsx/horror-game/blob/main/Tools/pixelart/codex_char.py)
- [https://github.com/Ander-tsx/horror-game/commit/9b9e58c992298528b12d0e8135b9dc5659f5dcd2](https://github.com/Ander-tsx/horror-game/commit/9b9e58c992298528b12d0e8135b9dc5659f5dcd2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/Ander-tsx/horror-game

[Back to the awesome list](../../README.md)
