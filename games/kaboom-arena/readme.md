# Kaboom Arena

> Verified game note.

![Kaboom Arena screenshot placeholder](kaboom-arena-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Ruby, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/janroudaut/kaboom-arena](https://github.com/janroudaut/kaboom-arena)
- **Evidence:** [direct model evidence](https://github.com/janroudaut/kaboom-arena/commit/df2e3dcd3435174ac86ac9ce674384c3fb00cf4b)
- **Live demo:** [open demo](https://kaboom.philament.club)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Bomberman-style bomb arena: solo against bots, local or online rooms, 2D and 3D renderers, installable PWA. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/janroudaut/kaboom-arena/blob/main/public/game/render3d.js](https://github.com/janroudaut/kaboom-arena/blob/main/public/game/render3d.js)
- [https://github.com/janroudaut/kaboom-arena/commit/df2e3dcd3435174ac86ac9ce674384c3fb00cf4b](https://github.com/janroudaut/kaboom-arena/commit/df2e3dcd3435174ac86ac9ce674384c3fb00cf4b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/janroudaut/kaboom-arena

[Back to the awesome list](../../README.md)
