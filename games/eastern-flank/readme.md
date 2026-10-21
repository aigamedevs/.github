# Eastern Flank

> Verified game note.

![Eastern Flank screenshot](https://raw.githubusercontent.com/dawidczarczynski/eastern-flank/master/docs/images/gameplay.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 6.8/10 ([manually reviewed image](https://github.com/dawidczarczynski/eastern-flank/blob/master/docs/images/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/dawidczarczynski/eastern-flank](https://github.com/dawidczarczynski/eastern-flank)
- **Evidence:** [direct model evidence](https://github.com/dawidczarczynski/eastern-flank/commit/27db5f415338f1f9f21d91bcb4412f81d5ce5c24)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/dawidczarczynski/eastern-flank/blob/master/docs/images/gameplay.png) — 📸 6.8/10 · manual visual review · Use this frame for the game-level score. 3D hex terrain with tanks, trees, selection highlight and turn bar; clean, readable strategy view.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Turn-based tactical 3D strategy on hexes – Godot 4 (GDScript), developed with the help of AI agents (Claude Code). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dawidczarczynski/eastern-flank/blob/master/docs/design/v2/game_screen.scene.js](https://github.com/dawidczarczynski/eastern-flank/blob/master/docs/design/v2/game_screen.scene.js)
- [https://github.com/dawidczarczynski/eastern-flank/commit/27db5f415338f1f9f21d91bcb4412f81d5ce5c24](https://github.com/dawidczarczynski/eastern-flank/commit/27db5f415338f1f9f21d91bcb4412f81d5ce5c24)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/dawidczarczynski/eastern-flank

[Back to the awesome list](../../README.md)
