# ramen-typing-game

> Verified game note.

![ramen-typing-game screenshot](https://raw.githubusercontent.com/KeitoAbe/ramen-typing-game/main/docs/images/screenshot-play.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/KeitoAbe/ramen-typing-game/blob/main/docs/images/screenshot-play.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/KeitoAbe/ramen-typing-game](https://github.com/KeitoAbe/ramen-typing-game)
- **Evidence:** [direct model evidence](https://github.com/KeitoAbe/ramen-typing-game/commit/e88adf0cefcb2a374b0ff97fb4af7488da62848d)
- **Live demo:** [open demo](https://ramen-typing.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/KeitoAbe/ramen-typing-game/blob/main/docs/images/screenshot-play.png) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. Night ramen stall with a steaming bowl, chef, lanterns, order prompt and timer; warm flat-illustration style, very readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

夜のラーメン屋台で、出てくる注文をローマ字で打って平らげるタイピングゲーム。AI エージェントが Issue を自律実装するループエンジニアリングで開発している. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/KeitoAbe/ramen-typing-game/blob/main/src/client/components/ramen-game/ramen-result.tsx](https://github.com/KeitoAbe/ramen-typing-game/blob/main/src/client/components/ramen-game/ramen-result.tsx)
- [https://github.com/KeitoAbe/ramen-typing-game/commit/e88adf0cefcb2a374b0ff97fb4af7488da62848d](https://github.com/KeitoAbe/ramen-typing-game/commit/e88adf0cefcb2a374b0ff97fb4af7488da62848d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/KeitoAbe/ramen-typing-game

[Back to the awesome list](../../README.md)
