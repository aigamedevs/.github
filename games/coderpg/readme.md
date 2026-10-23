# CodeRPG

> Verified game note.

![CodeRPG screenshot placeholder](coderpg-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/LiminallyYours/CodeRPG](https://github.com/LiminallyYours/CodeRPG)
- **Evidence:** [direct model evidence](https://github.com/LiminallyYours/CodeRPG/commit/ac97c5d27d77fcd3b78fd50626aa3aa015e39eb8)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A text RPG that runs inside Claude Code. Claude is the game master, and you type what you do at the normal prompt. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/LiminallyYours/CodeRPG/blob/main/rules/rpg.py](https://github.com/LiminallyYours/CodeRPG/blob/main/rules/rpg.py)
- [https://github.com/LiminallyYours/CodeRPG/commit/ac97c5d27d77fcd3b78fd50626aa3aa015e39eb8](https://github.com/LiminallyYours/CodeRPG/commit/ac97c5d27d77fcd3b78fd50626aa3aa015e39eb8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/LiminallyYours/CodeRPG

[Back to the awesome list](../../README.md)
