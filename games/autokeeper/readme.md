# Autokeeper

> Verified game note.

![Autokeeper screenshot](https://raw.githubusercontent.com/satoshinji2992/autokeeper/main/docs/img/game.png)

## At a glance

- **Score:** 8.1/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://raw.githubusercontent.com/satoshinji2992/autokeeper/main/docs/img/game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/satoshinji2992/autokeeper](https://github.com/satoshinji2992/autokeeper)
- **Evidence:** [direct model evidence](https://github.com/satoshinji2992/autokeeper/commit/234f4d0a4d89274a4d1db1409dea250010d27ba4)
- **Live demo:** [open demo](https://satoshinji2992.github.io/autokeeper/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://raw.githubusercontent.com/satoshinji2992/autokeeper/main/docs/img/game.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. ASCII-art library scene with dense Chinese text log, character card and dice; distinctive but text-heavy.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

在终端与浏览器里玩《克苏鲁的呼唤》第 7 版：AI 守秘人、彩色 ASCII 演出、3D 物理骰子，支持 AI 辅助车卡、导入模组、沙箱规则插件与好友网页联机. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/satoshinji2992/autokeeper/blob/main/src/autokeeper/engine/game.py](https://github.com/satoshinji2992/autokeeper/blob/main/src/autokeeper/engine/game.py)
- [https://github.com/satoshinji2992/autokeeper/commit/234f4d0a4d89274a4d1db1409dea250010d27ba4](https://github.com/satoshinji2992/autokeeper/commit/234f4d0a4d89274a4d1db1409dea250010d27ba4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/satoshinji2992/autokeeper

[Back to the awesome list](../../README.md)
