# BattleShip v1.0 (Amiral Battı)

> Verified game note.

![BattleShip v1.0 (Amiral Battı) screenshot](https://raw.githubusercontent.com/okantao/vurgahpeyi/main/docs/radar-animation.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/okantao/vurgahpeyi/blob/main/docs/radar-animation.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Java
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/okantao/vurgahpeyi](https://github.com/okantao/vurgahpeyi)
- **Evidence:** [direct model evidence](https://github.com/okantao/vurgahpeyi/commit/9aa66712fa907297913ac349b3dc55b4df0b9680)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/okantao/vurgahpeyi/blob/main/docs/radar-animation.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Battleship radar view; functional desktop UI

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Amiral Battı oyunu: ağ üzerinden (TCP) iki kişi veya bilgisayara karşı. Java 17 + Swing (FlatLaf koyu tema) arayüz, SQLite veritabanı. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/okantao/vurgahpeyi/blob/main/src/main/java/com/amiral/ui/BoardPanel.java](https://github.com/okantao/vurgahpeyi/blob/main/src/main/java/com/amiral/ui/BoardPanel.java)
- [https://github.com/okantao/vurgahpeyi/commit/9aa66712fa907297913ac349b3dc55b4df0b9680](https://github.com/okantao/vurgahpeyi/commit/9aa66712fa907297913ac349b3dc55b4df0b9680)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/okantao/vurgahpeyi

[Back to the awesome list](../../README.md)
