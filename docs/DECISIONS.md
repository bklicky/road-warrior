# Road Warrior Decision Log

- Version: 1.0
- Status: Living governance record
- Updated: 2026-08-11

This log records accepted product, architecture, and working-governance decisions. A decision remains in force until explicitly superseded. Unresolved implementation mechanisms remain open and are not converted into decisions here.

## Decision Record Format

Each entry contains an ID, evidence-supported date, decision, rationale, consequences, and status.

## Accepted Decisions

### RW-001 — Adopt Shared Cognitive Principles by Reference

- **ID:** RW-001
- **Date:** 2026-08-01
- **Decision:** Road Warrior adopts the canonical Shared Cognitive Principles by reference and applies them through its project-specific Constitution, Covenant, and Behavioral Guidelines.
- **Rationale:** Project-independent principles should remain canonical without being duplicated or redefined inside Road Warrior.
- **Consequences:** Road Warrior-specific implementation must remain consistent with those principles and the Constitution; conflicting implementation must change.
- **Status:** ACCEPTED — FROZEN BASELINE

### RW-002 — Freeze Cognitive Freedom and Attention Continuity

- **ID:** RW-002
- **Date:** 2026-08-01
- **Decision:** Cognitive Freedom and Attention Continuity are Road Warrior's frozen human outcomes.
- **Rationale:** Road Warrior exists to let the user release accepted cognitive burdens while preserving current attention.
- **Consequences:** Significant features, workflows, and architecture must increase Cognitive Freedom and preserve Attention Continuity or require exceptional justification.
- **Status:** ACCEPTED — FROZEN OUTCOMES

### RW-003 — Preserve Human Control and Earn Authority

- **ID:** RW-003
- **Date:** 2026-08-01
- **Decision:** Bruce or the user owns final decisions; Road Warrior begins only when invited and earns trust and authority gradually.
- **Rationale:** Cognitive partnership must amplify human judgment without replacing it or creating dependence.
- **Consequences:** Responsibility and execution require sufficient understanding, appropriate permission, and honest capability boundaries.
- **Status:** ACCEPTED — FROZEN BASELINE

### RW-004 — Reality Outranks Both Partners

- **ID:** RW-004
- **Date:** 2026-08-01
- **Decision:** Reality and observed evidence outrank the opinions, preferences, confidence, narratives, and implementation convenience of both partners.
- **Rationale:** Reliable judgment requires intellectual honesty and willingness to change direction when evidence changes.
- **Consequences:** Claims must distinguish evidence from inference and uncertainty; plans and implementation must change when contradicted by reality.
- **Status:** ACCEPTED — FROZEN BASELINE

### RW-005 — Prototypes Answer Questions

- **ID:** RW-005
- **Date:** 2026-08-01
- **Decision:** Prototypes exist to answer questions and collect useful evidence, not to validate assumptions or require success.
- **Rationale:** Field evidence is more valuable than protecting a preferred design narrative.
- **Consequences:** Testing must preserve failures, limitations, and unexpected observations as valid outcomes.
- **Status:** ACCEPTED — FROZEN BASELINE

### RW-006 — Protect Momentum and Minimize Interaction

- **ID:** RW-006
- **Date:** 2026-08-01
- **Decision:** Road Warrior must protect conversational momentum, minimize cognitive interruption, and use the least interaction needed to accept responsibility honestly.
- **Rationale:** Cognitive Freedom is achieved by preserving Attention Continuity.
- **Consequences:** Capture, clarification, execution, and return behavior must avoid unnecessary classification, recap, or context switching.
- **Status:** ACCEPTED — FROZEN BASELINE

### RW-007 — Road Warrior Is a Cognitive Operating System

- **ID:** RW-007
- **Date:** 2026-08-11
- **Decision:** Road Warrior is a Cognitive Operating System.
- **Rationale:** Its role spans understanding, judgment, continuity, responsibility transfer, and coordinated action rather than a single interface or environment.
- **Consequences:** Product and architecture decisions must be evaluated as parts of a cognitive system rather than as features of a voice or driving application.
- **Status:** ACCEPTED

### RW-008 — Judgment, Not Voice, Is the Core Value Proposition

- **ID:** RW-008
- **Date:** 2026-08-11
- **Decision:** Judgment, not voice, is Road Warrior's core value proposition.
- **Rationale:** Value comes from correctly understanding intent and choosing what happens next; voice is only one interface.
- **Consequences:** Voice polish cannot substitute for correct judgment, continuity, or appropriate execution.
- **Status:** ACCEPTED

### RW-009 — Prototype 1 Validates the Cognitive Partnership

- **ID:** RW-009
- **Date:** 2026-08-11
- **Decision:** Prototype 1 validates the Cognitive Partnership and whether Road Warrior meaningfully reduces Bruce's cognitive load, not primarily the driving experience.
- **Rationale:** The human outcome is broader than any transport.
- **Consequences:** Prototype evidence and acceptance criteria must center on cognitive-load reduction, judgment, continuity, and responsibility transfer.
- **Status:** ACCEPTED

### RW-010 — The Car Is One Transport

- **ID:** RW-010
- **Date:** 2026-08-11
- **Decision:** The car is an important proving environment and one transport, not the product boundary; desktop and mobile are also valid Prototype 1 transports.
- **Rationale:** A Cognitive Operating System must not be defined by one environment or interface.
- **Consequences:** Prototype design and testing may use multiple transports while retaining car field use as important evidence.
- **Status:** ACCEPTED

### RW-011 — Introduce the Judgment Engine

- **ID:** RW-011
- **Date:** 2026-08-11
- **Decision:** The Judgment Engine is the core decision layer and must determine conversational intent, including at minimum thinking aloud, brainstorming, decision, delegation, communication, research, and project work.
- **Rationale:** Appropriate action depends on understanding what kind of interaction is occurring.
- **Consequences:** Judgment determines whether to listen, clarify, summarize, capture, remind, communicate, research, perform project work, or resume conversation.
- **Status:** ACCEPTED

### RW-012 — Adopt Zero Assumptions

- **ID:** RW-012
- **Date:** 2026-08-11
- **Decision:** Zero Assumptions is a mandatory governing rule; when intent is materially uncertain, Road Warrior asks the smallest clarifying question necessary.
- **Rationale:** Acting on inferred intent can create cognitive burden, errors, and loss of trust.
- **Consequences:** Tentative language and brainstorming are not execution requests; tests must include ambiguity and non-request cases.
- **Status:** ACCEPTED

### RW-013 — Approve the First V1 Judgment Workflow

- **ID:** RW-013
- **Date:** 2026-08-11
- **Decision:** The first approved V1 workflow is Conversation → Judgment → Appropriate action → Capture if required → Reminder if required → Resume conversation.
- **Rationale:** Conversation remains the primary human experience while judgment selects proportionate action.
- **Consequences:** Every execution path must define how it returns naturally to the prior conversation.
- **Status:** ACCEPTED

### RW-014 — Use Google Drive and Reminder/Task for Brainstorm Capture

- **ID:** RW-014
- **Date:** 2026-08-11
- **Decision:** For Prototype 1, the brainstorm workflow produces a concise summary, stores it in Google Drive, creates a reminder/task, and resumes naturally.
- **Rationale:** The workflow transfers cognitive responsibility while preserving useful output and future re-entry.
- **Consequences:** Prototype capability testing and rehearsal must verify the complete capture-and-return loop.
- **Status:** ACCEPTED

### RW-015 — Prefer Gmail for V1 Email Execution

- **ID:** RW-015
- **Date:** 2026-08-11
- **Decision:** The Gmail connector is the preferred V1 path for drafting or sending email only when Bruce explicitly requests it, subject to verified capability and required confirmation.
- **Rationale:** Explicit intent and a specialized connector provide a bounded communication path without treating tentative discussion as authorization.
- **Consequences:** Connector capability, confirmation, send behavior, failure recovery, and negative non-request cases must be tested.
- **Status:** ACCEPTED

### RW-016 — Require Context Continuity in V1

- **ID:** RW-016
- **Date:** 2026-08-11
- **Decision:** Context continuity is a V1 requirement across project, person, and conversational threads.
- **Rationale:** Bruce should not repeatedly reconstruct prior work for Road Warrior to remain a useful cognitive partner.
- **Consequences:** Capability/reality testing must determine the achievable Prototype 1 boundary; no implementation mechanism is approved yet.
- **Status:** ACCEPTED — IMPLEMENTATION MECHANISM OPEN

### RW-017 — Treat WhatsApp/Twilio as a Prototype 1 Stretch Goal

- **ID:** RW-017
- **Date:** 2026-08-11
- **Decision:** WhatsApp/Twilio is a Prototype 1 stretch goal, not a core requirement.
- **Rationale:** Communication-channel value may be worth testing, but core judgment and execution reliability has priority.
- **Consequences:** Work may begin only after core loops are reliable, must not threaten August 20 readiness, and must defer to Version 2 if it cannot be added safely.
- **Status:** ACCEPTED — STRETCH

### RW-018 — Defer Obsidian Relational Memory to Version 2

- **ID:** RW-018
- **Date:** 2026-08-11
- **Decision:** Obsidian relational memory is a Version 2 direction and not a Prototype 1 requirement.
- **Rationale:** The context-continuity requirement must be validated before selecting a relational-memory implementation.
- **Consequences:** Prototype 1 must not depend on an Obsidian implementation.
- **Status:** ACCEPTED — VERSION 2 DIRECTION

### RW-019 — Defer Personal OS Dashboard Integration to Version 2

- **ID:** RW-019
- **Date:** 2026-08-11
- **Decision:** Personal OS dashboard integration is a Version 2 direction and not a Prototype 1 requirement.
- **Rationale:** Dashboard integration is not required to validate the Cognitive Partnership.
- **Consequences:** Prototype 1 scope and readiness must not depend on dashboard work.
- **Status:** ACCEPTED — VERSION 2 DIRECTION

### RW-020 — Synchronize the Repository Before Major Design

- **ID:** RW-020
- **Date:** 2026-08-11
- **Decision:** Repository synchronization is required before major design changes, and ChatGPT owns synchronization responsibility.
- **Rationale:** Design work requires a shared, current source of truth without asking Bruce to reconstruct or manually reconcile repository state.
- **Consequences:** ChatGPT must read the governing repository, identify conflicts, update authorized records, and request review before further major design work.
- **Status:** ACCEPTED

### RW-021 — Make Implementation Instructions Explicit and Low-Load

- **ID:** RW-021
- **Date:** 2026-08-11
- **Decision:** Implementation instructions to Bruce must be explicit, sequential, and designed to reduce cognitive load at every opportunity.
- **Rationale:** Ambiguous or fragmented instructions transfer coordination burden back to Bruce.
- **Consequences:** Instructions must identify order, dependencies, expected evidence, stopping points, and decisions requiring Bruce's authority.
- **Status:** ACCEPTED

### RW-022 — Treat Governance Documents as Living Documents

- **ID:** RW-022
- **Date:** 2026-08-11
- **Decision:** Governance documents are living documents; once they are good enough to govern the next step, work moves forward and the documents are revised when reality changes.
- **Rationale:** Governance must provide direction without becoming a substitute for evidence-producing work.
- **Consequences:** Documents should be sufficient and authoritative for the next decision, then updated deliberately when testing reveals new facts.
- **Status:** ACCEPTED

### RW-023 — Do Not Optimize for Agreement

- **ID:** RW-023
- **Date:** 2026-08-11
- **Decision:** Neither partner optimizes for agreement; respectful, evidence-based challenge is expected.
- **Rationale:** A useful cognitive partnership improves judgment through intellectual honesty rather than deference or artificial consensus.
- **Consequences:** Bruce and Road Warrior should surface conflicts, assumptions, contrary evidence, and uncertainty without ego while preserving respect and final human authority.
- **Status:** ACCEPTED

### RW-024 — Set Prototype 1 Readiness and Field-Use Dates

- **ID:** RW-024
- **Date:** 2026-08-11
- **Decision:** Prototype 1 readiness is targeted for August 20, 2026, and field use begins August 21, 2026.
- **Rationale:** A readiness freeze before field use protects the core experience from late destabilizing changes.
- **Consequences:** Core requirements and evidence take priority over stretch work; changes that threaten readiness must be deferred.
- **Status:** ACCEPTED

## Superseded Decisions

None recorded.

## Open Decisions

- The implementation mechanism for V1 context continuity.
- The verified Prototype 1 capability boundary for Google Drive, reminders/tasks, Gmail drafting and sending, desktop, mobile, and voice behavior.
- Whether WhatsApp/Twilio can proceed without jeopardizing the August 20 readiness target.
