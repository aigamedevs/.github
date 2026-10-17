# Mage Tower Battle

> Verified game note.

![Mage Tower Battle screenshot placeholder](mage-tower-battle-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/sgilson7/mage-tower-battle](https://github.com/sgilson7/mage-tower-battle)
- **Evidence:** [direct model evidence](https://github.com/sgilson7/mage-tower-battle/commit/97e02b5a84959694766c84612e456135bb8e9042)
- **Live demo:** [open demo](https://sgilson7.github.io/mage-tower-battle/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Builder game: rebuild a wrecked mage college's library, craft spells from pieces, teach students by drawing, then watch four towers hold. Rust core, WebAssembly, WebGL. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sgilson7/mage-tower-battle/blob/main/crates/core/src/session.rs](https://github.com/sgilson7/mage-tower-battle/blob/main/crates/core/src/session.rs)
- [https://github.com/sgilson7/mage-tower-battle/commit/97e02b5a84959694766c84612e456135bb8e9042](https://github.com/sgilson7/mage-tower-battle/commit/97e02b5a84959694766c84612e456135bb8e9042)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/sgilson7/mage-tower-battle

[Back to the awesome list](../../README.md)
