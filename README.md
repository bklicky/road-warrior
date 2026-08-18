# Road Warrior

Road Warrior is a Cognitive Operating System intended to reduce cognitive load through judgment, continuity, and responsible action. Its frozen human outcomes are **Cognitive Freedom** and **Attention Continuity**.

## Start Here

1. Read the [Operating Kernel](ROAD_WARRIOR_OPERATING_KERNEL.md) before any governed action.
2. Use the [Document Status Manifest](docs/DOCUMENT_STATUS.md) to locate the authoritative document for the question at hand.
3. Read [AGENTS.md](AGENTS.md) before changing the repository.
4. Run the governance checks after changing governed documentation:

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check_governance.ps1
   ```

## Authority Map

| Concern | Governing source |
| --- | --- |
| Frozen human outcomes and philosophy | [Foundation](docs/FOUNDATION.md), [Constitution](docs/CONSTITUTION.md), and [Covenant](docs/COVENANT.md) |
| Mandatory operational enforcement | [Operating Kernel](ROAD_WARRIOR_OPERATING_KERNEL.md) and [AGENTS.md](AGENTS.md) |
| Durable approved decisions | [Decision Log](docs/DECISIONS.md) |
| Prototype 1 scope and acceptance | [Product Requirements](docs/PRODUCT_REQUIREMENTS.md) |
| Current architecture and execution flow | [Architecture](docs/ARCHITECTURE.md) |
| Active sequencing and evidence requirements | [Implementation Plan](docs/IMPLEMENTATION_PLAN.md) |
| Operational continuity mechanism | [Current-State Continuity](docs/CURRENT_STATE_CONTINUITY.md) |
| Cross-project routing protocol | [Handoff Protocol](ROAD_WARRIOR_HANDOFFS.md) |
| Document classification and precedence | [Document Status Manifest](docs/DOCUMENT_STATUS.md) |

Current observed reality and independently verified external state outrank stale records. A conflict exposes a reconciliation requirement; it does not authorize a silent change to frozen or durable governance.

## Repository Layout

- `docs/`: governance, requirements, architecture, plans, evidence, and research horizon.
- `scripts/`: dependency-free local consistency checks.
- `tests/`: behavioral governance regression cases.
- `src/`: reserved for future implementation admitted by governed scope.

The repository is the source of truth for governance and durable decisions. Named external artifacts hold only the operational state explicitly assigned to them. No commit, push, or external mutation is implied by a local edit.
