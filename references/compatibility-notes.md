# Compatibility Notes

## Format

This package uses the open Agent Skills convention: a skill directory with a `SKILL.md` file containing YAML frontmatter (`name` and `description`) followed by Markdown instructions. Supporting documentation and templates are placed in `references/` and `assets/`.

## Portability

The content is deliberately vendor-neutral and avoids assuming a specific shell, editor, programming language, agent API, or permission model. It may be useful in coding agents that support the Agent Skills format or can read Markdown instructions.

Portability does **not** mean universal compatibility:

- A product may not support Agent Skills or may implement only part of the format.
- Discovery and installation paths differ by product, configuration, and version.
- Some clients may not automatically load referenced files or may require explicit user instructions.
- Tools, permissions, terminal access, browsing, test runners, and file-editing capabilities vary.
- Following written instructions is model- and context-dependent; the skill does not enforce policy technically.

## Installation advice

Use the target product's current official documentation to locate its supported skills directory and activation method. Install the whole skill folder where the client expects it, then test discovery with a simple, low-risk task. Do not assume copying a folder into an arbitrary path has enabled the skill.

For a product that does not support the standard directly, users may adapt the instructions to its native custom-instruction mechanism. Keep a clear note that such an adaptation is not identical to native support.

## Validation

This repository's validator checks basic local structure and references. It does not fully parse YAML or certify compatibility with any particular agent. Where available, run the official Agent Skills reference validator, then test on each target client/version and document the observed result.
