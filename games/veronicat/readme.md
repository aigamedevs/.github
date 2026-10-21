# Veronicat

> Verified game note.

![Veronicat screenshot placeholder](veronicat-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/k0-ba/veronicat](https://github.com/k0-ba/veronicat)
- **Evidence:** [direct model evidence](https://github.com/k0-ba/veronicat/commit/c06681452e04e319f54be14677260b3a32d64b7d)
- **Live demo:** [open demo](https://veronicat.pages.dev/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Veronicat — Stray-like cat game, three.js vertical slice. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/k0-ba/veronicat/blob/main/src/world/Lakotelep.ts](https://github.com/k0-ba/veronicat/blob/main/src/world/Lakotelep.ts)
- [https://github.com/k0-ba/veronicat/commit/c06681452e04e319f54be14677260b3a32d64b7d](https://github.com/k0-ba/veronicat/commit/c06681452e04e319f54be14677260b3a32d64b7d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/k0-ba/veronicat

[Back to the awesome list](../../README.md)
