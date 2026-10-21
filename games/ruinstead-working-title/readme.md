# Ruinstead (working title)

> Verified game note.

![Ruinstead (working title) screenshot placeholder](ruinstead-working-title-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Kinheadpump/PCS](https://github.com/Kinheadpump/PCS)
- **Evidence:** [direct model evidence](https://github.com/Kinheadpump/PCS/commit/42182d70af22b3471edf98ad5b26f7c5288a2b9e)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A lightweight, top-down, pixel-art colony simulation in Rust. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Kinheadpump/PCS/blob/main/crates/base/src/content.rs](https://github.com/Kinheadpump/PCS/blob/main/crates/base/src/content.rs)
- [https://github.com/Kinheadpump/PCS/commit/42182d70af22b3471edf98ad5b26f7c5288a2b9e](https://github.com/Kinheadpump/PCS/commit/42182d70af22b3471edf98ad5b26f7c5288a2b9e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Kinheadpump/PCS

[Back to the awesome list](../../README.md)
