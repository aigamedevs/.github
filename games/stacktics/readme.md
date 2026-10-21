# Stacktics

> Verified game note.

![Stacktics screenshot placeholder](stacktics-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/verdeyen-k/stacktics](https://github.com/verdeyen-k/stacktics)
- **Evidence:** [direct model evidence](https://github.com/verdeyen-k/stacktics/commit/0e85bbd7bd5ecce35fc6aaf639b83d8a913bd5be)
- **Live demo:** [open demo](https://verdeyen-k.github.io/stacktics/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Stacktics — stacking with tactics: a turn-based block-stacking physics game for phones. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/verdeyen-k/stacktics/blob/main/client.js](https://github.com/verdeyen-k/stacktics/blob/main/client.js)
- [https://github.com/verdeyen-k/stacktics/commit/0e85bbd7bd5ecce35fc6aaf639b83d8a913bd5be](https://github.com/verdeyen-k/stacktics/commit/0e85bbd7bd5ecce35fc6aaf639b83d8a913bd5be)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/verdeyen-k/stacktics

[Back to the awesome list](../../README.md)
