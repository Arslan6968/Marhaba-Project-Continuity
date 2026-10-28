# Release and Publication Checklist

Use the relevant items for the scope. Do not mark unchecked items as complete.

## Repository and diff

- [ ] Confirm the intended repository, branch, and target commit.
- [ ] Review `git status` and the complete diff.
- [ ] Confirm no unrelated work or accidental files are included.
- [ ] Confirm generated artifacts, caches, local downloads, and machine-specific files are excluded when appropriate.

## Security and privacy

- [ ] Check for API keys, tokens, passwords, private keys, `.env` files, private endpoints, and embedded credentials.
- [ ] Check logs, fixtures, screenshots, samples, and templates for personal/customer data.
- [ ] Confirm secrets are handled via appropriate configuration and are not merely hidden by a local ignore rule.
- [ ] If a secret was committed, treat it as exposed: remove it from the reachable history as appropriate and rotate/revoke it. Deleting the current file alone is insufficient.
- [ ] Review new dependencies and relevant security/licensing concerns.

## Quality and documentation

- [ ] Run relevant tests, lint/type checks, and/or build; record what ran and what did not.
- [ ] Review error paths and important regression risks.
- [ ] Update README/setup/configuration docs for material changes.
- [ ] Document known limitations and mark experimental/incomplete status honestly.
- [ ] Confirm the license matches the intended sharing terms and the project has rights to included material.

## GitHub action

- [ ] Confirm whether the user asked to commit, push, create a public repository, publish a release, or only prepare the files.
- [ ] Confirm visibility and target remote before a public push.
- [ ] Inspect the staged files before committing.
- [ ] Avoid force-push or history rewriting unless specifically authorized.
- [ ] After the action, verify the observed result and report the actual commit/URL/status when available.

## Decision

- **Ready:** material checks passed and remaining risks are understood.
- **Ready with limitations:** no known release blocker, but clearly stated checks or features remain incomplete.
- **Not ready:** an important unresolved security, data-loss, correctness, licensing, or release-scope issue remains.

This checklist supports judgement; it is not a guarantee that a project is secure or defect-free.
