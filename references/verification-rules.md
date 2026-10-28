# Verification Rules

Verification claims must match the evidence actually collected.

## Use the right level of checking

1. **Inspection:** read relevant code/configuration and reviewed the diff. This is not a test.
2. **Focused check:** run the closest relevant unit test, lint rule, type check, or targeted manual interaction.
3. **Regression check:** test important existing behavior that could be affected.
4. **Broader check:** run the project's appropriate test suite or build when feasible and proportionate.
5. **Environment validation:** verify the feature in the target runtime/platform only if that environment was actually available.

Not every task requires every level. Choose based on risk, scope, and available tooling.

## Report results precisely

Use clear statements such as:

- `Passed`: the command completed and its success result was observed.
- `Failed`: the check ran and returned a failure or exposed an issue.
- `Blocked`: the check could not run because of a specific missing dependency, permission, environment, or resource.
- `Not run`: the check was not attempted.
- `Partially verified`: only some relevant paths or environments were checked.

Include command names or concise evidence when useful. Do not paste huge logs unless requested; retain relevant error details.

## Avoid common false claims

- A file edit does not prove the code compiles.
- A successful build does not prove all features behave correctly.
- A passing unit test does not prove production deployment or all integrations.
- A code review is not the same as executing a test.
- A browser screenshot alone may not prove backend persistence or accessibility.
- A push command is not proof of success unless its completion/result is observed.
- A test suite that did not run is not a passing test suite.

## Final diff review

Before handoff, inspect:

- Files changed and whether each change belongs to the request.
- Accidentally staged or modified user work.
- Secrets, tokens, private endpoints, and sensitive personal/customer data.
- Generated artifacts, caches, local downloads, build output, and machine-specific paths.
- Updated tests and docs where behavior materially changed.
- Error handling and failure paths relevant to the change.

## When verification is unavailable

Say what was not run and why. Suggest the smallest useful next check instead of implying the work is verified.
