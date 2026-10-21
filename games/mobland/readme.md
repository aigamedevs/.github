# Mobland

> Verified game note.

![Mobland screenshot placeholder](mobland-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/mikaeleli-blip/mobland](https://github.com/mikaeleli-blip/mobland)
- **Evidence:** [direct model evidence](https://github.com/mikaeleli-blip/mobland/commit/49ad9282afc2ae69770bc6f6e2d9c43678b1f4df)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Top-down 3D mafia strategy game set in Prohibition-era New York (inspired by City of Gangsters / Empire of Sin). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mikaeleli-blip/mobland/blob/main/Tools/blender/human/gangster.py](https://github.com/mikaeleli-blip/mobland/blob/main/Tools/blender/human/gangster.py)
- [https://github.com/mikaeleli-blip/mobland/commit/49ad9282afc2ae69770bc6f6e2d9c43678b1f4df](https://github.com/mikaeleli-blip/mobland/commit/49ad9282afc2ae69770bc6f6e2d9c43678b1f4df)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/mikaeleli-blip/mobland

[Back to the awesome list](../../README.md)
