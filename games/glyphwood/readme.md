# Glyphwood

> Verified game note.

![Glyphwood screenshot](https://raw.githubusercontent.com/drugdamage/glyphwood/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/drugdamage/glyphwood/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/drugdamage/glyphwood](https://github.com/drugdamage/glyphwood)
- **Evidence:** [direct model evidence](https://github.com/drugdamage/glyphwood/commit/e38196ba65a42cb8e943d03f3ba8eb8ed18e4a11)
- **Live demo:** [open demo](https://drugdamage.github.io/glyphwood/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/drugdamage/glyphwood/blob/main/docs/gameplay.gif) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. Very dark ASCII-drawn platformer corridor with tiny glyph characters; hard to read at a glance.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Minimalist ASCII action platformer with roguelite runs. Made with Godot 4. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/drugdamage/glyphwood/blob/main/scripts/strings.gd](https://github.com/drugdamage/glyphwood/blob/main/scripts/strings.gd)
- [https://github.com/drugdamage/glyphwood/commit/e38196ba65a42cb8e943d03f3ba8eb8ed18e4a11](https://github.com/drugdamage/glyphwood/commit/e38196ba65a42cb8e943d03f3ba8eb8ed18e4a11)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/drugdamage/glyphwood

[Back to the awesome list](../../README.md)
