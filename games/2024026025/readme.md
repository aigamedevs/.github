# 2024026025 이지원 게임

> Verified game note.

![2024026025 이지원 게임 screenshot placeholder](2024026025-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Fable 5.1
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/powerwon03/game](https://github.com/powerwon03/game)
- **Evidence:** [direct model evidence](https://github.com/powerwon03/game/commit/5110f83770dff1ed6b63fb9f8b7da7de30118025)
- **Live demo:** [open demo](https://game-flax-alpha.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Next.js + Supabase 로 만든 가위바위보 웹 게임입니다. Vercel 에 배포합니다. Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/powerwon03/game/blob/main/src/components/Game.tsx](https://github.com/powerwon03/game/blob/main/src/components/Game.tsx)
- [https://github.com/powerwon03/game/commit/5110f83770dff1ed6b63fb9f8b7da7de30118025](https://github.com/powerwon03/game/commit/5110f83770dff1ed6b63fb9f8b7da7de30118025)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/powerwon03/game

[Back to the awesome list](../../README.md)
