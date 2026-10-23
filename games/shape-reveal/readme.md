# Shape Reveal

> Verified game note.

![Shape Reveal screenshot placeholder](shape-reveal-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game](https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game)
- **Evidence:** [direct model evidence](https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game/commit/7984bcadcf75d4c6e98a67f3a1dedb02f6ef4b82)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A picture puzzle played with falling Tetris shapes. Each piece carries the exact part of the picture that belongs on the board. Guide it into place; correct drops lock and reveal the image, while wrong drops come back in a retry order that never makes the… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game/blob/main/src/gameLogic.ts](https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game/blob/main/src/gameLogic.ts)
- [https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game/commit/7984bcadcf75d4c6e98a67f3a1dedb02f6ef4b82](https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game/commit/7984bcadcf75d4c6e98a67f3a1dedb02f6ef4b82)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Arsmi-17/arsmigames-tetris-picture-puzzle-web-game

[Back to the awesome list](../../README.md)
