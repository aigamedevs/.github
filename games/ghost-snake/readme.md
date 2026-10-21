# Ghost Snake

> Verified game note.

![Ghost Snake screenshot placeholder](ghost-snake-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/AbhishekSahukar/ghost-snake](https://github.com/AbhishekSahukar/ghost-snake)
- **Evidence:** [direct model evidence](https://github.com/AbhishekSahukar/ghost-snake/commit/71f8b67b99fc58b7dd1ff270a446f3d60b5342bc)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A retro-arcade take on Snake. Three ghosts wander the maze; eat the glowing power pellet and the tables turn for exactly five seconds. Plain HTML, CSS and JavaScript on a : no frameworks, no build step, no external assets. All sounds are synthesised with the… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AbhishekSahukar/ghost-snake/blob/feature/ghost-snake-game/js/renderer.js](https://github.com/AbhishekSahukar/ghost-snake/blob/feature/ghost-snake-game/js/renderer.js)
- [https://github.com/AbhishekSahukar/ghost-snake/commit/71f8b67b99fc58b7dd1ff270a446f3d60b5342bc](https://github.com/AbhishekSahukar/ghost-snake/commit/71f8b67b99fc58b7dd1ff270a446f3d60b5342bc)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/AbhishekSahukar/ghost-snake

[Back to the awesome list](../../README.md)
