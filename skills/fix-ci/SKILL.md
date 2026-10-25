---
name: fix-ci
description: "Deep CI repair: inspect failing PR checks, follow external log links (GitHub Actions, Maven Central, Docker Hub), extract root cause, apply focused fix. Complements loop-on-ci for hard failures."
allowed-tools: Read Write Edit Glob Grep Shell
---

# Fix-CI: Deep Failure Diagnosis & Repair

> **Difference from loop-on-ci:** loop-on-ci = automated loop on *this* PR. fix-ci = forensic analysis of *any* failing check, including external links, dependency graphs, and environmental factors.

## When to Load

- loop-on-ci hit max attempts / escalated
- Failure is in external system (Maven Central down, Docker Hub rate limit, GitHub Actions runner issue)
- Need to understand *why* before fixing
- Flaky test investigation
- Dependency resolution failures

---

## Data Sources (in priority order)

1. **GitHub Actions logs** — `gh run view <run-id> --log --log-failed`
2. **Check annotations** — `gh api /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations`
3. **External URLs in logs** — Maven Central, Docker Hub, npm registry, PyPI, CRAN, etc.
4. **Artifact downloads** — `gh run download <run-id>` for test reports, coverage, heap dumps
5. **Workflow YAML** — `.github/workflows/*.yml` to understand matrix, env, secrets
6. **Dependency graphs** — `mvn dependency:tree`, `gradle dependencies`, `npm ls`, `pipdeptree`

---

## Diagnosis Workflow

### 1. Classify the Failure

| Class | Signals | Typical Fix |
|---|---|---|
| **Compiler/Type** | `error:`, `FAILED: compileJava`, `tsc --noEmit` | Fix code (loop-on-ci territory) |
| **Test Logic** | `AssertionError`, `junit.framework.AssertionFailedError`, `pytest.fail` | Fix test or production code |
| **Test Flaky** | Same test passes/fails across equivalent runs, non-deterministic timing | Gather evidence and fix the root cause; quarantine/markers/skips require approval and a tracking issue |
| **Dependency Resolution** | `Could not find artifact`, `PKIX path building failed`, `403 Forbidden` | Mirror, pin version, fix repo config |
| **Infrastructure** | `OOMKilled`, `No space left`, `Runner stopped`, `timeout` | Retry, increase resources, split job |
| **Environment/Config** | `secret not found`, `permission denied`, `env var unset` | Fix workflow YAML, repo secrets |
| **External Service** | Maven Central 503, Docker Hub rate limit, npm registry down | Mirror, cache, retry with backoff |

### 2. Deep Extraction (per class)

#### Dependency Resolution — Maven Example
```bash
# 1. Get full error from logs
gh run view <run-id> --log | grep -A 20 "Could not find artifact"

# 2. Check if it's in local cache vs remote
# 3. Try to resolve locally with the repository's documented build command
./mvnw dependency:tree 2>&1 | grep <missing>

# 4. Check repository declarations in pom.xml
# 5. Check Maven mirror configuration in user/project settings.xml
# 6. Use --offline only to test whether an existing local cache is sufficient
```

#### Docker Hub Rate Limit
```bash
# Logs: "toomanyrequests: You have reached your pull rate limit"
# Fix: 
# - Use GHCR / Azure ACR / self-hosted registry
# - Authenticate: docker login (add DOCKERHUB_TOKEN secret)
# - Cache layers: actions/cache with key=docker-${{ hashFiles('Dockerfile') }}
```

#### Flaky Test Forensics
```bash
# 1. Download test reports from last 10 runs
gh run list --workflow=ci.yml --limit=10 --json databaseId
# 2. For each: gh run download <id> --name test-results
# 3. Compare: which tests fail intermittently?
# 4. Check: timing-dependent? shared state? random seed? external service?
```

---

## Fix Strategies (Focused, Minimal)

### Dependency Mirror (Maven)
```xml
<!-- settings.xml; mirrors belong in Maven settings, not build.gradle -->
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0">
<mirrors>
  <mirror>
    <id>organization-mirror</id>
    <mirrorOf>central</mirrorOf>
    <url>https://maven.example.invalid/repository/central/</url>
  </mirror>
</mirrors>
</settings>
```

### Suspected Flaky Tests

Re-run under equivalent conditions, preserve seeds/timing/logs, and investigate shared state,
ordering, clocks, concurrency, and external dependencies. Do not add flaky tags, exclusions,
quarantine, retries, or skips automatically. Any temporary suppression requires explicit approval,
a tracking issue, an owner, and a removal condition.

### Resource Increase (GitHub Actions)
```yaml
# .github/workflows/ci.yml
jobs:
  build:
    runs-on: ubuntu-latest
    # Add for memory-heavy Java builds
    env:
      GRADLE_OPTS: "-Xmx4g -XX:MaxMetaspaceSize=1g"
    # A larger runner is an option only when the repository actually provides one.
```

### Cache Strategy
```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.gradle/caches
      ~/.gradle/wrapper
      ~/.m2/repository
    key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}
    restore-keys: |
      ${{ runner.os }}-gradle-
```

---

## Output Format

```text
Illustrative report only; IDs, dependencies, URLs, commands, and outcomes are hypothetical.

## Fix-CI Report
**PR/Run:** #42 / run_id 1234567890
**Failure Class:** Dependency Resolution
**Root Cause:** Maven Central 503 on `org.apache.commons:commons-lang3:3.14.0` (transitive from plugin X)
**Evidence:** gh run view 1234567890 --log | grep -A 5 "503 Service Unavailable"
**External Check:** curl -I https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.14.0/ → 503
**Fix Applied:** Configured the approved Maven mirror in settings.xml and pinned the version in dependencyManagement
**Verification:** ./mvnw -o test → SUCCESS
**Confidence:** HIGH
**Follow-up:** File issue to plugin X to update transitive dependency
```

---

## Hard Gates

- ❌ **Never** guess the root cause — follow the log chain to evidence
- ❌ **Never** upgrade major versions to "fix" resolution — pin, mirror, or exclude
- ❌ **Never** disable SSL verification (`-Dmaven.wagon.http.ssl.insecure=true`)
- ❌ **Never** commit secrets to fix auth failures — use GitHub Secrets
- ❌ **Never** exclude, quarantine, mark, retry, or skip a flaky test automatically; require explicit approval and a tracking issue
- ❌ **Never** configure Maven mirrors in `build.gradle`; use the applicable Maven `settings.xml`
- ✅ Fix is minimal, targeted, and verifiable locally
- ✅ External service failures → mirror/cache/retry, not code change
- ✅ Document the external dependency in `DEPENDENCIES.md` if not already

---

## Usage

**Explicit:** "Run fix-ci on the failing Maven build in PR #42" or "Diagnose why Docker build fails on CI but works locally".

**With loop-on-ci:** loop-on-ci hits 3 failures → escalates to fix-ci for deep diagnosis → fix-ci returns root cause + fix → loop-on-ci applies and continues.

## Attribution

Adapted from [Cursor Team Kit `fix-ci` at commit `9580c23696ac8d7abed0c166f2f9918800afb819`](https://github.com/cursor/plugins/tree/9580c23696ac8d7abed0c166f2f9918800afb819/cursor-team-kit/skills/fix-ci), Copyright (c) 2026 Cursor, licensed under the MIT License. See the repository `THIRD_PARTY_NOTICES.md`.
