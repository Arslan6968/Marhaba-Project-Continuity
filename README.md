# Marhaba Project Continuity

**A practical, evidence-first workflow skill for AI coding agents.**

Marhaba Project Continuity helps an agent understand the repository before changing it, preserve working behavior, assess risk, verify results honestly, and leave useful handoff context for the next session or contributor.

> **Status: Experimental (0.1.0).** This is an initial public draft. It has structural checks and scenario-based evaluation material, but has not yet been validated across every agent or real-world project type.

## Why this exists

AI coding sessions can lose context, make assumptions about an unfamiliar codebase, change more than requested, overlook uncommitted work, or report success without sufficient verification. This skill provides a repeatable workflow to reduce those risks. It cannot guarantee bug-free changes; outcomes still depend on the agent, tools, project quality, and available tests.

## What it encourages

- Inspect before implementation.
- Preserve existing features and local work.
- Match the depth of investigation to the task's risk.
- Make small, focused, reversible changes.
- Verify with appropriate evidence and report limits honestly.
- Keep concise project-state notes when they provide real value.
- Review secrets, diffs, and release readiness before publication.

## Repository contents

```text
marhaba-project-continuity/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   ├── scenario_feedback.md
│   │   └── config.yml
│   ├── workflows/
│   │   └── validate.yml
│   └── pull_request_template.md
├── assets/
│   ├── DECISIONS.template.md
│   ├── PROJECT_CONTEXT.template.md
│   └── PROJECT_STATE.template.md
├── evals/
│   ├── expected-behavior.md
│   └── scenarios.md
├── references/
│   ├── compatibility-notes.md
│   ├── lifecycle-workflows.md
│   ├── release-checklist.md
│   ├── risk-policy.md
│   └── verification-rules.md
├── scripts/
│   └── validate_skill.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
└── SKILL.md
```

## How to use it

1. Download or clone this repository.
2. Copy the `marhaba-project-continuity` skill folder into the skills directory configured for your agent, or install it using that agent's supported skill mechanism.
3. Start or continue a coding task and check that the agent has discovered the skill. If not, use the agent's documented method to load or reference it.
4. For longer projects, adapt the templates in `assets/` only when useful; they are optional.

**Compatibility note:** The skill follows the open Agent Skills `SKILL.md` structure. This improves portability, but does not guarantee that every agent discovers it, follows every instruction, supports the same resources, or has the same tools. Installation paths and support vary by product and version. See [`references/compatibility-notes.md`](references/compatibility-notes.md).

## Validate the package

Requires Python 3.9+ and no third-party packages:

```bash
python scripts/validate_skill.py
```

This is a lightweight repository-structure check, not a complete YAML parser and not a replacement for the official Agent Skills validator. If available, also run the official `skills-ref validate` command for the target skill directory.

## Principles and limits

- The skill guides an agent; it does not grant tools, permissions, credentials, or repository access.
- It cannot independently guarantee security, compatibility, correctness, or preservation of every feature.
- High-impact actions still depend on explicit user authorization and the host agent's permission model.
- Templates are examples: tailor them and avoid storing secrets or private customer data.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Share reproducible scenarios and evidence of how the skill behaves, especially where an agent ignored an instruction, over-documented a project, or performed unnecessary work.

## Security

Do not submit secrets, private source code, personal information, or sensitive customer data in public issues. See [`SECURITY.md`](SECURITY.md).

## License

Licensed under the MIT License. See [`LICENSE`](LICENSE).
