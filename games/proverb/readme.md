# Proverb

> Verified game note.

![Proverb screenshot placeholder](proverb-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/AbdulMominAlam/proverb-game](https://github.com/AbdulMominAlam/proverb-game)
- **Evidence:** [direct model evidence](https://github.com/AbdulMominAlam/proverb-game/commit/55a1f040977c2af083fd10615573c59ec9499b67)
- **Live demo:** [open demo](https://proverb-game-nine.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A daily proverb guessing game. Each day everyone gets the same proverb from another language, shown as a literal English translation. Work out what it means, then guess which country it comes from. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AbdulMominAlam/proverb-game/blob/main/src/components/CountryInput.jsx](https://github.com/AbdulMominAlam/proverb-game/blob/main/src/components/CountryInput.jsx)
- [https://github.com/AbdulMominAlam/proverb-game/commit/55a1f040977c2af083fd10615573c59ec9499b67](https://github.com/AbdulMominAlam/proverb-game/commit/55a1f040977c2af083fd10615573c59ec9499b67)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/AbdulMominAlam/proverb-game

[Back to the awesome list](../../README.md)
