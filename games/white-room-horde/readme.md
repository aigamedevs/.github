# white-room-horde

> Verified game note.

![white-room-horde screenshot placeholder](white-room-horde-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/gkaragoz/white-room-horde](https://github.com/gkaragoz/white-room-horde)
- **Evidence:** [direct model evidence](https://github.com/gkaragoz/white-room-horde/commit/9b9f306fc73f2a80a6faca86530e9c119c15991b)
- **Live demo:** [open demo](https://gkaragoz.github.io/white-room-horde/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A co-op top-down horde shooter that runs in the browser (Three.js). Up to 11 players, one deterministic simulation that every client runs in lockstep, a 30 Hz tick, and a floor that keeps climbing: clear a floor and the squad is lifted to the next one. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/gkaragoz/white-room-horde/blob/main/packages/client/src/ui.ts](https://github.com/gkaragoz/white-room-horde/blob/main/packages/client/src/ui.ts)
- [https://github.com/gkaragoz/white-room-horde/commit/9b9f306fc73f2a80a6faca86530e9c119c15991b](https://github.com/gkaragoz/white-room-horde/commit/9b9f306fc73f2a80a6faca86530e9c119c15991b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/gkaragoz/white-room-horde

[Back to the awesome list](../../README.md)
