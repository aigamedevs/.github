# Bee Factory

> Verified game note.

![Bee Factory screenshot placeholder](bee-factory-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/FlorianDaunay/bee-factory](https://github.com/FlorianDaunay/bee-factory)
- **Evidence:** [direct model evidence](https://github.com/FlorianDaunay/bee-factory/commit/591e44f866c74e9ec7ff9c9b062c6ca8a1e9b946)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A cute gacha game about bees. Build hives that make honey, open country packs to recruit bees from around the world, and lead teams of up to six through a turn-based story (Brave Frontier style). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/FlorianDaunay/bee-factory/blob/main/src/features/battle/BattleScreen.tsx](https://github.com/FlorianDaunay/bee-factory/blob/main/src/features/battle/BattleScreen.tsx)
- [https://github.com/FlorianDaunay/bee-factory/commit/591e44f866c74e9ec7ff9c9b062c6ca8a1e9b946](https://github.com/FlorianDaunay/bee-factory/commit/591e44f866c74e9ec7ff9c9b062c6ca8a1e9b946)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/FlorianDaunay/bee-factory

[Back to the awesome list](../../README.md)
