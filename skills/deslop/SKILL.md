---
name: deslop
description: Remove AI-generated code slop: verbose comments, defensive try/catch, unnecessary casts, deep nesting → early returns, inconsistent patterns. Run on diffs before review.
allowed-tools: Read Write Edit Glob Grep Shell
---

# Deslop: Clean AI-Generated Code Patterns

> **Goal:** Make a focused diff simpler, clearer, and consistent with the surrounding code without changing intended behavior.

`deslop` is a review procedure supplied by this skill. It is not a command-line program, formatter, linter, pre-commit hook, or CI executable unless the current repository explicitly provides one.

## When to Load

- Before reviewing an AI-assisted changeset
- After generating or heavily refactoring code
- When asked to clean up, simplify, or remove generated-code artifacts
- Before handing a diff to a formatter, compiler, or final review

## Scope First

1. Inspect the requested diff or changed files.
2. Read enough surrounding code to learn local conventions.
3. Check whether version control history is available before relying on it.
4. Keep edits inside the requested scope.
5. Preserve behavior unless the user explicitly asks for semantic changes.

Prefer diff-only cleanup. A repository-wide consistency change is a separate task and needs explicit scope.

## Patterns to Review

### 1. Comments That Restate the Code

Remove comments that add no information:

```python
# Before: restates the next line
# Add the item to the result list
result.append(item)

# After
result.append(item)
```

Keep comments that explain rationale, constraints, invariants, compatibility workarounds, or non-obvious failure modes.

### 2. Catch-and-Rethrow Without Added Value

Review exception handlers that merely catch and rethrow:

```java
try {
    return repository.save(entity);
} catch (Exception e) {
    throw e;
}
```

The wrapper above is redundant. However, logging and rethrowing can be useful when it adds context unavailable at a higher layer, attaches structured fields, translates an exception, or marks an operational boundary. Avoid duplicate logging when a global handler already records the same failure.

**Rule:** remove a handler only after checking recovery, cleanup, context enrichment, exception translation, metrics, and logging ownership.

### 3. Unnecessary Type Assertions

```typescript
// Before
const user = (await fetchUser(id)) as unknown as User

// Prefer, when fetchUser is correctly typed
const user = await fetchUser(id)
```

Fix types at their source when possible. Keep validation or assertions at genuine trust boundaries such as parsed JSON, untyped dependencies, environment variables, and external input.

### 4. Deep Nesting

Use guard clauses when they make the happy path clearer and preserve control flow:

```python
if not request.is_valid:
    return invalid_response()
if not user.can_submit:
    return forbidden_response()

return submit(request)
```

Do not flatten code when cleanup order, transaction scope, `else` semantics, or shared teardown would become less clear.

### 5. Inconsistent Local Conventions

Flag naming, error handling, return shapes, and API patterns that differ from nearby code. Follow the established domain vocabulary rather than imposing a universal naming rule. Do not rename public APIs as incidental cleanup.

### 6. Redundant Annotations

Remove annotations that add no useful information when inference is clear. Keep annotations on public APIs, empty collections where inference is weak, complex generic boundaries, and code where the annotation documents an intentional contract.

### 7. Boolean Trap Parameters

Calls such as `render(true, false)` are hard to read. When scope permits, prefer named options or domain-specific methods. Treat signature changes as API changes, not automatic cleanup.

### 8. Dead or Commented-Out Code

Delete genuinely dead code only when its removal is safe and recoverability is known. Do not assume Git history exists: the project may not use Git, the file may be untracked, or history may be unavailable. Preserve unique evidence or move it only with user approval.

### 9. Premature Abstraction

Question one-off wrappers or indirection created only for hypothetical future use. Do not inline abstractions that establish a meaningful boundary, improve testability, isolate a dependency, or encode a domain concept.

### 10. Unexplained Literals

Name literals when the name adds domain meaning or centralizes a reused policy. Do not replace every obvious local value with a constant.

## Language-Specific Checks

### Java

- Simplify redundant `Optional` or stream constructs only when null semantics remain identical.
- Review broad `@SuppressWarnings`; keep it when justified and narrowly scoped.
- Follow the repository's conventions for explicit generic types and `var`.

### Python

- `if x is not None` and `if x` are **not equivalent**. Preserve `is not None` when valid falsy values such as `0`, `False`, `""`, or empty collections must pass.
- Replace `return True if condition else False` with `return bool(condition)` only if coercion is intended; use `return condition` only if it is already boolean.
- Do not silently swallow broad exceptions. Preserve intentional best-effort behavior with a clear rationale and appropriate observability.

### TypeScript

- Choosing `interface` versus `type` is contextual. Consider declaration merging, extension patterns, unions/intersections, public API style, and repository conventions; do not rewrite one to the other mechanically.
- Remove assertions only after confirming inference and runtime validation are sufficient.
- Keep nullability utilities where they express a real boundary or invariant.

### PowerShell

- Prefer structured output and `Write-Verbose` over incidental `Write-Host` debugging, unless host-only presentation is intentional.
- Avoid repeated `+=` array growth in hot paths, but preserve semantics before converting to pipeline collection.
- Avoid `Invoke-Expression` when direct invocation with an argument array works.

## Procedure

1. Determine the exact review scope: diff, files, or selected hunks.
2. Inspect repository guidance and nearby code.
3. Identify candidates from the patterns above.
4. Classify each candidate:
   - **High confidence:** behavior-preserving and consistent with local style.
   - **Needs review:** semantic, public API, ownership, generated-code, or evidence risk.
5. Apply only high-confidence edits within scope.
6. Review the resulting diff for accidental behavior changes.
7. Run the smallest relevant checks available: formatter check, lint, type-check, compile, or targeted tests.
8. Report what changed, what was left for manual review, and which checks actually ran.

## Mutating Tools

Formatters and auto-fix commands can rewrite files beyond the intended hunks. Commands such as `spotlessApply`, `prettier --write`, `eslint --fix`, `black`, and similar tools are mutating operations.

- Do not run them merely because this skill was loaded.
- Obtain approval when their scope may exceed the requested edits or repository policy requires it.
- Prefer check modes first when available.
- Always inspect and report the resulting diff after an approved mutating run.
- Do not discard unrelated formatter changes without user authorization.

## Hard Gates

- Never remove rationale, invariants, compliance notes, or compatibility explanations merely because they are comments.
- Never remove suppressions without verifying the underlying issue is resolved.
- Never change public APIs as incidental cleanup.
- Never edit generated code when the source template or generator is the correct target.
- Never claim behavior is unchanged without reviewing the diff and running relevant checks where available.
- Never assume version-control recovery exists.
- Keep uncertain findings as recommendations rather than automatic edits.

## Report Format

```markdown
## Deslop report

- Scope reviewed: <diff/files>
- High-confidence cleanups applied: <count>
- Manual-review findings: <count>
- Checks run: <commands and outcomes, or "not run">

### Applied
- `path:line` — concise reason

### Needs review
- `path:line` — tradeoff or semantic risk
```

The report must describe evidence from the current workspace. Do not invent counts, commands, or successful checks.

## Attribution

Adapted from [Cursor Team Kit `deslop` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/deslop), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
