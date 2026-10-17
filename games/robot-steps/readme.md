# Robot Steps

> Verified game note.

![Robot Steps screenshot](https://raw.githubusercontent.com/plwg/robot-steps/master/docs/level.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/plwg/robot-steps/blob/master/docs/level.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/plwg/robot-steps](https://github.com/plwg/robot-steps)
- **Evidence:** [direct model evidence](https://github.com/plwg/robot-steps/commit/fdab82a50592c5e2c373148e983c276ae38a3157)
- **Live demo:** [open demo](https://plwg.github.io/robot-steps/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/plwg/robot-steps/blob/master/docs/level.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Kids coding puzzle board with robot, stars, rocks and an arrow program strip; clean and friendly, flat UI art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A first coding game for young kids, written in Rust: program a robot with arrows, loops and ifs. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/plwg/robot-steps/blob/master/src/main.rs](https://github.com/plwg/robot-steps/blob/master/src/main.rs)
- [https://github.com/plwg/robot-steps/commit/fdab82a50592c5e2c373148e983c276ae38a3157](https://github.com/plwg/robot-steps/commit/fdab82a50592c5e2c373148e983c276ae38a3157)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/plwg/robot-steps

[Back to the awesome list](../../README.md)
