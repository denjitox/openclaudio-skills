# OpenClaudio Skills

Internal skill pack for AI coding agents. The repository is private and intended for the OpenClaudio toolchain.

## Skills

| Skill | Purpose |
|---|---|
| `check-compiler-errors` | Compile/type-check gate with evidence-driven repair. |
| `control-cli` | Reproducible CLI/TUI harness design and transcript capture. |
| `deslop` | Review changed code for common AI-generated maintenance debt. |
| `fix-ci` | Deep diagnosis of difficult CI failures. |
| `loop-on-ci` | Closed-loop CI monitoring and focused repair. |
| `review-and-ship` | Risk-based review pipeline from diff to ship recommendation. |
| `thermo-nuclear-ps` | Strict PowerShell maintainability and safety review. |
| `verify-this` | Falsifiable baseline/treatment validation protocol. |

## Install

OpenCode user scope:

```powershell
.\install.ps1 -Agent OpenCode -Scope User
```

OpenCode project scope:

```powershell
.\install.ps1 -Agent OpenCode -Scope Project -ProjectRoot C:\path\to\project
```

The installer refuses to overwrite an existing skill unless `-Force` is supplied. Review the diff before using `-Force`.

## Validate

```powershell
python .\scripts\validate_skills.py
```

Validation checks frontmatter, folder/name agreement, descriptions, Markdown fences, UTF-8 decoding, and common secret patterns.

## Provenance

These skills are expanded and adapted from workflows in Cursor Team Kit. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Cursor Team Kit is MIT-licensed.

Local modifications and original material are licensed under MIT; see [LICENSE](LICENSE).
