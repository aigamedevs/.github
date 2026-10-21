# HeliRescue

> Verified game note.

![HeliRescue screenshot placeholder](helirescue-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/soncsec/helirescue](https://github.com/soncsec/helirescue)
- **Evidence:** [direct model evidence](https://github.com/soncsec/helirescue/commit/61492d3cbeb0dfcf1da243623bde686e91b10f9f)
- **Live demo:** [open demo](https://soncsec.github.io/helirescue/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

HeliRescue: fly a rescue helicopter into a near-future war zone and bring the trapped people home. Soncrant Arcade. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/soncsec/helirescue/blob/main/src/scenes/GameScene.ts](https://github.com/soncsec/helirescue/blob/main/src/scenes/GameScene.ts)
- [https://github.com/soncsec/helirescue/commit/61492d3cbeb0dfcf1da243623bde686e91b10f9f](https://github.com/soncsec/helirescue/commit/61492d3cbeb0dfcf1da243623bde686e91b10f9f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/soncsec/helirescue

[Back to the awesome list](../../README.md)
