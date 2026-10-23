# Martini's Brainrot Brawl

> Verified game note.

![Martini's Brainrot Brawl screenshot](https://raw.githubusercontent.com/martinipolice/brainrot-brawl/main/img/og-image.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/martinipolice/brainrot-brawl/blob/main/img/og-image.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/martinipolice/brainrot-brawl](https://github.com/martinipolice/brainrot-brawl)
- **Evidence:** [direct model evidence](https://github.com/martinipolice/brainrot-brawl/commit/648ea6cf7a22dd5fe5084bd5f673abcf04a5e42a)
- **Live demo:** [open demo](https://martinipolice.github.io/brainrot-brawl/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/martinipolice/brainrot-brawl/blob/main/img/og-image.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Bright pixel-art title over a beach with meme fighters; colourful and coherent but a title card.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Open-source 1v1 pixel-art fighting game in the browser, starring Italian brainrot memes. It has four fighters, six stages that react to the fight, and arcade, versus CPU and 2-player modes. Plain JS with no build step. MIT. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/martinipolice/brainrot-brawl/blob/main/js/game/combat.js](https://github.com/martinipolice/brainrot-brawl/blob/main/js/game/combat.js)
- [https://github.com/martinipolice/brainrot-brawl/commit/648ea6cf7a22dd5fe5084bd5f673abcf04a5e42a](https://github.com/martinipolice/brainrot-brawl/commit/648ea6cf7a22dd5fe5084bd5f673abcf04a5e42a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/martinipolice/brainrot-brawl

[Back to the awesome list](../../README.md)
