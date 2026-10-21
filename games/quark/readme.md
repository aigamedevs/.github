# quark

> Verified game note.

![quark screenshot placeholder](quark-placeholder.svg)

## At a glance

- **Score:** 8.3/10
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/floration/quark](https://github.com/floration/quark)
- **Evidence:** [direct model evidence](https://github.com/floration/quark/commit/c93b118bb61a043a0aede2716eb3a07eb6e2800b)
- **Live demo:** [open demo](https://floration.github.io/quark)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A fast, minimal FPS on a fully custom C++17 engine (OpenGL 3.3, custom UDP netcode). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/floration/quark/blob/claude/compassionate-ritchie-07ah6i/third_party/glfw/deps/nuklear.h](https://github.com/floration/quark/blob/claude/compassionate-ritchie-07ah6i/third_party/glfw/deps/nuklear.h)
- [https://github.com/floration/quark/commit/c93b118bb61a043a0aede2716eb3a07eb6e2800b](https://github.com/floration/quark/commit/c93b118bb61a043a0aede2716eb3a07eb6e2800b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/floration/quark

[Back to the awesome list](../../README.md)
