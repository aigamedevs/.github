# Spectrum

> Verified game note.

![Spectrum screenshot placeholder](spectrum-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/henri-cmd/spectrum](https://github.com/henri-cmd/spectrum)
- **Evidence:** [direct model evidence](https://github.com/henri-cmd/spectrum/commit/ba1146002f8e9a9477ba0fa92a3ed40bf1a1d897)
- **Live demo:** [open demo](https://henri-cmd.github.io/spectrum/)
- **Additional live link:** [open demo](https://henri-cmd.github.io/spectrum/spectrum.html)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Two daily word games, live at https://henri-cmd.github.io/spectrum/ (Darts, on the sonar console) and https://henri-cmd.github.io/spectrum/spectrum.html (Spectrum). Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/henri-cmd/spectrum/blob/main/darts.js](https://github.com/henri-cmd/spectrum/blob/main/darts.js)
- [https://github.com/henri-cmd/spectrum/commit/ba1146002f8e9a9477ba0fa92a3ed40bf1a1d897](https://github.com/henri-cmd/spectrum/commit/ba1146002f8e9a9477ba0fa92a3ed40bf1a1d897)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/henri-cmd/spectrum

[Back to the awesome list](../../README.md)
