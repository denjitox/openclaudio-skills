---
name: thermo-nuclear-ps
description: Thermo-nuclear code quality review for PowerShell. Detects pipeline anti-patterns, hidden side-effects, splatting abuse, module boundary violations, and $ErrorActionPreference drift. Use for orchestrators, deployment scripts, and automation pipelines.
allowed-tools: Read Write Edit Glob Grep
---

# Thermo-Nuclear PowerShell Review

Use this skill for a rigorous review of PowerShell 5.1+ and PowerShell 7+ scripts and modules. Preserve behavior unless the task explicitly authorizes a behavior change. Prefer a small, explicit design over a clever pipeline.

## Review method

1. Read the repository instructions and identify the supported PowerShell editions.
2. Inspect the changed code, its callers, tests, module manifest, and analyzer configuration.
3. Trace the success, error, warning, verbose, information, and host streams separately.
4. Identify external mutations: files, registry, services, processes, network calls, environment variables, module/session state, and credentials.
5. Report findings by severity with file and line references. Explain the concrete failure mode; do not report stylistic preference as a defect.
6. Apply the smallest coherent fix when fixes are requested.
7. Run the project's Pester suite and `Invoke-ScriptAnalyzer` with the repository's settings. Preserve complete failure output.

## PowerShell review rules

### 1. Keep pipeline contracts visible

- A function's success output must be intentional. Remember that uncaptured command output, expression results, and method output all enter stream 1.
- Flag accidental output, formatting objects in reusable code, and mixtures of unrelated output shapes that force callers to inspect values at runtime.
- A function may emit several related types when that is its documented contract. Prefer one stable object shape, or a clearly discriminated result model, when consumers need automation-safe output.
- Use `Write-Verbose`, `Write-Debug`, `Write-Warning`, and `Write-Information` for diagnostics. Do not send status text to the success stream.
- Keep `Format-*` and `Out-Host` at presentation boundaries. `Write-Host` and `Write-Progress` are acceptable in an interactive entry point, but not as the only observable result of reusable library code.

`[OutputType()]` is documentation and tooling metadata, not runtime enforcement. Require it for public functions when it improves discoverability; do not require it on every private helper or function that intentionally has no output.

### 2. Judge side effects by clarity, not syntax

Side effects inside `ForEach-Object` are not inherently wrong. They are common in orchestration code. Flag them when they:

- hide a mutation behind what appears to be a transform or filter;
- mix operational/status output with business objects on the success stream;
- depend on implicit mutable outer state in a way that breaks ordering, retries, or tests;
- make partial failure or cleanup behavior unclear; or
- rely on parallel execution without safe synchronization.

Prefer a named mutating function, an explicit loop, or an advanced function with `begin`/`process`/`end` when that makes the contract and failure boundary clearer. Do not mechanically replace every `ForEach-Object` side effect.

### 3. Apply error semantics deliberately

- `try`/`catch` handles terminating errors only. Use `-ErrorAction Stop` where a normally non-terminating cmdlet error must cross a `catch` boundary.
- Establish `$ErrorActionPreference` at an application entry point when the application needs one policy. Do not repeatedly change it deep in the call graph.
- For an expected local exception, prefer the cmdlet's `-ErrorAction` over mutating ambient preference state.
- If a temporary preference change is necessary, save it and restore it in `finally`. A module must not unexpectedly change the caller's session policy when imported.
- Catch only to recover, translate into a domain error, add useful context, or clean up. Preserve the original exception (`throw` inside `catch`) unless replacement is intentional.
- Do not both report and rethrow the same error unless the extra record adds information and duplicate reporting is acceptable.

### 4. Use `ShouldProcess` at public mutation boundaries

Public cmdlet-like functions that mutate external state should normally use:

```powershell
[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(...)

if ($PSCmdlet.ShouldProcess($target, $operation)) {
    # mutation
}
```

- Call `ShouldProcess` immediately before the mutation, with a meaningful target and action.
- Propagate `-WhatIf`/`-Confirm` semantics through the public command. Private helpers do not each need `SupportsShouldProcess` when they can only be reached behind an already-approved boundary.
- Read-only functions do not need `-WhatIf`.
- For operations that cannot be simulated safely, document that limit rather than pretending `-WhatIf` is complete.

Idempotence is independent of `-Force`. Review whether a repeated invocation converges safely by checking current state, comparing desired state, using atomic replacement, or recording resumable progress as appropriate. The absence of `-Force` is not evidence of non-idempotence; `-Force` often changes confirmation or overwrite policy rather than repeatability.

### 5. Validate parameters at the right layer

- Use `[Parameter(Mandatory)]`, `[ValidateNotNullOrEmpty()]`, `[ValidateSet()]`, `[ValidateRange()]`, and similar attributes for cheap, declarative, single-parameter constraints.
- Use `[ValidateScript()]` for cheap declarative checks whose error behavior is clear, such as a simple path-kind or value-shape check.
- Put expensive I/O, cross-parameter rules, mutable-state checks, retries, authorization, and domain workflows in the function body or a named validation function. This keeps validation testable and produces useful errors.
- Do not duplicate attribute validation with an equivalent first-line `if` statement.

### 6. Keep splatting local and legible

Splatting is useful for forwarding common parameters and constructing optional arguments. Flag it when a hashtable becomes an undocumented protocol, is mutated across distant scopes, silently overrides caller intent, or bypasses a real parameter contract.

Prefer typed parameters and a local splat close to the invocation. For substantial configuration, use a documented configuration object or `.psd1` schema and validate it at the boundary. Do not reject a splat merely because it has many keys.

### 7. Protect module boundaries

- Define public exports in the module manifest or explicit `Export-ModuleMember` calls.
- Do not call another module's private implementation by scope tricks or path coupling.
- Prefer manifest `RequiredModules` or a clear bootstrap phase for fixed dependencies.
- Dynamic or conditional `Import-Module` is acceptable when the dependency is genuinely optional or selected at runtime, but validate the module/version and keep loading policy explicit.
- Avoid dot-sourcing untrusted or path-ambiguous files.

### 8. Prefer structured interfaces

- Prefer cmdlets and APIs that return objects over parsing display text.
- If an external program only returns text, isolate parsing in one function, validate exit code and shape, and emit a stable object.
- Treat `Invoke-Expression`, string-built scriptblocks, and interpolated native command lines as injection surfaces. Prefer the call operator with an argument array or a native API.
- Avoid `Select-Object *` as a public contract. Select or construct the fields consumers are meant to use.

### 9. Handle credentials and secrets explicitly

- Never embed or log passwords, tokens, connection strings, private keys, or credential objects.
- Prefer `[PSCredential]`, SecretManagement, a platform credential store, or the CI system's secret facility.
- Avoid interactive `Get-Credential` in unattended paths; accept credentials at the boundary instead.
- Treat `SecureString` as limited protection, especially off Windows. Do not convert plaintext with `ConvertTo-SecureString -AsPlainText -Force` merely to label it secure.
- Redact native-process arguments, transcripts, verbose output, and exception context that may expose secrets.

### 10. Guarantee cleanup

- Release disposable objects, streams, runspaces, jobs, temporary files, locks, and native processes on success and failure.
- Restore location, environment variables, preference variables, and other ambient state in `finally` when the function changes them temporarily.
- Use `using` where supported and appropriate; otherwise use `try`/`finally` and `.Dispose()`.
- Make cleanup tolerant of partially initialized resources without swallowing the primary failure.

## High-signal patterns

| Pattern | Review concern | Better direction |
|---|---|---|
| `$items = @(); $items += $item` in a large loop | Repeated array copies | Emit to the pipeline or use `List[T]` |
| `Where-Object` followed by side-effecting output | Success-stream contamination or hidden mutation | Separate selection from mutation when the contract is unclear |
| `Invoke-Expression $text` | Injection and quoting errors | Commands/functions plus explicit argument arrays |
| Native command invoked as one interpolated string | Incorrect quoting; secret leakage | Call operator and separate arguments; inspect `$LASTEXITCODE` |
| `Start-Sleep` polling with no deadline | Infinite or flaky waits | Poll with timeout, interval/backoff, and terminal-state handling |
| `catch { Write-Error $_; throw }` | Duplicate error records | Re-throw, or add context once with preserved cause |
| `$global:`/`$script:` mutable configuration | Hidden coupling and test interference | Pass configuration or expose controlled module state |
| `Format-*` in a reusable function | Formatting objects replace domain objects | Return objects; format at the UI boundary |
| `Get-Content` pipeline for very large input | Throughput and allocation cost | Measure first; consider `StreamReader` or `switch -File` |

## Approval bar

A change passes only when all applicable items hold:

1. Pester tests relevant to the change pass.
2. ScriptAnalyzer passes under the repository's committed configuration, or each suppression has a narrow written justification.
3. Public success output and diagnostic streams have stable, documented contracts.
4. Error behavior is deliberate; temporary preference changes are restored.
5. Public mutating cmdlets implement appropriate `ShouldProcess` behavior.
6. Repeat execution and partial failure have been considered independently of `-Force`.
7. Module dependencies and exports respect public/private boundaries.
8. No plaintext secrets or credential leakage is introduced.
9. Resources and ambient state are cleaned up on every exit path.
10. Any structural rewrite is supported by tests or another behavioral comparison; "cleaner" alone is not proof of equivalence.

## Invocation

Ask for: **“Run thermo-nuclear-ps on these PowerShell changes.”** State whether the task is review-only or includes fixes, and provide the project-specific test and analyzer commands when they differ from the defaults.

## Attribution

Adapted from [Cursor Team Kit at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit), licensed under the [MIT License](https://github.com/cursor/plugins/blob/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/LICENSE).
