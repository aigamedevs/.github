# QuickKen

> Verified game note.

![QuickKen screenshot placeholder](quickken-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, PixiJS, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/WallHackJack/QuickKen](https://github.com/WallHackJack/QuickKen)
- **Evidence:** [direct model evidence](https://github.com/WallHackJack/QuickKen/commit/bd994480204add0fb467a1aae0ec2b496600addb)
- **Live demo:** [open demo](https://wallhackjack.github.io/QuickKen/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

QuickKen: a fast, flashy KenKen-style number puzzle for the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/WallHackJack/QuickKen/blob/main/src/render/BoardView.ts](https://github.com/WallHackJack/QuickKen/blob/main/src/render/BoardView.ts)
- [https://github.com/WallHackJack/QuickKen/commit/bd994480204add0fb467a1aae0ec2b496600addb](https://github.com/WallHackJack/QuickKen/commit/bd994480204add0fb467a1aae0ec2b496600addb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/WallHackJack/QuickKen

[Back to the awesome list](../../README.md)
