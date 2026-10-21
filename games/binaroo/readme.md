# Binaroo

> Verified game note.

![Binaroo screenshot placeholder](binaroo-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Gernika-Labs/binaroo](https://github.com/Gernika-Labs/binaroo)
- **Evidence:** [direct model evidence](https://github.com/Gernika-Labs/binaroo/commit/d12847fe078e6bcd3c6e9378d06302ea7f8c6d9c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A mobile puzzle game that teaches binary. Fill an 8-wide board so each row's bits add up to its target number, before the row's timer runs out. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Gernika-Labs/binaroo/blob/main/game/src/app.ts](https://github.com/Gernika-Labs/binaroo/blob/main/game/src/app.ts)
- [https://github.com/Gernika-Labs/binaroo/commit/d12847fe078e6bcd3c6e9378d06302ea7f8c6d9c](https://github.com/Gernika-Labs/binaroo/commit/d12847fe078e6bcd3c6e9378d06302ea7f8c6d9c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Gernika-Labs/binaroo

[Back to the awesome list](../../README.md)
