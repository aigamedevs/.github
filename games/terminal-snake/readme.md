# Terminal Snake

> Verified game note.

![Terminal Snake screenshot placeholder](terminal-snake-placeholder.svg)

## At a glance

- **Score:** 6.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust, crossterm, Terminal
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/Prashanth2902/Terminal-snake-game](https://github.com/Prashanth2902/Terminal-snake-game)
- **Evidence:** [direct model evidence](https://github.com/Prashanth2902/Terminal-snake-game/commit/d50b74788db950df69e2a22638b1da8e9527263d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Classic snake for the terminal in Rust with crossterm; speeds up with score, pause and restart. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/Prashanth2902/Terminal-snake-game/blob/main/src/game.rs](https://github.com/Prashanth2902/Terminal-snake-game/blob/main/src/game.rs)
- [https://github.com/Prashanth2902/Terminal-snake-game/commit/d50b74788db950df69e2a22638b1da8e9527263d](https://github.com/Prashanth2902/Terminal-snake-game/commit/d50b74788db950df69e2a22638b1da8e9527263d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/Prashanth2902/Terminal-snake-game

[Back to the awesome list](../../README.md)
