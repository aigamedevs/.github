# Bustit

> Verified game note.

![Bustit screenshot placeholder](bustit-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/MuellerConstantin/bustit](https://github.com/MuellerConstantin/bustit)
- **Evidence:** [direct model evidence](https://github.com/MuellerConstantin/bustit/commit/d12f1e627c2e5d74682e454cb67d61477e0b56ad)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Multiplayer blackjack for closed groups, with play money only. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MuellerConstantin/bustit/blob/main/packages/engine/src/round/draft.ts](https://github.com/MuellerConstantin/bustit/blob/main/packages/engine/src/round/draft.ts)
- [https://github.com/MuellerConstantin/bustit/commit/d12f1e627c2e5d74682e454cb67d61477e0b56ad](https://github.com/MuellerConstantin/bustit/commit/d12f1e627c2e5d74682e454cb67d61477e0b56ad)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/MuellerConstantin/bustit

[Back to the awesome list](../../README.md)
