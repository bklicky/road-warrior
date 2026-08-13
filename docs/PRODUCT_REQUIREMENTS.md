# Road Warrior Prototype 1 Product Requirements

- Version: 1.3
- Status: Approved authoritative frozen Prototype 1 requirements baseline
- Date: 2026-08-13
- Approved: Bruce and ChatGPT, 2026-08-13
- Readiness target: 2026-08-20
- Field use begins: 2026-08-21

“Frozen” means sufficiently clear and approved to govern Prototype 1 implementation and testing. It does not prohibit a later explicitly governed amendment if reality testing reveals a material requirement change.

## Purpose

Road Warrior is a Cognitive Operating System. Its core value proposition is reducing cognitive load through judgment, continuity, and appropriate responsibility transfer.

Prototype 1 validates the Cognitive Partnership: whether Road Warrior meaningfully reduces Bruce's cognitive load. It does not primarily validate voice or the driving experience.

August 21 is a milestone for a credible, testable V1 baseline, not perfection or completion of later architecture.

## Scope and Transports

- Desktop and mobile are valid Prototype 1 transports.
- The car remains an important test environment, but it is not the product boundary.
- Voice is an interface, not the core value proposition.
- Judgment, relationship, and responsibility standards must remain consistent across desktop, mobile, and voice.
- Response length, pacing, structure, turn-taking, and progressive disclosure must adapt to the transport and Bruce's attention context.

## Functional Requirements

### Judgment Engine

The Judgment Engine must distinguish at minimum:

- Thinking aloud
- Brainstorming
- Decision
- Delegation
- Communication
- Research
- Project work

Judgment determines the appropriate next action.

### Execution Handoff Visibility

- For noticeable-duration work, Road Warrior must use `Accept → Signal → Execute → Close`.
- Road Warrior must briefly indicate what it accepted and that work is being performed when real execution is occurring.
- Road Warrior must explicitly report completion, blockage, or required input.
- Road Warrior must not imply background or continuing execution unless real execution is occurring.

### Zero Assumptions

- Zero Assumptions is mandatory.
- Road Warrior must not treat brainstorming, tentative language, or an undeveloped thought as an instruction to act.
- If intent is materially uncertain, Road Warrior must ask the smallest clarifying question necessary.

### Brainstorm Workflow

The approved Prototype 1 brainstorm workflow is:

Conversation → Judgment → Summary → Google Drive capture → Reminder/task → Resume naturally

The summary must be concise. Capture and reminder/task creation must not unnecessarily derail the conversation.

### External Communication Authorization

- An explicit send instruction authorizes sending through the requested approved channel, subject to verified capability and any required confirmation.
- An explicit draft instruction authorizes drafting but not sending.
- Materially ambiguous authorization requires the smallest clarifying question necessary.
- For V1 email, Road Warrior uses the Gmail connector. Drafting or sending remains subject to verified connector capability and any required confirmation.
- Road Warrior must not infer draft or send authority from brainstorming, tentative language, or discussion of communication.

### Obligation and Reminder Routing

- Timed obligations route to Google Calendar with a notification.
- Untimed obligations route to Google Tasks as the intended V1 rule.
- Google Calendar execution has positive reality-test evidence.
- Direct Google Tasks execution remains unproven and must not be represented as available until verified.
- ChatGPT Scheduled Tasks must not be used as a Road Warrior reminder mechanism. Reality testing found that they disrupted the primary conversation or chat state and introduced rate-limit friction.

### Context Continuity

- Context continuity is a V1 requirement.
- Road Warrior must preserve enough project, person, and conversational-thread context that Bruce does not repeatedly reconstruct prior work.
- This requirement applies across Road Warrior, Instagram, Personal OS, music, baking, relationships, and future approved projects.
- The approved V1 Context Routing mechanism is the shared repository-root `ROAD_WARRIOR_HANDOFFS.md` ledger.
- Capability/reality testing must determine what is actually achievable for Prototype 1.
- Contextual memory may support judgment, but authoritative artifacts remain necessary when exact wording, quantities, commitments, or other precision matters.

### Context Routing Handoffs

- Road Warrior must judge whether information is durable and project-relevant, determine its target project, and create a structured handoff entry.
- The receiving project must read entries addressed to it, incorporate the information into its own context or work, and acknowledge receipt.
- V1 handoff status is `Pending → Received`.
- Bruce must not be required to carry information between Road Warrior and receiving projects.
- The ledger is intentionally simple and replaceable. Its records must remain structured enough for later migration.
- V1 does not require software, database infrastructure, automation, APIs, or Obsidian integration for Context Routing.
- The approved mechanism does not establish that cross-project pickup and acknowledgment work end to end; that flow requires testing.

## Non-Functional Requirements

- Road Warrior must reduce cognitive load at every reasonable opportunity without removing Bruce's agency.
- Reality and observed evidence must override confidence, preference, or implementation convenience.
- Interaction must preserve attention continuity and resume the prior conversation naturally after an action.
- Responsibility must transfer only when Road Warrior has enough understanding and capability to accept it honestly.
- Adaptive Communication begins in V1 and remains a long-term requirement: Road Warrior should progressively adjust communication behavior from Bruce's explicit and observed feedback without converting isolated feedback into an unsupported universal assumption.

## Stretch Goal

WhatsApp/Twilio is a Prototype 1 stretch goal.

- It may be attempted only after the core Prototype 1 judgment and execution loops are working reliably.
- It must not threaten August 20 readiness.
- If it cannot be added safely within available time, it must be deferred to Version 2.

## Prototype 1 Non-Goals

- Android app
- Android Auto integration solution
- Obsidian implementation
- Personal OS dashboard integration
- Full autonomous multi-agent architecture
- Production infrastructure

Richer bidirectional cross-project context sharing is later architecture and research, not August 21 scope.

A V3/V4 knowledge-layer research direction may combine human-readable relational knowledge such as Obsidian with semantic retrieval. A graph database should be considered only if later complexity earns it. Road Warrior remains the judgment and routing layer; a knowledge layer would provide relational memory, not judgment.

Judgment-Driven Personal OS / Dynamic Mission Control is a V3 design direction. It is not a Prototype 1 requirement.

## Acceptance Criteria

Prototype 1 is ready for field use when evidence shows that:

- The Judgment Engine distinguishes the required intent categories or asks the minimum necessary clarifying question.
- Noticeable-duration work uses visible acceptance, real execution signaling, and an explicit close.
- The brainstorm workflow completes its summary, Google Drive capture, reminder/task, and conversational return without unnecessary cognitive burden.
- Email actions occur only after an explicit request and follow verified Gmail connector capability and confirmation requirements.
- Reminder handling routes timed obligations to Google Calendar and does not use ChatGPT Scheduled Tasks; unavailable Google Tasks execution is disclosed honestly.
- Context continuity is tested against real project, person, and thread scenarios, with achieved and unavailable behavior documented honestly.
- At least one Context Routing handoff is observed moving from `Pending` to `Received` after the addressed project incorporates it, without Bruce manually relaying the information.
- Core behavior works reliably on at least one desktop transport and one mobile transport.
- Communication remains coherent across tested transports while adapting to attention and interaction constraints.
- Car testing can proceed without redefining the car as the product boundary.
- Stretch work has not displaced or destabilized core readiness.
