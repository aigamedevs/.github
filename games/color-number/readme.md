# Color Number

> Verified game note.

![Color Number screenshot placeholder](color-number-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Sanitysr163216/pixel-color-by-number](https://github.com/Sanitysr163216/pixel-color-by-number)
- **Evidence:** [direct model evidence](https://github.com/Sanitysr163216/pixel-color-by-number/commit/f05a6b4ae52f5081c28a66c21f0c330161156a54)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A pixel-art color-by-number desktop game in Python + Kivy: turn any photo into a numbered grid and paint it cell by cell. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Sanitysr163216/pixel-color-by-number/blob/main/colornumber/ui/import_screen.py](https://github.com/Sanitysr163216/pixel-color-by-number/blob/main/colornumber/ui/import_screen.py)
- [https://github.com/Sanitysr163216/pixel-color-by-number/commit/f05a6b4ae52f5081c28a66c21f0c330161156a54](https://github.com/Sanitysr163216/pixel-color-by-number/commit/f05a6b4ae52f5081c28a66c21f0c330161156a54)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Sanitysr163216/pixel-color-by-number

[Back to the awesome list](../../README.md)
