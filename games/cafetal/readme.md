# Cafetal

> Verified game note.

![Cafetal screenshot placeholder](cafetal-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, PixiJS, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/frealgagu/Game](https://github.com/frealgagu/Game)
- **Evidence:** [direct model evidence](https://github.com/frealgagu/Game/commit/cbeb5c027f7e08d11b9d28de38762aa7de127e1f)
- **Live demo:** [open demo](https://frealgagu.github.io/Game/)
- **Additional live link:** [open demo](https://frealgagu.github.io/Game/cafetal.apk)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Juego incremental de cadena de suministros con estilo visual inspirado en Frozen City. Un cafetal ilimitado pero lento alimenta una cadena de estaciones (beneficiadero, secado, trilla, tueste, molienda y empaque) que se mejoran para producir cada vez más. Una… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/frealgagu/Game/blob/claude/frozen-city-supply-chain-game-jpdsxh/src/render/Buildings.js](https://github.com/frealgagu/Game/blob/claude/frozen-city-supply-chain-game-jpdsxh/src/render/Buildings.js)
- [https://github.com/frealgagu/Game/commit/cbeb5c027f7e08d11b9d28de38762aa7de127e1f](https://github.com/frealgagu/Game/commit/cbeb5c027f7e08d11b9d28de38762aa7de127e1f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/frealgagu/Game

[Back to the awesome list](../../README.md)
