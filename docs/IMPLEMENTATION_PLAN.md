# Road Warrior Prototype 1 Implementation Plan

- Version: 1.8
- Status: Active
- Date: 2026-08-18
- Readiness target: 2026-08-20
- Field use begins: 2026-08-21

Statuses are limited to `NOT STARTED`, `IN PROGRESS`, `WAITING`, and `COMPLETE`. Completion requires the stated evidence; planned work or discussion alone is not completion.

## Current Convergence Posture

- Road Warrior is in CONVERGENCE / “batten down the hatches” mode for the August 20 readiness decision and August 21 field use.
- Nothing new enters V1 unless it closes a demonstrated trip-readiness gap.
- The root-level Google Drive folder `RoadWarrior` is the default storage and retrieval boundary for clearly Road Warrior-owned operational artifacts; unrelated or ambiguous files are not moved automatically.
- The existing persistent Road Warrior conversation is the primary V1 conversational continuity mechanism across desktop, phone/mobile, and headphones/voice. `ROAD_WARRIOR_CURRENT_STATE.md` remains the operational checkpoint and recovery/orientation support, not a replacement for the living partnership.
- Fresh-chat operational retrieval has passed; fresh-chat partnership/voice and reasoning/decision equivalence failed and are later research rather than an August 21 requirement.
- Bidirectional WhatsApp is deferred from the August 21 requirement. True hands-free bidirectional in-car use is a known limitation and is not required for V1.
- Current ordered priorities are: connect the Instagram/O.G. Bruce project to the shared handoff mechanism and verify `RW-HO-0001` incorporation; resolve the still-open Alexa/Zapier/ChatGPT test only from evidence; perform a mobile/headphones rehearsal using the existing persistent Road Warrior conversation; perform the final August 20 readiness rehearsal; and begin August 21 field use only after a go decision.
- The V1.5 governed-worker architecture is approved as a direction only. It does not change current V1 priorities, authorize an Obligation Worker proof, or establish that durable/background dispatch is available.

## A. Repository Synchronization

- **Objective:** Integrate approved August 11 architecture, requirements, plan, and decisions into the repository without changing frozen principles.
- **Dependencies:** Approved August 11 architecture synchronization document and existing governance baseline.
- **Evidence required:** Reviewed diffs limited to authorized files; repository conflicts and unresolved questions listed; Bruce/ChatGPT approval to proceed.
- **Approval:** Bruce and ChatGPT approved completion on 2026-08-13.
- **Status:** COMPLETE

## B. Freeze Prototype 1 Requirements

- **Objective:** Establish the minimum authoritative scope, non-goals, acceptance criteria, readiness date, and stretch-goal boundary for Prototype 1.
- **Dependencies:** Phase A.
- **Evidence required:** Approved `PRODUCT_REQUIREMENTS.md` with no material ambiguity about core versus stretch scope.
- **Approval:** Bruce and ChatGPT approved `PRODUCT_REQUIREMENTS.md` as the authoritative frozen Prototype 1 requirements baseline on 2026-08-13.
- **Status:** COMPLETE

## C. Capability and Obligation Reality Testing

- **Objective:** Verify the actual capabilities and constraints of ChatGPT, Google Drive, Gmail, Google Calendar, Google Tasks, desktop, mobile, and relevant voice behavior before designing around them; test the approved Road Warrior-owned obligation architecture; and preserve the rejection of ChatGPT Scheduled Tasks as a reminder mechanism.
- **Dependencies:** Phase B.
- **Evidence rule:** Phase C discovers actual capability boundaries. A repeatably verified result such as `AVAILABLE`, `UNAVAILABLE`, `UNRELIABLE`, `CONFIRMATION-REQUIRED`, or another honestly documented bounded result is valid Phase C evidence; a capability does not have to work for its test to be completed successfully. Completing a capability test does not automatically satisfy later Prototype 1 functional requirements, acceptance criteria, or field-readiness requirements.
- **Evidence required:** Repeatable test results recording configuration, observed behavior, failures, confirmation requirements, and capability boundaries for ChatGPT, Google Drive, Gmail authorization and confirmation behavior, Google Calendar timed-obligation and notification behavior, direct Google Tasks execution, desktop, mobile, and relevant voice behavior; preservation of the ChatGPT Scheduled Tasks rejection and observed failure boundary; and bounded end-to-end evidence for durable obligation capture, contextual association, retrieval, surfacing, natural-language completion, status maintenance, and authorized reconciliation with an external notification artifact.
- **Evidence to date:** Direct Google Tasks execution is `UNAVAILABLE`. Initial obligation-ledger plumbing is `AVAILABLE` for Markdown creation, in-place update, and immediate independent readback through the current Codex Google Drive connector. Google Calendar timed notification/surfacing has basic positive evidence. Gmail read-side intelligence and explicitly authorized promotional-email deletion have basic positive reported evidence. Drive search and read/discovery of the shared handoff artifact are `AVAILABLE`. Bounded receiving-project consumption, durable incorporation, readback verification, and receipt acknowledgment are proven for Guitar and Baking; natural first-message-of-day trigger reliability beyond those examples remains under test. The canonical `ROAD_WARRIOR_CURRENT_STATE.md` Drive artifact has been created and independently read back, and a configured fresh chat successfully retrieved its operational state. The same test did not reproduce partnership/voice or reasoning/decision continuity and therefore did not replace the persistent conversation. The `RoadWarrior` Drive folder is verified as the parent of the current-state, handoff, obligation, and mind-map artifacts without changing their file IDs; it is now the default operational storage/retrieval boundary. Later-session and cross-transport obligation retrieval, open-obligation reporting, natural-language completion and ledger update, timed obligation-to-Calendar reconciliation, and mobile/headphones rehearsal remain unproven. See the Phase C evidence records dated 2026-08-13, 2026-08-14, and 2026-08-17.
- **Status:** IN PROGRESS

## D. Judgment Specification

- **Objective:** Define observable rules for conversational states, multiple intents, dependency ordering, obligation recognition and state reconciliation, external communication authorization, execution handoff visibility, Transport-Aware Communication, Adaptive Communication, and the Zero Assumptions clarification rule.
- **Dependencies:** Phases B and C.
- **Evidence required:** Reviewed intent examples, counterexamples, ambiguity cases, dependency cases, expected actions, `Accept → Signal → Execute → Close` cases, transport cases, feedback-adaptation cases, and minimum clarifying questions.
- **Approval:** Bruce and ChatGPT consider the existing Judgment Engine sufficient for Prototype 1 as of 2026-08-14. It is effectively frozen except for genuine defects discovered through use; ordinary behavioral coaching continues through use and feedback.
- **Status:** COMPLETE

## E. Prototype Instruction Package

- **Objective:** Create the explicit instruction and reference package that governs Prototype 1 judgment, execution visibility, obligation ownership and external surfacing, communication authorization, and adaptive transport behavior across approved transports.
- **Dependencies:** Phases B, C, and D.
- **Evidence required:** Versioned instruction package with an attachment manifest, setup sequence, operating instructions, and traceability to requirements.
- **Status:** NOT STARTED

## F. Core Functional Rehearsal

- **Objective:** Rehearse the Judgment Engine and brainstorm workflow from conversation through visible execution handoff, summary, Google Drive capture, authoritative obligation-ledger handling, appropriate external surfacing, explicit close, and natural resumption.
- **Dependencies:** Phase E and verified capabilities from Phase C.
- **Evidence required:** Successful repeated desktop and mobile runs, retained artifacts, transcripts, `Accept → Signal → Execute → Close` observations for noticeable-duration work, correct obligation capture and state maintenance, appropriate external surfacing or honest capability disclosure, timing observations, and documented failures.
- **Status:** NOT STARTED

## G. Context Continuity and Routing Testing

- **Objective:** Determine how much project, person, and thread continuity Prototype 1 can preserve; test contextual recall against authoritative artifacts; and test the shared Markdown handoff ledger from Road Warrior creation through receiving-project acknowledgment, without requiring Bruce to reconstruct or relay prior work.
- **Dependencies:** Phases C, D, E, and a stable core loop from Phase F.
- **Evidence required:** Scenario results across representative contexts; comparison of recalled context with an authoritative artifact when exactness matters; at least one addressed handoff observed moving from `Pending` to `Received` after incorporation by the receiving project; documented pickup, acknowledgment, continuity gaps, and recovery behavior; and an evidence-based Prototype 1 boundary.
- **Evidence to date:** Native fresh-chat continuity is strong for identity and history but insufficient for authoritative current operational state without the thin bootstrap. With the configured `ROAD_WARRIOR_CURRENT_STATE.md` source and retrieval rule, fresh-chat operational orientation passed. Partnership/voice continuity, reasoning/decision continuity, and overall replacement of the persistent Road Warrior conversation failed; fresh-chat equivalence is not an August 21 requirement. The persistent conversation is the primary V1 conversational continuity mechanism. Drive-based handoff search and read/discovery are proven in the current connector context. Bounded consumer incorporation, deduplication, readback verification, and acknowledgment are proven for Guitar and Baking. `RW-HO-0004` and `RW-HO-0005` are verified `Received`; broader natural first-message-of-day trigger reliability remains under test. See `CURRENT_STATE_CONTINUITY.md` and the Phase C evidence records dated 2026-08-14, 2026-08-17, and the Phase 2B reconciliation evidence dated 2026-08-18.
- **Status:** IN PROGRESS

## H. Communication-Return Testing

- **Objective:** Verify that explicit send instructions send, explicit draft instructions draft without sending, materially ambiguous authorization triggers the smallest necessary question, and Road Warrior returns to the prior conversation.
- **Dependencies:** Phases C, D, E, and a stable core loop from Phase F.
- **Evidence required:** Separate draft and send-path tests, ambiguous-authorization tests, confirmation behavior, negative tests for discussion and non-requests, connector failure handling, and successful conversational resumption.
- **Status:** NOT STARTED

## I. WhatsApp/Twilio Stretch Evaluation

- **Objective:** Decide whether the WhatsApp/Twilio stretch goal can be attempted safely without jeopardizing core reliability or August 20 readiness.
- **Dependencies:** Reliable completion of core behavior in Phases F, G, and H, plus sufficient schedule margin.
- **Evidence required:** Written proceed/defer decision based on verified capability, integration risk, time remaining, and regression risk.
- **Decision:** Deferred from the August 21 requirement. The likely V1 value is modest relative to unproven Meta WhatsApp Business, paid Zapier or equivalent, separate runtime plumbing, authentication/configuration, and relationship-preservation risk. Reconsider before the trip only if materially new evidence makes the path genuinely trivial and harmless to core readiness.
- **Status:** COMPLETE

## J. Abuse Testing

- **Objective:** Challenge judgment, clarification, capture, communication, execution visibility, continuity, recovery, obligation ownership and external surfacing, Transport-Aware Communication, and Adaptive Communication with ambiguous, interrupted, adversarial, and failure-prone scenarios.
- **Dependencies:** Phases F, G, and H; Phase I only if the stretch goal proceeds.
- **Evidence required:** Test matrix, observed failures, severity classification, fixes or accepted limitations, transport comparisons, evidence that feedback is adapted without unsupported generalization, and regression results.
- **Status:** NOT STARTED

## K. August 20 Freeze

- **Objective:** Freeze a credible, testable Prototype 1 baseline for August 21 while protecting the core loop from late destabilizing changes and excluding V2/V3/V4 expansion.
- **Dependencies:** Approved requirements and sufficient evidence from Phases C through J; stretch work may be deferred.
- **Evidence required:** Versioned frozen package, readiness checklist, known limitations, rollback or recovery instructions, and explicit go/no-go decision.
- **Status:** NOT STARTED

## L. August 21 Field Use

- **Objective:** Use Prototype 1 in real conditions to gather evidence about the Cognitive Partnership and reduction of Bruce's cognitive load.
- **Dependencies:** Phase K go decision and safe operating conditions for the chosen transports and environments.
- **Evidence required:** Session records, captured artifacts, continuity and judgment observations, field feedback, reflection, failures, and post-use assessment against Prototype 1 acceptance criteria.
- **Status:** NOT STARTED

## 2026-08-17 Convergence Update

- Cross-project handoff consumption is now proven at a bounded V1 level for Guitar and Baking: exact-ledger retrieval, target filtering, project-owned durable state/action update, readback verification, and receipt acknowledgment all succeeded.
- The consumer trigger is now deterministic: first user message in the participating project each calendar day, with no repeat check that day unless Bruce explicitly asks for a new Road Warrior-message check. No background monitoring or polling is claimed.
- Two handoffs (`RW-HO-0004` Guitar and `RW-HO-0005` Baking) were created as `Pending` for a natural first-message-of-day trigger test; both have since been verified `Received` with their destination receipts preserved.
- Twilio SMS has moved from abstract stretch research to an active optional transport experiment. Basic two-way SMS is proven, the Road Warrior Twilio Function is deployed, the permanent number `+1 805-600-2358` is acquired, and A2P campaign review is pending. SMS remains non-required for August 21 and must not destabilize core readiness.
- See `PHASE_C_CAPABILITY_EVIDENCE_2026-08-17.md`.

## M. Phase 1 Repository Governance Repair — 2026-08-18

- **Objective:** Install a local repository control plane that enforces existing values and accepted behavior without changing the frozen philosophy or mutating external systems.
- **Scope:** Operating Kernel, mandatory agent preflight, README authority map, document-status manifest, current architecture, current-document reconciliation, handoff protocol pointer, deferred V2 recommendation, and lightweight consistency/behavioral regression checks.
- **Evidence required:** Every repository document reviewed before editing; historical decision and evidence text preserved; local checks pass; changed-file diff reviewed; no external writes, commit, or push.
- **External boundary:** Phase 1 itself did not mutate external systems. The separately authorized Phase 2B reconciliation was completed and verified afterward.
- **Status:** COMPLETE

## N. Phase 2B External Reconciliation — 2026-08-18

- **Objective:** Reconcile the operational Drive, Calendar, Scheduled Task, handoff, ChatGPT Project, and current-state surfaces with the accepted repository governance while preserving stable identities and historical evidence.
- **Scope:** Obligation-ledger statuses and Calendar links; two baking Calendar events; unchanged Tirzepatide series; terminal Call Steph state; paused duplicate Scheduled Tasks; synchronized live handoff protocol; `RW-HO-0001` connector dependency; governed ChatGPT Project instructions; Project source-list audit; current-state refresh.
- **Evidence required:** Explicit authorization, authoritative-surface readback after every mutation, stable IDs preserved, no deletion, and no completion claim beyond the observed evidence.
- **Evidence:** `PHASE_2B_EXTERNAL_RECONCILIATION_EVIDENCE_2026-08-18.md`.
- **Remaining work:** Connect the Instagram/O.G. Bruce project and verify `RW-HO-0001` incorporation; resolve the open Alexa/Zapier/ChatGPT test only from evidence; continue mobile/headphones and readiness testing.
- **Status:** COMPLETE

## O. V1.5 Governed Worker Architecture Approval — 2026-08-18

- **Objective:** Durably separate Road Warrior's singular judgment and conversational control plane from narrow governed execution workers without changing frozen outcomes, the Judgment Engine taxonomy, existing authoritative-artifact identities, or current V1 implementation scope.
- **Scope:** Durable decisions RW-045 through RW-047; Operating Kernel acceptance/dispatch/closure rules; current architecture; approved V1.5 product requirements; canonical `GOVERNED_WORKER_CONTRACT.md`; minimal Judgment Engine clarification; agent controls; future Personal OS boundary; implementation sequencing; and static regression coverage.
- **Evidence required:** Cross-document consistency; explicit no-implementation boundary; worker non-authority; durable-acceptance and false-acceptance rules; separate acknowledgment/completion latency measures; idempotency, concurrency, verification, retry, and failure contracts; passing governance checks; reviewed diff; and current-state reconciliation by stable-ID readback.
- **External boundary:** Only the derived `ROAD_WARRIOR_CURRENT_STATE.md` snapshot may be reconciled for this material approved decision. No obligation, handoff, Calendar, Gmail, dashboard, service, queue, worker, agent, or infrastructure mutation is authorized.
- **Status:** COMPLETE

## P. V1.5 Obligation Worker Proof — NOT AUTHORIZED

- **Objective:** Prove one narrow synchronous Obligation Worker boundary before evaluating additional workers or detached execution infrastructure.
- **Initial scope:** One already-judged immutable obligation transaction; contract validation; stable ledger ID; idempotency; serialized or equivalent concurrency protection; authoritative read-before-write and readback; ambiguous-side-effect reconciliation; structured evidence; and failure states returned to Road Warrior.
- **Dependencies:** Separate explicit Bruce/ChatGPT implementation authorization; approved Phase O governance; verified connector capability; a reviewed proof design; and no destabilization of current V1 readiness.
- **Evidence required:** No duplicate on repeated transaction; stale precondition blocked; no blind retry after ambiguous outcome; verified authoritative result; `requires_judgment` on missing material input; no worker-to-Bruce communication; measured acknowledgment and completion latency; and documented proof boundaries.
- **Product boundary:** Synchronous success proves transaction safety, not non-blocking conversational continuity. Material blocking is evidence for later evaluation of a durable dispatcher/background substrate, not authority to build one.
- **Runtime boundary:** No queue, service, agent, MCP/tool surface, local runtime, hosted runtime, or infrastructure is selected. Any detached target should later be evaluated against the requirement that Bruce's Windows computer need not remain awake.
- **Status:** NOT STARTED — IMPLEMENTATION NOT AUTHORIZED
