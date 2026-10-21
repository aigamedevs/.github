# Motion Bowling

> Verified game note.

![Motion Bowling screenshot placeholder](motion-bowling-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/tejash111/PLYRO](https://github.com/tejash111/PLYRO)
- **Evidence:** [direct model evidence](https://github.com/tejash111/PLYRO/commit/b72192b7ca2575cdea6d02fc22cf4cdd0cce0f6f)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A walk-up 3D bowling game for macOS. Stand in front of the screen, swing your arm like a real bowler, and the ball rolls down the lane. Body tracking uses MediaPipe Pose through a native macOS plugin. The game is built in Unity 6. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tejash111/PLYRO/blob/main/tools/checks/lib/rules_structure.sh](https://github.com/tejash111/PLYRO/blob/main/tools/checks/lib/rules_structure.sh)
- [https://github.com/tejash111/PLYRO/commit/b72192b7ca2575cdea6d02fc22cf4cdd0cce0f6f](https://github.com/tejash111/PLYRO/commit/b72192b7ca2575cdea6d02fc22cf4cdd0cce0f6f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/tejash111/PLYRO

[Back to the awesome list](../../README.md)
