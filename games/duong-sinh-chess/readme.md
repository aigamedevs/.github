# Dương Sinh Chess

> Verified game note.

![Dương Sinh Chess screenshot placeholder](duong-sinh-chess-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/covuaduongsinh/chessminigame](https://github.com/covuaduongsinh/chessminigame)
- **Evidence:** [direct model evidence](https://github.com/covuaduongsinh/chessminigame/commit/ad663713f36d5fc5f3b70a3e5edf830ac335ef08)
- **Live demo:** [open demo](https://covuaduongsinh.github.io/chessminigame/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

a free platform that helps kids and beginners learn chess through fun mini-games. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/covuaduongsinh/chessminigame/blob/main/packages/chess-core/src/position.ts](https://github.com/covuaduongsinh/chessminigame/blob/main/packages/chess-core/src/position.ts)
- [https://github.com/covuaduongsinh/chessminigame/commit/ad663713f36d5fc5f3b70a3e5edf830ac335ef08](https://github.com/covuaduongsinh/chessminigame/commit/ad663713f36d5fc5f3b70a3e5edf830ac335ef08)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/covuaduongsinh/chessminigame

[Back to the awesome list](../../README.md)
