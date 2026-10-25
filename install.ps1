[CmdletBinding(SupportsShouldProcess)]
param(
    [ValidateSet('OpenCode')]
    [string]$Agent = 'OpenCode',

    [ValidateSet('User', 'Project')]
    [string]$Scope = 'User',

    [string]$ProjectRoot = (Get-Location).Path,

    [string[]]$Skill,

    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$sourceRoot = Join-Path $PSScriptRoot 'skills'
$targetRoot = if ($Scope -eq 'User') {
    Join-Path $HOME '.config\opencode\skills'
} else {
    Join-Path (Resolve-Path $ProjectRoot) '.opencode\skills'
}

$available = @(Get-ChildItem $sourceRoot -Directory | Select-Object -ExpandProperty Name)
$selected = if ($Skill) { $Skill } else { $available }
$unknown = @($selected | Where-Object { $_ -notin $available })
if ($unknown.Count -gt 0) {
    throw "Unknown skill(s): $($unknown -join ', '). Available: $($available -join ', ')"
}

New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null

foreach ($name in $selected) {
    $source = Join-Path $sourceRoot $name
    $target = Join-Path $targetRoot $name

    if ((Test-Path $target) -and -not $Force) {
        Write-Warning "Skipping existing skill: $target (use -Force to replace)"
        continue
    }

    if ($PSCmdlet.ShouldProcess($target, "Install skill $name")) {
        if (Test-Path $target) {
            Remove-Item -Recurse -Force $target
        }
        Copy-Item -Recurse -Path $source -Destination $target
        Write-Output "Installed $name -> $target"
    }
}
