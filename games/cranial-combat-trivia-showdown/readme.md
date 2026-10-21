# Cranial Combat: Trivia Showdown

> Verified game note.

![Cranial Combat: Trivia Showdown screenshot placeholder](cranial-combat-trivia-showdown-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/jasonadams76-eng/CranialCombat](https://github.com/jasonadams76-eng/CranialCombat)
- **Evidence:** [direct model evidence](https://github.com/jasonadams76-eng/CranialCombat/commit/4f70ea74208b8016cc892251d2f62fff6647ca41)
- **Live demo:** [open demo](https://jasonadams76-eng.github.io/CranialCombat/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A multiplayer browser trivia game powered by the Open Trivia DB API. One player hosts, everyone else joins with a 4-letter code. There is no game server: the host's browser runs the game and players connect to it directly (peer-to-peer, via PeerJS). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jasonadams76-eng/CranialCombat/blob/main/js/ui.js](https://github.com/jasonadams76-eng/CranialCombat/blob/main/js/ui.js)
- [https://github.com/jasonadams76-eng/CranialCombat/commit/4f70ea74208b8016cc892251d2f62fff6647ca41](https://github.com/jasonadams76-eng/CranialCombat/commit/4f70ea74208b8016cc892251d2f62fff6647ca41)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/jasonadams76-eng/CranialCombat

[Back to the awesome list](../../README.md)
