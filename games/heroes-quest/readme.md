# Heroes Quest

> Verified game note.

![Heroes Quest screenshot placeholder](heroes-quest-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/mshaffe1111/Heroes-Quest](https://github.com/mshaffe1111/Heroes-Quest)
- **Evidence:** [direct model evidence](https://github.com/mshaffe1111/Heroes-Quest/commit/fe16a35b03e8d9e85c4e43f58b017b05305a5bf7)
- **Live demo:** [open demo](https://mshaffe1111.github.io/Heroes-Quest/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Turn based strategy game where you conquer tte world. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mshaffe1111/Heroes-Quest/blob/main/docs/play/game.js](https://github.com/mshaffe1111/Heroes-Quest/blob/main/docs/play/game.js)
- [https://github.com/mshaffe1111/Heroes-Quest/commit/fe16a35b03e8d9e85c4e43f58b017b05305a5bf7](https://github.com/mshaffe1111/Heroes-Quest/commit/fe16a35b03e8d9e85c4e43f58b017b05305a5bf7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/mshaffe1111/Heroes-Quest

[Back to the awesome list](../../README.md)
