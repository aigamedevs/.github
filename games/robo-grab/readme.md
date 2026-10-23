# Robo-Grab

> Verified game note.

![Robo-Grab screenshot](https://raw.githubusercontent.com/Hauke12345/Robot/main/media/attempts_compare.png)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/Hauke12345/Robot/blob/main/media/attempts_compare.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Hauke12345/Robot](https://github.com/Hauke12345/Robot)
- **Evidence:** [direct model evidence](https://github.com/Hauke12345/Robot/commit/017632e8bdca8001cfd5f6e5ce76d51e039bd981)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Hauke12345/Robot/blob/main/media/attempts_compare.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Side-by-side robot arm attempts; diagram-like.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The arm has a shoulder joint, an elbow joint and a parallel gripper that always hangs straight down. The goal is to get the boxes into the bin. Everything runs on real 2D rigid-body physics (pymunk). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Hauke12345/Robot/blob/main/history/v2_physics_scripted_grip/robot.py](https://github.com/Hauke12345/Robot/blob/main/history/v2_physics_scripted_grip/robot.py)
- [https://github.com/Hauke12345/Robot/commit/017632e8bdca8001cfd5f6e5ce76d51e039bd981](https://github.com/Hauke12345/Robot/commit/017632e8bdca8001cfd5f6e5ce76d51e039bd981)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Hauke12345/Robot

[Back to the awesome list](../../README.md)
