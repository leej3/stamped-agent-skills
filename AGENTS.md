# Working on STAMPED skills

Canonical skill source is `skills/stamped-assess/`; APM publishes that tree.
Keep required operating instructions and agent adapters inside the skill directory.
The external assessment package is an explicit pinned dependency, not a Workshop dependency.
Run `pixi run check-apm` after package or skill changes and `pixi run audit-dependencies` after dependency changes.
Preserve historical drafts separately from active skill instructions.
