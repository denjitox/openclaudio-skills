---
name: loop-on-ci
description: "CI diagnosis loop: watch failing checks → extract actionable errors → apply and verify minimal fixes. Uses gh CLI, stops on flaky/infrastructure failures, and requires explicit authorization before commit or push."
allowed-tools: Read Write Edit Glob Grep Shell
---

# Loop-On-CI: Automated CI Repair Loop

> **Principle:** CI failures are data. Watch → diagnose → apply a minimal local fix → verify. Commit and push only with explicit user authorization.

## When to Load

- PR has failing checks
- You're iterating on a fix and want CI to validate each push
- A suspected flaky test needs investigation
- Before merging: "make CI green and keep it green"

---

## Prerequisites

- `gh` CLI authenticated (`gh auth status` → ok)
- Repo on GitHub with Actions enabled
- Permission to inspect the repository and CI logs
- Explicit user authorization before every commit or push operation

---

## Algorithm

```
INPUT: PR number or branch name
STATE: attempt = 0, max_attempts = 10

LOOP:
  1. FETCH checks: gh pr checks <PR>
     - Use only documented fields/options for the installed gh version.
     - Before relying on JSON fields, verify them with `gh pr checks --help`.
     - Otherwise parse the bounded text output or ask the user to verify `gh help`.
  2. IF all required checks succeeded → EXIT PASS
  3. IDENTIFY failing, cancelled, and timed-out checks from verified output
  4. FOR each failing check:
       a. GET logs: gh run view <run-id> --log-failed
       b. EXTRACT actionable error:
          - Compiler error (file:line, message)
          - Test failure (test name, assertion, stack trace)
          - Lint/style (rule, file:line)
          - Dependency/resolution (missing package, version conflict)
           - Infrastructure (runner OOM, network timeout, quota) → CLASSIFY as infra
  5. GROUP errors by (file, error_type, message_hash)
  6. PRIORITIZE:
       - Compiler/type errors first (block everything)
       - Test failures in changed files
       - Lint/style in changed files
       - Infrastructure/suspected flaky → gather evidence, then escalate
  7. FOR top-priority group (max 3 groups per iteration):
       APPLY minimal fix:
         - Compiler: add import, fix type, fix syntax
         - Test: fix assertion, update snapshot, fix test data
         - Lint: auto-fix if rule supports it, else manual
         - Dependency: update the declared dependency and regenerate the lockfile with the project's package manager
  8. IF no fixable groups → ESCALATE to human with full error dump
  9. RUN the relevant local verification required by the risk and repository policy
  10. REPORT the proposed commit and push
  11. ONLY WITH EXPLICIT AUTHORIZATION:
        a. COMMIT fix (for example, "ci: fix <error-type> in <file>")
        b. PUSH to the authorized branch
  12. attempt++
  13. IF attempt >= max_attempts → HALT, report

WAIT 30s between iterations (CI queue time)
```

---

## Error Extraction Patterns

| Check Type | Log Pattern | Actionable Fields |
|---|---|---|
| **Java (Gradle/Maven)** | `> Task :compileJava FAILED` / `ERROR: /path/Foo.java:10: incompatible types` | file, line, message, error_code |
| **Python (pytest/mypy)** | `FAILED test_foo.py::test_bar - AssertionError:` / `error: Incompatible return type` | file, line, test_name, message |
| **TypeScript (tsc/eslint)** | `error TS2322: Type 'X' is not assignable to type 'Y'` | file, line, ts_code, message |
| **PowerShell (ScriptAnalyzer)** | `RuleName,Severity,File,Line,Message` | rule, file, line, message |
| **Test (JUnit/pytest/Jest)** | `Tests run: X, Failures: Y` + stack trace | test_class, test_method, assertion, stack |

---

## Minimal Fix Strategies

### Compiler / Type Errors
```python
# Python: missing import → add at top of file
# Java: diamond inference → explicit type or var
# TS: implicit any → explicit type annotation
```

### Test Failures (Changed Files Only)
```bash
# 1. Run single test to confirm: ./gradlew test --tests "com.example.FooTest.bar"
# 2. If assertion changed intentionally → update snapshot / expected value
# 3. If test data stale → regenerate fixture
# 4. If suspected flaky, reproduce and collect evidence; do not mark or skip it automatically
# 5. Quarantine, flaky markers, or skips require explicit approval and a tracking issue
```

### Lint / Style
```bash
# Auto-fix if available: eslint --fix, prettier --write, gradlew spotlessApply
# Else: manual fix per rule
```

### Dependency / Resolution
```bash
# Gradle: ./gradlew dependencies --configuration compileClasspath | grep <missing>
# Maven: mvn dependency:tree
# npm/yarn/pnpm: preserve the lockfile; change the manifest deliberately and regenerate it
# pip: inspect constraints and pinned requirements before changing versions
```

---

## Flaky / Infrastructure Detection

| Signal | Action |
|---|---|
| `No space left on device` / `OOMKilled` / `Runner stopped` | Retry only if authorized and useful; do not promise or assume a different runner; then escalate |
| `Network timeout` / `Could not resolve host` / `403/429` | Retry once with backoff, then escalate |
| Same test passes/fails across equivalent runs | Record evidence and investigate nondeterminism; marking, quarantine, or skipping requires explicit approval and a tracking issue |
| `gh run view` shows `conclusion: CANCELLED` without our cancel | Infrastructure — retry once |

---

## Output Format (per iteration)

```text
Illustrative example only; names, IDs, counts, commits, and results are placeholders.

## Loop-On-CI Iteration 3/10
**PR:** #42 (branch: fix/example)
**Failing checks:** 2/12

### Check: "Build & Test" (run_id: 1234567890)
**Conclusion:** FAILURE
**Top errors:**
  1. src/main/java/ExampleService.java:47 — cannot find symbol: method getItems() (3 occurrences)
  2. test/ExampleServiceTest.java:12 — NoSuchMethodError: getItems (1 occurrence)

### Check: "Code Quality" (run_id: 1234567891)
**Conclusion:** FAILURE
**Top errors:**
  1. PSAvoidUsingCmdletAliases — scripts/check.ps1:15 (alias 'gci')

### Fixes applied:
- src/main/java/ExampleService.java:47 → corrected the method call
- scripts/check.ps1:15 → 'gci' → 'Get-ChildItem'

### Local verification: PASS
### Commit/push: not performed; awaiting explicit authorization
```

---

## Hard Gates

- ❌ **Never** push a fix that doesn't address the extracted error
- ❌ **Never** commit, amend, or push without explicit user authorization
- ❌ **Never** disable a check, mark a test flaky, quarantine it, or skip it automatically; require explicit approval and a tracking issue
- ❌ **Never** delete a lockfile as a generic dependency fix
- ❌ **Never** promise or assume that a retry will use a different runner
- ❌ **Never** exceed `max_attempts` without human decision
- ❌ **Never** fix errors in files **not changed in this PR** (unless trivial import/alias)
- ✅ Stop and escalate when: no actionable error, only infra failures, or architectural change needed
- ✅ Each commit message references the check/error it fixes

---

## Usage

**Explicit:** "Run loop-on-ci on PR #42" or "Diagnose CI on branch fix/example; ask before committing or pushing".

**As daemon:** "Start loop-on-ci on current PR, alert me when it stops or hits 5 iterations".

## Attribution

Adapted from [Cursor Team Kit `loop-on-ci` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/loop-on-ci), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
