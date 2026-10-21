# Bug Survivors

> Verified game note.

![Bug Survivors screenshot](https://raw.githubusercontent.com/PostHog/survivors/main/docs/header.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 6.6/10 ([manually reviewed image](https://github.com/PostHog/survivors/blob/main/docs/header.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Phaser, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/PostHog/survivors](https://github.com/PostHog/survivors)
- **Evidence:** [direct model evidence](https://github.com/PostHog/survivors/commit/93aba32e57d382655ff5740833d7bfe28f753e36)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/PostHog/survivors/blob/main/docs/header.png) — 📸 6.6/10 · manual visual review · Use this frame for the game-level score. Top-down arena packed with bug enemies, pickups, waves and survival HUD; busy, energetic survivors scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Bug Survivors, the PostHog browser game, and the Cloudflare Worker that makes a themed copy per prospect. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/PostHog/survivors/blob/main/game/bug-survivors/public/guide.html](https://github.com/PostHog/survivors/blob/main/game/bug-survivors/public/guide.html)
- [https://github.com/PostHog/survivors/commit/93aba32e57d382655ff5740833d7bfe28f753e36](https://github.com/PostHog/survivors/commit/93aba32e57d382655ff5740833d7bfe28f753e36)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/PostHog/survivors

[Back to the awesome list](../../README.md)
