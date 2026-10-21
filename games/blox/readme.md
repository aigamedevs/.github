# BloX

> Verified game note.

![BloX screenshot placeholder](blox-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/magori/blox](https://github.com/magori/blox)
- **Evidence:** [direct model evidence](https://github.com/magori/blox/commit/a3d4b105b322503b19438f7057da38729f7c1135)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jeu de blocs pour Android, à usage personnel. Premier mode : Classique, fidèle aux règles. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/magori/blox/blob/main/feature/home/src/androidTest/kotlin/ch/magori/blox/feature/home/HomeScreenTest.kt](https://github.com/magori/blox/blob/main/feature/home/src/androidTest/kotlin/ch/magori/blox/feature/home/HomeScreenTest.kt)
- [https://github.com/magori/blox/commit/a3d4b105b322503b19438f7057da38729f7c1135](https://github.com/magori/blox/commit/a3d4b105b322503b19438f7057da38729f7c1135)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/magori/blox

[Back to the awesome list](../../README.md)
