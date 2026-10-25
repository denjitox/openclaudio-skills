---
name: control-cli
description: Build deterministic harnesses for CLI/TUI testing: subprocess or PTY automation, reproducible bug repro, keyboard flow verification, transcript capture, memory/startup profiling.
allowed-tools: Read Write Edit Glob Grep Shell
---

# Control-CLI: Deterministic CLI and TUI Harnesses

> **Goal:** Reproduce command-line behavior with controlled inputs, bounded waits, useful artifacts, and reliable cleanup.

This skill describes how to design a harness. Any APIs shown below are conceptual contracts, not claims that a harness implementation already exists in the repository.

## Choose the Smallest Suitable Transport

Use a normal subprocess for non-interactive commands whose behavior is fully represented by arguments, stdin, stdout, stderr, and exit code. Use a pseudoterminal only when terminal behavior matters.

| Scenario | Recommended transport |
|---|---|
| Batch CLI, filters, compiler wrappers | Subprocess with pipes |
| One-shot stdin input without terminal detection | Subprocess with pipes |
| Prompts that require a TTY | PTY / pseudoconsole |
| Full-screen TUI, cursor movement, resize, colors | PTY / pseudoconsole with terminal parsing |
| Remote interactive command | Pexpect/SSH tooling or an equivalent controlled transport |
| Manual inspection or persistent Linux session | `tmux`, optionally driven by a test harness |

Do not require a PTY for non-interactive CLIs. Pipes are simpler, preserve separate stdout/stderr, and are usually more deterministic.

## Recommended Libraries

- **Node.js:** [`node-pty`](https://github.com/microsoft/node-pty), the Microsoft-maintained package for spawning processes in a pseudoterminal. The package name is `node-pty`, not `@pty.js/pty`.
- **Python:** [`pexpect`](https://pexpect.readthedocs.io/) for expect-style interaction on supported platforms. Its PTY behavior is strongest on Unix-like systems; verify the selected Windows strategy separately.
- **Windows:** use a library backed by ConPTY when terminal semantics are required. Do not imply that redirecting `System.Diagnostics.Process` streams creates a PTY.
- **Linux/macOS:** `pexpect`, native PTY facilities, or `tmux` are reasonable choices depending on whether programmatic control, screen state, or session persistence matters.

Pin dependency versions according to the repository's package policy and confirm platform support in the chosen library's current documentation.

## Harness Model

```text
test case
  ├─ launch: command, argv, cwd, environment, terminal dimensions
  ├─ interact: send bytes/keys, resize, close input
  ├─ observe: raw output, normalized transcript, screen state, exit status
  ├─ synchronize: wait for explicit output/state with a deadline
  ├─ assert: content, ordering, exit status, artifacts, measured timing
  └─ cleanup: graceful stop, bounded wait, process-tree termination, evidence capture
```

Record enough metadata to reproduce a failure: command and argument array, cwd, relevant environment, platform, terminal dimensions, timestamps, timeout, exit status, and captured output. Redact secrets.

## Conceptual APIs

### Subprocess harness

```typescript
interface SubprocessHarness {
  spawn(command: string, args: string[], options?: SpawnOptions): Promise<ProcessSession>
  write(session: ProcessSession, data: string | Uint8Array): Promise<void>
  closeStdin(session: ProcessSession): Promise<void>
  waitForOutput(session: ProcessSession, pattern: string | RegExp, timeoutMs: number): Promise<Match>
  waitForExit(session: ProcessSession, timeoutMs: number): Promise<ExitResult>
  terminate(session: ProcessSession): Promise<void>
}
```

### PTY/TUI harness

```typescript
interface PtyHarness {
  spawn(command: string, args: string[], options?: PtySpawnOptions): Promise<PtySession>
  send(session: PtySession, data: string | Uint8Array): Promise<void>
  sendKey(session: PtySession, key: Key): Promise<void>
  resize(session: PtySession, cols: number, rows: number): Promise<void>
  waitForOutput(session: PtySession, pattern: string | RegExp, timeoutMs: number): Promise<Match>
  getScreen(session: PtySession): Promise<string>
  waitForExit(session: PtySession, timeoutMs: number): Promise<ExitResult>
  terminate(session: PtySession): Promise<void>
}
```

### Profiling

Profiling launches the process itself, so its signature accepts a command rather than an already-running session:

```typescript
interface CliProfiler {
  profileStartup(
    command: string,
    args: string[],
    options: StartupProfileOptions
  ): Promise<StartupProfile>

  profileProcess(
    command: string,
    args: string[],
    options: ProcessProfileOptions
  ): Promise<ProcessProfile>
}
```

Define “ready” explicitly in `StartupProfileOptions`, for example first output, prompt regex, health check, or process exit. Do not mix incompatible signatures such as declaring `profileStartup(session)` and calling `profileStartup(command, args)`.

## Synchronization Rules

- Wait for observable states, not arbitrary sleeps.
- Every wait has a timeout and reports the state observed at expiry.
- Match stable semantic text or screen state; avoid brittle full-output equality unless using a deliberately reviewed golden transcript.
- Treat ANSI normalization, line endings, locale, and terminal dimensions as explicit test policy.
- Preserve raw output alongside normalized output when debugging terminal behavior.
- For PTYs, stdout and stderr may be merged by terminal semantics; do not promise separate streams unless the backend supports them.

## Test Patterns

### Non-interactive CLI

```python
result = run_process(
    command="example-tool",
    args=["validate", "fixture.json"],
    timeout_seconds=30,
)

assert result.exit_code == 0
assert "validation complete" in result.stdout
assert result.timed_out is False
```

Use a subprocess harness here. A PTY adds complexity without testing additional behavior.

### Interactive prompt

```python
with pty_harness.spawn("example-tool", ["configure"], cols=100, rows=30) as session:
    session.expect(r"Continue\? \[y/N\]", timeout=5)
    session.send("y\r")
    session.expect("configuration saved", timeout=10)
    assert session.wait_for_exit(timeout=5).exit_code == 0
```

### TUI keyboard flow

1. Spawn with fixed terminal dimensions and locale.
2. Wait for the initial screen marker.
3. Send named keys rather than timing-dependent byte bursts.
4. Parse terminal control sequences into screen state.
5. Assert visible state, not only raw escape sequences.
6. Capture the final screen and raw transcript on failure.

### Reproducible race investigation

- Fix all controllable inputs and record the seed if the program supports one.
- Run a stated number of independent attempts.
- Save each attempt's command, timestamps, exit status, and failure evidence.
- Report the observed rate; do not call a race fixed from a single successful run.
- Separate product failures from harness timeouts and infrastructure failures.

### Startup profiling

- Define process start and readiness events before measuring.
- Warm and cold starts are different experiments; label them.
- Record sample count and individual measurements, not only an average.
- Measure memory/CPU with platform-appropriate tools and identify whether child processes are included.
- Use broad, justified CI thresholds because shared runners are noisy.

## PowerShell: Subprocess Harness, No PTY

The following pattern is for non-interactive CLIs. It redirects pipes and **must not be used to test TUI rendering, terminal detection, cursor movement, or raw key handling**.

```powershell
function Invoke-SubprocessHarness {
    param(
        [Parameter(Mandatory)] [string] $Command,
        [string[]] $ArgumentList = @(),
        [string] $InputText,
        [int] $TimeoutSeconds = 30
    )

    $psi = [System.Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = $Command
    $psi.UseShellExecute = $false
    $psi.RedirectStandardInput = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.WorkingDirectory = (Get-Location).Path
    foreach ($argument in $ArgumentList) {
        [void] $psi.ArgumentList.Add($argument)
    }

    $process = [System.Diagnostics.Process]::new()
    $process.StartInfo = $psi
    if (-not $process.Start()) {
        throw "Failed to start process: $Command"
    }

    try {
        # Begin both reads before waiting so neither full pipe can deadlock the child.
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()

        if ($PSBoundParameters.ContainsKey('InputText')) {
            $process.StandardInput.Write($InputText)
        }
        $process.StandardInput.Close()

        if (-not $process.WaitForExit($TimeoutSeconds * 1000)) {
            try { $process.Kill($true) } catch { $process.Kill() }
            $process.WaitForExit()
            throw "Process timed out after $TimeoutSeconds seconds: $Command"
        }

        [PSCustomObject]@{
            ExitCode = $process.ExitCode
            StdOut   = $stdoutTask.GetAwaiter().GetResult()
            StdErr   = $stderrTask.GetAwaiter().GetResult()
            TimedOut = $false
        }
    }
    finally {
        $process.Dispose()
    }
}

$result = Invoke-SubprocessHarness `
    -Command "example-tool" `
    -ArgumentList @("validate", "fixture.json") `
    -TimeoutSeconds 30

if ($result.ExitCode -ne 0) {
    throw "CLI failed: $($result.StdErr)"
}
```

Passing arguments through `ProcessStartInfo.ArgumentList` avoids constructing a shell command string. Starting both asynchronous reads before waiting prevents stdout/stderr pipe deadlocks. The bounded wait terminates the process tree when supported and reports timeout as a failure rather than reading `ExitCode` from a still-running process.

## Artifacts

| Artifact | Suggested contents |
|---|---|
| Transcript | timestamp, direction, raw data, normalized data |
| Screen snapshot | terminal dimensions and parsed visible cells |
| Exit result | exit code or signal, timeout flag, duration |
| Profile | readiness definition, samples, startup/memory/CPU measurements |
| Reproduction record | command array, cwd, redacted environment, platform, dependency versions |

Golden transcripts are optional, not automatically authoritative. Review updates because output changes can reflect regressions, intentional copy changes, locale changes, or nondeterministic data.

## Cleanup and Failure Handling

- Put cleanup in `finally`/context-manager disposal.
- Attempt graceful shutdown first when the test covers shutdown behavior.
- Bound graceful shutdown, then terminate the process tree.
- Capture evidence before cleanup when practical.
- Use unique temporary directories and ports per test.
- Never leave credentials in transcripts or reproduction bundles.
- Distinguish timeout, assertion failure, crash, and harness error.

## Hard Gates

- Do not claim redirected pipes are a PTY.
- Do not use a subprocess-only harness for TUI assertions.
- Do not require a real PTY when testing a non-interactive CLI.
- Do not use unbounded reads or waits.
- Do not read stdout and stderr sequentially in a way that can deadlock on full pipes.
- Do not concatenate untrusted arguments into a shell command string.
- Do not assert timing without a defined start event, readiness event, and measured evidence.
- Do not leave sessions or descendant processes orphaned.
- Do not present conceptual interfaces as existing project APIs.

## Deliverable

Report:

1. transport chosen and why;
2. platform and dependencies;
3. synchronization and timeout strategy;
4. assertions and artifacts;
5. cleanup behavior;
6. exact commands/tests run and observed results.

If execution was not performed, say so explicitly.

## Attribution

Adapted from [Cursor Team Kit `control-cli` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/control-cli), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
