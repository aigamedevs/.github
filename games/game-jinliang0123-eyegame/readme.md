# 眼動控制遊戲集錦

> Verified game note.

![眼動控制遊戲集錦 screenshot placeholder](game-jinliang0123-eyegame-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/jinliang0123/Eyegame](https://github.com/jinliang0123/Eyegame)
- **Evidence:** [direct model evidence](https://github.com/jinliang0123/Eyegame/commit/72d1fc3e9f8b6fa84a4b28fed40dee962cd4730d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

純前端（無需後端、無需安裝）的眼動控制網頁，使用網路攝影機 + MediaPipe Face Landmarker（含虹膜關鍵點與眨眼 blendshape）。影像只在瀏覽器本機處理。. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jinliang0123/Eyegame/blob/claude/sleepy-galileo-llvg4s/js/race.js](https://github.com/jinliang0123/Eyegame/blob/claude/sleepy-galileo-llvg4s/js/race.js)
- [https://github.com/jinliang0123/Eyegame/commit/72d1fc3e9f8b6fa84a4b28fed40dee962cd4730d](https://github.com/jinliang0123/Eyegame/commit/72d1fc3e9f8b6fa84a4b28fed40dee962cd4730d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/jinliang0123/Eyegame

[Back to the awesome list](../../README.md)
