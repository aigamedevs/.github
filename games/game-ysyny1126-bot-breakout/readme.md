# 마카롱 벽돌깨기

> Verified game note.

![마카롱 벽돌깨기 screenshot placeholder](game-ysyny1126-bot-breakout-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/ysyny1126-bot/breakout](https://github.com/ysyny1126-bot/breakout)
- **Evidence:** [direct model evidence](https://github.com/ysyny1126-bot/breakout/commit/8bf8481cb54dc0d9a94ebfa27d6e9110fc487941)
- **Live demo:** [open demo](https://ysyny1126-bot.github.io/breakout/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

파스텔 디저트 테마의 브라우저 벽돌깨기 게임입니다. 설치 없이 index.html 하나로 동작합니다. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ysyny1126-bot/breakout/blob/main/index.html](https://github.com/ysyny1126-bot/breakout/blob/main/index.html)
- [https://github.com/ysyny1126-bot/breakout/commit/8bf8481cb54dc0d9a94ebfa27d6e9110fc487941](https://github.com/ysyny1126-bot/breakout/commit/8bf8481cb54dc0d9a94ebfa27d6e9110fc487941)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/ysyny1126-bot/breakout

[Back to the awesome list](../../README.md)
