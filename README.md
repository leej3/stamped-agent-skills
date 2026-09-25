# STAMPED agent skills

This APM skill store initially publishes one skill: `stamped-assess`.
It helps an agent assess a particular version of a research or digital object against a declared use-case rubric and retain reviewable evidence.
The schema, validator, reference data, and assessment store live independently in [stamped-skills-assessment](https://github.com/stamped-principles/stamped-skills-assessment).
Neither project needs Skills Workshop.

## Install

Use APM 0.31.0 and pin an exact published commit in your project's `apm.yml`:

```yaml
name: my-assessment-project
version: 0.0.0
targets: [agent-skills, claude]
dependencies:
  apm:
    - git: stamped-principles/stamped-agent-skills
      ref: FULL_PUBLISHED_COMMIT
      skills: [stamped-assess]
```

Run `apm install`, commit the manifest and generated `apm.lock.yaml`, and ignore `apm_modules/`, `.agents/skills/stamped-assess/`, and `.claude/skills/stamped-assess/`.
Use `apm install --frozen` for subsequent restoration and `apm audit --ci` for integrity checks.
Choose just the targets your project uses.
APM performs native deployment; `agents/openai.yaml` supplies Codex metadata and the bundled Claude adapter describes its native entry point.

Install the assessment tool through your project's Python environment manager using the deployed skill's `requirements.txt`.
It pins the independent assessment package to an exact source revision.
Then ask the agent to use `stamped-assess` with your object and intended use.

A project that wants a startup reminder can add this to `AGENTS.md`:

> Use the installed `stamped-assess` skill when assessing artifacts with STAMPED.
> Record the intended use, scope, evidence, and unresolved barriers.

The package does not automatically edit startup instructions or publish assessment records.

## Develop

```sh
pixi install --locked
pixi run check-apm
pixi run audit-dependencies
pixi run python tools/check_assessment_dependency.py
```

The package check uses the actual APM CLI in disposable consumers, checks all skill resources for both agent targets, restores from the lock, and verifies that tampering is detected.
The source remains in `skills/stamped-assess/`; consumers keep generated copies outside version control.

The earlier general STAMPED draft and planning notes are preserved under `docs/history/`.
They are not published as active skills.
The move is separate from the new assessor's behavior and does not assert a license for those historical documents.
New assessor instructions are CC-BY-4.0; new packaging code is MIT.
