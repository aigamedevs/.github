# Bridge Lab

> Verified game note.

![Bridge Lab screenshot placeholder](bridge-lab-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/KFTamang/sim_game](https://github.com/KFTamang/sim_game)
- **Evidence:** [direct model evidence](https://github.com/KFTamang/sim_game/commit/befe9362cbe3911680eb02b4cfcba5b5ebf9eacd)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Physics-intuition game: design 2D truss bridges and chase high scores; solver and design modules in bridge_lab/. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/KFTamang/sim_game/blob/main/bridge_lab/js/game.js](https://github.com/KFTamang/sim_game/blob/main/bridge_lab/js/game.js)
- [https://github.com/KFTamang/sim_game/commit/befe9362cbe3911680eb02b4cfcba5b5ebf9eacd](https://github.com/KFTamang/sim_game/commit/befe9362cbe3911680eb02b4cfcba5b5ebf9eacd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/KFTamang/sim_game

[Back to the awesome list](../../README.md)
