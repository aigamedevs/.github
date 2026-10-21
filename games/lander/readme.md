# Lander

> Verified game note.

![Lander screenshot placeholder](lander-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/briandgoldberg/Lander](https://github.com/briandgoldberg/Lander)
- **Evidence:** [direct model evidence](https://github.com/briandgoldberg/Lander/commit/98fa3bc6753f6167f6a60a162538ad9136612f3d)
- **Live demo:** [open demo](https://lander-topaz.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Launch from one planet, land on another. Your JavaScript gets 10 seconds to plan the path. Most fuel left wins. Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/briandgoldberg/Lander/blob/main/index.html](https://github.com/briandgoldberg/Lander/blob/main/index.html)
- [https://github.com/briandgoldberg/Lander/commit/98fa3bc6753f6167f6a60a162538ad9136612f3d](https://github.com/briandgoldberg/Lander/commit/98fa3bc6753f6167f6a60a162538ad9136612f3d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/briandgoldberg/Lander

[Back to the awesome list](../../README.md)
