# Carrazy

> Verified game note.

![Carrazy screenshot placeholder](carrazy-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/GrantBuonviri/Carrazy](https://github.com/GrantBuonviri/Carrazy)
- **Evidence:** [direct model evidence](https://github.com/GrantBuonviri/Carrazy/commit/d0b5ae7fe73a7dee3f0268de94ac52239787f659)
- **Live demo:** [open demo](https://grantbuonviri.github.io/Carrazy/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser puzzle game about conquering a 20 × 20 grid. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GrantBuonviri/Carrazy/blob/claude/amazing-noether-mlvxt1/src/ui/renderer.ts](https://github.com/GrantBuonviri/Carrazy/blob/claude/amazing-noether-mlvxt1/src/ui/renderer.ts)
- [https://github.com/GrantBuonviri/Carrazy/commit/d0b5ae7fe73a7dee3f0268de94ac52239787f659](https://github.com/GrantBuonviri/Carrazy/commit/d0b5ae7fe73a7dee3f0268de94ac52239787f659)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/GrantBuonviri/Carrazy

[Back to the awesome list](../../README.md)
