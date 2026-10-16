# holdumb

> Verified game note.

![holdumb screenshot placeholder](holdumb-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/creynia/holdumb](https://github.com/creynia/holdumb)
- **Evidence:** [direct model evidence](https://github.com/creynia/holdumb/commit/c65ba821772fe77842de6affc3a64fd7ba2166ae)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ultimate Texas Hold'em trainer with an interactive table simulator showing the EV of each decision. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/creynia/holdumb/blob/main/src/content/compile.ts](https://github.com/creynia/holdumb/blob/main/src/content/compile.ts)
- [https://github.com/creynia/holdumb/commit/c65ba821772fe77842de6affc3a64fd7ba2166ae](https://github.com/creynia/holdumb/commit/c65ba821772fe77842de6affc3a64fd7ba2166ae)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/creynia/holdumb

[Back to the awesome list](../../README.md)
