# darmok-games

> Verified game note.

![darmok-games screenshot placeholder](darmok-games-placeholder.svg)

## At a glance

- **Score:** 6.2/10
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/EinarTho/darmok-games](https://github.com/EinarTho/darmok-games)
- **Evidence:** [direct model evidence](https://github.com/EinarTho/darmok-games/commit/d947152fa0f3bae1b449d5995573c7946173cc72)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Tic-tac-toe and Game of Life in the Darmok (Tamarian) language. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/EinarTho/darmok-games/blob/main/tictactoe.c](https://github.com/EinarTho/darmok-games/blob/main/tictactoe.c)
- [https://github.com/EinarTho/darmok-games/commit/d947152fa0f3bae1b449d5995573c7946173cc72](https://github.com/EinarTho/darmok-games/commit/d947152fa0f3bae1b449d5995573c7946173cc72)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/EinarTho/darmok-games

[Back to the awesome list](../../README.md)
