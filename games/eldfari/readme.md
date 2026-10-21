# eldfari

> Verified game note.

![eldfari screenshot placeholder](eldfari-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** Go
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/aleksejunas/eldfari](https://github.com/aleksejunas/eldfari)
- **Evidence:** [direct model evidence](https://github.com/aleksejunas/eldfari/commit/f36b3741edc432abfdcf73c68bdc927beba9b971)
- **Live demo:** [open demo](https://aleksejunas.github.io/eldfari/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A game written in Go inspired by the finnish Amiga game turboraketti. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/aleksejunas/eldfari/blob/master/sim/levelfile.go](https://github.com/aleksejunas/eldfari/blob/master/sim/levelfile.go)
- [https://github.com/aleksejunas/eldfari/commit/f36b3741edc432abfdcf73c68bdc927beba9b971](https://github.com/aleksejunas/eldfari/commit/f36b3741edc432abfdcf73c68bdc927beba9b971)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/aleksejunas/eldfari

[Back to the awesome list](../../README.md)
