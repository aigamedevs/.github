# Tic-Tac-Toe for Two

> Verified game note.

![Tic-Tac-Toe for Two screenshot placeholder](tic-tac-toe-for-two-placeholder.svg)

## At a glance

- **Score:** 6.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Python, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/YeseniaCarrasco/tictactoe-online](https://github.com/YeseniaCarrasco/tictactoe-online)
- **Evidence:** [direct model evidence](https://github.com/YeseniaCarrasco/tictactoe-online/commit/28706bbe8c537a268e19ebf2b1fc1f2d23eabdb3)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A two-player tic-tac-toe game built with Flask. Two people each play in their own browser, and the server runs the game: it keeps the board, makes sure players take turns, and decides who won. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/YeseniaCarrasco/tictactoe-online/blob/main/app.py](https://github.com/YeseniaCarrasco/tictactoe-online/blob/main/app.py)
- [https://github.com/YeseniaCarrasco/tictactoe-online/commit/28706bbe8c537a268e19ebf2b1fc1f2d23eabdb3](https://github.com/YeseniaCarrasco/tictactoe-online/commit/28706bbe8c537a268e19ebf2b1fc1f2d23eabdb3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/YeseniaCarrasco/tictactoe-online

[Back to the awesome list](../../README.md)
