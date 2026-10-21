# Scripture Slinger

> Verified game note.

![Scripture Slinger screenshot](https://raw.githubusercontent.com/MasterTemple/scripture-slinger/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.5/10 ([manually reviewed image](https://github.com/MasterTemple/scripture-slinger/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/MasterTemple/scripture-slinger](https://github.com/MasterTemple/scripture-slinger)
- **Evidence:** [direct model evidence](https://github.com/MasterTemple/scripture-slinger/commit/6a9e831e35869df3afc1356d3ca546c2e6ee8ab7)
- **Live demo:** [open demo](https://mastertemple.github.io/scripture-slinger/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/MasterTemple/scripture-slinger/blob/main/docs/gameplay.gif) — 📸 5.5/10 · manual visual review · Use this frame for the game-level score. Moonlit desert wave screen with a lone figure, horizon city and wave banner; atmospheric but empty.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A typing game in the style of ZType, themed on the Bible. You are David with a sling. Locusts, ravens, fiery serpents and the occasional Goliath come at you, and you type their words to bring them down. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MasterTemple/scripture-slinger/blob/main/src/game.ts](https://github.com/MasterTemple/scripture-slinger/blob/main/src/game.ts)
- [https://github.com/MasterTemple/scripture-slinger/commit/6a9e831e35869df3afc1356d3ca546c2e6ee8ab7](https://github.com/MasterTemple/scripture-slinger/commit/6a9e831e35869df3afc1356d3ca546c2e6ee8ab7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/MasterTemple/scripture-slinger

[Back to the awesome list](../../README.md)
