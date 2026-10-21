# RoomShift

> Verified game note.

![RoomShift screenshot placeholder](roomshift-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Jenil005/roomshift](https://github.com/Jenil005/roomshift)
- **Evidence:** [direct model evidence](https://github.com/Jenil005/roomshift/commit/efedf7b7ae11495687281a1347377da41f0cda6a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

RoomShift is a cooperative mixed-reality puzzle game: players in the same room get different private clues on their phones, talk to each other, and arrange real objects to restore power to a virtual facility. The server decides every outcome. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Jenil005/roomshift/blob/main/backend/src/game/engine.ts](https://github.com/Jenil005/roomshift/blob/main/backend/src/game/engine.ts)
- [https://github.com/Jenil005/roomshift/commit/efedf7b7ae11495687281a1347377da41f0cda6a](https://github.com/Jenil005/roomshift/commit/efedf7b7ae11495687281a1347377da41f0cda6a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Jenil005/roomshift

[Back to the awesome list](../../README.md)
