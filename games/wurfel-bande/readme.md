# Würfel-Bande

> Verified game note.

![Würfel-Bande screenshot placeholder](wurfel-bande-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Babylon.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/maSchoeller/mario-party](https://github.com/maSchoeller/mario-party)
- **Evidence:** [direct model evidence](https://github.com/maSchoeller/mario-party/commit/45264b963d0fc50ecd29e06caf1028e9c54e27d4)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

3D-Party-Brettspiel im Browser: Ein Laptop am TV zeigt das Spielbrett, die Spieler steuern mit dem Handy. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/maSchoeller/mario-party/blob/main/apps/web/src/host/session.ts](https://github.com/maSchoeller/mario-party/blob/main/apps/web/src/host/session.ts)
- [https://github.com/maSchoeller/mario-party/commit/45264b963d0fc50ecd29e06caf1028e9c54e27d4](https://github.com/maSchoeller/mario-party/commit/45264b963d0fc50ecd29e06caf1028e9c54e27d4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/maSchoeller/mario-party

[Back to the awesome list](../../README.md)
