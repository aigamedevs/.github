# Contour

> Verified game note.

![Contour screenshot placeholder](contour-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/paravent/contour](https://github.com/paravent/contour)
- **Evidence:** [direct model evidence](https://github.com/paravent/contour/commit/0af124bf2f6bd549ceecbd9795ca6eae0a4d89bf)
- **Live demo:** [open demo](https://metmuseum.github.io/)
- **Additional live link:** [open demo](https://nasa-gibs.github.io/gibs-api-docs/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A daily geography puzzle. You see an unlabelled contour map of somewhere on Earth and have six guesses to name the country. Contour lines are coloured by height on one scale for the whole day (teal lowlands up through green and gold to pale peaks), with a… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/paravent/contour/blob/main/web/src/components/Palette.tsx](https://github.com/paravent/contour/blob/main/web/src/components/Palette.tsx)
- [https://github.com/paravent/contour/commit/0af124bf2f6bd549ceecbd9795ca6eae0a4d89bf](https://github.com/paravent/contour/commit/0af124bf2f6bd549ceecbd9795ca6eae0a4d89bf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/paravent/contour

[Back to the awesome list](../../README.md)
