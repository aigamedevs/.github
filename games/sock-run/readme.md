# Sock Run

> Verified game note.

![Sock Run screenshot](https://raw.githubusercontent.com/ahab94/sock-run/main/docs/media/sock-run.gif)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/ahab94/sock-run/blob/main/docs/media/sock-run.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/ahab94/sock-run](https://github.com/ahab94/sock-run)
- **Evidence:** [direct model evidence](https://github.com/ahab94/sock-run/commit/5d39dc7d39964bd81de909f05195097d37fc6057)
- **Live demo:** [open demo](https://ahab94.github.io/sock-run/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ahab94/sock-run/blob/main/docs/media/sock-run.gif) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Warm 3D parkour room with on-screen tutorial text dominating.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The floor is lava. You're wearing socks. A 3D parkour game in Godot 4, playable in the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ahab94/sock-run/blob/main/scripts/hud.gd](https://github.com/ahab94/sock-run/blob/main/scripts/hud.gd)
- [https://github.com/ahab94/sock-run/commit/5d39dc7d39964bd81de909f05195097d37fc6057](https://github.com/ahab94/sock-run/commit/5d39dc7d39964bd81de909f05195097d37fc6057)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/ahab94/sock-run

[Back to the awesome list](../../README.md)
