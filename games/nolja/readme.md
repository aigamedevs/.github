# Nolja

> Verified game note.

![Nolja screenshot placeholder](nolja-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/pusam/nolja](https://github.com/pusam/nolja)
- **Evidence:** [direct model evidence](https://github.com/pusam/nolja/commit/38fa31a2bf1841dbd258965c3f4fea8daaaf3c6e)
- **Live demo:** [open demo](https://pusam.github.io/nolja/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

거실 TV에서 조이콘 들고 같이 노는 게임 모음. 브라우저(PC 크롬·엣지)에서 돌아가고, 조이콘은 WebHID로 직접 읽음. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/pusam/nolja/blob/main/games/tennis/tennis.js](https://github.com/pusam/nolja/blob/main/games/tennis/tennis.js)
- [https://github.com/pusam/nolja/commit/38fa31a2bf1841dbd258965c3f4fea8daaaf3c6e](https://github.com/pusam/nolja/commit/38fa31a2bf1841dbd258965c3f4fea8daaaf3c6e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/pusam/nolja

[Back to the awesome list](../../README.md)
