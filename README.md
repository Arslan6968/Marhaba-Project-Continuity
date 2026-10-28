# Marhaba Project Continuity

**An evidence-first workflow skill that helps AI coding agents understand a project, protect working behavior, make focused changes, verify results, and hand work off clearly.**

> **Status: Experimental · v0.1.0**  
> Designed for portability, but not yet validated across every supported agent or project type. Expect to review and adapt it to your workflow.

## Why use it?

AI coding agents can be useful contributors, but unfamiliar repositories and incomplete session context can lead to avoidable mistakes: changing unrelated code, overlooking local work, assuming how a feature works, or claiming a test passed when it was never run.

Marhaba Project Continuity provides a repeatable, risk-aware workflow to help reduce those mistakes. It encourages agents to inspect before editing, preserve existing behavior, make small reversible changes, verify with evidence, and report limitations honestly.

## What it helps an agent do

- **Understand before changing:** inspect project instructions, architecture, repository status, relevant code, and available checks.
- **Preserve working behavior:** treat existing features, user data, interfaces, and compatibility as constraints unless the task says otherwise.
- **Work within scope:** avoid unrelated redesigns, speculative refactors, and unnecessary dependencies.
- **Scale caution to risk:** pay extra attention to data loss, secrets, authentication, migrations, deployments, and destructive Git operations.
- **Verify honestly:** separate what changed, what was tested, what passed, and what remains unverified.
- **Maintain continuity:** use concise project notes when they provide lasting value—without creating documentation for documentation's sake.
- **Prepare safer releases:** review diffs, secrets, licensing, known limitations, and release readiness before publishing.

## Quick start

1. Download or clone this repository.
2. Install the skill using the skill-loading mechanism documented by your AI coding agent. If the agent supports the open Agent Skills format, provide the folder containing `SKILL.md`.
3. Confirm the agent has discovered or loaded the skill; installation paths and activation methods vary by product.
4. Ask the agent to inspect the current project and follow the skill's workflow for your task.
5. For an existing or long-running project, consider adapting the optional templates in `assets/`.

Clone the repository:

```bash
git clone https://github.com/Arslan6968/marhaba-project-continuity.git
```

If the repository has not yet been published at that address, download the ZIP from GitHub after publication, or replace the URL with your actual repository URL.

### Example request

> Before changing anything, inspect this repository and follow Marhaba Project Continuity. Identify the relevant code, check for uncommitted work, preserve unrelated changes, make the smallest appropriate fix, run the relevant checks, and report exactly what was and was not verified. Do not commit or publish anything unless I ask.

## What's included

```text
marhaba-project-continuity/
├── SKILL.md                         # Main skill instructions
├── README.md                        # Overview and quick start
├── LICENSE                          # MIT License
├── SECURITY.md                      # Safe-use and reporting guidance
├── CONTRIBUTING.md                  # Contribution workflow
├── CHANGELOG.md                     # Version history
├── GITHUB_SETUP.md                  # Suggested GitHub description and topics
├── .gitignore
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── references/
│   ├── lifecycle-workflows.md
│   ├── risk-policy.md
│   ├── verification-rules.md
│   ├── release-checklist.md
│   └── compatibility-notes.md
├── assets/
│   ├── PROJECT_CONTEXT.template.md
│   ├── PROJECT_STATE.template.md
│   └── DECISIONS.template.md
├── evals/
│   ├── scenarios.md
│   └── expected-behavior.md
└── scripts/
    └── validate_skill.py
```

## Optional continuity templates

Use these only if the project benefits from them. Small projects may need none of them.

| Template | Purpose |
|---|---|
| `assets/PROJECT_CONTEXT.template.md` | Stable purpose, architecture, commands, and constraints |
| `assets/PROJECT_STATE.template.md` | Current state, verified facts, blockers, and next steps |
| `assets/DECISIONS.template.md` | Important decisions and why they were made |

Keep notes current and concise. Never put passwords, API keys, tokens, private customer information, or other secrets in them.

## Validate the repository

Requires Python 3.9+ and uses the standard library only:

```bash
python scripts/validate_skill.py
```

This script performs lightweight structural checks. It is **not** a full YAML parser, a security audit, or proof that the skill behaves correctly. Review the evaluation scenarios in `evals/` and test the skill with the agents and project types you actually use. If available, also use the official Agent Skills validator.

## Compatibility

The skill uses the `SKILL.md`-based Agent Skills structure to improve portability. Compatibility is not guaranteed: agents differ in discovery, installation paths, supported metadata, referenced-file handling, tools, permissions, and instruction-following behavior. Read [`references/compatibility-notes.md`](references/compatibility-notes.md) and verify support in your agent's own documentation.

## Safety and limitations

- This is guidance for an AI agent, **not a security boundary**.
- It does not grant access to files, tools, credentials, or permissions.
- It cannot guarantee correct code, complete testing, security, or preservation of every feature.
- Review commands and diffs before allowing consequential actions.
- Explicitly authorize high-impact operations such as publishing, deployment, destructive migrations, deletion, or force-pushing.
- Treat all AI-generated changes as reviewable work.

## Project status and roadmap

This is an early experimental release. Priorities for future versions include:

- Test and document behavior across more coding agents.
- Expand evaluation scenarios based on reproducible real-world outcomes.
- Improve validation and installation guidance where evidence shows it is needed.
- Keep the core skill focused and avoid unnecessary process for small tasks.

See [`CHANGELOG.md`](CHANGELOG.md) for release history. Proposed improvements are welcome through issues and pull requests.

## Contributing

Please share concrete examples: the task, relevant agent and version, expected behavior, actual behavior, and checks performed. Avoid sharing private source code or secrets. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Security

Do not post credentials, private code, or sensitive customer data in public issues. Read [`SECURITY.md`](SECURITY.md) before reporting a concern.

## License

Released under the [MIT License](LICENSE). The license applies to this repository's contents; it does not imply that third-party tools, agents, or dependencies are licensed the same way.

---

Created as an independent community-oriented project. Product and company names mentioned for compatibility are the property of their respective owners; no affiliation or endorsement is implied.
