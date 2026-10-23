# 六族遠征

> Verified game note.

![六族遠征 screenshot placeholder](game-devil10421-source-chess-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/devil10421-source/chess](https://github.com/devil10421-source/chess)
- **Evidence:** [direct model evidence](https://github.com/devil10421-source/chess/commit/06bdbee88c6a075ceb04598c8b73fdca71eedd66)
- **Live demo:** [open demo](https://devil10421-source.github.io/chess/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

單機 PVE 自走棋原型：六大文明、24 回合、TFT 式 7×8 錯位六角棋盤、34 種棋子（六族 24＋中立 10）、三星合成、商店／利息／文明等級、三層羈絆、文明 Buff／Debuff、遠征生命。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/devil10421-source/chess/blob/main/scripts/ui/game_screen.gd](https://github.com/devil10421-source/chess/blob/main/scripts/ui/game_screen.gd)
- [https://github.com/devil10421-source/chess/commit/06bdbee88c6a075ceb04598c8b73fdca71eedd66](https://github.com/devil10421-source/chess/commit/06bdbee88c6a075ceb04598c8b73fdca71eedd66)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/devil10421-source/chess

[Back to the awesome list](../../README.md)
