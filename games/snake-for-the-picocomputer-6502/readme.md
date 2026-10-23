# Snake for the Picocomputer 6502

> Verified game note.

![Snake for the Picocomputer 6502 screenshot](https://raw.githubusercontent.com/ulften/snake6502/main/docs/screenshot.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/ulften/snake6502/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** CMake
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/ulften/snake6502](https://github.com/ulften/snake6502)
- **Evidence:** [direct model evidence](https://github.com/ulften/snake6502/commit/6a10a2c78db0d22edd93b0e53dcbd3608843785c)
- **Live demo:** [open demo](https://picocomputer.github.io/)
- **Additional live link:** [open demo](https://picocomputer.github.io/sdk.html#sdk-install)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ulften/snake6502/blob/main/docs/screenshot.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Retro green snake field with dots; very basic.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Snake for the Picocomputer 6502 (RP6502). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ulften/snake6502/blob/main/tools/rp6502.py](https://github.com/ulften/snake6502/blob/main/tools/rp6502.py)
- [https://github.com/ulften/snake6502/commit/6a10a2c78db0d22edd93b0e53dcbd3608843785c](https://github.com/ulften/snake6502/commit/6a10a2c78db0d22edd93b0e53dcbd3608843785c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/ulften/snake6502

[Back to the awesome list](../../README.md)
