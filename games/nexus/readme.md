# NEXUS

> Verified game note.

![NEXUS screenshot placeholder](nexus-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/noahkoldow/triviagame](https://github.com/noahkoldow/triviagame)
- **Evidence:** [direct model evidence](https://github.com/noahkoldow/triviagame/commit/d83108c2e0e670899aecca1e7e7e6ec9dc540ed7)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Wissens-Quiz im zerstörten Netzwerk: Baue vom zentralen Chip aus Bahnen wieder auf, sammle Datenfragmente, merke sie dir und beantworte Fragen. Konzept: docs/CONCEPT.md. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/noahkoldow/triviagame/blob/main/packages/shared/src/content.ts](https://github.com/noahkoldow/triviagame/blob/main/packages/shared/src/content.ts)
- [https://github.com/noahkoldow/triviagame/commit/d83108c2e0e670899aecca1e7e7e6ec9dc540ed7](https://github.com/noahkoldow/triviagame/commit/d83108c2e0e670899aecca1e7e7e6ec9dc540ed7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/noahkoldow/triviagame

[Back to the awesome list](../../README.md)
