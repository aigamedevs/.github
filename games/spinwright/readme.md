# Spinwright

> Verified game note.

![Spinwright screenshot placeholder](spinwright-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, PixiJS, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/DavidNyholm/spinwright](https://github.com/DavidNyholm/spinwright)
- **Evidence:** [direct model evidence](https://github.com/DavidNyholm/spinwright/commit/3ec63da65feda496409924a1d2a764f660f13372)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Play-money slot machines and a clicker, in TypeScript and PixiJS. Pure math engines checked by exact calculation and Monte Carlo simulation, free spins with locked wilds, a cascade machine with a heat multiplier, and a Forge clicker that earns the credits.… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/DavidNyholm/spinwright/blob/main/src/ui/cascadeView.ts](https://github.com/DavidNyholm/spinwright/blob/main/src/ui/cascadeView.ts)
- [https://github.com/DavidNyholm/spinwright/commit/3ec63da65feda496409924a1d2a764f660f13372](https://github.com/DavidNyholm/spinwright/commit/3ec63da65feda496409924a1d2a764f660f13372)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub repository search: exact model phrase, created 2026-10-17T01:30Z..2026-10-21T01:00Z; https://github.com/DavidNyholm/spinwright

[Back to the awesome list](../../README.md)
