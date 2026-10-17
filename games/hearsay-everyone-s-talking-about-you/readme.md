# Hearsay: Everyone's talking about you.

> Verified game note.

![Hearsay: Everyone's talking about you. screenshot](https://raw.githubusercontent.com/Yashgurav002/hearsay/main/docs/screenshots/3d-inn.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/Yashgurav002/hearsay/blob/main/docs/screenshots/3d-inn.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Unreal Engine, C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Yashgurav002/hearsay](https://github.com/Yashgurav002/hearsay)
- **Evidence:** [direct model evidence](https://github.com/Yashgurav002/hearsay/commit/bfadf84452d4aae5c334027d74773db8744de6bf)
- **Live demo:** [open demo](https://hearsay-six.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Yashgurav002/hearsay/blob/main/docs/screenshots/3d-inn.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Low-poly village square with NPCs, speech bubbles and gossip panel; readable, modest detail.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

NPCs that remember what you did, and gossip about it. A 3D game + NPC memory engine on a FalkorDB graph (Graph Hacks 2026). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Yashgurav002/hearsay/blob/main/frontend/src/Game3D.tsx](https://github.com/Yashgurav002/hearsay/blob/main/frontend/src/Game3D.tsx)
- [https://github.com/Yashgurav002/hearsay/commit/bfadf84452d4aae5c334027d74773db8744de6bf](https://github.com/Yashgurav002/hearsay/commit/bfadf84452d4aae5c334027d74773db8744de6bf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Yashgurav002/hearsay

[Back to the awesome list](../../README.md)
