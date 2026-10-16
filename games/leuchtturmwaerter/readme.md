# Leuchtturmwaerter

> Verified game note.

![Leuchtturmwaerter screenshot placeholder](leuchtturmwaerter-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/dtghgthf/BrowserGame](https://github.com/dtghgthf/BrowserGame)
- **Evidence:** [direct model evidence](https://github.com/dtghgthf/BrowserGame/commit/381c9fce73a6955805df31db38bc19d2129201fa)
- **Live demo:** [open demo](https://game.echterhofflabs.me)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Co-op browser game for 2-4 players without voice: run ship stations together through storm, fog and kraken attacks to reach the lighthouse; shared simulation plus server. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/dtghgthf/BrowserGame/blob/claude/leuchtturmwaerter-game-sprqmg/shared/src/simulation.ts](https://github.com/dtghgthf/BrowserGame/blob/claude/leuchtturmwaerter-game-sprqmg/shared/src/simulation.ts)
- [https://github.com/dtghgthf/BrowserGame/commit/381c9fce73a6955805df31db38bc19d2129201fa](https://github.com/dtghgthf/BrowserGame/commit/381c9fce73a6955805df31db38bc19d2129201fa)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/dtghgthf/BrowserGame

[Back to the awesome list](../../README.md)
