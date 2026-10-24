# Bikini Atoll

> Verified game note.

![Bikini Atoll screenshot](https://raw.githubusercontent.com/redconfetti/atoll/master/assets/screenshots/01-title.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/redconfetti/atoll/blob/master/assets/screenshots/01-title.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Assembly
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/redconfetti/atoll](https://github.com/redconfetti/atoll)
- **Evidence:** [direct model evidence](https://github.com/redconfetti/atoll/commit/6173fa4076749587d88ad18776eae8d36ea9eaab)
- **Live demo:** [open demo](https://cc65.github.io/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/redconfetti/atoll/blob/master/assets/screenshots/01-title.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. SNES-style title over an atoll seascape; retro charm but a title screen.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Bikini Atoll: an SNES flight game in 65816 assembly. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/redconfetti/atoll/blob/master/src/main.s](https://github.com/redconfetti/atoll/blob/master/src/main.s)
- [https://github.com/redconfetti/atoll/commit/6173fa4076749587d88ad18776eae8d36ea9eaab](https://github.com/redconfetti/atoll/commit/6173fa4076749587d88ad18776eae8d36ea9eaab)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/redconfetti/atoll

[Back to the awesome list](../../README.md)
