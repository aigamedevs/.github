# RoadRush LAN

> Verified game note.

![RoadRush LAN screenshot placeholder](roadrush-lan-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Auchit-Sawai/roadrush-lan](https://github.com/Auchit-Sawai/roadrush-lan)
- **Evidence:** [direct model evidence](https://github.com/Auchit-Sawai/roadrush-lan/commit/385ff309687ae135b70c11494138011fe3415c72)
- **Live demo:** [open demo](https://auchit-sawai.github.io/roadrush-lan/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Low-poly arcade motorcycle racing in the browser. Punch rivals, dodge traffic, outrun the police. Single-player online, LAN multiplayer for 2 to 8 riders. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Auchit-Sawai/roadrush-lan/blob/main/server/server.bundle.mjs](https://github.com/Auchit-Sawai/roadrush-lan/blob/main/server/server.bundle.mjs)
- [https://github.com/Auchit-Sawai/roadrush-lan/commit/385ff309687ae135b70c11494138011fe3415c72](https://github.com/Auchit-Sawai/roadrush-lan/commit/385ff309687ae135b70c11494138011fe3415c72)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Auchit-Sawai/roadrush-lan

[Back to the awesome list](../../README.md)
