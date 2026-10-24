# 星くずキャッチ (Stardust Catch)

> Verified game note.

![星くずキャッチ (Stardust Catch) screenshot placeholder](stardust-catch-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/GigaOwO/game_test](https://github.com/GigaOwO/game_test)
- **Evidence:** [direct model evidence](https://github.com/GigaOwO/game_test/commit/ea2acf24b1fe0f06cbfac4802b34e735004555b3)
- **Live demo:** [open demo](https://game-test-lilac.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

UFOを動かして降ってくる星を集め、隕石をよけるアクションゲームです。Next.js で作り、Vercel にデプロイしています。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GigaOwO/game_test/blob/main/src/components/StardustGame.tsx](https://github.com/GigaOwO/game_test/blob/main/src/components/StardustGame.tsx)
- [https://github.com/GigaOwO/game_test/commit/ea2acf24b1fe0f06cbfac4802b34e735004555b3](https://github.com/GigaOwO/game_test/commit/ea2acf24b1fe0f06cbfac4802b34e735004555b3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/GigaOwO/game_test

[Back to the awesome list](../../README.md)
