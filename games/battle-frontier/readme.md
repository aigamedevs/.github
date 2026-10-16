# Battle Frontier

> Verified game note.

![Battle Frontier screenshot placeholder](battle-frontier-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Rust, WebAssembly, WebGPU, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/LouisMareau/battle-frontier](https://github.com/LouisMareau/battle-frontier)
- **Evidence:** [direct model evidence](https://github.com/LouisMareau/battle-frontier/commit/ddd0a312b57bd14bf7e30da8ed05c9ea6161668f)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Original creature-catching RPG and engine in Rust for browser and desktop with timing-based battles, a content browser and a map editor. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/LouisMareau/battle-frontier/blob/main/crates/core/src/battle.rs](https://github.com/LouisMareau/battle-frontier/blob/main/crates/core/src/battle.rs)
- [https://github.com/LouisMareau/battle-frontier/commit/ddd0a312b57bd14bf7e30da8ed05c9ea6161668f](https://github.com/LouisMareau/battle-frontier/commit/ddd0a312b57bd14bf7e30da8ed05c9ea6161668f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/LouisMareau/battle-frontier

[Back to the awesome list](../../README.md)
