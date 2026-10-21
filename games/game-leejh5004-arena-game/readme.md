# 토너먼트 아레나

> Verified game note.

![토너먼트 아레나 screenshot placeholder](game-leejh5004-arena-game-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/leejh5004/arena-game](https://github.com/leejh5004/arena-game)
- **Evidence:** [direct model evidence](https://github.com/leejh5004/arena-game/commit/5a1c1ddfb3b7fe7a4795fbaa453b4ac03e2e6ca8)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

웹 앱(PWA) 빌드 v54. 직접 고치지 말고 game/buildweb.py 로 다시 만들어 올려요. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/leejh5004/arena-game/blob/main/js/lib/jsQR.js](https://github.com/leejh5004/arena-game/blob/main/js/lib/jsQR.js)
- [https://github.com/leejh5004/arena-game/commit/5a1c1ddfb3b7fe7a4795fbaa453b4ac03e2e6ca8](https://github.com/leejh5004/arena-game/commit/5a1c1ddfb3b7fe7a4795fbaa453b4ac03e2e6ca8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/leejh5004/arena-game

[Back to the awesome list](../../README.md)
