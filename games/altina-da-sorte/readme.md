# Altina da Sorte

> Verified game note.

![Altina da Sorte screenshot placeholder](altina-da-sorte-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/GuTorelliImpacta/testejogo](https://github.com/GuTorelliImpacta/testejogo)
- **Evidence:** [direct model evidence](https://github.com/GuTorelliImpacta/testejogo/commit/7607cbb393d18676e636e84991fc254fb432a5fd)
- **Live demo:** [open demo](https://altina-da-sorte.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jogo de bingo para tablet, feito para a Dona Altina: cartelas grandes, voz narrando as bolas, créditos que nunca acabam (o jogo dá um presente quando o saldo zera) e um "painel do neto" protegido por PIN para ajustar a dificuldade. Funciona offline (PWA); o… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GuTorelliImpacta/testejogo/blob/claude/new-session-t2beg1/src/audio/music.ts](https://github.com/GuTorelliImpacta/testejogo/blob/claude/new-session-t2beg1/src/audio/music.ts)
- [https://github.com/GuTorelliImpacta/testejogo/commit/7607cbb393d18676e636e84991fc254fb432a5fd](https://github.com/GuTorelliImpacta/testejogo/commit/7607cbb393d18676e636e84991fc254fb432a5fd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/GuTorelliImpacta/testejogo

[Back to the awesome list](../../README.md)
