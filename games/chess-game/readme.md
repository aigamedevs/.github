# Chess Game

> Verified game note.

![Chess Game screenshot placeholder](chess-game-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/rochano/chess](https://github.com/rochano/chess)
- **Evidence:** [direct model evidence](https://github.com/rochano/chess/commit/3dc06dc69878280a0a1644cd4da42e2289acc3d8)
- **Live demo:** [open demo](https://rochano.github.io/chess/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A playable chess game in a single HTML page: two players on one device or against the computer, with clocks, hints, undo and full rules (castling, en passant, promotion, stalemate and draw rules). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/rochano/chess/blob/main/index.html](https://github.com/rochano/chess/blob/main/index.html)
- [https://github.com/rochano/chess/commit/3dc06dc69878280a0a1644cd4da42e2289acc3d8](https://github.com/rochano/chess/commit/3dc06dc69878280a0a1644cd4da42e2289acc3d8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/rochano/chess

[Back to the awesome list](../../README.md)
