# X85

> Verified game note.

![X85 screenshot placeholder](x85-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** C++, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/matheusnunes/x85](https://github.com/matheusnunes/x85)
- **Evidence:** [direct model evidence](https://github.com/matheusnunes/x85/commit/839b5bb066ce22370abda815d0dd09be2dfe7f0d)
- **Live demo:** [open demo](https://x85-game.netlify.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

X85 — jogo de nave premiado (2010), original em C++/Chien2D e port para o navegador (TypeScript + WebGL2). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/matheusnunes/x85/blob/main/X85-devcore 2/chien2d2mapa.cpp](https://github.com/matheusnunes/x85/blob/main/X85-devcore 2/chien2d2mapa.cpp)
- [https://github.com/matheusnunes/x85/commit/839b5bb066ce22370abda815d0dd09be2dfe7f0d](https://github.com/matheusnunes/x85/commit/839b5bb066ce22370abda815d0dd09be2dfe7f0d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/matheusnunes/x85

[Back to the awesome list](../../README.md)
