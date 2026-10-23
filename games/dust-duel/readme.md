# Dust Duel

> Verified game note.

![Dust Duel screenshot placeholder](dust-duel-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/jomzrules-dotcom/dust-duel](https://github.com/jomzrules-dotcom/dust-duel)
- **Evidence:** [direct model evidence](https://github.com/jomzrules-dotcom/dust-duel/commit/133c83b90e0b5b572989de5d95d86e47a86cad5c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

1v1 game where two robot vacuums race to clean a dirty house. Whoever owns the most clean floor after 1 minute wins. Plays like Splatoon, but you drive over dirt instead of spraying paint. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jomzrules-dotcom/dust-duel/blob/main/client/game.js](https://github.com/jomzrules-dotcom/dust-duel/blob/main/client/game.js)
- [https://github.com/jomzrules-dotcom/dust-duel/commit/133c83b90e0b5b572989de5d95d86e47a86cad5c](https://github.com/jomzrules-dotcom/dust-duel/commit/133c83b90e0b5b572989de5d95d86e47a86cad5c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/jomzrules-dotcom/dust-duel

[Back to the awesome list](../../README.md)
