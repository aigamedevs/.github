# Kitefall

> Verified game note.

![Kitefall screenshot placeholder](kitefall-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Tekrontech/Kitefall](https://github.com/Tekrontech/Kitefall)
- **Evidence:** [direct model evidence](https://github.com/Tekrontech/Kitefall/commit/52d2291444956b52db1cdb579931a798740bdd87)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online competitive 3D kite-fighting for mobile – "Read the wind, win the cross, cut the line.". Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Tekrontech/Kitefall/blob/claude/amazing-bardeen-xi1xqo/Assets/Scripts/Core/Match/MatchSimulation.cs](https://github.com/Tekrontech/Kitefall/blob/claude/amazing-bardeen-xi1xqo/Assets/Scripts/Core/Match/MatchSimulation.cs)
- [https://github.com/Tekrontech/Kitefall/commit/52d2291444956b52db1cdb579931a798740bdd87](https://github.com/Tekrontech/Kitefall/commit/52d2291444956b52db1cdb579931a798740bdd87)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Tekrontech/Kitefall

[Back to the awesome list](../../README.md)
