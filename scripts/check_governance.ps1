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
    'docs/GOVERNED_WORKER_CONTRACT.md',
    'docs/OBLIGATION_WORKER_PROOF_2026-08-18.md',
    'docs/IMPLEMENTATION_PLAN.md',
    'docs/CURRENT_STATE_CONTINUITY.md',
    'tests/behavioral_regressions.json',
    'tests/test_obligation_worker_proof.py',
    'scripts/obligation_worker_proof.py'
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
Assert-Contains 'docs/DECISIONS.md' '### RW-045' 'WORKER-CONTROL-PLANE-DECISION'
Assert-Contains 'docs/DECISIONS.md' '### RW-046' 'DURABLE-ACCEPTANCE-DECISION'
Assert-Contains 'docs/DECISIONS.md' '### RW-047' 'EVIDENCE-GATED-WORKER-DECISION'
Assert-Contains 'docs/HORIZON.md' '### Deferred V2 Local-First Recommendation' 'V2-DEFERRED-RECOMMENDATION'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' 'Workers execute; Road Warrior judges.' 'SINGULAR-JUDGMENT-ENGINE'
Assert-Contains 'ROAD_WARRIOR_OPERATING_KERNEL.md' 'Durable acceptance is not completion, and false acceptance is prohibited.' 'FALSE-ACCEPTANCE-PROHIBITION'
Assert-Contains 'docs/PRODUCT_REQUIREMENTS.md' 'approximate design target of one to two seconds' 'ACKNOWLEDGMENT-LATENCY'
Assert-Contains 'docs/PRODUCT_REQUIREMENTS.md' 'Multi-minute blocking execution before acknowledgment is a product failure' 'BLOCKING-EXECUTION-FAILURE'
Assert-Contains 'docs/JUDGMENT_ENGINE_V1.md' 'Road Warrior may delegate execution but never judgment.' 'JUDGMENT-ENGINE-PRESERVATION'
Assert-Contains 'AGENTS.md' 'Architecture approval is not implementation authority.' 'NO-WORKER-IMPLEMENTATION-AUTHORITY'
Assert-Contains 'docs/ARCHITECTURE.md' 'No dispatcher, queue, background runtime, production worker, service, agent, or deployment exists or is authorized.' 'WORKER-CAPABILITY-REALITY'
Assert-Contains 'docs/IMPLEMENTATION_PLAN.md' 'V1.5 Obligation Worker Proof' 'OBLIGATION-WORKER-PROOF-BOUNDARY'
Assert-Contains 'docs/IMPLEMENTATION_PLAN.md' 'SYNCHRONOUS LEDGER-ONLY SAFETY PROOF; NO PRODUCTION OR BACKGROUND AUTHORITY' 'OBLIGATION-WORKER-PROOF-RESULT'
Assert-Contains 'docs/OBLIGATION_WORKER_PROOF_2026-08-18.md' 'controlled single-writer scope' 'OBLIGATION-WORKER-CONCURRENCY-LIMIT'
Assert-Contains 'docs/OBLIGATION_WORKER_PROOF_2026-08-18.md' 'does not prove or authorize production use, detached/background execution, durable dispatch' 'OBLIGATION-WORKER-NON-CLAIMS'
Assert-Contains 'scripts/obligation_worker_proof.py' 'TARGET_RESOURCE_ID = "1sy1jB1MECL-DTDdd4s7Q7K2_cgTnWT94"' 'OBLIGATION-WORKER-STABLE-TARGET'
Assert-Contains 'scripts/obligation_worker_proof.py' 'REQUIRED_FORBIDDEN_ACTIONS' 'OBLIGATION-WORKER-SCOPE-BOUNDARY'
Assert-Contains 'scripts/obligation_worker_proof.py' 'accepted_responsibility' 'OBLIGATION-WORKER-CANONICAL-ENVELOPE'
Assert-Contains 'tests/test_obligation_worker_proof.py' 'test_e_ambiguous_outcome_reads_before_retry_and_does_not_duplicate' 'OBLIGATION-WORKER-AMBIGUOUS-OUTCOME-TEST'
Assert-Contains 'docs/HORIZON.md' 'dashboard must not independently redefine priorities or write authoritative obligation or handoff state' 'DASHBOARD-NON-AUTHORITY'

foreach ($relativePath in @('ROAD_WARRIOR_OPERATING_KERNEL.md', 'AGENTS.md', 'README.md', 'docs/ARCHITECTURE.md', 'docs/PRODUCT_REQUIREMENTS.md', 'docs/DECISIONS.md', 'docs/DOCUMENT_STATUS.md', 'docs/IMPLEMENTATION_PLAN.md')) {
    Assert-Contains $relativePath 'GOVERNED_WORKER_CONTRACT.md' 'WORKER-CONTRACT-ROUTING'
}

foreach ($needle in @(
    'Workers execute. Road Warrior judges.',
    'requires_judgment',
    'transaction_id',
    'outcome_unknown',
    'False acceptance is prohibited.',
    'Re-delivery of the same transaction must not create a duplicate',
    'Never blindly retry an irreversible or externally visible action',
    'no production worker runtime is authorized',
    'should not depend on Bruce''s Windows computer remaining awake'
)) {
    Assert-Contains 'docs/GOVERNED_WORKER_CONTRACT.md' $needle 'WORKER-CONTRACT-INVARIANT'
}
Assert-NotContains 'docs/GOVERNED_WORKER_CONTRACT.md' 'worker may interpret Bruce' 'WORKER-NON-JUDGMENT'

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
        'RW-BEH-005-COMPLETION-CLAIMS',
        'RW-BEH-006-DURABLE-ACCEPTANCE',
        'RW-BEH-007-WORKER-AUTHORITY',
        'RW-BEH-008-WORKER-IDEMPOTENCY',
        'RW-BEH-009-WORKER-CLOSURE'
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
    foreach ($term in @('independently read', 'Google Calendar', 'ChatGPT Scheduled Tasks', 'Pending', 'Received', 'explicit draft', 'explicit send', 'authoritative state', 'durably accepts', 'requires_judgment', 'transaction ID', 'idempotent', 'outcome_unknown', 'structured evidence', 'Attention Continuity')) {
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

Write-Host "Governance checks PASSED: $assertionCount assertions across document consistency, links, manifest coverage, and $(@($fixture.cases).Count) behavioral regression cases."
exit 0
