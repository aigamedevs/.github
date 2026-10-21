# Extremely Lifelike Fishing

> Verified game note.

![Extremely Lifelike Fishing screenshot placeholder](extremely-lifelike-fishing-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/sgilson7/el-fishing](https://github.com/sgilson7/el-fishing)
- **Evidence:** [direct model evidence](https://github.com/sgilson7/el-fishing/commit/f981a132dacaac50a78bf1f066e3f239c658ceec)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Extremely Lifelike Fishing: a 3D browser fishing game with a simulated sea, line and fish, built as a Builder project. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sgilson7/el-fishing/blob/main/crates/core/src/session.rs](https://github.com/sgilson7/el-fishing/blob/main/crates/core/src/session.rs)
- [https://github.com/sgilson7/el-fishing/commit/f981a132dacaac50a78bf1f066e3f239c658ceec](https://github.com/sgilson7/el-fishing/commit/f981a132dacaac50a78bf1f066e3f239c658ceec)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/sgilson7/el-fishing

[Back to the awesome list](../../README.md)
