---
name: verify-this
description: Empirical validation protocol. Turn claims into falsifiable experiments: baseline → treatment → verdict (VERIFIED/NOT VERIFIED/INCONCLUSIVE). Use when someone says "it works", "it's faster", or "it's fixed" without evidence.
allowed-tools: Read Write Edit Glob Grep Shell
---

# Verify-This: Empirical Validation Protocol

> **Core principle:** A claim without a falsifiable test is an opinion. Test each claim through **Claim → Baseline → Treatment → Evidence → Verdict**.

## When to Load

- A change is claimed to improve correctness, performance, memory, or reliability.
- A PR claims an improvement without reproducible evidence.
- You are about to describe a result as verified.

## Protocol

### 1. State a Falsifiable Claim

Define:

- **Metric:** what is measured and in which unit.
- **Condition:** workload, input, environment, and configuration.
- **Threshold:** the predeclared pass/fail boundary.
- **Comparison:** absolute target, baseline difference, or both.

Example: *"Under the fixed benchmark fixture, p95 latency is at least 5% lower than baseline without increasing peak RSS."*

### 2. Measure the Baseline

- Run the unchanged code under the declared conditions.
- Record the exact command, environment, inputs, and raw output.
- For variable performance measurements, use at least 3 runs and report `median [min,max]`.
- Three runs are only a descriptive minimum. They do **not** establish statistical significance.

### 3. Measure the Treatment

- Apply only the change under test.
- Repeat the same procedure under identical conditions.
- Capture evidence in the same format as the baseline.

For an exact, deterministic functional test, one reproducible run may be sufficient. Record the command and exact expected and observed result. This exception does not apply to noisy timing, memory, throughput, or reliability claims.

### 4. Issue a Verdict

| Outcome | Criteria |
|---|---|
| **VERIFIED** | The evidence directly tests the claim and meets its predeclared threshold. |
| **NOT VERIFIED** | The evidence contradicts the claim or misses its threshold. |
| **INCONCLUSIVE** | Evidence is missing, incomparable, too noisy, underpowered, or produced by a flawed measurement. |

Do not claim statistical significance from three runs. If significance is part of the claim, use a justified sample size and statistical method; otherwise report only the observed descriptive result.

## Report Format

```text
## Verify-This Report
**Claim:** <one sentence>
**Metric:** <name and unit, or exact functional result>
**Condition:** <environment, input, configuration>
**Threshold:** <predeclared pass criterion>
**Baseline (median [min,max], n=X):** <value> — evidence: <file/command>
**Treatment (median [min,max], n=X):** <value> — evidence: <file/command>
**Verdict:** VERIFIED | NOT VERIFIED | INCONCLUSIVE
**Confidence:** HIGH | MEDIUM | LOW — <reason>
**Limitations:** <noise, sample size, or scope>
```

For an exact deterministic test, replace the baseline/treatment summary with expected and observed values and report `n=1`.

## Hard Gates

- No baseline when the claim is comparative → **INCONCLUSIVE**.
- Different input, configuration, or environment → **INCONCLUSIVE** unless the difference is the treatment.
- A single run for a variable performance or reliability claim → **INCONCLUSIVE**.
- An exact deterministic functional result may use one reproducible run.
- Missing raw evidence or reproduction command → **INCONCLUSIVE**.
- Different metrics between baseline and treatment → **INCONCLUSIVE**.
- Anecdotal observation without recorded evidence → **NOT VERIFIED**.

## Generic Examples

### Performance

```text
1. Run the project's benchmark command against a fixed fixture at least 3 times.
2. Apply the change and repeat under the same load and environment.
3. Preserve each raw output and report median [min,max].
```

### Deterministic Bug Fix

```text
1. Add or identify a test that fails with the exact reported input before the change.
2. Apply the change and run the same test.
3. Record the command, expected result, and exact observed result.
```

## Anti-Patterns

| Claim | Problem |
|---|---|
| "It's faster now" | No metric, baseline, condition, or threshold. |
| "Memory usage dropped" | No defined memory metric or comparable workload. |
| "All tests pass" | Supports only the behavior and inputs those tests cover. |
| "I ran it and it worked" | No reproducible command or preserved evidence. |
| "The result is significant" | Requires an appropriate design and statistical analysis; three runs are insufficient by themselves. |

## Usage

Invoke with: `Run verify-this on the claim that <measurable outcome> improved.`

## Attribution

Adapted from [Cursor Team Kit `verify-this` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/verify-this), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
