# Nozvi

> Verified game note.

![Nozvi screenshot placeholder](nozvi-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/nozvi-studio/NOZVI-GAME-01](https://github.com/nozvi-studio/NOZVI-GAME-01)
- **Evidence:** [direct model evidence](https://github.com/nozvi-studio/NOZVI-GAME-01/commit/445881c4a1281812bbd3b342523ce530ef046c08)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A rebuild of the Mirror puzzle game, following the design and architecture specification approved on 2026-09-30. Built with Phaser 3, TypeScript and Vite, and packaged for Android with Capacitor. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nozvi-studio/NOZVI-GAME-01/blob/dev/src/presentation/scenes/LevelSelectScene.ts](https://github.com/nozvi-studio/NOZVI-GAME-01/blob/dev/src/presentation/scenes/LevelSelectScene.ts)
- [https://github.com/nozvi-studio/NOZVI-GAME-01/commit/445881c4a1281812bbd3b342523ce530ef046c08](https://github.com/nozvi-studio/NOZVI-GAME-01/commit/445881c4a1281812bbd3b342523ce530ef046c08)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/nozvi-studio/NOZVI-GAME-01

[Back to the awesome list](../../README.md)
