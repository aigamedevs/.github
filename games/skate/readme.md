# Skate

> Verified game note.

![Skate screenshot placeholder](skate-placeholder.svg)

## At a glance

- **Score:** 6.6/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/lorenzaquinzi/skate](https://github.com/lorenzaquinzi/skate)
- **Evidence:** [direct model evidence](https://github.com/lorenzaquinzi/skate/commit/de8bb0b4af60a28a53a8047176b08edad37fa560)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A tiny endless skateboard runner, in the spirit of Chrome's offline dinosaur. Skate down a street, jump the obstacles (cones, bins, hydrants, benches, barriers), and beat your high score. One hit ends the run. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/lorenzaquinzi/skate/blob/main/game.js](https://github.com/lorenzaquinzi/skate/blob/main/game.js)
- [https://github.com/lorenzaquinzi/skate/commit/de8bb0b4af60a28a53a8047176b08edad37fa560](https://github.com/lorenzaquinzi/skate/commit/de8bb0b4af60a28a53a8047176b08edad37fa560)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/lorenzaquinzi/skate

[Back to the awesome list](../../README.md)
