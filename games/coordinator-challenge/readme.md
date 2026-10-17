# Coordinator Challenge

> Verified game note.

![Coordinator Challenge screenshot placeholder](coordinator-challenge-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/benjtharm41/coordinator-challenge](https://github.com/benjtharm41/coordinator-challenge)
- **Evidence:** [direct model evidence](https://github.com/benjtharm41/coordinator-challenge/commit/2d4f917ea00cb4263023cd8820c3fa115476a3d4)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Mobile NFL play-calling game: call every play on offense and defense. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/benjtharm41/coordinator-challenge/blob/main/src/ui/app.ts](https://github.com/benjtharm41/coordinator-challenge/blob/main/src/ui/app.ts)
- [https://github.com/benjtharm41/coordinator-challenge/commit/2d4f917ea00cb4263023cd8820c3fa115476a3d4](https://github.com/benjtharm41/coordinator-challenge/commit/2d4f917ea00cb4263023cd8820c3fa115476a3d4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/benjtharm41/coordinator-challenge

[Back to the awesome list](../../README.md)
