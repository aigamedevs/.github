# LATTICE

> Verified game note.

![LATTICE screenshot placeholder](lattice-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Malkefjes/newgame](https://github.com/Malkefjes/newgame)
- **Evidence:** [direct model evidence](https://github.com/Malkefjes/newgame/commit/5fbe8ec20f3907083a747effa3348d23e4de5ae9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser tower defense where towers are nodes you wire together with beams. Nodes block. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Malkefjes/newgame/blob/claude/new-session-k9k6u0/src/sim/game.ts](https://github.com/Malkefjes/newgame/blob/claude/new-session-k9k6u0/src/sim/game.ts)
- [https://github.com/Malkefjes/newgame/commit/5fbe8ec20f3907083a747effa3348d23e4de5ae9](https://github.com/Malkefjes/newgame/commit/5fbe8ec20f3907083a747effa3348d23e4de5ae9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Malkefjes/newgame

[Back to the awesome list](../../README.md)
