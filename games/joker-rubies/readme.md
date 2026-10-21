# Joker Rubies

> Verified game note.

![Joker Rubies screenshot placeholder](joker-rubies-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/egr-meister/JokerRubies](https://github.com/egr-meister/JokerRubies)
- **Evidence:** [direct model evidence](https://github.com/egr-meister/JokerRubies/commit/7fdfe0f558d17fc5333a29d548e15990f4622014)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Joker Rubies — offline Android quiz & matching pairs game (Kotlin, Jetpack Compose). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/egr-meister/JokerRubies/blob/main/app/src/main/java/com/jokerrubies/game/ui/components/Components.kt](https://github.com/egr-meister/JokerRubies/blob/main/app/src/main/java/com/jokerrubies/game/ui/components/Components.kt)
- [https://github.com/egr-meister/JokerRubies/commit/7fdfe0f558d17fc5333a29d548e15990f4622014](https://github.com/egr-meister/JokerRubies/commit/7fdfe0f558d17fc5333a29d548e15990f4622014)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/egr-meister/JokerRubies

[Back to the awesome list](../../README.md)
