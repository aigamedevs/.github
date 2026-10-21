# Wildmere

> Verified game note.

![Wildmere screenshot placeholder](wildmere-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/tamoghnakabi-wq/wildmere](https://github.com/tamoghnakabi-wq/wildmere)
- **Evidence:** [direct model evidence](https://github.com/tamoghnakabi-wq/wildmere/commit/88a383daa1360f2931cbfc417ab57ac17f1285b5)
- **Live demo:** [open demo](https://wildmere-game.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Wildmere — an original voxel survival sandbox for macOS and Windows (Unity 6.3 URP). Shape the wild. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tamoghnakabi-wq/wildmere/blob/main/Assets/Scripts/QA/QaHarness.cs](https://github.com/tamoghnakabi-wq/wildmere/blob/main/Assets/Scripts/QA/QaHarness.cs)
- [https://github.com/tamoghnakabi-wq/wildmere/commit/88a383daa1360f2931cbfc417ab57ac17f1285b5](https://github.com/tamoghnakabi-wq/wildmere/commit/88a383daa1360f2931cbfc417ab57ac17f1285b5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/tamoghnakabi-wq/wildmere

[Back to the awesome list](../../README.md)
