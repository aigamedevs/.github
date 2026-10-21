# Lane Runner

> Verified game note.

![Lane Runner screenshot placeholder](lane-runner-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Snehiths19/lane-runner](https://github.com/Snehiths19/lane-runner)
- **Evidence:** [direct model evidence](https://github.com/Snehiths19/lane-runner/commit/f55b8432b75858d8ef5b711210f3695814585b76)
- **Live demo:** [open demo](https://snehiths19.github.io/lane-runner/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Personal 3-lane endless runner (Subway Surfers-inspired) in Three.js - PC + phone. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Snehiths19/lane-runner/blob/main/src/world.js](https://github.com/Snehiths19/lane-runner/blob/main/src/world.js)
- [https://github.com/Snehiths19/lane-runner/commit/f55b8432b75858d8ef5b711210f3695814585b76](https://github.com/Snehiths19/lane-runner/commit/f55b8432b75858d8ef5b711210f3695814585b76)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Snehiths19/lane-runner

[Back to the awesome list](../../README.md)
