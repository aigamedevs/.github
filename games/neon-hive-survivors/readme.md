# Neon Hive Survivors 霓虹虫巢幸存者

> Verified game note.

![Neon Hive Survivors 霓虹虫巢幸存者 screenshot placeholder](neon-hive-survivors-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/machuiwen/swarm-survivor](https://github.com/machuiwen/swarm-survivor)
- **Evidence:** [direct model evidence](https://github.com/machuiwen/swarm-survivor/commit/9f22b8d68c7ae66c830d59c00bf130e82849515c)
- **Live demo:** [open demo](https://machuiwen.github.io/swarm-survivor/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A neon survivor-style browser game. You only move: your weapons fire on their own. Survive 15 minutes of the bug swarm and defeat the final boss, the Void Lord. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/machuiwen/swarm-survivor/blob/main/js/game.js](https://github.com/machuiwen/swarm-survivor/blob/main/js/game.js)
- [https://github.com/machuiwen/swarm-survivor/commit/9f22b8d68c7ae66c830d59c00bf130e82849515c](https://github.com/machuiwen/swarm-survivor/commit/9f22b8d68c7ae66c830d59c00bf130e82849515c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/machuiwen/swarm-survivor

[Back to the awesome list](../../README.md)
