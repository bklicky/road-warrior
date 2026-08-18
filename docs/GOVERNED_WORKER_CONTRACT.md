# Road Warrior Governed Worker Contract

- Version: 1.0
- Status: Canonical V1.5 architecture contract; one bounded synchronous proof verified; no production worker runtime is authorized
- Date: 2026-08-18
- Approved: Bruce and ChatGPT, 2026-08-18

## Purpose

This contract defines the authority boundary and transaction rules for any Road Warrior governed worker. It governs the separately authorized bounded Obligation Worker proof, but does not authorize a production worker, dispatcher, queue, service, agent, or deployment.

The governing rule is:

> Workers execute. Road Warrior judges.

Road Warrior remains the singular executive judgment engine and conversational relationship with Bruce. A worker is a narrow, bounded, preferably deterministic executor that receives an already-judged transaction and returns structured evidence.

## Exclusive Road Warrior Responsibilities

Only Road Warrior may:

- interpret Bruce's natural language, conversational state, intent, confidence, and material ambiguity;
- decide whether to listen, clarify, challenge, accept, decline, wait, or do nothing;
- determine authority, priority, dependencies, completion conditions, and whether a change is material;
- accept and retain responsibility for obligations;
- choose the human-facing acknowledgment, failure surfacing, and closure behavior;
- preserve Road Warrior's voice, relationship continuity, and adaptive communication; and
- propose or change governance through the governed process.

Workers never communicate directly with Bruce and never produce Bruce-facing prose as an exercise of worker authority.

## Worker Authority Boundary

A worker may:

- validate a supplied transaction against this contract;
- retrieve the exact authoritative target by stable resource ID;
- perform only the ordered operations explicitly authorized by the transaction;
- protect authoritative state through concurrency and idempotency controls;
- independently read back and verify the resulting authoritative state; and
- return structured success, partial, blocked, failure, or uncertainty evidence to Road Warrior.

A worker may not:

- reinterpret Bruce, infer a missing material field, or broaden scope;
- choose priorities, recipients, deadlines, destinations, or follow-up work;
- redefine success, authority, or the accepted responsibility;
- change governance or an authoritative-artifact identity;
- become an alternate judgment engine or competing source of truth; or
- ask Bruce a question directly.

When a material field is missing, ambiguous, contradictory, or stale, the worker returns `requires_judgment` to Road Warrior without guessing.

## Immutable Transaction Envelope

Every worker request must be immutable, versioned, and bounded. It contains at minimum:

| Field | Requirement |
| --- | --- |
| `contract_version` | Worker-contract version used to validate the request. |
| `transaction_id` | Globally unique stable transaction identifier. |
| `idempotency_key` | Stable key used to recognize re-delivery without duplicating an operation. |
| `intent_type` | Intent already judged by Road Warrior. |
| `accepted_responsibility` | Exact responsibility Road Warrior owns. |
| `authority` | Evidence and boundaries of the user's authorization. |
| `operations` | Ordered exact operations the worker may perform. |
| `payload` | Fully resolved values required by those operations. |
| `resource_ids` | Stable authoritative target and related resource IDs. |
| `preconditions` | Expected revision, hash, timestamp, state, or other concurrency guards. |
| `completion_condition` | Evidence required for verified completion. |
| `forbidden_actions` | Explicit scope the worker must not enter. |
| `expiry` | Time after which execution requires renewed judgment. |
| `retry_policy` | Bounded retry count and retryable error classes. |
| `closure_policy` | Conditions Road Warrior must evaluate for human-facing closure. |

The worker rejects an envelope that is incomplete, expired, internally inconsistent, unsupported, or outside its declared capability.

## Transaction Lifecycle

```text
created -> durably_dispatched -> running -> verifying -> succeeded
                                      |-> partial
                                      |-> requires_judgment
                                      |-> blocked
                                      |-> failed
                                      |-> outcome_unknown
```

- `created` is not durable acceptance.
- `durably_dispatched` requires a real execution mechanism that can retain and execute the transaction beyond the conversational acknowledgment.
- `succeeded` requires the specified authoritative readback evidence.
- `partial` preserves verified successful work and identifies the incomplete remainder.
- `outcome_unknown` requires authoritative reconciliation before retry or completion.

No current Road Warrior mechanism is presumed to provide durable dispatch merely because this lifecycle is approved.

## Acceptance, Completion, and Closure

- Road Warrior may acknowledge accepted responsibility before the underlying transaction finishes only after a real execution mechanism has durably accepted the transaction.
- Durable acceptance is not completion. False acceptance is prohibited.
- Road Warrior retains responsibility until verified completion or explicit return/failure handling.
- Routine verified success need not interrupt Bruce solely to announce plumbing. Road Warrior may close briefly during natural interaction, silently, or through a later approved low-salience mechanism.
- A failure, material change, ambiguity requiring judgment, or condition threatening an obligation must be returned to Road Warrior for appropriate surfacing.
- The worker never decides whether or how Bruce is interrupted.

## Verification and Evidence Result

The worker returns a structured result containing at minimum:

- `transaction_id` and terminal or current lifecycle state;
- per-operation status and timestamps;
- authoritative resource IDs and observed before/after versions;
- independent readback evidence satisfying or failing the completion condition;
- created external resource IDs, when applicable;
- retry count and classified error details;
- whether the error is retryable;
- unresolved inconsistencies or an `outcome_unknown` boundary; and
- facts Road Warrior needs to judge urgency and closure.

A tool response, request acceptance, local plan, or worker claim without authoritative evidence is not completion.

## Idempotency, Concurrency, and Retry Rules

- The `transaction_id` is the idempotency key across dispatch and execution.
- Re-delivery of the same transaction must not create a duplicate obligation, event, message, handoff, or receipt.
- A worker reads current authoritative state immediately before mutation and validates preconditions.
- Writes to the same authoritative artifact or logical record must be serialized or protected by an equivalent concurrency control.
- A stale precondition returns `blocked` or `requires_judgment`; it is not silently overwritten.
- Retry only errors explicitly classified as transient and within the bounded retry policy.
- After a timeout or ambiguous side effect, read authoritative state using the transaction ID or exact operation identity before retrying.
- Never blindly retry an irreversible or externally visible action such as sending a message.

## Authoritative-Artifact Protection

- Use the stable IDs established by Road Warrior governance.
- Preserve unknown fields, historical records, existing receipts, and unrelated content.
- Prefer the smallest exact record mutation; do not replace a whole artifact from stale content.
- Validate schema and governance invariants before and after mutation.
- Keep dispatch queues, logs, caches, and evidence stores subordinate to the authoritative artifact; they are not competing ledgers.
- A derived current-state projection must never be used to overwrite an authoritative obligation or handoff record.
- A State Steward or projection worker may apply only a Road-Warrior-approved material update; it may not decide materiality.

## Latency Evidence

- The conversational acknowledgment design target is approximately one to two seconds where technically possible.
- Measure acknowledgment latency separately from transaction-completion latency.
- Multi-minute blocking execution before acknowledgment is a product failure even when the eventual transaction succeeds.
- A synchronous worker proof may validate boundaries and transaction safety, but synchronous success alone does not prove Attention Continuity.
- If synchronous execution materially blocks the conversation, that evidence may justify evaluation of a durable background substrate.

## Admission and Implementation Boundary

- The first candidate was one Obligation Worker proof.
- Bruce/ChatGPT separately authorized only the controlled ledger-only proof on 2026-08-18; its evidence is `OBLIGATION_WORKER_PROOF_2026-08-18.md`.
- That proof established the bounded contract, authority refusal, idempotency, single-writer stale-state protection, read/write verification, ambiguous-outcome reconciliation, and failure semantics. It did not establish production readiness, durable dispatch, detached execution, or fast conversational acknowledgment.
- Additional worker types require individual evidence and durable governance admission.
- A general multi-agent architecture is not approved.
- Prefer deterministic code for deterministic work; do not choose an agent merely because one is available.
- No queue, local service, hosted service, MCP surface, always-on infrastructure, agent, or other runtime is selected.
- If detached execution is later justified, the target runtime should not depend on Bruce's Windows computer remaining awake.

## Future Personal OS Boundary

Future workers may gather verified state and maintain derived projections for a Personal OS surface. Road Warrior alone determines salience, priority, meaning, and what deserves Bruce's attention. The dashboard may display projections of judged state and return user actions to Road Warrior as new intent. It must not independently redefine priorities or write authoritative obligation or handoff state.

This direction remains future scope and does not authorize dashboard design or implementation.
