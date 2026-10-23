# Chess Platform

> Verified game note.

![Chess Platform screenshot placeholder](chess-platform-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/jaymandaliya/chess-game](https://github.com/jaymandaliya/chess-game)
- **Evidence:** [direct model evidence](https://github.com/jaymandaliya/chess-game/commit/b9eece65d1bfc431c88dd2f253044eb4947e0fa9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online chess platform: a player app for Android and iOS, an admin web portal, and the backend that runs the API,. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jaymandaliya/chess-game/blob/main/backend/src/game/gameManager.js](https://github.com/jaymandaliya/chess-game/blob/main/backend/src/game/gameManager.js)
- [https://github.com/jaymandaliya/chess-game/commit/b9eece65d1bfc431c88dd2f253044eb4947e0fa9](https://github.com/jaymandaliya/chess-game/commit/b9eece65d1bfc431c88dd2f253044eb4947e0fa9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/jaymandaliya/chess-game

[Back to the awesome list](../../README.md)
