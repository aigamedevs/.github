# Gladiator

> Verified game note.

![Gladiator screenshot](https://raw.githubusercontent.com/Proximo0/gladiator/main/docs/renders/arena-decor/after_1280x720_q2_box.jpg)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/Proximo0/gladiator/blob/main/docs/renders/arena-decor/after_1280x720_q2_box.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.1
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Proximo0/gladiator](https://github.com/Proximo0/gladiator)
- **Evidence:** [direct model evidence](https://github.com/Proximo0/gladiator/commit/e0cb42547c06583341345dd29acc91955084384a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Proximo0/gladiator/blob/main/docs/renders/arena-decor/after_1280x720_q2_box.jpg) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Arena interior with stands and banners in first person; solid 3D.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Godot 4.7.2 project started from the starter kit: the tooling that proved itself on the skate project, there from. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Proximo0/gladiator/blob/main/game/fighter/fighter.gd](https://github.com/Proximo0/gladiator/blob/main/game/fighter/fighter.gd)
- [https://github.com/Proximo0/gladiator/commit/e0cb42547c06583341345dd29acc91955084384a](https://github.com/Proximo0/gladiator/commit/e0cb42547c06583341345dd29acc91955084384a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Proximo0/gladiator

[Back to the awesome list](../../README.md)
