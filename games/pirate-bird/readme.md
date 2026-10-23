# Pirate Bird

> Verified game note.

![Pirate Bird screenshot](https://raw.githubusercontent.com/Ameer-Assi/pirate-bird-fpga/main/docs/gameplay.gif)

## At a glance

- **Score:** 5.8/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/Ameer-Assi/pirate-bird-fpga/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** SystemVerilog
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Ameer-Assi/pirate-bird-fpga](https://github.com/Ameer-Assi/pirate-bird-fpga)
- **Evidence:** [direct model evidence](https://github.com/Ameer-Assi/pirate-bird-fpga/commit/c769609d06d4e96358d2a6045819f1332baeb356)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Ameer-Assi/pirate-bird-fpga/blob/main/docs/gameplay.gif) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Photo of the FPGA board driving a small VGA monitor; game barely visible.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Flappy Bird-style pirate game in SystemVerilog for a Cyclone V FPGA (DE10-Standard) with 640x480 VGA output. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ameer-Assi/pirate-bird-fpga](https://github.com/Ameer-Assi/pirate-bird-fpga)
- [https://github.com/Ameer-Assi/pirate-bird-fpga/commit/c769609d06d4e96358d2a6045819f1332baeb356](https://github.com/Ameer-Assi/pirate-bird-fpga/commit/c769609d06d4e96358d2a6045819f1332baeb356)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Ameer-Assi/pirate-bird-fpga

[Back to the awesome list](../../README.md)
