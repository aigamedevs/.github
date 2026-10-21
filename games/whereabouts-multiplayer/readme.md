# Whereabouts: multiplayer

> Verified game note.

![Whereabouts: multiplayer screenshot placeholder](whereabouts-multiplayer-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/vic-goncalves/whereabouts-multiplayer](https://github.com/vic-goncalves/whereabouts-multiplayer)
- **Evidence:** [direct model evidence](https://github.com/vic-goncalves/whereabouts-multiplayer/commit/0bee92db8167af137f0d6fdd85b93034193ad1ef)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A GeoGuessr-style geography game with live party mode. You're dropped somewhere in Google Street View with no road names or address; look around, then pin where you think you are. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/vic-goncalves/whereabouts-multiplayer/blob/main/src/components/party/PartyGame.tsx](https://github.com/vic-goncalves/whereabouts-multiplayer/blob/main/src/components/party/PartyGame.tsx)
- [https://github.com/vic-goncalves/whereabouts-multiplayer/commit/0bee92db8167af137f0d6fdd85b93034193ad1ef](https://github.com/vic-goncalves/whereabouts-multiplayer/commit/0bee92db8167af137f0d6fdd85b93034193ad1ef)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/vic-goncalves/whereabouts-multiplayer

[Back to the awesome list](../../README.md)
