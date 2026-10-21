# Parqués

> Verified game note.

![Parqués screenshot](https://raw.githubusercontent.com/jdmahecha1/parques/main/docs/screenshot.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 4.8/10 ([manually reviewed image](https://github.com/jdmahecha1/parques/blob/main/docs/screenshot.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/jdmahecha1/parques](https://github.com/jdmahecha1/parques)
- **Evidence:** [direct model evidence](https://github.com/jdmahecha1/parques/commit/5ac58f888317f7a1abc61249d047cb6207c8dbeb)
- **Live demo:** [open demo](https://jdmahecha1.github.io/parques/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jdmahecha1/parques/blob/main/docs/screenshot.jpg) — 📸 4.8/10 · manual visual review · Use this frame for the game-level score. Parques board with four coloured homes, tokens and a player list; clean flat board.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Colombian parqués in the browser: play bots or friends online. One pure TypeScript rules engine refereeing both the client and a Supabase Edge Function. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jdmahecha1/parques/blob/main/supabase/functions/parques/service.ts](https://github.com/jdmahecha1/parques/blob/main/supabase/functions/parques/service.ts)
- [https://github.com/jdmahecha1/parques/commit/5ac58f888317f7a1abc61249d047cb6207c8dbeb](https://github.com/jdmahecha1/parques/commit/5ac58f888317f7a1abc61249d047cb6207c8dbeb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/jdmahecha1/parques

[Back to the awesome list](../../README.md)
