# Garbage Kingdom

> Verified game note.

![Garbage Kingdom screenshot placeholder](garbage-kingdom-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/antonycorp11-blip/garbage](https://github.com/antonycorp11-blip/garbage)
- **Evidence:** [direct model evidence](https://github.com/antonycorp11-blip/garbage/commit/41a2de1b35daa17a88b703dceaa2783d60b22dbe)
- **Live demo:** [open demo](https://athg.antonycorp11.workers.dev)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jogo incremental 2D top-down de coleta, reciclagem e automação: remova 1.000.000 de unidades de lixo de um terreno gigantesco. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/antonycorp11-blip/garbage/blob/claude/garbage-kingdom-game/src/render/machinesDraw.ts](https://github.com/antonycorp11-blip/garbage/blob/claude/garbage-kingdom-game/src/render/machinesDraw.ts)
- [https://github.com/antonycorp11-blip/garbage/commit/41a2de1b35daa17a88b703dceaa2783d60b22dbe](https://github.com/antonycorp11-blip/garbage/commit/41a2de1b35daa17a88b703dceaa2783d60b22dbe)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/antonycorp11-blip/garbage

[Back to the awesome list](../../README.md)
