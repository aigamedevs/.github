# Emergent Tactics

> Verified game note.

![Emergent Tactics screenshot placeholder](emergent-tactics-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Fable 5.1
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/cfeduke/emergent-tactics](https://github.com/cfeduke/emergent-tactics)
- **Evidence:** [direct model evidence](https://github.com/cfeduke/emergent-tactics/commit/60ebf64308ad6daf43bbaf8e53a2fc8101158d90)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A card battler for learning ISMCTS + neural network opponents: Rust engine, PyTorch training, gRPC inference, SvelteKit client. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cfeduke/emergent-tactics/blob/main/crates/et-engine/src/state.rs](https://github.com/cfeduke/emergent-tactics/blob/main/crates/et-engine/src/state.rs)
- [https://github.com/cfeduke/emergent-tactics/commit/60ebf64308ad6daf43bbaf8e53a2fc8101158d90](https://github.com/cfeduke/emergent-tactics/commit/60ebf64308ad6daf43bbaf8e53a2fc8101158d90)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/cfeduke/emergent-tactics

[Back to the awesome list](../../README.md)
