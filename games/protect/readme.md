# Protect

> Verified game note.

![Protect screenshot](https://raw.githubusercontent.com/hsglc/protect/main/docs/hero.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/hsglc/protect/blob/main/docs/hero.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/hsglc/protect](https://github.com/hsglc/protect)
- **Evidence:** [direct model evidence](https://github.com/hsglc/protect/commit/3a077e8f0f0880e7b44405ed0076ccdcb70258f2)
- **Live demo:** [open demo](https://protect.huseyinglc0-946.workers.dev)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hsglc/protect/blob/main/docs/hero.jpg) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. Glowing co-op tower-defence path on a dark island with towers, lanes and player list; clean neon style.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Two rifts open on a floating island. Monsters pour out of both and wind their way toward a single castle. You and up to three friends share the same battlefield, the same castle and the same twelve build sites — and you either hold it together or lose it… Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hsglc/protect/blob/main/src/client/ui/ui.ts](https://github.com/hsglc/protect/blob/main/src/client/ui/ui.ts)
- [https://github.com/hsglc/protect/commit/3a077e8f0f0880e7b44405ed0076ccdcb70258f2](https://github.com/hsglc/protect/commit/3a077e8f0f0880e7b44405ed0076ccdcb70258f2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/hsglc/protect

[Back to the awesome list](../../README.md)
