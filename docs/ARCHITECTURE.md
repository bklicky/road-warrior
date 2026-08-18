# Road Warrior Architecture

- Version: 1.0
- Status: Current V1 architecture
- Date: 2026-08-18

Road Warrior is a Cognitive Operating System whose core is judgment and responsibility, not a particular interface, model, connector, or storage product. This architecture implements the frozen outcomes of Cognitive Freedom and Attention Continuity through a small governed control loop and explicit authoritative records.

## Architecture Overview

```text
Conversation on an approved transport
  -> Judgment Engine determines intent, confidence, authority, and dependencies
  -> Operating Kernel selects the governed path and authoritative record
  -> Capability adapter performs an authorized local or external action
  -> Independent verification reads the resulting authoritative state
  -> Responsibility closes, blocks, or returns explicitly
  -> Conversation resumes naturally
```

The cognitive partnership is the front end. The Judgment Engine and Operating Kernel form the control plane. Connectors and applications are replaceable capability adapters. Repository governance and named operational artifacts provide durable state and evidence.

## System Boundaries

### Inside Road Warrior V1

- Conversational judgment, clarification, dependency ordering, and responsibility transfer.
- The repository governance control plane: frozen principles, accepted decisions, requirements, kernel, manifest, architecture, plan, protocols, and tests.
- Road Warrior ownership of obligations and producer-side context routing judgment.
- Verification requirements and explicit completion/blockage reporting.

### External but Governed

- The persistent Road Warrior conversation, which is the primary V1 conversational-continuity surface.
- Google Drive operational artifacts: current-state snapshot, obligation ledger, and handoff ledger.
- Google Calendar as the approved timed surfacing mechanism for time-sensitive obligations.
- Approved communication connectors used only with explicit authorization and verified capability.
- Receiving projects, which own durable incorporation and receipt acknowledgment for handoffs addressed to them.

### Outside V1 Authority or Scope

- ChatGPT Scheduled Tasks as a reminder mechanism.
- Google Tasks as a required obligation store.
- Background monitoring or autonomous project invocation.
- WhatsApp or production SMS as an August 21 requirement.
- Relational-memory infrastructure, semantic retrieval, dashboards, Android/Android Auto software, and production multi-agent infrastructure.
- Any external action not explicitly authorized by the user and verified after execution.

## Components

| Component | Responsibility | Authority / state |
| --- | --- | --- |
| Conversation and transports | Preserve the working relationship across desktop, mobile, and voice while adapting delivery to attention. | Persistent Road Warrior conversation is primary V1 continuity. |
| Judgment Engine | Distinguish intent, confidence, dependencies, and whether to listen, clarify, capture, accept, act, or wait. | `JUDGMENT_ENGINE_V1.md`. |
| Operating Kernel | Enforce obligation, handoff, external-action, verification, and completion rules before governed actions. | `ROAD_WARRIOR_OPERATING_KERNEL.md`. |
| Repository control plane | Govern values, requirements, decisions, architecture, sequencing, and regression checks. | GitHub repository; manifest defines document roles. |
| Obligation service | Capture and maintain timed and untimed commitments; reconcile completion and external surfacing. | Drive `ROAD_WARRIOR_OBLIGATIONS.md` is authoritative. |
| Timed surfacing adapter | Create an appropriate notification for a time-sensitive obligation. | Google Calendar is a surface, not the obligation authority. |
| Context router | Create structured targeted handoffs and preserve producer verification. | Drive `ROAD_WARRIOR_HANDOFFS` is the live ledger; root file is protocol only. |
| Receiving project consumer | Filter, deduplicate, incorporate, verify, and acknowledge addressed handoffs. | Project-owned durable artifact plus verified receipt. |
| Current-state bootstrap | Provide bounded operational recovery/orientation. | Drive `ROAD_WARRIOR_CURRENT_STATE.md`; derived, not governance authority. |
| Capability adapters | Perform approved Drive, Calendar, Gmail, or other bounded operations. | Actual availability and confirmation requirements are established by evidence. |
| Verification layer | Independently read back authoritative state before a completion claim. | Evidence, receipts, and capability records. |

## Data and Control Flows

### Capture: "Remember this"

1. Judgment distinguishes durable capture from brainstorming, obligation, or external action.
2. Road Warrior resolves the appropriate authoritative artifact and necessary context.
3. The item is written and independently read back.
4. Road Warrior confirms only the verified bounded result and resumes the prior thread.

### Obligation: "Remind me"

1. Judgment resolves the obligation and any material timing ambiguity.
2. Road Warrior writes the obligation to the authoritative Drive ledger.
3. If time-sensitive, Road Warrior also creates a Google Calendar event with an appropriate notification.
4. Road Warrior verifies the ledger and, when required, the Calendar artifact independently.
5. Only then does it close the responsibility. ChatGPT Scheduled Tasks are never used.

### Cross-Project Handoff

1. Road Warrior writes and verifies a targeted `Pending` entry in the authoritative Drive handoff ledger.
2. On its governed trigger, the receiving project filters for entries addressed to it.
3. The receiving project writes to and reads back its own durable artifact.
4. It then writes and verifies the receipt, changing the entry to `Received`.
5. Failure at either verification boundary leaves the handoff `Pending`; Bruce is not asked to relay it.

### External Action

1. Judgment separates discussion, draft authority, and explicit execution authority.
2. The adapter performs only the named action within verified capability and confirmation boundaries.
3. The resulting external state is verified.
4. Road Warrior reports completion, blockage, or the smallest required input and returns to the conversation.

### Governance Change

1. Read the kernel, manifest, and governing canonical source.
2. Reconcile current documents without altering dated evidence or silently rewriting prior decisions.
3. Update documentation and regression fixtures together.
4. Run `scripts/check_governance.ps1` and inspect the Git diff.
5. External operational records are reconciled only in a separately authorized phase.

## Operational Considerations

- **Verification before completion:** a successful request or planned write is not a receipt. Use independent readback or equivalent evidence.
- **Single authority per state:** the repository governs durable project rules; named Drive artifacts govern assigned operational state. Pointer documents must not become competing stores.
- **Reality before belief:** capability labels are bounded by observed evidence and must be downgraded when reality changes.
- **Least interruption:** acceptance and closure are brief; clarification is limited to uncertainty that changes the next action.
- **Failure behavior:** preserve recoverable work, keep obligations and handoffs open when verification fails, report the boundary, and do not silently return coordination to Bruce.
- **Security and authority:** external mutations require explicit user authority; discussion or tool availability is not authorization.
- **Change discipline:** frozen outcomes remain stable, historical evidence remains intact, current governance is synchronized, and tests accompany behavior changes.
- **Deferred evolution:** the V2 local-first handoff recommendation is recorded in `HORIZON.md`; it is not implemented by this architecture.
