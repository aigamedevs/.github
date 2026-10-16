# PromptCraft

> Verified game note.

![PromptCraft screenshot placeholder](promptcraft-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser, Node.js
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/NotRithik/edge-city-game-jam-promptcraft](https://github.com/NotRithik/edge-city-game-jam-promptcraft)
- **Evidence:** [direct model evidence](https://github.com/NotRithik/edge-city-game-jam-promptcraft/commit/b4ed41457cfc0d8f3578e9330e17c4c585a8a09b)
- **Live demo:** [open demo](https://edge-city-mc-univ.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Single-page Minecraft-like voxel sandbox from a game jam where an AI (Gemini 4 Argon by default) builds structures and invents blocks at runtime; the Gemini use is runtime, the authoring evidence is a Claude Opus 5.5 trailer. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/NotRithik/edge-city-game-jam-promptcraft/blob/main/public/index.html](https://github.com/NotRithik/edge-city-game-jam-promptcraft/blob/main/public/index.html)
- [https://github.com/NotRithik/edge-city-game-jam-promptcraft/commit/b4ed41457cfc0d8f3578e9330e17c4c585a8a09b](https://github.com/NotRithik/edge-city-game-jam-promptcraft/commit/b4ed41457cfc0d8f3578e9330e17c4c585a8a09b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/NotRithik/edge-city-game-jam-promptcraft

[Back to the awesome list](../../README.md)
