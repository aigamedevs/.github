# Squad Test

> Verified game note.

![Squad Test screenshot placeholder](squad-test-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Kmad666/Squad-test](https://github.com/Kmad666/Squad-test)
- **Evidence:** [direct model evidence](https://github.com/Kmad666/Squad-test/commit/df3de7e68c3b4cc94ef37398c2135df7783ea822)
- **Live demo:** [open demo](https://kmad666.github.io/Squad-test/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Godot 4 third-person squad shooter prototype, playable in the browser (PC). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Kmad666/Squad-test/blob/main/scripts/main.gd](https://github.com/Kmad666/Squad-test/blob/main/scripts/main.gd)
- [https://github.com/Kmad666/Squad-test/commit/df3de7e68c3b4cc94ef37398c2135df7783ea822](https://github.com/Kmad666/Squad-test/commit/df3de7e68c3b4cc94ef37398c2135df7783ea822)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Kmad666/Squad-test

[Back to the awesome list](../../README.md)
