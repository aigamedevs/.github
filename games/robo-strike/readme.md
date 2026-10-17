# Robo Strike 机器人大作战

> Verified game note.

![Robo Strike 机器人大作战 screenshot placeholder](robo-strike-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/machuiwen/robo-strike](https://github.com/machuiwen/robo-strike)
- **Evidence:** [direct model evidence](https://github.com/machuiwen/robo-strike/commit/745dc0ae4ae9d4667212e0fc28306c204c14a5b8)
- **Live demo:** [open demo](https://machuiwen.github.io/robo-strike/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

一个卡通风格的第一人称射击小游戏。打败一波又一波的机器人和无人机，它们被击中后会碎成火花、螺丝和零件，没有任何流血内容，适合小朋友。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/machuiwen/robo-strike/blob/main/js/main.js](https://github.com/machuiwen/robo-strike/blob/main/js/main.js)
- [https://github.com/machuiwen/robo-strike/commit/745dc0ae4ae9d4667212e0fc28306c204c14a5b8](https://github.com/machuiwen/robo-strike/commit/745dc0ae4ae9d4667212e0fc28306c204c14a5b8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/machuiwen/robo-strike

[Back to the awesome list](../../README.md)
