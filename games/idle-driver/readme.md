# Idle Driver

> Verified game note.

![Idle Driver screenshot placeholder](idle-driver-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/maybetallgames/Idle-Driver](https://github.com/maybetallgames/Idle-Driver)
- **Evidence:** [direct model evidence](https://github.com/maybetallgames/Idle-Driver/commit/7372eeaff421087654c2ac1994ce9e035fb68281)
- **Live demo:** [open demo](https://maybetallgames.github.io/Idle-Driver/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An idle game where you control the autopilot of a family SUV on its trip to the mountains. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/maybetallgames/Idle-Driver/blob/main/src/scene/scene.ts](https://github.com/maybetallgames/Idle-Driver/blob/main/src/scene/scene.ts)
- [https://github.com/maybetallgames/Idle-Driver/commit/7372eeaff421087654c2ac1994ce9e035fb68281](https://github.com/maybetallgames/Idle-Driver/commit/7372eeaff421087654c2ac1994ce9e035fb68281)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/maybetallgames/Idle-Driver

[Back to the awesome list](../../README.md)
