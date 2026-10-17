# Chameleon

> Verified game note.

![Chameleon screenshot placeholder](chameleon-destrukter-chameleon-app-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/destrukter/Chameleon_app](https://github.com/destrukter/Chameleon_app)
- **Evidence:** [direct model evidence](https://github.com/destrukter/Chameleon_app/commit/f85a05a062ae145d4b366ec2fe5cd34f236a5346)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An Android take on the social-deduction party game The Chameleon: everybody knows the secret word except. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/destrukter/Chameleon_app/blob/claude/eager-feynman-ibqoc4/app/src/main/java/com/destrukter/chameleon/ui/OnlineScreens.kt](https://github.com/destrukter/Chameleon_app/blob/claude/eager-feynman-ibqoc4/app/src/main/java/com/destrukter/chameleon/ui/OnlineScreens.kt)
- [https://github.com/destrukter/Chameleon_app/commit/f85a05a062ae145d4b366ec2fe5cd34f236a5346](https://github.com/destrukter/Chameleon_app/commit/f85a05a062ae145d4b366ec2fe5cd34f236a5346)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/destrukter/Chameleon_app

[Back to the awesome list](../../README.md)
