# ECHO LOOP

> Verified game note.

![ECHO LOOP screenshot placeholder](echo-loop-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/djkdb/echo-loop](https://github.com/djkdb/echo-loop)
- **Evidence:** [direct model evidence](https://github.com/djkdb/echo-loop/commit/ae4122a3c979854f372be3f1e05852e7a8238732)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

10초 동안의 내 움직임이 녹화되고, 루프가 끝날 때마다 방이 처음으로 돌아가며 방금의 나는 "과거의 나(고스트)"로 남아. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/djkdb/echo-loop/blob/main/actors/player.gd](https://github.com/djkdb/echo-loop/blob/main/actors/player.gd)
- [https://github.com/djkdb/echo-loop/commit/ae4122a3c979854f372be3f1e05852e7a8238732](https://github.com/djkdb/echo-loop/commit/ae4122a3c979854f372be3f1e05852e7a8238732)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/djkdb/echo-loop

[Back to the awesome list](../../README.md)
