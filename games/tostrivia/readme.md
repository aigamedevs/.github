# Tostrivia

> Verified game note.

![Tostrivia screenshot placeholder](tostrivia-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/cperez233/Tostrivia-gg](https://github.com/cperez233/Tostrivia-gg)
- **Evidence:** [direct model evidence](https://github.com/cperez233/Tostrivia-gg/commit/ed1929a1d518fdc2c271619d49741e790ba69fac)
- **Live demo:** [open demo](https://tostrivia-gg.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Trivia en español de anime, videojuegos, series, películas y cultura general. Gira la ruleta, responde 10 preguntas contra el reloj y no rompas la racha. Algunas preguntas suenan antes de verse: el opening empieza con la pantalla tapada y la imagen se revela… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cperez233/Tostrivia-gg/blob/main/src/game/GameScreen.tsx](https://github.com/cperez233/Tostrivia-gg/blob/main/src/game/GameScreen.tsx)
- [https://github.com/cperez233/Tostrivia-gg/commit/ed1929a1d518fdc2c271619d49741e790ba69fac](https://github.com/cperez233/Tostrivia-gg/commit/ed1929a1d518fdc2c271619d49741e790ba69fac)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/cperez233/Tostrivia-gg

[Back to the awesome list](../../README.md)
