# Fathom

> Verified game note.

![Fathom screenshot placeholder](fathom-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/andyqueyl/fathom](https://github.com/andyqueyl/fathom)
- **Evidence:** [direct model evidence](https://github.com/andyqueyl/fathom/commit/99e6592e000a57f85390ab8047bc34252f19cd14)
- **Live demo:** [open demo](https://andyqueyl.github.io/fathom/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Free daily-dive trivia game: name something, rarer answers sink deeper. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/andyqueyl/fathom/blob/main/data/pack-life.js](https://github.com/andyqueyl/fathom/blob/main/data/pack-life.js)
- [https://github.com/andyqueyl/fathom/commit/99e6592e000a57f85390ab8047bc34252f19cd14](https://github.com/andyqueyl/fathom/commit/99e6592e000a57f85390ab8047bc34252f19cd14)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/andyqueyl/fathom

[Back to the awesome list](../../README.md)
