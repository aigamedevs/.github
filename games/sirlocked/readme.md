# SirLocked

> Verified game note.

![SirLocked screenshot placeholder](sirlocked-placeholder.svg)

## At a glance

- **Score:** 8.1/10
- **Model:** Claude Opus 5.5
- **Technology:** C#, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/duongtuankiet-se/SirLocked](https://github.com/duongtuankiet-se/SirLocked)
- **Evidence:** [direct model evidence](https://github.com/duongtuankiet-se/SirLocked/commit/abc4ff71c1f1bf76a9e7a04a087ba63d27c0c6ec)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A two-player cooperative detective game featuring real-time investigation, role-based gameplay, and AI-assisted case generation. Built with ASP.NET Core, MongoDB, SignalR, and Phaser 4. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/duongtuankiet-se/SirLocked/blob/main/src/BE/Services/AiCaseService.cs](https://github.com/duongtuankiet-se/SirLocked/blob/main/src/BE/Services/AiCaseService.cs)
- [https://github.com/duongtuankiet-se/SirLocked/commit/abc4ff71c1f1bf76a9e7a04a087ba63d27c0c6ec](https://github.com/duongtuankiet-se/SirLocked/commit/abc4ff71c1f1bf76a9e7a04a087ba63d27c0c6ec)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/duongtuankiet-se/SirLocked

[Back to the awesome list](../../README.md)
