# RISKBOUND

> Verified game note.

![RISKBOUND screenshot](https://raw.githubusercontent.com/mutima89/riskbound/main/Docs/Screenshots/Cast_Workspace.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.8/10 ([manually reviewed image](https://github.com/mutima89/riskbound/blob/main/Docs/Screenshots/Cast_Workspace.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Unreal Engine, C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/mutima89/riskbound](https://github.com/mutima89/riskbound)
- **Evidence:** [direct model evidence](https://github.com/mutima89/riskbound/commit/926ad22f10459774dd2eb0ed888a2ff2f3f98210)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/mutima89/riskbound/blob/main/Docs/Screenshots/Cast_Workspace.jpg) — 📸 6.8/10 · manual visual review · Use this frame for the game-level score. Realistic office interior with lit desks, monitors and NPCs; solid lighting and scene detail.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Riskbound is a risk management career simulator exploring real-world risk analysis, financial decision-making, enterprise risk tools, and career progression from Junior Risk Analyst to Chief Risk Officer. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mutima89/riskbound/blob/main/Source/Riskbound/Private/World/RbValtrenHQ.cpp](https://github.com/mutima89/riskbound/blob/main/Source/Riskbound/Private/World/RbValtrenHQ.cpp)
- [https://github.com/mutima89/riskbound/commit/926ad22f10459774dd2eb0ed888a2ff2f3f98210](https://github.com/mutima89/riskbound/commit/926ad22f10459774dd2eb0ed888a2ff2f3f98210)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/mutima89/riskbound

[Back to the awesome list](../../README.md)
