# Claude Code adapter

APM's `claude` target deploys the shared skill to `.claude/skills/stamped-assess/`.
Claude Code reads that directory's `SKILL.md` directly.
No second set of assessment instructions is needed.

When a project wants a startup reminder, it can add this to `CLAUDE.md`:

> Use the installed `stamped-assess` skill for STAMPED assessments.
> Follow its use-case rubric and preserve scoped evidence and uncertainty.

This snippet is optional project setup guidance, not automatically executed by installing the skill.
