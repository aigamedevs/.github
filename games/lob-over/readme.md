# LOB, Over

> Verified game note.

![LOB, Over screenshot placeholder](lob-over-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/tamu-game-lab/lob-over](https://github.com/tamu-game-lab/lob-over)
- **Evidence:** [direct model evidence](https://github.com/tamu-game-lab/lob-over/commit/ee43757ebd3ea3c4bcd2e05f943735164c1116e3)
- **Live demo:** [open demo](https://tamu-game-lab.github.io/lob-over/)
- **Additional live link:** [open demo](https://tamu-game-lab.github.io/lob-over/play.html?host=browser)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Play it in the browser: https://tamu-game-lab.github.io/lob-over/ (the field manual PDF is linked on the landing page). Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tamu-game-lab/lob-over/blob/main/Assets/LOBOver/Tests/EditMode/SitePresentationTests.cs](https://github.com/tamu-game-lab/lob-over/blob/main/Assets/LOBOver/Tests/EditMode/SitePresentationTests.cs)
- [https://github.com/tamu-game-lab/lob-over/commit/ee43757ebd3ea3c4bcd2e05f943735164c1116e3](https://github.com/tamu-game-lab/lob-over/commit/ee43757ebd3ea3c4bcd2e05f943735164c1116e3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/tamu-game-lab/lob-over

[Back to the awesome list](../../README.md)
