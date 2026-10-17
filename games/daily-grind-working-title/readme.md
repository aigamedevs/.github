# Daily Grind (working title)

> Verified game note.

![Daily Grind (working title) screenshot placeholder](daily-grind-working-title-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/JohnnyNero/daily-grind](https://github.com/JohnnyNero/daily-grind)
- **Evidence:** [direct model evidence](https://github.com/JohnnyNero/daily-grind/commit/05dbbc9a574149b3ccb76fe5e77c7b1d2ae8c85b)
- **Live demo:** [open demo](https://johnnynero.github.io/daily-grind/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A café sim for phones. You set up the café, staff it with characters you made up or recognise from work, and watch it run. Inspired by RimWorld's emergent drama and the Sims' everyday autonomy; drawn in the "Pawn" style. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/JohnnyNero/daily-grind/blob/main/src/sim/sim.ts](https://github.com/JohnnyNero/daily-grind/blob/main/src/sim/sim.ts)
- [https://github.com/JohnnyNero/daily-grind/commit/05dbbc9a574149b3ccb76fe5e77c7b1d2ae8c85b](https://github.com/JohnnyNero/daily-grind/commit/05dbbc9a574149b3ccb76fe5e77c7b1d2ae8c85b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/JohnnyNero/daily-grind

[Back to the awesome list](../../README.md)
