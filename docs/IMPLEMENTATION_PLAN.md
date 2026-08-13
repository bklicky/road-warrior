# Road Warrior Prototype 1 Implementation Plan

- Version: 1.3
- Status: Active
- Date: 2026-08-13
- Readiness target: 2026-08-20
- Field use begins: 2026-08-21

Statuses are limited to `NOT STARTED`, `IN PROGRESS`, `WAITING`, and `COMPLETE`. Completion requires the stated evidence; planned work or discussion alone is not completion.

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

## C. Capability and Reminder Reality Testing

- **Objective:** Verify the actual capabilities and constraints of ChatGPT, Google Drive, Gmail, Google Calendar, Google Tasks, desktop, mobile, and relevant voice behavior before designing around them; preserve the rejection of ChatGPT Scheduled Tasks as a reminder mechanism.
- **Dependencies:** Phase B.
- **Evidence rule:** Phase C discovers actual capability boundaries. A repeatably verified result such as `AVAILABLE`, `UNAVAILABLE`, `UNRELIABLE`, `CONFIRMATION-REQUIRED`, or another honestly documented bounded result is valid Phase C evidence; a capability does not have to work for its test to be completed successfully. Completing a capability test does not automatically satisfy later Prototype 1 functional requirements, acceptance criteria, or field-readiness requirements.
- **Evidence required:** Repeatable test results recording configuration, observed behavior, failures, confirmation requirements, and capability boundaries for ChatGPT, Google Drive, Gmail authorization and confirmation behavior, Google Calendar timed-obligation and notification behavior, direct Google Tasks execution, desktop, mobile, and relevant voice behavior; and preservation of the ChatGPT Scheduled Tasks rejection and observed failure boundary.
- **Status:** NOT STARTED

## D. Judgment Specification

- **Objective:** Define observable rules for conversational states, multiple intents, dependency ordering, external communication authorization, execution handoff visibility, Transport-Aware Communication, Adaptive Communication, and the Zero Assumptions clarification rule.
- **Dependencies:** Phases B and C.
- **Evidence required:** Reviewed intent examples, counterexamples, ambiguity cases, dependency cases, expected actions, `Accept → Signal → Execute → Close` cases, transport cases, feedback-adaptation cases, and minimum clarifying questions.
- **Status:** NOT STARTED

## E. Prototype Instruction Package

- **Objective:** Create the explicit instruction and reference package that governs Prototype 1 judgment, execution visibility, reminder routing, communication authorization, and adaptive transport behavior across approved transports.
- **Dependencies:** Phases B, C, and D.
- **Evidence required:** Versioned instruction package with an attachment manifest, setup sequence, operating instructions, and traceability to requirements.
- **Status:** NOT STARTED

## F. Core Functional Rehearsal

- **Objective:** Rehearse the Judgment Engine and brainstorm workflow from conversation through visible execution handoff, summary, Google Drive capture, correctly routed obligation handling, explicit close, and natural resumption.
- **Dependencies:** Phase E and verified capabilities from Phase C.
- **Evidence required:** Successful repeated desktop and mobile runs, retained artifacts, transcripts, `Accept → Signal → Execute → Close` observations for noticeable-duration work, correct timed-versus-untimed routing or honest capability disclosure, timing observations, and documented failures.
- **Status:** NOT STARTED

## G. Context Continuity and Routing Testing

- **Objective:** Determine how much project, person, and thread continuity Prototype 1 can preserve; test contextual recall against authoritative artifacts; and test the shared Markdown handoff ledger from Road Warrior creation through receiving-project acknowledgment, without requiring Bruce to reconstruct or relay prior work.
- **Dependencies:** Phases C, D, E, and a stable core loop from Phase F.
- **Evidence required:** Scenario results across representative contexts; comparison of recalled context with an authoritative artifact when exactness matters; at least one addressed handoff observed moving from `Pending` to `Received` after incorporation by the receiving project; documented pickup, acknowledgment, continuity gaps, and recovery behavior; and an evidence-based Prototype 1 boundary.
- **Status:** NOT STARTED

## H. Communication-Return Testing

- **Objective:** Verify that explicit send instructions send, explicit draft instructions draft without sending, materially ambiguous authorization triggers the smallest necessary question, and Road Warrior returns to the prior conversation.
- **Dependencies:** Phases C, D, E, and a stable core loop from Phase F.
- **Evidence required:** Separate draft and send-path tests, ambiguous-authorization tests, confirmation behavior, negative tests for discussion and non-requests, connector failure handling, and successful conversational resumption.
- **Status:** NOT STARTED

## I. WhatsApp/Twilio Stretch Evaluation

- **Objective:** Decide whether the WhatsApp/Twilio stretch goal can be attempted safely without jeopardizing core reliability or August 20 readiness.
- **Dependencies:** Reliable completion of core behavior in Phases F, G, and H, plus sufficient schedule margin.
- **Evidence required:** Written proceed/defer decision based on verified capability, integration risk, time remaining, and regression risk.
- **Status:** WAITING

## J. Abuse Testing

- **Objective:** Challenge judgment, clarification, capture, communication, execution visibility, continuity, recovery, reminder routing, Transport-Aware Communication, and Adaptive Communication with ambiguous, interrupted, adversarial, and failure-prone scenarios.
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
