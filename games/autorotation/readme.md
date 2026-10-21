# Autorotation

> Verified game note.

![Autorotation screenshot placeholder](autorotation-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/CarlosEscat/autorotation-game](https://github.com/CarlosEscat/autorotation-game)
- **Evidence:** [direct model evidence](https://github.com/CarlosEscat/autorotation-game/commit/02c4d07baa901f9dbf17990ccafb0824f772221b)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser-based, low-poly 3D helicopter arcade game in the style of N64-era graphics. You are cruising along when the engine quits. Lower the collective, manage rotor RPM and airspeed, pick a field, flare, and cushion the touchdown. Every attempt is scored… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/CarlosEscat/autorotation-game/blob/main/src/game/levels.ts](https://github.com/CarlosEscat/autorotation-game/blob/main/src/game/levels.ts)
- [https://github.com/CarlosEscat/autorotation-game/commit/02c4d07baa901f9dbf17990ccafb0824f772221b](https://github.com/CarlosEscat/autorotation-game/commit/02c4d07baa901f9dbf17990ccafb0824f772221b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/CarlosEscat/autorotation-game

[Back to the awesome list](../../README.md)
