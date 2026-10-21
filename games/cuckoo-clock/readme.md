# Cuckoo Clock

> Verified game note.

![Cuckoo Clock screenshot placeholder](cuckoo-clock-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/tb-x/cuckoo-clock](https://github.com/tb-x/cuckoo-clock)
- **Evidence:** [direct model evidence](https://github.com/tb-x/cuckoo-clock/commit/6f5eb5564f27c4d61f9fda6974c9f5e190c4d302)
- **Live demo:** [open demo](https://tb-x.github.io/cuckoo-clock/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Cuckoo Clock: a telling-the-time game for young kids (hand clock, digital clock and the spoken time). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tb-x/cuckoo-clock/blob/main/index.html](https://github.com/tb-x/cuckoo-clock/blob/main/index.html)
- [https://github.com/tb-x/cuckoo-clock/commit/6f5eb5564f27c4d61f9fda6974c9f5e190c4d302](https://github.com/tb-x/cuckoo-clock/commit/6f5eb5564f27c4d61f9fda6974c9f5e190c4d302)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/tb-x/cuckoo-clock

[Back to the awesome list](../../README.md)
