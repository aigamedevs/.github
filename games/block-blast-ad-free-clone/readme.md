# Block Blast (ad-free clone)

> Verified game note.

![Block Blast (ad-free clone) screenshot placeholder](block-blast-ad-free-clone-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/yahlibrown/Block-Blast](https://github.com/yahlibrown/Block-Blast)
- **Evidence:** [direct model evidence](https://github.com/yahlibrown/Block-Blast/commit/4cd70abe5c5298bcfb01d95e8f00bba4012dc57f)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An ad-free, single-player Block Blast Classic clone. TypeScript + Vite + Canvas 2D, no framework or game engine (see docs/adr/0001-.md). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/yahlibrown/Block-Blast/blob/block-blast/src/renderer/renderer.ts](https://github.com/yahlibrown/Block-Blast/blob/block-blast/src/renderer/renderer.ts)
- [https://github.com/yahlibrown/Block-Blast/commit/4cd70abe5c5298bcfb01d95e8f00bba4012dc57f](https://github.com/yahlibrown/Block-Blast/commit/4cd70abe5c5298bcfb01d95e8f00bba4012dc57f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/yahlibrown/Block-Blast

[Back to the awesome list](../../README.md)
