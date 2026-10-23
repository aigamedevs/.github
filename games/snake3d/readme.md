# Snake3D

> Verified game note.

![Snake3D screenshot placeholder](snake3d-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/yJulian/snake3d](https://github.com/yJulian/snake3d)
- **Evidence:** [direct model evidence](https://github.com/yJulian/snake3d/commit/db6cb9dacaf2b2b9ff791503a19c8940f7ea21a8)
- **Live demo:** [open demo](https://yjulian.github.io/snake3d/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser Snake in 3D, built with Vite, TypeScript and Three.js. The background is pure black (#000, OLED-friendly). Only the snakes and the items are colored. The board is a grid with gray lines. Screen effects (speed blur, glitch, fisheye, rain refraction and… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/yJulian/snake3d/blob/master/src/render/post/uberShader.ts](https://github.com/yJulian/snake3d/blob/master/src/render/post/uberShader.ts)
- [https://github.com/yJulian/snake3d/commit/db6cb9dacaf2b2b9ff791503a19c8940f7ea21a8](https://github.com/yJulian/snake3d/commit/db6cb9dacaf2b2b9ff791503a19c8940f7ea21a8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/yJulian/snake3d

[Back to the awesome list](../../README.md)
