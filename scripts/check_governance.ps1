[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$failures = New-Object System.Collections.Generic.List[string]
$assertionCount = 0

function Get-RepositoryText {
    param([Parameter(Mandatory = $true)][string]$RelativePath)

    $path = Join-Path $repoRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        $script:failures.Add("Missing required file: $RelativePath")
        return ''
    }

    return [System.IO.File]::ReadAllText($path)
}

function Assert-Contains {
    param(
        [Parameter(Mandatory = $true)][string]$RelativePath,
        [Parameter(Mandatory = $true)][string]$Needle,
        [Parameter(Mandatory = $true)][string]$Rule
    )

    $script:assertionCount++
    $text = Get-RepositoryText -RelativePath $RelativePath
    if (-not $text.Contains($Needle)) {
        $script:failures.Add("[$Rule] $RelativePath does not contain required text: $Needle")
    }
}

function Assert-NotContains {
    param(
        [Parameter(Mandatory = $true)][string]$RelativePath,
        [Parameter(Mandatory = $true)][string]$Needle,
        [Parameter(Mandatory = $true)][string]$Rule
    )

    $script:assertionCount++
    $text = Get-RepositoryText -RelativePath $RelativePath
    if ($text.Contains($Needle)) {
        $script:failures.Add("[$Rule] $RelativePath contains prohibited stale text: $Needle")
    }
}

$requiredFiles = @(
    'ROAD_WARRIOR_OPERATING_KERNEL.md',
    'AGENTS.md',
    'README.md',
    'ROAD_WARRIOR_HANDOFFS.md',
    'docs/DOCUMENT_STATUS.md',
    'docs/ARCHITECTURE.md',
    'docs/PRODUCT_REQUIREMENTS.md',
    'docs/DECISIONS.md',
    'docs/IMPLEMENTATION_PLAN.md',
    'docs/CURRENT_STATE_CONTINUITY.md',
    'tests/behavioral_regressions.json'
)

foreach ($relativePath in $requiredFiles) {
    $assertionCount++
    if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $relativePath) -PathType Leaf)) {
        $failures.Add("Missing required control-plane file: $relativePath")
    }
}

Assert-Contains 'docs/FOUNDATION.md' '### Cognitive Freedom' 'FROZEN-OUTCOMES'
Assert-Contains 'docs/FOUNDATION.md' '### Attention Continuity' 'FROZEN-OUTCOMES'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' 'Cognitive Freedom' 'KERNEL-PRIME-DIRECTIVE'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' 'Attention Continuity' 'KERNEL-PRIME-DIRECTIVE'
Assert-Contains 'AGENTS.md' 'Before accepting or performing a governed action' 'MANDATORY-KERNEL-PREFLIGHT'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' 'Google Calendar' 'TIMED-SURFACING'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' 'ChatGPT Scheduled Tasks are prohibited' 'SCHEDULED-TASKS-PROHIBITION'
Assert-Contains 'docs/PRODUCT_REQUIREMENTS.md' 'must not be used as a Road Warrior reminder mechanism' 'SCHEDULED-TASKS-PROHIBITION'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' '## Verification Before Completion' 'VERIFICATION-BEFORE-COMPLETION'
Assert-Contains 'docs/DECISIONS.md' '### RW-043' 'CONTROL-PLANE-DECISION'
Assert-Contains 'docs/DECISIONS.md' '### RW-044' 'HANDOFF-AUTHORITY-DECISION'
Assert-Contains 'docs/HORIZON.md' '### Deferred V2 Local-First Recommendation' 'V2-DEFERRED-RECOMMENDATION'

$handoffId = '1U4YvjjmwGAbspYwKo5dwlXd4NHbvSlnMdbWPPQYCGHc'
foreach ($relativePath in @('ROAD_WARRIOR_OPERATING_KERNEL.md', 'ROAD_WARRIOR_HANDOFFS.md', 'docs/PRODUCT_REQUIREMENTS.md', 'docs/CURRENT_STATE_CONTINUITY.md', 'docs/DECISIONS.md')) {
    Assert-Contains $relativePath $handoffId 'SINGLE-HANDOFF-AUTHORITY'
}
Assert-NotContains 'ROAD_WARRIOR_HANDOFFS.md' '## Handoff Entries' 'ROOT-FILE-IS-PROTOCOL'
Assert-NotContains 'ROAD_WARRIOR_HANDOFFS.md' 'Status: Active V1 mechanism' 'ROOT-FILE-IS-PROTOCOL'
Assert-NotContains 'docs/PRODUCT_REQUIREMENTS.md' 'shared repository-root `ROAD_WARRIOR_HANDOFFS.md` ledger' 'NO-COMPETING-HANDOFF-LEDGER'

$manifest = Get-RepositoryText -RelativePath 'docs/DOCUMENT_STATUS.md'
$markdownFiles = Get-ChildItem -LiteralPath $repoRoot -Recurse -File -Filter '*.md' |
    Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' }

$strictUtf8 = New-Object System.Text.UTF8Encoding($false, $true)
$textControlFiles = Get-ChildItem -LiteralPath $repoRoot -Recurse -File |
    Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' -and $_.Extension -in @('.md', '.json', '.ps1') }
foreach ($file in $textControlFiles) {
    $assertionCount++
    try {
        [void]$strictUtf8.GetString([System.IO.File]::ReadAllBytes($file.FullName))
    } catch {
        $relativePath = $file.FullName.Substring($repoRoot.Length + 1).Replace('\', '/')
        $failures.Add("[UTF8] Invalid UTF-8 in control-plane file: $relativePath")
    }
}

foreach ($file in $markdownFiles) {
    $relativePath = $file.FullName.Substring($repoRoot.Length + 1).Replace('\', '/')
    $assertionCount++
    if (-not $manifest.Contains(('`' + $relativePath + '`'))) {
        $failures.Add("[DOCUMENT-MANIFEST-COVERAGE] Missing Markdown document: $relativePath")
    }
}

foreach ($file in $markdownFiles) {
    $text = [System.IO.File]::ReadAllText($file.FullName)
    $links = [regex]::Matches($text, '\[[^\]]+\]\(([^)]+)\)')
    foreach ($link in $links) {
        $target = $link.Groups[1].Value.Trim()
        if (($target -eq '') -or ($target.StartsWith('#')) -or ($target -match '^[a-zA-Z][a-zA-Z0-9+.-]*:')) {
            continue
        }
        $targetPath = $target.Split('#')[0]
        $resolved = Join-Path $file.DirectoryName $targetPath
        $assertionCount++
        if (-not (Test-Path -LiteralPath $resolved)) {
            $relativeSource = $file.FullName.Substring($repoRoot.Length + 1).Replace('\', '/')
            $failures.Add("[MARKDOWN-LINK] $relativeSource has missing target: $target")
        }
    }
}

$fixturePath = Join-Path $repoRoot 'tests/behavioral_regressions.json'
try {
    $fixture = [System.IO.File]::ReadAllText($fixturePath) | ConvertFrom-Json
} catch {
    $failures.Add("[BEHAVIORAL-FIXTURE] Invalid JSON: $($_.Exception.Message)")
    $fixture = $null
}

if ($null -ne $fixture) {
    $expectedIds = @(
        'RW-BEH-001-REMEMBER-THIS',
        'RW-BEH-002-REMIND-ME',
        'RW-BEH-003-CROSS-PROJECT-HANDOFF',
        'RW-BEH-004-EXTERNAL-ACTIONS',
        'RW-BEH-005-COMPLETION-CLAIMS'
    )
    $actualIds = @($fixture.cases | ForEach-Object { $_.id })
    foreach ($id in $expectedIds) {
        $assertionCount++
        if ($actualIds -notcontains $id) {
            $failures.Add("[BEHAVIORAL-FIXTURE] Missing case: $id")
        }
    }
    foreach ($case in $fixture.cases) {
        foreach ($property in @('id', 'utterances', 'classification', 'required_actions', 'forbidden_actions', 'completion_evidence')) {
            $assertionCount++
            if (($null -eq $case.$property) -or (@($case.$property).Count -eq 0)) {
                $failures.Add("[BEHAVIORAL-FIXTURE] Case $($case.id) lacks $property")
            }
        }
    }

    $fixtureText = $fixture | ConvertTo-Json -Depth 10
    foreach ($term in @('independently read', 'Google Calendar', 'ChatGPT Scheduled Tasks', 'Pending', 'Received', 'explicit draft', 'explicit send', 'authoritative state')) {
        $assertionCount++
        if ($fixtureText -notmatch [regex]::Escape($term)) {
            $failures.Add("[BEHAVIORAL-FIXTURE] Expected governed behavior is absent: $term")
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Host "Governance checks FAILED: $($failures.Count) failure(s), $assertionCount assertions."
    foreach ($failure in $failures) {
        Write-Host " - $failure"
    }
    exit 1
}

Write-Host "Governance checks PASSED: $assertionCount assertions across document consistency, links, manifest coverage, and 5 behavioral regression cases."
exit 0
