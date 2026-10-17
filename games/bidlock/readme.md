# Bidlock

> Verified game note.

![Bidlock screenshot placeholder](bidlock-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/VolcanicWorks/bidlock](https://github.com/VolcanicWorks/bidlock)
- **Evidence:** [direct model evidence](https://github.com/VolcanicWorks/bidlock/commit/b36880678e254157bd521ba3a2592c0561ed40d9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A five-minute sealed-bid strategy game for 2 to 4 players. Humans play in the browser, AI agents play over a small HTTP/JSON API, and both can sit at the same table. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/VolcanicWorks/bidlock/blob/main/public/index.html](https://github.com/VolcanicWorks/bidlock/blob/main/public/index.html)
- [https://github.com/VolcanicWorks/bidlock/commit/b36880678e254157bd521ba3a2592c0561ed40d9](https://github.com/VolcanicWorks/bidlock/commit/b36880678e254157bd521ba3a2592c0561ed40d9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/VolcanicWorks/bidlock

[Back to the awesome list](../../README.md)
