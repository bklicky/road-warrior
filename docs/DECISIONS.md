# Road Warrior Decision Log

- Version: 2.1
- Status: Living governance record
- Updated: 2026-08-18

This log records accepted product, architecture, and working-governance decisions. A decision remains in force until explicitly superseded. Unresolved implementation mechanisms remain open and are not converted into decisions here.

## Document Authority

- `FOUNDATION.md` and `CONSTITUTION.md` govern frozen human outcomes and constitutional commitments.
- Current `DECISIONS.md` governs durable approved decisions.
- `PRODUCT_REQUIREMENTS.md` governs Prototype 1 scope and acceptance requirements.
- The repository-root `ROAD_WARRIOR_OPERATING_KERNEL.md` compiles mandatory operational enforcement but cannot silently amend frozen outcomes, accepted decisions, or requirements.
- `DOCUMENT_STATUS.md` classifies document roles and conflict handling.
- `IMPLEMENTATION_PLAN.md` governs active phase sequencing and evidence requirements.
- Older dated milestone documents, workflows, architecture records, and specialized test protocols remain historical or specialized inputs and do not override those current authorities.

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
- **Status:** ACCEPTED AS AMENDED BY RW-037 — REMINDER/TASK STEP NOW USES THE ROAD WARRIOR OBLIGATION LEDGER AND EXTERNAL SURFACING WHEN REQUIRED

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
- **Consequences:** RW-028 approves the shared Markdown handoff ledger as the V1 Context Routing mechanism. Capability/reality testing must still determine the achievable end-to-end Prototype 1 boundary.
- **Status:** ACCEPTED — V1 MECHANISM SET BY RW-028

### RW-017 — Treat WhatsApp/Twilio as a Prototype 1 Stretch Goal

- **ID:** RW-017
- **Date:** 2026-08-11
- **Decision:** WhatsApp/Twilio is a Prototype 1 stretch goal, not a core requirement.
- **Rationale:** Communication-channel value may be worth testing, but core judgment and execution reliability has priority.
- **Consequences:** Work may begin only after core loops are reliable, must not threaten August 20 readiness, and must defer to Version 2 if it cannot be added safely.
- **Status:** ACCEPTED — STRETCH

### RW-018 — Defer Relational Knowledge Infrastructure Beyond Prototype 1

- **ID:** RW-018
- **Date:** 2026-08-11
- **Decision:** Relational knowledge infrastructure is not a Prototype 1 requirement. Human-readable relational knowledge such as Obsidian plus semantic retrieval is a V3/V4 research direction, with a graph database considered only if later complexity earns it.
- **Rationale:** Context and continuity requirements must be validated before selecting deeper relational-memory infrastructure, and infrastructure complexity must be justified by evidence.
- **Consequences:** Prototype 1 must not depend on Obsidian, semantic retrieval, or graph-database implementation.
- **Status:** ACCEPTED — V3/V4 RESEARCH DIRECTION

### RW-019 — Defer Personal OS Dashboard Integration Beyond Prototype 1

- **ID:** RW-019
- **Date:** 2026-08-11
- **Decision:** Personal OS dashboard integration is a later direction and not a Prototype 1 requirement. RW-026 records the current V3 Judgment-Driven Personal OS / Dynamic Mission Control direction.
- **Rationale:** Dashboard integration is not required to validate the Cognitive Partnership.
- **Consequences:** Prototype 1 scope and readiness must not depend on dashboard work.
- **Status:** ACCEPTED — V3 DIRECTION

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
- **Consequences:** Core requirements and evidence take priority over stretch work; changes that threaten readiness must be deferred. August 21 is a milestone for a credible, testable V1 baseline, not perfection.
- **Status:** ACCEPTED

### RW-025 — Preserve Context Routing as an Architectural Concept

- **ID:** RW-025
- **Date:** 2026-08-12
- **Decision:** Context Routing means Road Warrior should judge not only whether information should be remembered, but where it belongs and where it should become available later.
- **Rationale:** Information learned in one Road Warrior context should become available in the relevant project or context without requiring Bruce to act as the courier.
- **Consequences:** Context Routing is preserved as an architectural concept. RW-028 selects the shared Markdown handoff ledger as its V1 mechanism; end-to-end continuity remains subject to testing.
- **Status:** ACCEPTED — V1 MECHANISM SET BY RW-028

### RW-026 — Establish Judgment-Driven Personal OS / Dynamic Mission Control as a V3 Direction

- **ID:** RW-026
- **Date:** 2026-08-12
- **Decision:** In V3, Road Warrior and its Judgment Engine should provide the cognitive prioritization layer above Personal OS, while Personal OS becomes a dynamic presentation and action surface informed by projects, calendar, tasks, investments, trades, communications, and other approved signals.
- **Rationale:** Static lists or Kanban views should not require Bruce to supply all classification and prioritization manually. The dashboard should display judgment, not create it.
- **Consequences:** Judgment-Driven Personal OS / Dynamic Mission Control is not a Prototype 1 implementation requirement. No implementation mechanism is selected, and August 21 scope must not expand to include it.
- **Status:** ACCEPTED — V3 DIRECTION

### RW-027 — Order Multiple Intents by Dependency

- **ID:** RW-027
- **Date:** 2026-08-12
- **Decision:** When multiple intents or responsibilities depend on one another, the Judgment Engine must identify the dependency and order the responsibilities so prerequisites are resolved before downstream work.
- **Rationale:** Correctly classifying several intents is insufficient when one controls whether or how another should proceed.
- **Consequences:** Clarification and execution should address the controlling dependency first while preserving authorization boundaries and avoiding premature downstream action.
- **Status:** ACCEPTED

### RW-028 — Use a Shared Markdown Handoff Ledger for V1 Context Routing

- **ID:** RW-028
- **Date:** 2026-08-12
- **Decision:** The repository-root `ROAD_WARRIOR_HANDOFFS.md` ledger is the approved V1 Context Routing mechanism. Road Warrior creates structured handoff entries, and receiving projects incorporate entries addressed to them and acknowledge receipt.
- **Rationale:** A shared Markdown ledger provides a simple, inspectable mechanism that removes Bruce from the synchronization path without prematurely introducing software or infrastructure.
- **Consequences:** V1 uses the status flow `Pending → Received`. The mechanism is intentionally simple and replaceable, but entries must remain structured enough for later migration. Creating a ledger entry does not prove cross-project pickup or acknowledgment; the end-to-end flow must be tested.
- **Status:** ACCEPTED — END-TO-END TESTING REQUIRED

### RW-029 — Keep Context Judgment Separate From Relational Memory

- **ID:** RW-029
- **Date:** 2026-08-12
- **Decision:** Road Warrior remains the judgment and routing layer. A future human-readable relational knowledge layer such as Obsidian, combined with semantic retrieval, may replace or extend the V1 ledger to support cross-project relationships and interconnected concepts, but it would serve as relational memory rather than the source of judgment.
- **Rationale:** Storage and relationship representation must support Road Warrior's judgment without displacing it or allowing an implementation mechanism to define intent.
- **Consequences:** V1 does not require Obsidian or semantic-retrieval integration. The Markdown ledger must remain replaceable and structured for possible migration. A graph database remains conditional research and should be introduced only if later complexity earns it.
- **Status:** ACCEPTED — V3/V4 RESEARCH DIRECTION

### RW-030 — Require Execution Handoff Visibility in V1

- **ID:** RW-030
- **Date:** 2026-08-12
- **Decision:** For noticeable-duration V1 work, Road Warrior uses `Accept → Signal → Execute → Close`: briefly accept responsibility, signal real execution, perform the work, and explicitly report completion, blockage, or required input.
- **Rationale:** Visible responsibility prevents Bruce from wondering whether work was accepted, is still occurring, or silently failed.
- **Consequences:** Road Warrior must not imply background or continuing execution unless real execution is occurring. Immediate conversational responses do not require ceremonial progress narration.
- **Status:** ACCEPTED — V1 REQUIREMENT

### RW-031 — Route V1 Obligations by Time and Reject ChatGPT Scheduled Tasks

- **ID:** RW-031
- **Date:** 2026-08-12
- **Decision:** Timed obligations route to Google Calendar with a notification; untimed obligations route to Google Tasks as the intended V1 rule. ChatGPT Scheduled Tasks are rejected as a Road Warrior reminder mechanism.
- **Rationale:** Google Calendar execution succeeded in reality testing. ChatGPT Scheduled Tasks disrupted the primary conversation or chat state and introduced rate-limit friction.
- **Consequences:** Direct Google Tasks execution remains unproven and must be disclosed as unavailable until verified. Reminder architecture and tests must exclude ChatGPT Scheduled Tasks.
- **Status:** ACCEPTED IN PART — OBLIGATION-STORAGE ROUTING SUPERSEDED BY RW-037; CALENDAR AND SCHEDULED TASKS BOUNDARIES RETAINED

### RW-032 — Define External Communication Authorization

- **ID:** RW-032
- **Date:** 2026-08-12
- **Decision:** An explicit send instruction authorizes sending, an explicit draft instruction authorizes drafting but not sending, and materially ambiguous authorization requires the smallest clarifying question necessary.
- **Rationale:** Discussing a communication does not itself transfer authority to act externally.
- **Consequences:** Road Warrior must not infer send authority from brainstorming, tentative language, or discussion. Actual execution remains subject to verified capability and required confirmation.
- **Status:** ACCEPTED — V1 REQUIREMENT

### RW-033 — Require Transport-Aware Communication in V1

- **ID:** RW-033
- **Date:** 2026-08-12
- **Decision:** Judgment, relationship, and responsibility standards remain consistent across desktop, mobile, and voice, while response length, pacing, structure, turn-taking, and progressive disclosure adapt to transport and attention context.
- **Rationale:** The cognitive partnership should remain coherent without forcing every environment into the same communication shape.
- **Consequences:** V1 instructions and testing must cover both invariants and transport-specific delivery behavior.
- **Status:** ACCEPTED — V1 REQUIREMENT

### RW-034 — Begin Adaptive Communication in V1

- **ID:** RW-034
- **Date:** 2026-08-12
- **Decision:** Adaptive Communication is a long-term requirement beginning in V1. Road Warrior should progressively adjust communication behavior from Bruce's explicit and observed feedback.
- **Rationale:** Communication should improve through use while remaining grounded in evidence.
- **Consequences:** Individual feedback may guide the current context or form a hypothesis for further testing, but it must not become an unsupported universal assumption.
- **Status:** ACCEPTED — V1 FOUNDATION; LONG-TERM REQUIREMENT

### RW-035 — Distinguish Contextual Memory From Authoritative Artifacts

- **ID:** RW-035
- **Date:** 2026-08-12
- **Decision:** Contextual memory may support judgment, but authoritative artifacts remain necessary when exact wording, quantities, commitments, or other precision matters.
- **Rationale:** A successful recall can be useful without proving reliable universal cross-project memory or exact source fidelity.
- **Consequences:** Cross-context recall must be tested further and represented cautiously. Richer bidirectional cross-project information sharing remains later architecture and research, not August 21 scope.
- **Status:** ACCEPTED — V1 OPERATING BOUNDARY; LATER RESEARCH

### RW-036 — Accept Bounded Capability Results as Phase C Evidence

- **ID:** RW-036
- **Date:** 2026-08-13
- **Decision:** Phase C exists to discover actual capability boundaries. A repeatably verified result such as `AVAILABLE`, `UNAVAILABLE`, `UNRELIABLE`, `CONFIRMATION-REQUIRED`, or another honestly documented bounded result is valid Phase C evidence. A capability does not have to work for its Phase C test to be completed successfully.
- **Rationale:** Capability testing must report reality rather than force a preferred capability outcome.
- **Consequences:** Phase C must explicitly test Google Calendar notification behavior, direct Google Tasks execution or boundary, Gmail authorization and confirmation behavior, Google Drive behavior, desktop, mobile, relevant voice behavior, and the ChatGPT Scheduled Tasks rejection and observed failure boundary. Completing a capability test does not automatically satisfy later Prototype 1 functional requirements, acceptance criteria, or field-readiness requirements.
- **Status:** ACCEPTED — PHASE C EVIDENCE RULE

### RW-037 — Road Warrior Owns V1 Obligations

- **ID:** RW-037
- **Date:** 2026-08-13
- **Decision:** Road Warrior owns obligations and maintains the authoritative V1 obligation ledger. The ledger contains timed and untimed obligations in a simple human-readable Markdown file on a shared Google Drive surface accessible to Road Warrior across relevant transports. External systems may execute, notify, or surface obligations, but they are not the authoritative obligation store.
- **Rationale:** Formal Phase C testing found direct Google Tasks execution `UNAVAILABLE`, prompting review of the assumption that an external task application should own Road Warrior obligations. Road Warrior ownership better preserves Cognitive Freedom by keeping capture, contextual association, status maintenance, retrieval, surfacing, and appropriate reconciliation within the accepted responsibility.
- **Consequences:** Google Tasks is not a required V1 obligation store, and its `UNAVAILABLE` Phase C result remains evidence. Time-sensitive obligations remain in the Road Warrior ledger and may also use Google Calendar for external notification. ChatGPT Scheduled Tasks remain rejected. Road Warrior should recognize natural-language completion using context and judgment, ask the smallest clarifying question when identification is materially ambiguous, update the authoritative obligation state, and reconcile related external artifacts when necessary and authorized. Bruce must not be required to manage the ledger manually. Markdown and Google Drive are replaceable V1 implementation choices; databases, Obsidian, semantic retrieval, TencentDB Agent Memory, and other relational or shared-memory systems remain later research. The ledger architecture must be reality-tested before it is treated as proven.
- **Status:** ACCEPTED — GOVERNED PROTOTYPE 1 REQUIREMENTS AMENDMENT; REALITY TESTING REQUIRED

### RW-038 — Use One Thin Current-State Bootstrap for V1

- **ID:** RW-038
- **Date:** 2026-08-14
- **Decision:** V1 uses one canonical `ROAD_WARRIOR_CURRENT_STATE.md` Markdown file on shared Google Drive as its authoritative derived operational snapshot. Bruce adds the stable Drive link as a Road Warrior ChatGPT Project source, and Project Instructions require retrieval before judgments about current phase, readiness, capabilities, limitations, priorities, or next action.
- **Rationale:** A no-bootstrap fresh-chat test recovered identity and history well but returned a materially stale operational state. One named current-state source closes that demonstrated gap without introducing a general memory architecture.
- **Consequences:** GitHub remains authoritative for frozen requirements, durable architectural decisions, implementation sequencing, and historical evidence. Snapshot contents are not duplicated in the repository. The snapshot remains approximately one rendered page and under roughly 800 words, is updated only for material operational changes, and is independently verified after writes. `ROAD_WARRIOR_CONTEXT_INDEX.md`, a Memory Steward agent or skill, databases, semantic retrieval, transcript archives, Obsidian integration, and autonomous background memory infrastructure are not V1 mechanisms. The configured fresh-chat test proved operational retrieval but did not reproduce the living partnership or reasoning continuity; RW-040 defines that V1 boundary.
- **Status:** ACCEPTED — V1 OPERATIONAL CONTINUITY MECHANISM; OPERATIONAL RETRIEVAL PROVEN

### RW-039 — Use the RoadWarrior Drive Folder as the Operational Boundary

- **ID:** RW-039
- **Date:** 2026-08-14
- **Decision:** The root-level Google Drive folder `RoadWarrior` is the default storage and retrieval boundary for Road Warrior operational artifacts.
- **Rationale:** A single bounded Drive location improves operational discovery and maintenance without changing artifact authority or introducing a broader memory architecture.
- **Consequences:** Clearly Road Warrior-owned operational artifacts should use this folder by default. Existing stable file IDs and links remain authoritative references when files are moved into the folder. Unrelated or ambiguous files must not be moved automatically. `ROAD_WARRIOR_CURRENT_STATE.md` remains the canonical Drive-only derived operational snapshot, while GitHub retains its existing governance and evidence authority.
- **Status:** ACCEPTED — V1 OPERATIONAL STORAGE/RETRIEVAL BOUNDARY

### RW-040 — Use the Persistent Road Warrior Conversation as Primary V1 Continuity

- **ID:** RW-040
- **Date:** 2026-08-14
- **Decision:** The existing persistent Road Warrior conversation is the primary V1 conversational continuity mechanism. Bruce should use that same conversation across desktop, phone/mobile, and headphones/voice and should not deliberately start fresh Road Warrior chats merely to manage context-window size. `ROAD_WARRIOR_CURRENT_STATE.md` remains the operational checkpoint and recovery/orientation support; it does not replace the persistent conversational relationship.
- **Rationale:** The configured fresh-chat test recovered current operational state but did not reproduce Road Warrior voice, the working relationship with Bruce, interaction cadence, accumulated understanding of how Bruce thinks, conversational shorthand, judgment style, or reasoning continuity. Bruce experienced the fresh chat as a stranger. These relationship qualities are part of the Road Warrior value proposition, not cosmetic presentation.
- **Consequences:** Operational/current-state retrieval is a V1 pass; partnership/voice continuity, reasoning/decision continuity, and overall replacement of the persistent conversation failed. Fresh-chat equivalence is not an August 21 requirement and becomes later research. The Project-source retrieval mechanism remains in force for recovery and orientation. No giant bootstrap, transcript ingestion, Memory Steward, context index, database, embeddings, knowledge graph, or other new memory infrastructure is admitted before the trip. A later progressive-retrieval direction may conceptually be living conversation → recent durable memory → historical/index layer → deeper authoritative archive/source, but it is not current implementation scope.
- **Status:** ACCEPTED — V1 CONVERSATIONAL CONTINUITY BOUNDARY

### RW-041 — Defer WhatsApp and Use the Persistent Chat Across V1 Transports

- **ID:** RW-041
- **Date:** 2026-08-14
- **Decision:** Bidirectional WhatsApp transport is degraded/deferred from the August 21 requirement. The V1 communication baseline is the same persistent Road Warrior conversation on desktop, phone/mobile, and headphones/voice. True hands-free bidirectional in-car Road Warrior is a known limitation and is not required for V1.
- **Rationale:** Likely near-term WhatsApp value is modest relative to unproven integration effort involving possible Meta WhatsApp Business, paid Zapier or equivalent, separate messaging/runtime plumbing, authentication and configuration, and uncertain preservation of the Road Warrior relationship. That risk is not justified during convergence.
- **Consequences:** Do not pursue WhatsApp, Meta, or Zapier integration before the trip unless materially new evidence makes it genuinely trivial and it cannot threaten core readiness. WhatsApp, Zapier, Composio, Airbyte, Alexa, and related communication mechanisms remain later research candidates. August 21 tests whether the Road Warrior judgment partnership reduces Bruce's cognitive load in ordinary life, not whether sophisticated automotive transport has been engineered.
- **Status:** ACCEPTED — DEFERRED FROM AUGUST 21; LATER RESEARCH

## Superseded Decisions

- RW-037 supersedes only the obligation-storage routing portion of RW-031. RW-031's Google Calendar notification role and rejection of ChatGPT Scheduled Tasks remain in force.
- RW-041 supersedes the pre-August-21 attempt path in RW-017. WhatsApp/Twilio remains a later research candidate, not a core Prototype 1 requirement.
- RW-044 supersedes only the repository-root storage-location portion of RW-028. RW-028's shared Markdown mechanism, ownership, structure, status flow, replaceability, and verification requirements remain in force.
- RW-046 supersedes only RW-030's requirement that every noticeable-duration successful execution receive an explicit Bruce-facing completion message. Real acceptance and execution signaling, the prohibition on implied background work, verified completion, and explicit surfacing of failures, blockers, required judgment, and threatened obligations remain in force.

## Open Questions

- The verified Prototype 1 capability boundary for Google Drive, Gmail drafting and sending, desktop, mobile, and voice behavior. Direct Google Tasks execution is `UNAVAILABLE` and retained as Phase C evidence.

## Accepted Decisions (continued)

### RW-042 — Use a Once-Per-Day Project Handoff Consumer Trigger

- **ID:** RW-042
- **Date:** 2026-08-17
- **Decision:** Participating projects consume Road Warrior handoffs on the first user message in that project each calendar day. Before responding, the project checks the exact shared `ROAD_WARRIOR_HANDOFFS` ledger for Pending entries unambiguously addressed to it. After a successful check, it does not check again that calendar day unless Bruce explicitly requests another Road Warrior-message check.
- **Rationale:** The prior “open or meaningfully resume” trigger was ambiguous, while checking every user turn would impose unnecessary Drive latency. A deterministic once-per-calendar-day trigger preserves automatic pickup after Bruce has been away without making Bruce remember to request synchronization.
- **Consequences:** There is no background monitoring or polling. Receiving projects remain responsible for durable incorporation, deduplication, verified readback, and acknowledgment only after success. Automatic background project invocation remains unproven and is not required for this V1 mechanism.
- **Status:** ACCEPTED — V1 CROSS-PROJECT CONSUMER TRIGGER

### RW-043 — Establish the Repository Governance Control Plane

- **ID:** RW-043
- **Date:** 2026-08-18
- **Decision:** Road Warrior uses a concise repository-root Operating Kernel, mandatory agent preflight, repository entry-point authority map, document-status manifest, current architecture, and executable governance regression checks as its local control plane.
- **Rationale:** The governing philosophy and frozen outcomes are sound, but dispersed documents did not reliably enforce current obligation, handoff, authorization, verification, or completion rules.
- **Consequences:** Governed actions must consult the Operating Kernel and the appropriate canonical source. The kernel compiles existing authority; it cannot silently amend frozen outcomes or historical evidence. Documentation and tests change together, and local repository work does not imply external-system synchronization.
- **Status:** ACCEPTED — PHASE 1 GOVERNANCE ENFORCEMENT

### RW-044 — Make the Shared Drive Artifact the Authoritative Live V1 Handoff Ledger

- **ID:** RW-044
- **Date:** 2026-08-18
- **Decision:** The Google Drive artifact `ROAD_WARRIOR_HANDOFFS` with file ID `1U4YvjjmwGAbspYwKo5dwlXd4NHbvSlnMdbWPPQYCGHc` is the one authoritative live V1 handoff ledger. The repository-root `ROAD_WARRIOR_HANDOFFS.md` is the protocol and stable-location pointer, not a competing operational ledger.
- **Rationale:** Later verified operation had already established the shared Drive artifact as the cross-project surface, while the repository-root file still presented itself as an active ledger. Two live authorities create ambiguous writes, receipts, and completion claims.
- **Consequences:** Producers and consumers use the exact Drive artifact and follow the repository protocol. Git history preserves the former root-ledger snapshot. A handoff remains `Pending` until the receiving project's durable incorporation and both required readbacks succeed; Bruce is not the courier.
- **Status:** ACCEPTED — V1 AUTHORITY CLARIFICATION

### RW-045 — Establish Road Warrior as the Control Plane and Governed Workers as the Execution Plane

- **ID:** RW-045
- **Date:** 2026-08-18
- **Decision:** Road Warrior is the singular brain, executive judgment engine, control plane, and conversational relationship with Bruce. V1.5 may add narrow governed workers as a replaceable execution plane. Workers receive already-judged immutable transactions, execute only bounded authorized operations, independently verify authoritative results, and return structured evidence. Workers do not interpret Bruce, determine ambiguity, set priorities, broaden authority, redefine completion, change governance, or communicate directly with Bruce.
- **Rationale:** Live regression testing showed that governed connector plumbing could consume roughly two and a half minutes and make the conversational surface unusably slow even when the selected mechanisms were correct. Separating execution plumbing protects Attention Continuity without diluting the scarce product asset: Road Warrior's accumulated judgment, voice, and relationship.
- **Consequences:** `GOVERNED_WORKER_CONTRACT.md` is the canonical worker boundary. Prefer deterministic code for deterministic work. A general multi-agent architecture is not approved. Existing authoritative artifact identities and Road Warrior's logical ownership of obligations remain unchanged. The future Personal OS may display verified projections of Road Warrior-judged state, but workers and the dashboard do not create judgment or independently write authoritative obligation or handoff state.
- **Status:** ACCEPTED — V1.5 ARCHITECTURE DIRECTION; NO WORKER IMPLEMENTATION AUTHORIZED

### RW-046 — Separate Durable Acceptance From Verified Completion and Protect Conversational Latency

- **ID:** RW-046
- **Date:** 2026-08-18
- **Decision:** Road Warrior may acknowledge accepted responsibility before a worker transaction finishes only after a real execution mechanism has durably accepted the complete bounded transaction. Durable acceptance is not completion, false acceptance is prohibited, and Road Warrior retains responsibility until verified completion or explicit return/failure handling. Routine verified success may close silently or through a low-salience mechanism when Bruce has moved on; Road Warrior decides human-facing communication, while failures, material changes, required judgment, and threats to an obligation surface appropriately.
- **Rationale:** Bruce should be able to stop carrying an accepted responsibility without watching backend plumbing, but an immediate conversational response must not manufacture execution durability or completion.
- **Consequences:** The acknowledgment design target is approximately one to two seconds where technically possible, with acknowledgment latency measured separately from transaction-completion latency. Multi-minute blocking execution before acknowledgment is a product failure. No current mechanism may be represented as durable background execution until that capability is independently verified. Workers return facts and evidence; they never decide whether or how Bruce is interrupted.
- **Status:** ACCEPTED — V1.5 ATTENTION-CONTINUITY AND RESPONSIBILITY RULE

### RW-047 — Admit Workers Individually Through Evidence, Starting With an Obligation Worker Proof

- **ID:** RW-047
- **Date:** 2026-08-18
- **Decision:** The first worker candidate is one synchronous Obligation Worker proof. Before any detached-runtime decision, it must prove the worker boundary, immutable contract, authority enforcement, idempotency, concurrency safety, authoritative read/write verification, ambiguous-side-effect reconciliation, and structured failure semantics. Additional workers require individual evidence and governance admission.
- **Rationale:** A synchronous proof can answer transaction-safety questions without assuming infrastructure. It cannot prove the desired non-blocking product experience; continued conversational blocking would be evidence that a durable dispatcher or background substrate has been earned.
- **Consequences:** This decision does not authorize implementation of the proof. Separate Bruce/ChatGPT approval is required. No queue, service, agent, MCP/tool surface, local runtime, hosted runtime, or infrastructure is selected. If detached execution is later justified, the target should operate without Bruce's Windows computer remaining awake.
- **Status:** ACCEPTED — EVIDENCE-GATED V1.5 SEQUENCING; PROOF NOT AUTHORIZED
