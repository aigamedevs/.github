# PortalShift

> Verified game note.

![PortalShift screenshot placeholder](portalshift-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Fable 5.1
- **Technology:** C#, Unity, Desktop
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/chvolk/PortalShifter](https://github.com/chvolk/PortalShifter)
- **Evidence:** [direct model evidence](https://github.com/chvolk/PortalShifter/commit/f9151e0586296eb2ddde411f037a49c93ea20900)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Unity car-combat racing with Splitgate-style portals: three-lap race, deathrace and battle modes over LAN netcode. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/chvolk/PortalShifter/blob/main/unity/PortalShift/Assets/PortalShift/Editor/TrackGen.cs](https://github.com/chvolk/PortalShifter/blob/main/unity/PortalShift/Assets/PortalShift/Editor/TrackGen.cs)
- [https://github.com/chvolk/PortalShifter/commit/f9151e0586296eb2ddde411f037a49c93ea20900](https://github.com/chvolk/PortalShifter/commit/f9151e0586296eb2ddde411f037a49c93ea20900)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/chvolk/PortalShifter

[Back to the awesome list](../../README.md)
