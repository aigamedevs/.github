# ORION

> Verified game note.

![ORION screenshot](https://raw.githubusercontent.com/Adichapati/Orion/main/docs/images/castle-map.png)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 3.0/10 ([manually reviewed image](https://github.com/Adichapati/Orion/blob/main/docs/images/castle-map.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Lua
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Adichapati/Orion](https://github.com/Adichapati/Orion)
- **Evidence:** [direct model evidence](https://github.com/Adichapati/Orion/commit/a1c861d3e91368415d8e6cc182da1503a5be9f4e)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Adichapati/Orion/blob/main/docs/images/castle-map.png) — 📸 3.0/10 · manual visual review · Use this frame for the game-level score. Level-route diagram with labelled nodes; design documentation, not a game frame.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

ORION: an isometric pixel-art stealth and sword-duel game — design docs and, later, the Godot project. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Adichapati/Orion/blob/main/art/_scripts/make_art.lua](https://github.com/Adichapati/Orion/blob/main/art/_scripts/make_art.lua)
- [https://github.com/Adichapati/Orion/commit/a1c861d3e91368415d8e6cc182da1503a5be9f4e](https://github.com/Adichapati/Orion/commit/a1c861d3e91368415d8e6cc182da1503a5be9f4e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Adichapati/Orion

[Back to the awesome list](../../README.md)
