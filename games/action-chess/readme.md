# Action Chess

> Verified game note.

![Action Chess screenshot](https://raw.githubusercontent.com/UriZ/action-chess/main/docs/images/armies.jpg)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/UriZ/action-chess/blob/main/docs/images/armies.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/UriZ/action-chess](https://github.com/UriZ/action-chess)
- **Evidence:** [direct model evidence](https://github.com/UriZ/action-chess/commit/70bf8c213ff0c2977efcc5f1d7ea8e138014ec36)
- **Live demo:** [open demo](https://uriz.github.io/action-chess/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/UriZ/action-chess/blob/main/docs/images/armies.jpg) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Painted crusader chess-piece figures lined up on black; good art but a sprite sheet, not a game scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Battle-Chess-style animated chess: painted crusader warriors that walk, fight, and die on the board. Includes a reusable, style-agnostic AI art pipeline. Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/UriZ/action-chess/blob/main/public/character-demo.html](https://github.com/UriZ/action-chess/blob/main/public/character-demo.html)
- [https://github.com/UriZ/action-chess/commit/70bf8c213ff0c2977efcc5f1d7ea8e138014ec36](https://github.com/UriZ/action-chess/commit/70bf8c213ff0c2977efcc5f1d7ea8e138014ec36)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/UriZ/action-chess

[Back to the awesome list](../../README.md)
