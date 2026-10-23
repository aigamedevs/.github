# Kindling

> Verified game note.

![Kindling screenshot](https://raw.githubusercontent.com/Preponderous-Software/kindling/main/docs/images/reveal.gif)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/Preponderous-Software/kindling/blob/main/docs/images/reveal.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C++, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Preponderous-Software/kindling](https://github.com/Preponderous-Software/kindling)
- **Evidence:** [direct model evidence](https://github.com/Preponderous-Software/kindling/commit/cc5f17e7a19547606df41a62e66fa36eb2465313)
- **Live demo:** [open demo](https://kindling.play.danielstephenson.dev)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Preponderous-Software/kindling/blob/main/docs/images/reveal.gif) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Dark first-person cabin interior, low detail.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A cozy first-person frontier homestead game on the Strata engine: survey, clear, repair, furnish and light the hearth of a ruined cabin for the settler moving in. C++17, for Windows, Linux and the browser (WebGL 2), with saves. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Preponderous-Software/kindling/blob/main/src/bridge/room.cpp](https://github.com/Preponderous-Software/kindling/blob/main/src/bridge/room.cpp)
- [https://github.com/Preponderous-Software/kindling/commit/cc5f17e7a19547606df41a62e66fa36eb2465313](https://github.com/Preponderous-Software/kindling/commit/cc5f17e7a19547606df41a62e66fa36eb2465313)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Preponderous-Software/kindling

[Back to the awesome list](../../README.md)
