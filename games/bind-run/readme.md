# bind-run（仮称）

> Verified game note.

![bind-run（仮称） screenshot placeholder](bind-run-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/suutukuru/bind-run](https://github.com/suutukuru/bind-run)
- **Evidence:** [direct model evidence](https://github.com/suutukuru/bind-run/commit/543cf29db7b6d6f03c2a8b5ab6a473e6e525c2be)
- **Live demo:** [open demo](https://suutukuru.github.io/bind-run/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

ゴム紐でつながった 2 人のキャラクターを同時に操作し、敵の群れを生き延びる 2D サバイバルアクション型ローグライト。スマートフォン（iOS / Android）向けで、Godot 4 で開発する。. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/suutukuru/bind-run/blob/claude/phase0-docs/scenes/debug/tuning_panel.gd](https://github.com/suutukuru/bind-run/blob/claude/phase0-docs/scenes/debug/tuning_panel.gd)
- [https://github.com/suutukuru/bind-run/commit/543cf29db7b6d6f03c2a8b5ab6a473e6e525c2be](https://github.com/suutukuru/bind-run/commit/543cf29db7b6d6f03c2a8b5ab6a473e6e525c2be)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/suutukuru/bind-run

[Back to the awesome list](../../README.md)
