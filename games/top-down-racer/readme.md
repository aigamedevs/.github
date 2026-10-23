# Top Down Racer

> Verified game note.

![Top Down Racer screenshot placeholder](top-down-racer-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/ckopp22/SimpleRacing](https://github.com/ckopp22/SimpleRacing)
- **Evidence:** [direct model evidence](https://github.com/ckopp22/SimpleRacing/commit/dbb7f6b3997cb4b7d8924c023b6ec79637550e43)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

See MDD.md. Plain ES modules, vendored three.js (lib/), no build step. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ckopp22/SimpleRacing/blob/main/js/online.js](https://github.com/ckopp22/SimpleRacing/blob/main/js/online.js)
- [https://github.com/ckopp22/SimpleRacing/commit/dbb7f6b3997cb4b7d8924c023b6ec79637550e43](https://github.com/ckopp22/SimpleRacing/commit/dbb7f6b3997cb4b7d8924c023b6ec79637550e43)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/ckopp22/SimpleRacing

[Back to the awesome list](../../README.md)
