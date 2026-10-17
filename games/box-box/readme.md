# Box Box

> Verified game note.

![Box Box screenshot placeholder](box-box-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Vybyranyi/box-box](https://github.com/Vybyranyi/box-box)
- **Evidence:** [direct model evidence](https://github.com/Vybyranyi/box-box/commit/3ff656c92de67623d145cc1a54737a57eec90a5e)
- **Live demo:** [open demo](https://box-box-tau.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Race-strategy game set in the 2026 season: run the pit wall and make the calls. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Vybyranyi/box-box/blob/main/.agents/skills/ui-ux-pro-max/scripts/design_system.py](https://github.com/Vybyranyi/box-box/blob/main/.agents/skills/ui-ux-pro-max/scripts/design_system.py)
- [https://github.com/Vybyranyi/box-box/commit/3ff656c92de67623d145cc1a54737a57eec90a5e](https://github.com/Vybyranyi/box-box/commit/3ff656c92de67623d145cc1a54737a57eec90a5e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Vybyranyi/box-box

[Back to the awesome list](../../README.md)
