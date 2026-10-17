# Lucky Monkey: On-Call in the Jungle

> Verified game note.

![Lucky Monkey: On-Call in the Jungle screenshot](https://raw.githubusercontent.com/LuckyMonkey/luckymonkey-game/main/docs/img/oncall-overview.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.9/10 ([manually reviewed image](https://github.com/LuckyMonkey/luckymonkey-game/blob/main/docs/img/oncall-overview.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/LuckyMonkey/luckymonkey-game](https://github.com/LuckyMonkey/luckymonkey-game)
- **Evidence:** [direct model evidence](https://github.com/LuckyMonkey/luckymonkey-game/commit/6348398aa3b08290248ec8bf6287bedac916637b)
- **Live demo:** [open demo](https://go.fridge.run/luckymonkey)
- **Additional live link:** [open demo](https://dejavu-fonts.github.io)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/LuckyMonkey/luckymonkey-game/blob/main/docs/img/oncall-overview.png) — 📸 6.9/10 · manual visual review · Use this frame for the game-level score. Isometric jungle network map with nodes, paths and an incident panel; distinctive, busy text.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

🐵 On-call in the jungle: a Bevy/WebAssembly game about keeping a make-believe network alive. Trace problems to their origin, delegate to a crew of five, run real commands, read the verdict. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/LuckyMonkey/luckymonkey-game/blob/main/game/src/ops.rs](https://github.com/LuckyMonkey/luckymonkey-game/blob/main/game/src/ops.rs)
- [https://github.com/LuckyMonkey/luckymonkey-game/commit/6348398aa3b08290248ec8bf6287bedac916637b](https://github.com/LuckyMonkey/luckymonkey-game/commit/6348398aa3b08290248ec8bf6287bedac916637b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/LuckyMonkey/luckymonkey-game

[Back to the awesome list](../../README.md)
