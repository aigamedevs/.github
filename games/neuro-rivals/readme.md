# Neuro Rivals

> Verified game note.

![Neuro Rivals screenshot](https://raw.githubusercontent.com/Chloudde/neuro-rivals/main/docs/screenshots/race-start.jpg)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/Chloudde/neuro-rivals/blob/main/docs/screenshots/race-start.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Chloudde/neuro-rivals](https://github.com/Chloudde/neuro-rivals)
- **Evidence:** [direct model evidence](https://github.com/Chloudde/neuro-rivals/commit/cb166a918ab5224ee7433255ccecf0a25fa26e41)
- **Live demo:** [open demo](https://chloudde.github.io/neuro-rivals/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Chloudde/neuro-rivals/blob/main/docs/screenshots/race-start.jpg) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Portrait top-down race start grid with coloured cars, lap and timer; simple.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

2D top-down racer where neuroevolved neural-network AI drivers learn to race, and you race against them. TypeScript + Canvas. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Chloudde/neuro-rivals/blob/main/src/ui/EditorScene.ts](https://github.com/Chloudde/neuro-rivals/blob/main/src/ui/EditorScene.ts)
- [https://github.com/Chloudde/neuro-rivals/commit/cb166a918ab5224ee7433255ccecf0a25fa26e41](https://github.com/Chloudde/neuro-rivals/commit/cb166a918ab5224ee7433255ccecf0a25fa26e41)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Chloudde/neuro-rivals

[Back to the awesome list](../../README.md)
