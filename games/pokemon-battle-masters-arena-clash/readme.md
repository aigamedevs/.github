# Pokemon Battle Masters (Arena Clash)

> Verified game note.

![Pokemon Battle Masters (Arena Clash) screenshot placeholder](pokemon-battle-masters-arena-clash-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/TxHandles/pokemonarena](https://github.com/TxHandles/pokemonarena)
- **Evidence:** [direct model evidence](https://github.com/TxHandles/pokemonarena/commit/f1130f508dbe8620c4eae9baf8c639c6bdd6c83a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 2D real-time Pokemon arena battler in C++ with raylib: 18 types, ~170 moves with Pokemon-style. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/TxHandles/pokemonarena/blob/main/src/screens_story.cpp](https://github.com/TxHandles/pokemonarena/blob/main/src/screens_story.cpp)
- [https://github.com/TxHandles/pokemonarena/commit/f1130f508dbe8620c4eae9baf8c639c6bdd6c83a](https://github.com/TxHandles/pokemonarena/commit/f1130f508dbe8620c4eae9baf8c639c6bdd6c83a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/TxHandles/pokemonarena

[Back to the awesome list](../../README.md)
