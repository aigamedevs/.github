# Two Wheel Simulator

> Verified game note.

![Two Wheel Simulator screenshot placeholder](two-wheel-simulator-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/MartyJCross/TwoWheelSimulator](https://github.com/MartyJCross/TwoWheelSimulator)
- **Evidence:** [direct model evidence](https://github.com/MartyJCross/TwoWheelSimulator/commit/c56f46bb3ac3b2134f53c7a34652c06796a89233)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D off-road motorcycle simulator: hard enduro, wheelies, motocross, trials and freestyle (bicycles later). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MartyJCross/TwoWheelSimulator/blob/main/sim/bike.cpp](https://github.com/MartyJCross/TwoWheelSimulator/blob/main/sim/bike.cpp)
- [https://github.com/MartyJCross/TwoWheelSimulator/commit/c56f46bb3ac3b2134f53c7a34652c06796a89233](https://github.com/MartyJCross/TwoWheelSimulator/commit/c56f46bb3ac3b2134f53c7a34652c06796a89233)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/MartyJCross/TwoWheelSimulator

[Back to the awesome list](../../README.md)
