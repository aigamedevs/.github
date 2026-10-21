# CSS Battle Royale

> Verified game note.

![CSS Battle Royale screenshot placeholder](css-battle-royale-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Shrxmy/kickoff-battle-royale](https://github.com/Shrxmy/kickoff-battle-royale)
- **Evidence:** [direct model evidence](https://github.com/Shrxmy/kickoff-battle-royale/commit/036bae0e1249dd0d71637219f09f614165a1920e)
- **Live demo:** [open demo](https://kickoff-battle-royale.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Blooket-style Battle Royale for the Computer Science Society kickoff. The projector runs /host; members scan the QR (or open / and type the code) on their phones, pick a CSAR and duel 1v1 until one is left. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Shrxmy/kickoff-battle-royale/blob/main/src/app/host/page.tsx](https://github.com/Shrxmy/kickoff-battle-royale/blob/main/src/app/host/page.tsx)
- [https://github.com/Shrxmy/kickoff-battle-royale/commit/036bae0e1249dd0d71637219f09f614165a1920e](https://github.com/Shrxmy/kickoff-battle-royale/commit/036bae0e1249dd0d71637219f09f614165a1920e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Shrxmy/kickoff-battle-royale

[Back to the awesome list](../../README.md)
