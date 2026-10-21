# Hohenfeuer

> Verified game note.

![Hohenfeuer screenshot](https://raw.githubusercontent.com/tobiasosborne/hohenfeuer/main/tests/goldens/danger-match1.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/tobiasosborne/hohenfeuer/blob/main/tests/goldens/danger-match1.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/tobiasosborne/hohenfeuer](https://github.com/tobiasosborne/hohenfeuer)
- **Evidence:** [direct model evidence](https://github.com/tobiasosborne/hohenfeuer/commit/169ee4236ab59c84b40d6283448bc44c543ba7b9)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/tobiasosborne/hohenfeuer/blob/main/tests/goldens/danger-match1.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. First-person castle cannon view over green hills with compass, aiming readout and control panel; decent but HUD-heavy.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Hohenfeuer: a first-person, block-castle artillery duel in three.js, re-imagining Ballerburg: Castle Siege (2001). Built by orchestrated AI agents in tracer-bullet slices. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tobiasosborne/hohenfeuer/blob/main/src/contracts.js](https://github.com/tobiasosborne/hohenfeuer/blob/main/src/contracts.js)
- [https://github.com/tobiasosborne/hohenfeuer/commit/169ee4236ab59c84b40d6283448bc44c543ba7b9](https://github.com/tobiasosborne/hohenfeuer/commit/169ee4236ab59c84b40d6283448bc44c543ba7b9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/tobiasosborne/hohenfeuer

[Back to the awesome list](../../README.md)
