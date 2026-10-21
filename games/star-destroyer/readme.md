# Star Destroyer

> Verified game note.

![Star Destroyer screenshot placeholder](star-destroyer-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/soncsec/star-destroyer](https://github.com/soncsec/star-destroyer)
- **Evidence:** [direct model evidence](https://github.com/soncsec/star-destroyer/commit/06d1386692bba9a45050d69d5da95c6adba3477c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser vertical space shooter (Phaser 4 + TypeScript) for Soncrant Arcade. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/soncsec/star-destroyer/blob/main/src/scenes/GameScene.ts](https://github.com/soncsec/star-destroyer/blob/main/src/scenes/GameScene.ts)
- [https://github.com/soncsec/star-destroyer/commit/06d1386692bba9a45050d69d5da95c6adba3477c](https://github.com/soncsec/star-destroyer/commit/06d1386692bba9a45050d69d5da95c6adba3477c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/soncsec/star-destroyer

[Back to the awesome list](../../README.md)
