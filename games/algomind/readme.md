# Algomind

> Verified game note.

![Algomind screenshot](https://raw.githubusercontent.com/shahadathhs/Algomind/main/docs/design/overview-light.png)

## At a glance

- **Score:** 8.0/10
- **Screenshot rating:** 3.4/10 ([manually reviewed image](https://github.com/shahadathhs/Algomind/blob/main/docs/design/overview-light.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/shahadathhs/Algomind](https://github.com/shahadathhs/Algomind)
- **Evidence:** [direct model evidence](https://github.com/shahadathhs/Algomind/commit/2af2cde822af0587c77ff6b881ded4dc5fb21466)
- **Live demo:** [open demo](https://playalgomind.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/shahadathhs/Algomind/blob/main/docs/design/overview-light.png) — 📸 3.4/10 · manual visual review · Use this frame for the game-level score. Sheet of many small app screens showing tile puzzles; a design overview rather than one game frame.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A programming puzzle for Android. Build a program from instruction tiles, run it, and guide the automaton to the target. Offline first. No ads. No purchases. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/shahadathhs/Algomind/blob/main/apps/game/addons/gut/gut.gd](https://github.com/shahadathhs/Algomind/blob/main/apps/game/addons/gut/gut.gd)
- [https://github.com/shahadathhs/Algomind/commit/2af2cde822af0587c77ff6b881ded4dc5fb21466](https://github.com/shahadathhs/Algomind/commit/2af2cde822af0587c77ff6b881ded4dc5fb21466)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/shahadathhs/Algomind

[Back to the awesome list](../../README.md)
