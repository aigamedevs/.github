# Сумеречный шабаш — квиз с кнопками

> Verified game note.

![Сумеречный шабаш — квиз с кнопками screenshot placeholder](game-nafanyan-halloween-app-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Nafanyan/halloween_app](https://github.com/Nafanyan/halloween_app)
- **Evidence:** [direct model evidence](https://github.com/Nafanyan/halloween_app/commit/41481a6257cabaa39e55348d786bf90b51d5be7d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Своя игра для вечеринки в локальной сети: большой экран (ТВ), телефоны игроков как кнопки, ведущий управляет с админ-страницы. Работает без интернета. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Nafanyan/halloween_app/blob/main/server/src/server.ts](https://github.com/Nafanyan/halloween_app/blob/main/server/src/server.ts)
- [https://github.com/Nafanyan/halloween_app/commit/41481a6257cabaa39e55348d786bf90b51d5be7d](https://github.com/Nafanyan/halloween_app/commit/41481a6257cabaa39e55348d786bf90b51d5be7d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Nafanyan/halloween_app

[Back to the awesome list](../../README.md)
