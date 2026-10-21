# Fish Fight

> Verified game note.

![Fish Fight screenshot placeholder](fish-fight-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/NafeesMansoor/fish-fight](https://github.com/NafeesMansoor/fish-fight)
- **Evidence:** [direct model evidence](https://github.com/NafeesMansoor/fish-fight/commit/e1b5234295d17cd3a2621d75bac893df68a7d414)
- **Live demo:** [open demo](https://nafeesmansoor.github.io/fish-fight/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A colorful 2D underwater survival-and-growth game for desktop and mobile browsers. You start as a small fish, eat smaller fish and food to grow, and avoid bigger predators. A strong score earns a better start in your next game. An unbelievably amazing score… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/NafeesMansoor/fish-fight/blob/main/src/ui/UI.ts](https://github.com/NafeesMansoor/fish-fight/blob/main/src/ui/UI.ts)
- [https://github.com/NafeesMansoor/fish-fight/commit/e1b5234295d17cd3a2621d75bac893df68a7d414](https://github.com/NafeesMansoor/fish-fight/commit/e1b5234295d17cd3a2621d75bac893df68a7d414)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/NafeesMansoor/fish-fight

[Back to the awesome list](../../README.md)
