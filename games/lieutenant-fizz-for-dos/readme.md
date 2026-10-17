# Lieutenant Fizz for DOS

> Verified game note.

![Lieutenant Fizz for DOS screenshot placeholder](lieutenant-fizz-for-dos-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Rust, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/ScottMorris/lieutenant-fizz-dos](https://github.com/ScottMorris/lieutenant-fizz-dos)
- **Evidence:** [direct model evidence](https://github.com/ScottMorris/lieutenant-fizz-dos/commit/3c4f6858faa05cd2502410871ac63dd4103249b0)
- **Live demo:** [open demo](https://scottmorris.github.io/lieutenant-fizz-dos/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Lieutenant Fizz Episode 1 for DOS — a Rust port with VGA graphics and AdLib sound that runs in DOSBox, in a browser and on a 1.44 MB floppy. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ScottMorris/lieutenant-fizz-dos/blob/main/m2/game/src/levels.rs](https://github.com/ScottMorris/lieutenant-fizz-dos/blob/main/m2/game/src/levels.rs)
- [https://github.com/ScottMorris/lieutenant-fizz-dos/commit/3c4f6858faa05cd2502410871ac63dd4103249b0](https://github.com/ScottMorris/lieutenant-fizz-dos/commit/3c4f6858faa05cd2502410871ac63dd4103249b0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/ScottMorris/lieutenant-fizz-dos

[Back to the awesome list](../../README.md)
