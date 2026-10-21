# Picle

> Verified game note.

![Picle screenshot placeholder](picle-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/nickelstacker/picle](https://github.com/nickelstacker/picle)
- **Evidence:** [direct model evidence](https://github.com/nickelstacker/picle/commit/25345c60d832d07ad067f042cf42dc8536f21420)
- **Live demo:** [open demo](https://nickelstacker.github.io/picle/?day=2&x=0.65&y=0.87&zoom=16)
- **Additional live link:** [open demo](https://nickelstacker.github.io/picle/)
- **Additional live link:** [open demo](https://nickelstacker.github.io/picle/?analytics=off)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Daily zoomed-in photo guessing game. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nickelstacker/picle/blob/main/src/components/Game.tsx](https://github.com/nickelstacker/picle/blob/main/src/components/Game.tsx)
- [https://github.com/nickelstacker/picle/commit/25345c60d832d07ad067f042cf42dc8536f21420](https://github.com/nickelstacker/picle/commit/25345c60d832d07ad067f042cf42dc8536f21420)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/nickelstacker/picle

[Back to the awesome list](../../README.md)
