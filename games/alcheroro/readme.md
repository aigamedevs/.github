# AlcheRoro

> Verified game note.

![AlcheRoro screenshot placeholder](alcheroro-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/SuzukiCecil/AlcheRoro](https://github.com/SuzukiCecil/AlcheRoro)
- **Evidence:** [direct model evidence](https://github.com/SuzukiCecil/AlcheRoro/commit/bfe5e4357f84fb618c8c92f7de9a2bc11fe03291)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

要件定義書（要件定義書.md）に基づく、プレイヤー vs CPU の2人対戦Webボードゲーム。. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/SuzukiCecil/AlcheRoro/blob/main/src/components/Modals.tsx](https://github.com/SuzukiCecil/AlcheRoro/blob/main/src/components/Modals.tsx)
- [https://github.com/SuzukiCecil/AlcheRoro/commit/bfe5e4357f84fb618c8c92f7de9a2bc11fe03291](https://github.com/SuzukiCecil/AlcheRoro/commit/bfe5e4357f84fb618c8c92f7de9a2bc11fe03291)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/SuzukiCecil/AlcheRoro

[Back to the awesome list](../../README.md)
