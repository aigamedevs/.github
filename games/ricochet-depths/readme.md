# Ricochet Depths

> Verified game note.

![Ricochet Depths screenshot placeholder](ricochet-depths-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/shepherd2047/ricochet-depths](https://github.com/shepherd2047/ricochet-depths)
- **Evidence:** [direct model evidence](https://github.com/shepherd2047/ricochet-depths/commit/85b5b01cb3041dc671a16e3a62bdf348f65aca48)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Original ball-bouncing roguelite for TikTok mini games (Unity). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/shepherd2047/ricochet-depths/blob/main/pit-unity/Assets/Scripts/Game/Board3D.cs](https://github.com/shepherd2047/ricochet-depths/blob/main/pit-unity/Assets/Scripts/Game/Board3D.cs)
- [https://github.com/shepherd2047/ricochet-depths/commit/85b5b01cb3041dc671a16e3a62bdf348f65aca48](https://github.com/shepherd2047/ricochet-depths/commit/85b5b01cb3041dc671a16e3a62bdf348f65aca48)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/shepherd2047/ricochet-depths

[Back to the awesome list](../../README.md)
