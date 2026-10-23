# Stack to Orbit

> Verified game note.

![Stack to Orbit screenshot placeholder](stack-to-orbit-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/boidbit/stack-tower](https://github.com/boidbit/stack-tower)
- **Evidence:** [direct model evidence](https://github.com/boidbit/stack-tower/commit/de69ef8a8500c462a67c35c6debbc1fbc97a0b6c)
- **Live demo:** [open demo](https://boidbit.github.io/stack-tower/privacy.html)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A one-tap stacking game in a single HTML file (index.html). No build step, no dependencies, works offline. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/boidbit/stack-tower/blob/main/index.html](https://github.com/boidbit/stack-tower/blob/main/index.html)
- [https://github.com/boidbit/stack-tower/commit/de69ef8a8500c462a67c35c6debbc1fbc97a0b6c](https://github.com/boidbit/stack-tower/commit/de69ef8a8500c462a67c35c6debbc1fbc97a0b6c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/boidbit/stack-tower

[Back to the awesome list](../../README.md)
