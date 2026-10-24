# Caro X-O

> Verified game note.

![Caro X-O screenshot](https://raw.githubusercontent.com/tuankun-279/Caro_XO/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 4.8/10 ([manually reviewed image](https://github.com/tuankun-279/Caro_XO/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/tuankun-279/Caro_XO](https://github.com/tuankun-279/Caro_XO)
- **Evidence:** [direct model evidence](https://github.com/tuankun-279/Caro_XO/commit/1bf497e6a45dc7e96aebcea8b16f8bcf69749d8c)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/tuankun-279/Caro_XO/blob/main/docs/gameplay.gif) — 📸 4.8/10 · manual visual review · Use this frame for the game-level score. Hand-drawn notebook-style Caro menu on a phone screen; charming but just a menu.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Play against a three-level AI or with a friend on the same phone. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tuankun-279/Caro_XO/blob/main/Assets/_Caro/Editor/CaroUiBuilder.cs](https://github.com/tuankun-279/Caro_XO/blob/main/Assets/_Caro/Editor/CaroUiBuilder.cs)
- [https://github.com/tuankun-279/Caro_XO/commit/1bf497e6a45dc7e96aebcea8b16f8bcf69749d8c](https://github.com/tuankun-279/Caro_XO/commit/1bf497e6a45dc7e96aebcea8b16f8bcf69749d8c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/tuankun-279/Caro_XO

[Back to the awesome list](../../README.md)
