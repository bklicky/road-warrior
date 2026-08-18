# Road Warrior Document Status Manifest

- Version: 1.1
- Status: Canonical repository authority map
- Date: 2026-08-18

This manifest classifies every repository Markdown document by its present role. A category describes how a document is used; it does not erase its internal status, approval history, or evidence value.

## Categories

- **Canonical:** approved principles, requirements, durable decisions, or control rules. Changes require explicit reconciliation with higher authority.
- **Living:** current design or product material expected to evolve when evidence changes.
- **Operational:** instructions, protocols, sequencing, or continuity mechanisms used to perform current work.
- **Historical:** dated evidence or a past synchronization/milestone record. Preserve it; current governance may supersede its conclusions without rewriting the record.
- **Working:** incomplete or specialized material used to develop or test the system. It cannot override canonical or operational governance.

## Conflict Rules

Current verified reality comes first. Among documents, frozen outcomes and the Constitution outrank requirements and durable decisions; those outrank compiled operational controls, plans, living design, historical evidence, and working material. The [Operating Kernel](../ROAD_WARRIOR_OPERATING_KERNEL.md) is mandatory for governed action, but if it conflicts with a higher canonical source it must be corrected rather than used to amend that source silently.

## Manifest

| Document | Category | Role |
| --- | --- | --- |
| `AGENTS.md` | Operational | Repository-wide agent preflight and enforcement rules. |
| `README.md` | Operational | Repository entry point and authority map. |
| `ROAD_WARRIOR_OPERATING_KERNEL.md` | Canonical | Mandatory compiled operational control. |
| `ROAD_WARRIOR_HANDOFFS.md` | Operational | Cross-project handoff protocol and live-ledger pointer; not a ledger. |
| `docs/DOCUMENT_STATUS.md` | Canonical | Document classification and conflict map. |
| `docs/FOUNDATION.md` | Canonical | Frozen Road Warrior mission and human outcomes. |
| `docs/CONSTITUTION.md` | Canonical | Highest project-specific behavioral and implementation principles. |
| `docs/COVENANT.md` | Canonical | Frozen interaction commitments. |
| `docs/BEHAVIORAL_GUIDELINES.md` | Canonical | Frozen behavioral baseline. |
| `docs/DECISIONS.md` | Canonical | Living log of durable accepted and superseded decisions. |
| `docs/PRODUCT_REQUIREMENTS.md` | Canonical | Approved Prototype 1 scope and acceptance baseline. |
| `docs/JUDGMENT_ENGINE_V1.md` | Canonical | Approved V1 cognitive operating model. |
| `docs/GOVERNED_WORKER_CONTRACT.md` | Canonical | Approved V1.5 worker authority, transaction, evidence, and implementation-boundary contract. |
| `docs/VISION.md` | Living | Concise vision summary derived from the canonical Foundation. |
| `docs/ARCHITECTURAL_PRINCIPLES.md` | Living | Evolving architecture principles constrained by frozen outcomes. |
| `docs/ARCHITECTURE.md` | Living | Current system boundaries, components, and execution flow. |
| `docs/EXPERIENCE_BACKLOG.md` | Living | Intended human experiences and trust tests. |
| `docs/HORIZON.md` | Living | Deferred possibilities and research directions; not implementation authority. |
| `docs/CURRENT_STATE_CONTINUITY.md` | Operational | Current-state artifact identity, authority boundary, and reconciliation rules. |
| `docs/IMPLEMENTATION_PLAN.md` | Operational | Active sequencing, status, dependencies, and evidence requirements. |
| `docs/STATIONARY_TEST_PROTOCOL.md` | Working | Specialized pre-drive test procedure. |
| `docs/USER_WORKFLOWS.md` | Working | Incomplete workflow research and approved workflow fragments. |
| `docs/JUDGMENT_ENGINE_REALITY_TEST_2026-08-12.md` | Historical | Dated conversational reality-test evidence. |
| `docs/PROTOTYPE_1_ARCHITECTURE_UPDATE_2026-08-11.md` | Historical | Dated architecture synchronization record. |
| `docs/PROTOTYPE_MILESTONE_2026-08-21.md` | Historical | Original dated milestone definition; current requirements govern conflicts. |
| `docs/PHASE_C_CAPABILITY_EVIDENCE_2026-08-13.md` | Historical | Dated capability evidence. |
| `docs/PHASE_C_CAPABILITY_EVIDENCE_2026-08-14.md` | Historical | Dated capability and continuity evidence. |
| `docs/PHASE_C_CAPABILITY_EVIDENCE_2026-08-17.md` | Historical | Dated handoff and SMS capability evidence. |
| `docs/PHASE_2B_EXTERNAL_RECONCILIATION_EVIDENCE_2026-08-18.md` | Historical | Dated verified external-reconciliation evidence and explicit evidence limits. |
| `docs/OBLIGATION_WORKER_PROOF_2026-08-18.md` | Historical | Dated bounded Obligation Worker transaction-safety proof and evidence limits. |

Non-Markdown fixtures and scripts under `tests/` and `scripts/` are verification assets, not governing documents.
