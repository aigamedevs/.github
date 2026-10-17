# VIBE CODER

> Verified game note.

![VIBE CODER screenshot](https://raw.githubusercontent.com/ichorid/vibecoder/main/docs/screenshot.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/ichorid/vibecoder/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/ichorid/vibecoder](https://github.com/ichorid/vibecoder)
- **Evidence:** [direct model evidence](https://github.com/ichorid/vibecoder/commit/0ac73d255830ed24d632599d8d82cffc1f25fc2a)
- **Live demo:** [open demo](https://ichorid.github.io/vibecoder/)
- **Additional live link:** [open demo](https://ichorid.github.io/vibecoder/music-lab/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ichorid/vibecoder/blob/main/docs/screenshot.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Phone clicker UI with office scene, prompt button, upgrades and log; tidy pixel UI, small.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Clicker game about vibe coding. Based on real events. Got a cat in it and some vibes. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ichorid/vibecoder/blob/main/src/game/selectors.ts](https://github.com/ichorid/vibecoder/blob/main/src/game/selectors.ts)
- [https://github.com/ichorid/vibecoder/commit/0ac73d255830ed24d632599d8d82cffc1f25fc2a](https://github.com/ichorid/vibecoder/commit/0ac73d255830ed24d632599d8d82cffc1f25fc2a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/ichorid/vibecoder

[Back to the awesome list](../../README.md)
