# PieceOff

> Verified game note.

![PieceOff screenshot](https://raw.githubusercontent.com/UnsupervisedMedia/PieceOffApp/main/docs/media/pieceoff-gameplay.gif)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 4.5/10 ([manually reviewed image](https://github.com/UnsupervisedMedia/PieceOffApp/blob/main/docs/media/pieceoff-gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/UnsupervisedMedia/PieceOffApp](https://github.com/UnsupervisedMedia/PieceOffApp)
- **Evidence:** [direct model evidence](https://github.com/UnsupervisedMedia/PieceOffApp/commit/7c0c73b71fa56e94e916f4060036472f64aecff2)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/UnsupervisedMedia/PieceOffApp/blob/main/docs/media/pieceoff-gameplay.gif) — 📸 4.5/10 · manual visual review · Use this frame for the game-level score. Jigsaw board with video pieces in a dark editor-like frame; mostly empty space.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Multiplayer jigsaw puzzles with smooth looping video, built in Rust (egui + axum WebSocket rooms). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/UnsupervisedMedia/PieceOffApp/blob/main/crates/pieceoff-server/src/lib.rs](https://github.com/UnsupervisedMedia/PieceOffApp/blob/main/crates/pieceoff-server/src/lib.rs)
- [https://github.com/UnsupervisedMedia/PieceOffApp/commit/7c0c73b71fa56e94e916f4060036472f64aecff2](https://github.com/UnsupervisedMedia/PieceOffApp/commit/7c0c73b71fa56e94e916f4060036472f64aecff2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/UnsupervisedMedia/PieceOffApp

[Back to the awesome list](../../README.md)
