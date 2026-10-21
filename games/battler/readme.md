# Battler

> Verified game note.

![Battler screenshot placeholder](battler-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ari0ch/battler](https://github.com/ari0ch/battler)
- **Evidence:** [direct model evidence](https://github.com/ari0ch/battler/commit/c474bdbfd37ffdd0e26e95190dc43db3217a4227)
- **Live demo:** [open demo](https://ari0ch.github.io/battler/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A fantasy autobattler prototype where you program your units' behaviour with a tiny. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ari0ch/battler/blob/main/crates/game/src/planning.rs](https://github.com/ari0ch/battler/blob/main/crates/game/src/planning.rs)
- [https://github.com/ari0ch/battler/commit/c474bdbfd37ffdd0e26e95190dc43db3217a4227](https://github.com/ari0ch/battler/commit/c474bdbfd37ffdd0e26e95190dc43db3217a4227)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ari0ch/battler

[Back to the awesome list](../../README.md)
