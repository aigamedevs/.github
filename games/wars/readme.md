# Wars

> Verified game note.

![Wars screenshot](https://raw.githubusercontent.com/Devace-93/wars/main/docs/screenshots/desktop-dark-age.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/Devace-93/wars/blob/main/docs/screenshots/desktop-dark-age.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Devace-93/wars](https://github.com/Devace-93/wars)
- **Evidence:** [direct model evidence](https://github.com/Devace-93/wars/commit/769b5ee2df5ad569d06717bfc330567e7d1ebf9f)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Devace-93/wars/blob/main/docs/screenshots/desktop-dark-age.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Isometric RTS map with town and HUD panels; clear and readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Wars: an open-source real-time strategy game in the spirit of the classic age-advancing RTS. Rust sim, server, desktop, console, Android and iOS clients. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Devace-93/wars/blob/main/crates/sim/src/unit.rs](https://github.com/Devace-93/wars/blob/main/crates/sim/src/unit.rs)
- [https://github.com/Devace-93/wars/commit/769b5ee2df5ad569d06717bfc330567e7d1ebf9f](https://github.com/Devace-93/wars/commit/769b5ee2df5ad569d06717bfc330567e7d1ebf9f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Devace-93/wars

[Back to the awesome list](../../README.md)
