# Ten-Year Tape

> Verified game note.

![Ten-Year Tape screenshot](https://raw.githubusercontent.com/rajarshi-bose/ten-year-tape/main/docs/gameplay.png)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/rajarshi-bose/ten-year-tape/blob/main/docs/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/rajarshi-bose/ten-year-tape](https://github.com/rajarshi-bose/ten-year-tape)
- **Evidence:** [direct model evidence](https://github.com/rajarshi-bose/ten-year-tape/commit/241ef89210d768047321e3f2c29d621525d8b484)
- **Live demo:** [open demo](https://rajarshi-bose.github.io/ten-year-tape/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/rajarshi-bose/ten-year-tape/blob/main/docs/gameplay.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Stock-market trading screen with ticker cards, sparkline charts and order panel; clean but a data UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

scrapes BSL and Yahoo Finance data to create a realistic simulator for stock market trading over a 10 year period between 1985-2025. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/rajarshi-bose/ten-year-tape/blob/main/index.html](https://github.com/rajarshi-bose/ten-year-tape/blob/main/index.html)
- [https://github.com/rajarshi-bose/ten-year-tape/commit/241ef89210d768047321e3f2c29d621525d8b484](https://github.com/rajarshi-bose/ten-year-tape/commit/241ef89210d768047321e3f2c29d621525d8b484)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/rajarshi-bose/ten-year-tape

[Back to the awesome list](../../README.md)
