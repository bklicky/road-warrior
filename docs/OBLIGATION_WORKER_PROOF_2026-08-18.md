# Obligation Worker Proof — 2026-08-18

- Status: COMPLETE — bounded synchronous ledger-only transaction-safety proof
- Authorization: Bruce/ChatGPT explicitly authorized this proof only on 2026-08-18
- Authoritative target: Drive `ROAD_WARRIOR_OBLIGATIONS.md`
- Stable Drive ID: `1sy1jB1MECL-DTDdd4s7Q7K2_cgTnWT94`
- Implementation: `scripts/obligation_worker_proof.py`
- Automated cases: `tests/test_obligation_worker_proof.py`

## Scope and Design

Road Warrior supplied one already-judged untimed test obligation. A dependency-free deterministic Python core validated the envelope, refused out-of-scope or stale work, detected prior application, produced one exact candidate mutation, reconciled ambiguous outcomes from authoritative state, and verified an independent readback. The live environment adapter performed fresh Drive retrieval, revision retrieval, the one in-place file update, and independent readback. No LLM or subagent participated in transaction logic.

The proof used one controlled writer. It did not touch Calendar, Gmail, handoffs, Scheduled Tasks, Personal OS, a queue, a service, a daemon, a VPS, or any other ledger. The raw Drive file was updated in place; its ID remained unchanged.

## Final Implemented Create Transaction Envelope

```json
{
  "contract_version": "1.0",
  "transaction_id": "rw-owp-20260818-001-create",
  "idempotency_key": "rw-owp-20260818-001-create-v1",
  "intent_type": "record_untimed_obligation",
  "accepted_responsibility": "Governed Obligation Worker proof — disposable test obligation.",
  "authority": {
    "authorized_by": "Bruce/ChatGPT",
    "scope": "One controlled ledger-only Obligation Worker proof."
  },
  "operations": ["append_exact_obligation_record"],
  "payload": {
    "obligation_text": "Governed Obligation Worker proof — disposable test obligation.",
    "context": "Road Warrior V1.5 — controlled ledger-only Obligation Worker proof; disposable, no real-world consequence, and no Calendar action.",
    "timing": "untimed",
    "target_record_id": "RW-OB-20260818-006"
  },
  "resource_ids": {
    "obligation_ledger": "1sy1jB1MECL-DTDdd4s7Q7K2_cgTnWT94",
    "obligation_record": "RW-OB-20260818-006"
  },
  "operation": "create",
  "obligation_text": "Governed Obligation Worker proof — disposable test obligation.",
  "context": "Road Warrior V1.5 — controlled ledger-only Obligation Worker proof; disposable, no real-world consequence, and no Calendar action.",
  "timing": "untimed",
  "target_resource_id": "1sy1jB1MECL-DTDdd4s7Q7K2_cgTnWT94",
  "target_record_id": "RW-OB-20260818-006",
  "allowed_side_effects": ["append_exact_obligation_record"],
  "forbidden_actions": [
    "calendar_write",
    "delete_ledger_record",
    "gmail_write",
    "governance_change",
    "handoff_write",
    "human_communication",
    "modify_unrelated_content",
    "priority_change",
    "scheduled_task_write"
  ],
  "completion_condition": "The exact test record, stable Drive identity, create transaction ID, idempotency marker, and unchanged unrelated content are independently verified from the authoritative ledger.",
  "required_verification_evidence": [
    "stable_resource_id",
    "exact_record_once",
    "transaction_marker_once",
    "idempotency_marker_once",
    "unrelated_content_preserved"
  ],
  "expiry": "2026-08-19T00:00:00-07:00",
  "retry_policy": {"max_retries": 0, "retryable_errors": []},
  "closure_policy": {"decision_owner": "Road Warrior", "worker_may_communicate": false},
  "preconditions": {
    "content_sha256": "1eebdaa49c4d2c02151d1a1ab395bac4d56c071b90895ff5f70b44ff596551ba",
    "modified_time": "2026-08-18T20:12:49.283Z",
    "revision_id": "0B7fDT2CH5h_May9wYWR6SEI4N0QxcmgvSzRka2Exb01WYklvPQ"
  },
  "captured_at": "2026-08-18T15:29:51-07:00"
}
```

The initial live mutation encoded the task-specific values in this envelope but did not yet expose every generic canonical field by its final name. Final contract crosswalk made `accepted_responsibility`, `authority`, `operations`, `payload`, `resource_ids`, `expiry`, `retry_policy`, and `closure_policy` explicit and enforceable without changing mutation semantics. The complete envelope above was then re-delivered non-mutatingly against a fresh final authoritative snapshot: contract validation passed, the result was `already_applied`, transaction and idempotency marker counts were one, and no candidate or write was produced. The complete named-field new-transaction path is covered by the deterministic case A; no second live test record was created.

The terminal transaction used the same bounded shape with `operation: terminalize`, intent `terminalize_test_obligation`, transaction `rw-owp-20260818-001-terminal`, idempotency key `rw-owp-20260818-001-terminal-v1`, the then-current content/revision/modified-time preconditions, and only `transition_exact_test_record_to_terminal` allowed.

## Observed Cases

| Case | Observed result |
| --- | --- |
| A — valid new transaction | `succeeded`. `RW-OB-20260818-006` appeared exactly once with the exact obligation, transaction, and idempotency markers. Stable Drive ID, exact candidate hash, and unrelated content were independently verified. Content hash changed from `1eebdaa49c4d2c02151d1a1ab395bac4d56c071b90895ff5f70b44ff596551ba` to `e4acdbcf3eabc02d69cb056f1a48e2917c4a7d1a68a9f66a9bbca93b50a76c64`; revision changed to `0B7fDT2CH5h_MWDVPOU15UTF1TFZGK2dhbnRObnY4RHpHdW84PQ`. |
| B — duplicate delivery | `already_applied`. The same transaction and idempotency key produced no candidate or write; record, transaction marker, and idempotency marker counts remained one. |
| C — missing material field | `blocked`, typed error `MISSING_MATERIAL_FIELD`, `requires_judgment: true`; no candidate and no write. |
| D — stale/concurrency conflict | `blocked`, typed error `STALE_STATE`; mismatched content hash, revision, and modified time were reported; no candidate and no write. |
| E — ambiguous write outcome | After simulating an uncertain response for the already-applied create, authoritative reconciliation returned `already_applied_after_ambiguous_outcome`, `retry_performed: false`, and no duplicate. |
| F — terminal cleanup | `succeeded`. The record transitioned to `Canceled (Test-Only)` without deletion; original create markers and new terminal markers remain. Final hash `48c6428590096530f7ce0b96db6c7df7737c5723d26b190fd5bd367296856e77`; final revision `0B7fDT2CH5h_MWENjRlVoOU8zYk5BK3lja1hZQ04xSk9iTVY0PQ`; unrelated before/after hash matched at `8f750764bd433510599d4aca1acf71aeaeb7b5ed0604bfb082f43bab0d55d511`. |

Every structured result contains status, transaction and idempotency identifiers, target resource ID, observed before/after state where available, per-step results, verification evidence, retry count, typed error, `requires_judgment`, and a nullable user-notification field whose decision owner is explicitly Road Warrior. The worker generated no Bruce-facing prose.

## Concurrency, Idempotency, and Write Safety

The create and terminal paths each used a fresh authoritative content read plus Drive revision and modified time, incorporated SHA-256/revision/modified-time preconditions into the immutable transaction, and repeated the authoritative read immediately before the one in-place update. Any mismatch blocks preparation. The candidate is derived only from that exact snapshot, and independent readback must match the exact candidate hash, stable Drive ID, one record, one transaction marker, one idempotency marker, and unchanged unrelated content.

Drive's raw-file update connector does not expose an atomic compare-and-swap or `If-Match` condition. Therefore this proof establishes sufficient protection only for its explicitly controlled single-writer scope. A narrow time-of-check/time-of-use window remains, and multi-writer or production use must not be authorized without atomic concurrency control or an equivalent lock/serialization mechanism.

Idempotency is durable in the authoritative record. Re-delivery checks the operation-specific idempotency key, matching transaction marker, record ID, and exact obligation before any stale-state or write path. An ambiguous result always reads authoritative state first and never blindly retries.

## Timing

- Create mutation connector call: 2.637 seconds.
- Create mutation plus authoritative readback: 3.507 seconds.
- Terminal mutation connector call: 4.922 seconds.
- Terminal mutation plus authoritative readback: 5.867 seconds.
- Six local deterministic regression cases: 0.225 seconds in the final complete run (0.240 seconds in the first complete run).

These are synchronous transaction-path measurements, not acknowledgment latency. The proof core and live Drive adapter were orchestrated interactively rather than through a dispatcher, so no end-to-end durable-dispatch latency was measured.

## Limits and Non-Claims

This result proves the bounded worker contract and ledger transaction-safety behaviors under a controlled single-writer test. It does not prove or authorize production use, detached/background execution, durable dispatch, a one-to-two-second conversational acknowledgment, Calendar surfacing, queue infrastructure, orchestration, multi-agent behavior, Personal OS integration, deployment, or any additional worker. The synchronous Drive write/readback measurements exceed the acknowledgment target, so this proof cannot itself deliver Attention Continuity before a real durable-dispatch mechanism exists.
