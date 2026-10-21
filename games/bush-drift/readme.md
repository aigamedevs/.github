# Bush Drift

> Verified game note.

![Bush Drift screenshot placeholder](bush-drift-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/aedyle/Bush-Drift](https://github.com/aedyle/Bush-Drift)
- **Evidence:** [direct model evidence](https://github.com/aedyle/Bush-Drift/commit/aa2085143abb944273f09e5e1af1be5203643d0a)
- **Live demo:** [open demo](https://aedyle.github.io/Bush-Drift/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A small drifting game on a real dirt road: 7.8 km from Alexanders Hut in the South East Forest National Park. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/aedyle/Bush-Drift/blob/main/src/main.c](https://github.com/aedyle/Bush-Drift/blob/main/src/main.c)
- [https://github.com/aedyle/Bush-Drift/commit/aa2085143abb944273f09e5e1af1be5203643d0a](https://github.com/aedyle/Bush-Drift/commit/aa2085143abb944273f09e5e1af1be5203643d0a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/aedyle/Bush-Drift

[Back to the awesome list](../../README.md)
