# Chess Battle

> Verified game note.

![Chess Battle screenshot placeholder](chess-battle-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/forestmack/chess-battle](https://github.com/forestmack/chess-battle)
- **Evidence:** [direct model evidence](https://github.com/forestmack/chess-battle/commit/77deeb18eed25037704a757b0906622aa5270438)
- **Live demo:** [open demo](https://forestmack.github.io/chess-battle/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Chess with a gold economy. Each side starts with a king, 3 pawns and a knight. Capture pieces to earn gold, spend it to drop reinforcements, and checkmate your opponent. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/forestmack/chess-battle/blob/main/index.html](https://github.com/forestmack/chess-battle/blob/main/index.html)
- [https://github.com/forestmack/chess-battle/commit/77deeb18eed25037704a757b0906622aa5270438](https://github.com/forestmack/chess-battle/commit/77deeb18eed25037704a757b0906622aa5270438)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/forestmack/chess-battle

[Back to the awesome list](../../README.md)
