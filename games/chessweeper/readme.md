# Chessweeper

> Verified game note.

![Chessweeper screenshot placeholder](chessweeper-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/aviate15/chessweeper](https://github.com/aviate15/chessweeper)
- **Evidence:** [direct model evidence](https://github.com/aviate15/chessweeper/commit/f8a175be51998693adadf749cd6544b1bf5c756d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Chess meets Minesweeper. Mines hide on the board, landing on a square reveals how many mines surround it, and pieces that step on a mine blow up. Kings have three lives. Numbers are public, flags are private, and every few turns (6 by default) without a… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/aviate15/chessweeper/blob/main/apps/server/src/server.ts](https://github.com/aviate15/chessweeper/blob/main/apps/server/src/server.ts)
- [https://github.com/aviate15/chessweeper/commit/f8a175be51998693adadf749cd6544b1bf5c756d](https://github.com/aviate15/chessweeper/commit/f8a175be51998693adadf749cd6544b1bf5c756d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/aviate15/chessweeper

[Back to the awesome list](../../README.md)
