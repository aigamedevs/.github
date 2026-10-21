# Warlock

> Verified game note.

![Warlock screenshot](https://raw.githubusercontent.com/jannef/warlock/main/docs/screenshots/m3-light-hall.png)

## At a glance

- **Score:** 8.3/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/jannef/warlock/blob/main/docs/screenshots/m3-light-hall.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.1
- **Technology:** Rust, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/jannef/warlock](https://github.com/jannef/warlock)
- **Evidence:** [direct model evidence](https://github.com/jannef/warlock/commit/de5ef62cf83ad65cfb31142989fa69bc06b085b0)
- **Live demo:** [open demo](https://jannef.github.io/warlock/)
- **Additional live link:** [open demo](https://jannef.github.io/warlock/wiki/)
- **Additional live link:** [open demo](https://jannef.github.io/warlock/wiki/controls.html)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jannef/warlock/blob/main/docs/screenshots/m3-light-hall.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. ASCII roguelike hall with coloured hash walls, glyph player and lighting caption; minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A turn-based ASCII roguelike in the spirit of ADOM, drawn entirely in glyphs and rendered on the. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jannef/warlock/blob/main/THIRD_PARTY_LICENSES.html](https://github.com/jannef/warlock/blob/main/THIRD_PARTY_LICENSES.html)
- [https://github.com/jannef/warlock/commit/de5ef62cf83ad65cfb31142989fa69bc06b085b0](https://github.com/jannef/warlock/commit/de5ef62cf83ad65cfb31142989fa69bc06b085b0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/jannef/warlock

[Back to the awesome list](../../README.md)
