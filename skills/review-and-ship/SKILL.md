---
name: review-and-ship
description: "End-to-end review pipeline from diff through risk-based testing and ship-ready recommendations. Commit, amend, push, and PR operations require explicit authorization."
allowed-tools: Read Write Edit Glob Grep Shell
---

# Review-and-Ship: Complete Changeset Review Pipeline

> **Goal:** One pass from diff to a ship-ready recommendation. No "LGTM" without evidence. Commit, amend, push, and PR creation require explicit user authorization.

## When to Load

- Before creating a PR
- Reviewing a PR from another agent/human
- "Ship this" — run the full pipeline
- Post-implementation, pre-merge

---

## Pipeline Stages (Sequential, Gates Between)

```
INPUT: Branch/commit range / PR number

STAGE 1: DIFF INTAKE
  - gh pr diff <PR> OR git diff <base>..<head>
  - Parse: files changed, lines added/removed, language per file
  - Classify: feature / fix / refactor / test / config / docs / chore
  - OUTPUT: structured diff summary

STAGE 2: TARGETED TESTS
  - For EACH changed file:
      - Find related tests (naming convention, proximity, imports)
      - Run targeted tests first
      - Then select the relevant broader suite, integration tests, or end-to-end tests according to risk and repository policy
      - Capture only measured pass/fail and duration
      - Report coverage or a coverage delta only when produced by a coverage tool
  - IF any targeted test FAILS → HALT, report

STAGE 3: CORRECTNESS REVIEW
  For EACH logical change (grouped by intent):
      a. Intent match: Does code do what commit message/PR says?
      b. Edge cases: Null, empty, boundary, concurrent, partial failure
      c. Invariants: Pre/post conditions, type contracts, API compatibility
      d. State mutations: Where does state change? Is it visible? Tested?
  - OUTPUT: correctness findings (PASS / CONCERN / FAIL)

STAGE 4: SECURITY REVIEW
  - Secrets: No keys, tokens, passwords, connection strings in diff
  - Injection: SQL, command, LDAP, XSS, path traversal, deserialization
  - Permissions: Least privilege? New endpoints need authz?
  - Crypto: Proper algorithms, key management, no custom crypto
  - Dependencies: New deps scanned (OSV, Snyk, `npm audit`, `safety check`)
  - OUTPUT: security findings (PASS / CONCERN / FAIL)

STAGE 5: INTENT & MINIMALISM REVIEW
  - Does every changed line serve the stated intent?
  - Dead code? Commented code? Debug prints? Unused imports?
  - Could the same outcome be achieved with fewer lines/files?
  - "Code judo": Is there a simpler restructuring?
  - OUTPUT: minimalism findings (PASS / CONCERN / FAIL)

STAGE 6: FIX CRITICAL
  - For each FAIL from stages 3-5:
      - Apply minimal fix (see fix strategies below)
      - Re-run STAGE 2 targeted tests for affected files
      - Re-evaluate STAGE 3-5 for that change only
  - IF unfixable in scope → ESCALATE with reason

STAGE 7: SELECTIVE COMMIT
  - STOP unless the user explicitly authorizes commit/amend operations
  - Group fixes by logical concern (not by file)
  - One commit per concern, conventional messages:
      fix(scope): <what>
      refactor(scope): <what>
      test(scope): <what>
      chore(scope): <what>
  - NO "fix review feedback" / "wip" / "minor" commits
  - Amend only with explicit user authorization and only when repository policy allows it

STAGE 8: PR CREATE / UPDATE
  - STOP unless the user explicitly authorizes push and PR creation/update
  - Title: <type>(<scope>): <imperative summary>
  - Body: Intent + Evidence (test results, benchmarks, screenshots)
  - Apply labels only if they are verified to exist and the user authorized the PR operation
  - Reviewers: auto-assign based on CODEOWNERS

OUTPUT: PR URL + review summary
```

---

## Fix Strategies (Stage 6)

| Finding Type | Minimal Fix |
|---|---|
| Missing null check | Add guard at entry point, not scattered |
| Runtime invariant | Use explicit validation/exception handling; do not rely on Java `assert` in production |
| SQL injection risk | Parameterized query / prepared statement |
| Hardcoded secret | Remove from diff, add to secret store, rotate |
| Unused import/variable | Delete line |
| Debug `console.log` / `Write-Host` | Delete |
| Duplicate logic | Extract to shared function (if >2 uses) |
| Magic number | Named constant with comment |
| Missing test | Add targeted test for the specific behavior |
| Breaking API change | Add deprecation path or version bump justification |

---

## Targeted Test Discovery (Stage 2)

| Language | Discovery Heuristic |
|---|---|
| **Java** | `src/test/**/*<ClassName>*Test.java`, `src/test/**/<ClassName>Test.java` |
| **Python** | `tests/**/test_<module>.py`, `tests/**/<module>_test.py`, adjacent `test_<file>.py` |
| **TypeScript** | `**/*.test.ts`, `**/*.spec.ts`, `__tests__/**/<file>.test.ts` |
| **PowerShell** | `**/<ScriptName>.Tests.ps1`, `tests/**/<ScriptName>.Tests.ps1` |

**Run command per language:**
- Java: `./gradlew test --tests "com.example.<ClassName>Test" -q`
- Python: `pytest tests/test_<module>.py -v --tb=short`
- TypeScript: `npx vitest run <file>.test.ts`
- PowerShell: `Invoke-Pester -Path <ScriptName>.Tests.ps1 -PassThru`

Targeted tests are a fast first signal, not a universal release gate. Expand validation when a
change crosses modules, data stores, network boundaries, deployment configuration, public APIs,
concurrency, security controls, or other high-risk behavior.

---

## Output Format

```text
Illustrative example only; branches, hashes, files, counts, results, performance claims, commits,
PRs, and URLs below are hypothetical and must not be reported as actual evidence.

## Review-and-Ship Report
**Branch:** fix/example (a1b2c3d..f4e5g6h)
**Files changed:** 4
**Lines:** +80 / -25

### Stage 1: Diff Intake
- Feature: Example request validation
- Refactor: Validation logic → separate helper

### Stage 2: Targeted Tests
- ExampleServiceTest: 12/12 PASS (45s)
- Relevant integration suite: 8/8 PASS (12s)
- Coverage delta: not reported; no coverage tool was run

### Stage 3: Correctness
- PASS: Intent matches the requested validation behavior
- CONCERN: ExampleService assumes normalized input — add explicit validation
- PASS: Error behavior is covered

### Stage 4: Security
- PASS: No secrets in diff
- PASS: No injection vectors found in reviewed input handling
- PASS: No new dependencies

### Stage 5: Minimalism
- CONCERN: ExampleService.java grew substantially; helper extraction may improve focus
- PASS: No dead code, no debug prints

### Stage 6: Fix Critical
- ExampleService.validate(): added explicit validation that throws a documented exception
- ExampleService.java: extracted ExampleValidator
- Re-ran targeted and relevant integration tests: PASS

### Stage 7: Selective Commit
Proposed only; not committed without explicit authorization:
1. fix(service): validate normalized input
2. refactor(service): extract input validator

### Stage 8: PR
**PR:** not created; awaiting explicit authorization
**Verdict:** READY TO SHIP, subject to authorized commit/push/PR operations
```

---

## Hard Gates

- ❌ **Never** skip Stage 2 (targeted tests) — if no tests exist, that's a finding
- ❌ **Never** treat targeted tests as sufficient when risk or repository policy requires broader suites or integration tests
- ❌ **Never** ship with FAIL in Stage 3 or 4
- ❌ **Never** combine unrelated fixes in one commit
- ❌ **Never** write "fix review feedback" commit messages
- ❌ **Never** commit, amend, push, create, or update a PR without explicit user authorization
- ❌ **Never** report coverage or a coverage delta unless a coverage tool measured it
- ❌ **Never** use Java `assert` for production invariants; use explicit validation and exceptions
- ❌ **Never** assume repository labels exist; verify before proposing or applying them
- ✅ CONCERN can ship IF documented in PR body with mitigation plan
- ✅ Minimalism CONCERN can ship IF architectural change is out of scope

---

## Usage

**Explicit:** "Run review-and-ship on branch fix/example; ask before any commit, push, or PR action" or "Review PR #42".

**As gate:** "Before I push, run review-and-ship on my uncommitted changes".

## Attribution

Adapted from [Cursor Team Kit `review-and-ship` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/review-and-ship), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
