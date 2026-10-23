# Korean Division

> Verified game note.

![Korean Division screenshot](https://raw.githubusercontent.com/FailingVillain/gameProject/main/korean-division/assets/themes/kd1920/buildings/village-capture/village-capture.png)

## At a glance

- **Score:** 8.0/10
- **Screenshot rating:** 5.5/10 ([manually reviewed image](https://github.com/FailingVillain/gameProject/blob/main/korean-division/assets/themes/kd1920/buildings/village-capture/village-capture.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.1
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/FailingVillain/gameProject](https://github.com/FailingVillain/gameProject)
- **Evidence:** [direct model evidence](https://github.com/FailingVillain/gameProject/commit/a1a35e6b1d0de166dd6d94da28c51f816030baea)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/FailingVillain/gameProject/blob/main/korean-division/assets/themes/kd1920/buildings/village-capture/village-capture.png) — 📸 5.5/10 · manual visual review · Use this frame for the game-level score. Top-down pixel village capture tiles, repeated.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

gameProject = monorepo of korean-division (C# 1920 campaign RTS) + game-tools (art/audio pipelines that feed it). Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/FailingVillain/gameProject/blob/main/korean-division/src/Game.cs](https://github.com/FailingVillain/gameProject/blob/main/korean-division/src/Game.cs)
- [https://github.com/FailingVillain/gameProject/commit/a1a35e6b1d0de166dd6d94da28c51f816030baea](https://github.com/FailingVillain/gameProject/commit/a1a35e6b1d0de166dd6d94da28c51f816030baea)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/FailingVillain/gameProject

[Back to the awesome list](../../README.md)
