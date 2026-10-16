# Switch

> Verified game note.

![Switch screenshot placeholder](switch-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/aaronchongsl-del/switch-game](https://github.com/aaronchongsl-del/switch-game)
- **Evidence:** [direct model evidence](https://github.com/aaronchongsl-del/switch-game/commit/5b881b4a545d06c3ae7b3ff96210f1feab8e6fa8)
- **Live demo:** [open demo](https://switch-game-jet.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

90-second browser speed game switching between maths, memory, logic, wordplay, spatial and code puzzles, with a Supabase leaderboard. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/aaronchongsl-del/switch-game/blob/main/js/questions.js](https://github.com/aaronchongsl-del/switch-game/blob/main/js/questions.js)
- [https://github.com/aaronchongsl-del/switch-game/commit/5b881b4a545d06c3ae7b3ff96210f1feab8e6fa8](https://github.com/aaronchongsl-del/switch-game/commit/5b881b4a545d06c3ae7b3ff96210f1feab8e6fa8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/aaronchongsl-del/switch-game

[Back to the awesome list](../../README.md)
