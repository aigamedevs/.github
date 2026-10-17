# Chaos Theory

> Verified game note.

![Chaos Theory screenshot placeholder](chaos-theory-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/riddhisingla2028-cpu/chaos-theory](https://github.com/riddhisingla2028-cpu/chaos-theory)
- **Evidence:** [direct model evidence](https://github.com/riddhisingla2028-cpu/chaos-theory/commit/59dc2e1c46ede9263d671e1111db25cf841900a6)
- **Live demo:** [open demo](https://chaos-theory-eight.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A minimalist browser survival game where players adapt to constantly changing rules and chaos events. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/riddhisingla2028-cpu/chaos-theory/blob/main/src/game/engine.ts](https://github.com/riddhisingla2028-cpu/chaos-theory/blob/main/src/game/engine.ts)
- [https://github.com/riddhisingla2028-cpu/chaos-theory/commit/59dc2e1c46ede9263d671e1111db25cf841900a6](https://github.com/riddhisingla2028-cpu/chaos-theory/commit/59dc2e1c46ede9263d671e1111db25cf841900a6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/riddhisingla2028-cpu/chaos-theory

[Back to the awesome list](../../README.md)
