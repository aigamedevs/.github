# Minesweeper

> Verified game note.

![Minesweeper screenshot](https://raw.githubusercontent.com/1cto/minesweeper/main/docs/screenshot.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/1cto/minesweeper/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/1cto/minesweeper](https://github.com/1cto/minesweeper)
- **Evidence:** [direct model evidence](https://github.com/1cto/minesweeper/commit/15db963d88f0ff9d2f62109c42da8b0e7147d2ed)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/1cto/minesweeper/blob/main/docs/screenshot.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Faithful Windows 9x Minesweeper board mid-game; crisp but tiny and plain.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A faithful browser recreation of Windows 95/98 Minesweeper, built with React and TypeScript. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/1cto/minesweeper/blob/main/src/ui/sprites.ts](https://github.com/1cto/minesweeper/blob/main/src/ui/sprites.ts)
- [https://github.com/1cto/minesweeper/commit/15db963d88f0ff9d2f62109c42da8b0e7147d2ed](https://github.com/1cto/minesweeper/commit/15db963d88f0ff9d2f62109c42da8b0e7147d2ed)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/1cto/minesweeper

[Back to the awesome list](../../README.md)
