# 台灣人生模擬（暫名）

> Verified game note.

![台灣人生模擬（暫名） screenshot placeholder](game-lieroliu-taiwanese-simulator-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/lieroliu/taiwanese-simulator](https://github.com/lieroliu/taiwanese-simulator)
- **Evidence:** [direct model evidence](https://github.com/lieroliu/taiwanese-simulator/commit/9ca490a8be27020070fdd73f139ade8e310a41e4)
- **Live demo:** [open demo](https://lieroliu.github.io/taiwanese-simulator/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

以台灣為舞台的人生模擬網頁遊戲。玩家選擇一個出生世代，被隨機分配身分、家庭與出生地，從出生走到人生終點。重點不在數值，而在角色每個階段的心境與遇到的處境。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/lieroliu/taiwanese-simulator/blob/main/index.html](https://github.com/lieroliu/taiwanese-simulator/blob/main/index.html)
- [https://github.com/lieroliu/taiwanese-simulator/commit/9ca490a8be27020070fdd73f139ade8e310a41e4](https://github.com/lieroliu/taiwanese-simulator/commit/9ca490a8be27020070fdd73f139ade8e310a41e4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/lieroliu/taiwanese-simulator

[Back to the awesome list](../../README.md)
