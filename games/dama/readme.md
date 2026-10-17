# Dama

> Verified game note.

![Dama screenshot placeholder](dama-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/AndreaAcanfora/dama](https://github.com/AndreaAcanfora/dama)
- **Evidence:** [direct model evidence](https://github.com/AndreaAcanfora/dama/commit/e368bd8cc5c582ae454de2d392e83781727f077e)
- **Live demo:** [open demo](https://andreaacanfora.github.io/dama/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Italian draughts (dama italiana) in the browser: five AI levels, online play with a friend, installable PWA. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AndreaAcanfora/dama/blob/main/training/dama/rules.py](https://github.com/AndreaAcanfora/dama/blob/main/training/dama/rules.py)
- [https://github.com/AndreaAcanfora/dama/commit/e368bd8cc5c582ae454de2d392e83781727f077e](https://github.com/AndreaAcanfora/dama/commit/e368bd8cc5c582ae454de2d392e83781727f077e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/AndreaAcanfora/dama

[Back to the awesome list](../../README.md)
