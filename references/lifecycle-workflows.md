# Lifecycle Workflows

Use the workflow that matches the request; these are decision guides, not mandatory paperwork.

## A. New project

1. Extract the desired outcome, users, platform, constraints, and definition of done from the request.
2. Inspect the current directory and any generated scaffold before adding a new structure.
3. Identify the smallest useful end-to-end path. Prefer a working vertical slice over speculative architecture.
4. Check runtime, framework, dependency, and packaging constraints before selecting tools.
5. Implement the minimum coherent structure, run available checks, and document how to run it.
6. Flag assumptions that materially affect architecture or user-visible behavior.

Avoid building future features, plugin systems, elaborate abstractions, or extensive documentation without a current need.

## B. Existing project: feature or improvement

1. Trace the current user flow and identify the code that owns it.
2. Locate public interfaces, configuration, stored data, tests, and callers that could be affected.
3. Write a brief list of expected behaviors that must remain stable.
4. Implement a narrow change and extend tests where practical.
5. Review the final diff for accidental unrelated edits and compatibility changes.

Do not treat a request for one feature as permission to redesign the whole interface or replace the stack.

## C. Bug investigation

1. Capture the symptom, trigger, expected behavior, and actual behavior.
2. Reproduce the problem or identify why reproduction is not possible.
3. Trace the path from input to failure and check relevant logs, state, and edge cases.
4. Form a testable hypothesis; prefer evidence that can distinguish competing causes.
5. Fix the cause rather than only suppressing the visible symptom.
6. Add a regression check where practical, then run focused and relevant broader tests.
7. State whether the original failure was reproduced and whether the fix was verified.

Do not claim a root cause as confirmed when it is only plausible.

## D. Resuming a project or session

1. Inspect repository status before editing.
2. Read current project instructions and relevant state/handoff notes.
3. Confirm branch, latest commits, changed files, and relevant test/build status where available.
4. Compare notes with current files; stale notes must not override observed repository state.
5. Identify completed work, unfinished work, blockers, and the smallest next useful action.
6. Continue without repeating completed work unless verification or changed context requires it.

If essential state is missing, reconstruct what you can from available evidence before asking a focused question.

## E. Refactor or dependency change

1. Explain the reason and identify the behavior that must stay unchanged.
2. Assess compatibility, maintenance, licensing, security, deployment, and upgrade impact.
3. Confirm the proposed tool or dependency fits the existing project constraints.
4. Make a limited change with a rollback path where practical.
5. Run behavior/regression tests and inspect lockfiles, manifests, and generated files.
6. Report remaining migration and compatibility risks.

## F. Review or release preparation

1. Identify the exact branch, commit, files, feature, or release being reviewed.
2. Examine changes and compare them with the intended scope.
3. Run checks available in the environment; clearly identify checks that were skipped.
4. Review secrets, user data, licensing, third-party dependencies, documentation, and known limitations.
5. Use the release checklist and report blockers before release actions.
6. Publishing, pushing, deployment, or release is a separate action: do it only when authorized and tools permit.
