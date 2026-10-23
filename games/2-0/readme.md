# 贪吃蛇 2.0

> Verified game note.

![贪吃蛇 2.0 screenshot placeholder](2-0-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/CharlieZhang7/snake-2](https://github.com/CharlieZhang7/snake-2)
- **Evidence:** [direct model evidence](https://github.com/CharlieZhang7/snake-2/commit/87b0f66e8cc08c3cbee7680e8b4035a46686e1e5)
- **Live demo:** [open demo](https://charliezhang7.github.io/snake-2/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

能画弧线转弯的贪吃蛇，带特殊果子、连击、三档难度和最高分记录。单个 HTML 文件，无任何依赖。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/CharlieZhang7/snake-2/blob/main/index.html](https://github.com/CharlieZhang7/snake-2/blob/main/index.html)
- [https://github.com/CharlieZhang7/snake-2/commit/87b0f66e8cc08c3cbee7680e8b4035a46686e1e5](https://github.com/CharlieZhang7/snake-2/commit/87b0f66e8cc08c3cbee7680e8b4035a46686e1e5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/CharlieZhang7/snake-2

[Back to the awesome list](../../README.md)
