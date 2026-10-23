# Mr. Eggy

> Verified game note.

![Mr. Eggy screenshot placeholder](mr-eggy-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/ducthais/brain-puzzle-game](https://github.com/ducthais/brain-puzzle-game)
- **Evidence:** [direct model evidence](https://github.com/ducthais/brain-puzzle-game/commit/5498d5907fe3534b220a0def522f4eb52620ded2)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Game giải đố 2D thể loại "troll": đưa nhân vật Mr. Eggy tới lá cờ vàng bằng cách di chuyển, nhảy và tương tác với chính giao diện — kéo thả mặt đất, lá cờ, nút điều khiển, nhân bản nhân vật làm cầu... Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ducthais/brain-puzzle-game/blob/main/Assets/Plugins/CW/LeanTouch/Required/Documentation.html](https://github.com/ducthais/brain-puzzle-game/blob/main/Assets/Plugins/CW/LeanTouch/Required/Documentation.html)
- [https://github.com/ducthais/brain-puzzle-game/commit/5498d5907fe3534b220a0def522f4eb52620ded2](https://github.com/ducthais/brain-puzzle-game/commit/5498d5907fe3534b220a0def522f4eb52620ded2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/ducthais/brain-puzzle-game

[Back to the awesome list](../../README.md)
