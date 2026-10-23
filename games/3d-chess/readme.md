# 3D Chess

> Verified game note.

![3D Chess screenshot placeholder](3d-chess-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/businessfordevsav/3d-chess](https://github.com/businessfordevsav/3d-chess)
- **Evidence:** [direct model evidence](https://github.com/businessfordevsav/3d-chess/commit/ad5d931b61e70c918549f2c49a52ee355b6fc899)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D chess game that runs in the browser: Three.js renders the board, chess.js enforces the rules, and Stockfish 10 is the computer opponent. Everything lives in index.html, with the libraries loaded from a CDN. There is no build step. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/businessfordevsav/3d-chess/blob/main/index.html](https://github.com/businessfordevsav/3d-chess/blob/main/index.html)
- [https://github.com/businessfordevsav/3d-chess/commit/ad5d931b61e70c918549f2c49a52ee355b6fc899](https://github.com/businessfordevsav/3d-chess/commit/ad5d931b61e70c918549f2c49a52ee355b6fc899)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/businessfordevsav/3d-chess

[Back to the awesome list](../../README.md)
