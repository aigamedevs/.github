# Paahde

> Verified game note.

![Paahde screenshot placeholder](paahde-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/woltsu/paahde](https://github.com/woltsu/paahde)
- **Evidence:** [direct model evidence](https://github.com/woltsu/paahde/commit/4691315ff90b8e269cb48c78cb56003d40ddf188)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online multiplayer desert survival game, made in the dadajam game jam (repo name: dadajam). three.js (WebGPU renderer, automatic WebGL2 fallback) + TypeScript + Vite,. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/woltsu/paahde/blob/main/tools/blender/crashsites.py](https://github.com/woltsu/paahde/blob/main/tools/blender/crashsites.py)
- [https://github.com/woltsu/paahde/commit/4691315ff90b8e269cb48c78cb56003d40ddf188](https://github.com/woltsu/paahde/commit/4691315ff90b8e269cb48c78cb56003d40ddf188)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/woltsu/paahde

[Back to the awesome list](../../README.md)
