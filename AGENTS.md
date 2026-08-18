# Road Warrior Agent Guidance

This file defines the repository-wide guardrails that contributors and automated agents must follow while working on Road Warrior.

## Mandatory Operating Preflight

Before accepting or performing a governed action, read and apply [ROAD_WARRIOR_OPERATING_KERNEL.md](ROAD_WARRIOR_OPERATING_KERNEL.md). Governed actions include:

- accepting, recording, surfacing, completing, or returning an obligation;
- creating or acknowledging a cross-project handoff;
- drafting, sending, deleting, creating, or changing anything in an external system;
- changing a source-of-truth or current-state artifact;
- claiming that work, storage, delivery, synchronization, or verification is complete.

Also consult the governing source identified in [docs/DOCUMENT_STATUS.md](docs/DOCUMENT_STATUS.md). The kernel is a concise operational compilation, not permission to override frozen outcomes, accepted decisions, or verified reality.

## Project Scope

- Road Warrior is a standalone project.
- Shared Cognitive Principles may be referenced as canonical project-independent guidance but must not introduce Trade Intelligence implementation, terminology, architecture, or domain-specific behavior.
- It must not reference or integrate with Trade Intelligence, Hermes, Claude, or trading-related Obsidian systems.

## Source of Truth

- GitHub is authoritative for repository governance, requirements, durable decisions, architecture, implementation sequencing, tests, and historical evidence.
- Named Google Drive artifacts are authoritative only for the operational state assigned to them by repository governance.
- Current observed reality and independently verified external state outrank stale documentation. Conflicts must be stated and reconciled; they must not be silently resolved from memory.

## Enforcement Rules

- Preserve Cognitive Freedom and Attention Continuity as frozen human outcomes.
- Judge intent before selecting a capability. Discussion and tentative language are not execution authority.
- Accept responsibility only when intent, authority, material boundaries, and capability are sufficient.
- Use the authoritative obligation and handoff locations named by the kernel; do not create competing live ledgers.
- Verify writes, external actions, receipts, and completion state before claiming success.
- Never use ChatGPT Scheduled Tasks as a Road Warrior reminder mechanism.
- Do not make Bruce the manual courier, ledger administrator, or synchronization mechanism.
- When evidence contradicts belief or documentation, report the evidence and repair the correct governing layer without rewriting historical records.

## Change Discipline

- Documentation and tests must be updated with implementation changes.
- Run `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check_governance.ps1` after governance changes.
- Do not modify external operational systems as an incidental part of repository work.
- Do not commit or push automatically.
