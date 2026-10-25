---
name: check-compiler-errors
description: "Hard gate: run the project's compiler, type checker, or static analyzer; group diagnostics; fix only high-confidence issues; and re-run until clean. Use before review or a PR. Covers Java, Python, TypeScript, and PowerShell."
allowed-tools: Read Write Edit Glob Grep Shell
---

# Check-Compiler-Errors: Hard Gate Before Review

> **Rule:** Run the checks configured by the project before requesting review. PowerShell ScriptAnalyzer is a static analyzer, not a compiler.

## When to Load

- Before creating a PR.
- After changes to types, imports, signatures, or build configuration.
- When CI reports compilation, type-checking, or static-analysis failures.

## Choose the Project Command

Prefer the repository's documented build or check command. Inspect its configuration rather than inventing flags.

| Language | Preferred command examples | Scope |
|---|---|---|
| **Java** | Maven/Gradle wrapper or the documented build task, such as `./mvnw compile` or `./gradlew compileJava` | Compilation with the project's dependencies and options. |
| **Python** | The configured `mypy` or `pyright` command, often through the project's task runner | Static type checking; exact diagnostics depend on configuration. |
| **TypeScript** | The project's type-check script or `tsc --noEmit` with its `tsconfig.json` | Type checking under project configuration. |
| **PowerShell** | The project's `Invoke-ScriptAnalyzer` command | Static analysis under the selected rules and severity. |

Use direct `javac` only for a self-contained source set or when the complete classpath, module path, release level, annotation processors, and compiler options are known. Do not replace a configured build with an ad hoc source-file search.

`mypy` does not report unused imports by itself. Use a separately configured linter if that check is required.

## Algorithm

```text
1. Discover and run the project's configured check command.
2. If its exit code is zero, report PASS for that command.
3. Otherwise:
   a. Preserve the full diagnostics.
   b. Group them by file, diagnostic code, and message pattern.
   c. Apply only fixes whose intent and semantics are clear.
   d. Report ambiguous fixes with file, line, code, and context.
4. Re-run the same command after each fix batch.
5. After three unsuccessful iterations, stop and report remaining diagnostics.
```

Passing one command proves only that command passed. It does not replace tests, linting, packaging, or other CI checks.

## Fix Policy

Potentially mechanical fixes include correcting an unambiguous symbol typo or removing a demonstrably redundant suppression. Even these require reviewing the diff and rerunning the check.

The following usually require semantic understanding and relevant tests; do not treat them as automatic fixes:

- Adding or changing type annotations.
- Adding null/`None` guards.
- Selecting an import when multiple symbols match.
- Adding `@Override` or changing a Java method signature.
- Removing or renaming variables, parameters, or imports.
- Replacing casts or narrowing TypeScript values.
- Changing PowerShell scope, parameters, or command invocation.

## Report Format

```text
## Compiler and Static-Analysis Gate Report
**Language:** Java | Python | TypeScript | PowerShell
**Check kind:** compiler | type checker | static analyzer
**Command:** <exact command>
**Iteration:** <number>

### Diagnostics
1. path/to/file:line — <code> — <message> (<count>)

**Fixed:** <items, with rationale>
**Remaining:** <items requiring semantic review>
**Status:** PASS | FAIL
**Additional checks not run:** <tests, lint, package build, or none>
```

## Hard Gates

- Never suppress or downgrade diagnostics merely to make the gate pass.
- Do not modify semantics without understanding intent and running relevant tests.
- Preserve and report the exact command and remaining diagnostics.
- Treat warnings according to the project's configured policy; do not silently ignore a failing exit code.
- Stop rather than guessing when dependencies, classpaths, configuration, or intended types are unclear.

## Usage

Invoke with: `Run check-compiler-errors on these changes using the project's configured checks.`

## Attribution

Adapted from [Cursor Team Kit `check-compiler-errors` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/check-compiler-errors), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
