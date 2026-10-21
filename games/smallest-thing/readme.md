# Smallest Thing

> Verified game note.

![Smallest Thing screenshot placeholder](smallest-thing-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/jackkav/tiny-idle](https://github.com/jackkav/tiny-idle)
- **Evidence:** [direct model evidence](https://github.com/jackkav/tiny-idle/commit/06ab50a4de0cef2c2680912f690dfa3ee0b3811a)
- **Live demo:** [open demo](https://jackkav.github.io/tiny-idle/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Smallest Thing: an idle game that starts at 1e-101 kg. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jackkav/tiny-idle/blob/main/features/challenges.js](https://github.com/jackkav/tiny-idle/blob/main/features/challenges.js)
- [https://github.com/jackkav/tiny-idle/commit/06ab50a4de0cef2c2680912f690dfa3ee0b3811a](https://github.com/jackkav/tiny-idle/commit/06ab50a4de0cef2c2680912f690dfa3ee0b3811a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/jackkav/tiny-idle

[Back to the awesome list](../../README.md)
