# scroller

> Verified game note.

![scroller screenshot](https://raw.githubusercontent.com/binfpmr/scroller/main/docs/screenshots/level3.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/binfpmr/scroller/blob/main/docs/screenshots/level3.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/binfpmr/scroller](https://github.com/binfpmr/scroller)
- **Evidence:** [direct model evidence](https://github.com/binfpmr/scroller/commit/ca7acfc3215f44a1a104d281e6b591e84d80a4de)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/binfpmr/scroller/blob/main/docs/screenshots/level3.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Simple pixel platformer with grass blocks, hills, clouds and a few enemies; clean but basic.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A small 2D platformer that boots on bare-metal x8664 through UEFI: no operating system, no libc. Freestanding C++23,. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/binfpmr/scroller/blob/main/src/drivers/xhci.cpp](https://github.com/binfpmr/scroller/blob/main/src/drivers/xhci.cpp)
- [https://github.com/binfpmr/scroller/commit/ca7acfc3215f44a1a104d281e6b591e84d80a4de](https://github.com/binfpmr/scroller/commit/ca7acfc3215f44a1a104d281e6b591e84d80a4de)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/binfpmr/scroller

[Back to the awesome list](../../README.md)
