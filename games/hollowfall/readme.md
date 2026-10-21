# Hollowfall

> Verified game note.

![Hollowfall screenshot placeholder](hollowfall-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Sonnet 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ewanc26/Hollowfall](https://github.com/ewanc26/Hollowfall)
- **Evidence:** [direct model evidence](https://github.com/ewanc26/Hollowfall/commit/e4cfed68f6888c9ed2eb23da820f3d9c4ddf3e15)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A procedural voxel dungeon crawler with fast, aggressive combat and portals. C# on Godot 4. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ewanc26/Hollowfall/blob/main/game/scripts/SmokeTest.cs](https://github.com/ewanc26/Hollowfall/blob/main/game/scripts/SmokeTest.cs)
- [https://github.com/ewanc26/Hollowfall/commit/e4cfed68f6888c9ed2eb23da820f3d9c4ddf3e15](https://github.com/ewanc26/Hollowfall/commit/e4cfed68f6888c9ed2eb23da820f3d9c4ddf3e15)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ewanc26/Hollowfall

[Back to the awesome list](../../README.md)
