# Dessert Pop! — 디저트 매치3 H5 게임

> Verified game note.

![Dessert Pop! — 디저트 매치3 H5 게임 screenshot placeholder](dessert-pop-3-h5-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/BryanRha/dessert-pop](https://github.com/BryanRha/dessert-pop)
- **Evidence:** [direct model evidence](https://github.com/BryanRha/dessert-pop/commit/ae192696d0bb48654bcd581bbb4f48405b0ec479)
- **Live demo:** [open demo](https://bryanrha.github.io/dessert-pop/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

브라우저에서 바로 실행되는 세로형 매치3 퍼즐 게임. Phaser 3 + 순수 JS (빌드 도구 없음). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BryanRha/dessert-pop/blob/main/src/scenes/Game.js](https://github.com/BryanRha/dessert-pop/blob/main/src/scenes/Game.js)
- [https://github.com/BryanRha/dessert-pop/commit/ae192696d0bb48654bcd581bbb4f48405b0ec479](https://github.com/BryanRha/dessert-pop/commit/ae192696d0bb48654bcd581bbb4f48405b0ec479)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/BryanRha/dessert-pop

[Back to the awesome list](../../README.md)
