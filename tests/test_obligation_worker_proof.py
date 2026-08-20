import json
import tempfile
import unittest
from pathlib import Path

from scripts import obligation_worker_proof as worker


BASE_LEDGER = """# Road Warrior Obligations

Authoritative Prototype 1 obligation ledger. Road Warrior maintains this ledger for Bruce.

## RW-OB-EXISTING-001

- Status: Open
- Obligation: Preserve this unrelated obligation.
- Context: Existing test fixture.
- Timing: Untimed
- External surfacing: None
"""


def state_for(ledger: str, revision: str = "revision-1", modified: str = "2026-08-18T20:00:00Z"):
    return {
        "resource_id": worker.TARGET_RESOURCE_ID,
        "title": "ROAD_WARRIOR_OBLIGATIONS.md",
        "mime_type": "text/markdown",
        "revision_id": revision,
        "modified_time": modified,
        "content_sha256": worker.sha256(ledger),
    }


def envelope_for(ledger: str, state: dict, operation: str = "create"):
    terminal = operation == "terminalize"
    return {
        "contract_version": "1.0",
        "transaction_id": "rw-owp-test-terminal" if terminal else "rw-owp-test-create",
        "idempotency_key": "rw-owp-test-terminal-v1" if terminal else "rw-owp-test-create-v1",
        "intent_type": "terminalize_test_obligation" if terminal else "record_untimed_obligation",
        "accepted_responsibility": "Governed Obligation Worker proof — disposable test obligation.",
        "authority": {
            "authorized_by": "Bruce/ChatGPT",
            "scope": "One controlled ledger-only Obligation Worker proof.",
        },
        "operations": [worker.TERMINAL_SIDE_EFFECT if terminal else worker.CREATE_SIDE_EFFECT],
        "payload": {
            "obligation_text": "Governed Obligation Worker proof — disposable test obligation.",
            "context": "Road Warrior V1.5 — controlled ledger-only proof.",
            "timing": "untimed",
            "target_record_id": "RW-OB-TEST-001",
        },
        "resource_ids": {
            "obligation_ledger": worker.TARGET_RESOURCE_ID,
            "obligation_record": "RW-OB-TEST-001",
        },
        "operation": operation,
        "obligation_text": "Governed Obligation Worker proof — disposable test obligation.",
        "context": "Road Warrior V1.5 — controlled ledger-only proof.",
        "timing": "untimed",
        "target_resource_id": worker.TARGET_RESOURCE_ID,
        "target_record_id": "RW-OB-TEST-001",
        "allowed_side_effects": [worker.TERMINAL_SIDE_EFFECT if terminal else worker.CREATE_SIDE_EFFECT],
        "forbidden_actions": sorted(worker.REQUIRED_FORBIDDEN_ACTIONS),
        "completion_condition": "Exact record and idempotency marker verified by authoritative readback.",
        "required_verification_evidence": [
            "stable_resource_id",
            "exact_record_once",
            "transaction_marker_once",
            "idempotency_marker_once",
            "unrelated_content_preserved",
        ],
        "expiry": "2099-08-19T00:00:00Z",
        "retry_policy": {"max_retries": 0, "retryable_errors": []},
        "closure_policy": {"decision_owner": "Road Warrior", "worker_may_communicate": False},
        "preconditions": {
            "content_sha256": worker.sha256(ledger),
            "revision_id": state["revision_id"],
            "modified_time": state["modified_time"],
        },
        "captured_at": "2026-08-18T15:00:00-07:00",
    }


class WorkerHarness:
    def __init__(self, root: Path):
        self.root = root

    def path(self, name: str) -> Path:
        return self.root / name

    def write_text(self, name: str, value: str) -> Path:
        path = self.path(name)
        worker.write_text(path, value)
        return path

    def write_json(self, name: str, value: dict) -> Path:
        path = self.path(name)
        worker.write_json(path, value)
        return path

    def prepare(self, envelope: dict, ledger: str, state: dict, prefix: str, ambiguous: bool = False):
        args = type("Args", (), {})()
        args.envelope = self.write_json(f"{prefix}-envelope.json", envelope)
        args.ledger = self.write_text(f"{prefix}-ledger.md", ledger)
        args.state = self.write_json(f"{prefix}-state.json", state)
        args.candidate = self.path(f"{prefix}-candidate.md")
        args.proposal = self.path(f"{prefix}-proposal.json")
        args.result = self.path(f"{prefix}-result.json")
        worker.prepare(args, ambiguous=ambiguous)
        return worker.read_json(args.result), args


class ObligationWorkerProofTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path.cwd())
        self.root = Path(self.temp.name)
        self.harness = WorkerHarness(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_a_valid_new_transaction_and_readback_verification(self):
        state = state_for(BASE_LEDGER)
        envelope = envelope_for(BASE_LEDGER, state)
        prepared, args = self.harness.prepare(envelope, BASE_LEDGER, state, "a")
        self.assertEqual("prepared", prepared["status"])
        candidate = worker.read_text(args.candidate)
        self.assertEqual(1, candidate.count("## RW-OB-TEST-001"))
        after_state = state_for(candidate, revision="revision-2", modified="2026-08-18T20:01:00Z")
        verify_args = type("Args", (), {})()
        verify_args.envelope = args.envelope
        verify_args.before = args.ledger
        verify_args.after = self.harness.write_text("a-after.md", candidate)
        verify_args.before_state = args.state
        verify_args.after_state = self.harness.write_json("a-after-state.json", after_state)
        verify_args.proposal = args.proposal
        verify_args.result = self.harness.path("a-verify.json")
        worker.verify(verify_args)
        verified = worker.read_json(verify_args.result)
        self.assertEqual("succeeded", verified["status"])
        self.assertTrue(verified["verification_evidence"]["unrelated_content_preserved"])

    def test_b_duplicate_delivery_is_idempotent(self):
        state = state_for(BASE_LEDGER)
        envelope = envelope_for(BASE_LEDGER, state)
        _, args = self.harness.prepare(envelope, BASE_LEDGER, state, "b-first")
        candidate = worker.read_text(args.candidate)
        current_state = state_for(candidate, revision="revision-2", modified="2026-08-18T20:01:00Z")
        duplicate, duplicate_args = self.harness.prepare(envelope, candidate, current_state, "b-duplicate")
        self.assertEqual("already_applied", duplicate["status"])
        self.assertFalse(duplicate_args.candidate.exists())
        self.assertEqual(1, candidate.count("- Idempotency key: rw-owp-test-create-v1"))
        self.assertEqual(1, duplicate["verification_evidence"]["transaction_marker_count"])

    def test_c_missing_material_field_requires_judgment_and_writes_nothing(self):
        state = state_for(BASE_LEDGER)
        envelope = envelope_for(BASE_LEDGER, state)
        del envelope["obligation_text"]
        result, args = self.harness.prepare(envelope, BASE_LEDGER, state, "c")
        self.assertEqual("blocked", result["status"])
        self.assertTrue(result["requires_judgment"])
        self.assertEqual("MISSING_MATERIAL_FIELD", result["typed_error"]["code"])
        self.assertFalse(args.candidate.exists())

    def test_d_stale_state_blocks_without_candidate(self):
        state = state_for(BASE_LEDGER)
        envelope = envelope_for(BASE_LEDGER, state)
        changed = BASE_LEDGER + "\nUnrelated concurrent content.\n"
        changed_state = state_for(changed, revision="revision-2", modified="2026-08-18T20:01:00Z")
        result, args = self.harness.prepare(envelope, changed, changed_state, "d")
        self.assertEqual("blocked", result["status"])
        self.assertEqual("STALE_STATE", result["typed_error"]["code"])
        self.assertFalse(args.candidate.exists())

    def test_e_ambiguous_outcome_reads_before_retry_and_does_not_duplicate(self):
        state = state_for(BASE_LEDGER)
        envelope = envelope_for(BASE_LEDGER, state)
        _, args = self.harness.prepare(envelope, BASE_LEDGER, state, "e-first")
        candidate = worker.read_text(args.candidate)
        current_state = state_for(candidate, revision="revision-2", modified="2026-08-18T20:01:00Z")
        result, reconcile_args = self.harness.prepare(envelope, candidate, current_state, "e-reconcile", ambiguous=True)
        self.assertEqual("already_applied_after_ambiguous_outcome", result["status"])
        self.assertFalse(result["verification_evidence"]["retry_performed"])
        self.assertFalse(reconcile_args.candidate.exists())
        self.assertEqual(1, candidate.count("## RW-OB-TEST-001"))

    def test_f_terminal_transition_preserves_history(self):
        initial_state = state_for(BASE_LEDGER)
        create_envelope = envelope_for(BASE_LEDGER, initial_state)
        _, create_args = self.harness.prepare(create_envelope, BASE_LEDGER, initial_state, "f-create")
        open_ledger = worker.read_text(create_args.candidate)
        open_state = state_for(open_ledger, revision="revision-2", modified="2026-08-18T20:01:00Z")
        terminal_envelope = envelope_for(open_ledger, open_state, operation="terminalize")
        prepared, terminal_args = self.harness.prepare(terminal_envelope, open_ledger, open_state, "f-terminal")
        self.assertEqual("prepared", prepared["status"])
        terminal_ledger = worker.read_text(terminal_args.candidate)
        self.assertIn("- Status: Canceled (Test-Only)", terminal_ledger)
        self.assertIn("- Terminal idempotency key: rw-owp-test-terminal-v1", terminal_ledger)
        self.assertIn("- Idempotency key: rw-owp-test-create-v1", terminal_ledger)
        self.assertIn("Preserve this unrelated obligation.", terminal_ledger)
        after_state = state_for(terminal_ledger, revision="revision-3", modified="2026-08-18T20:02:00Z")
        verify_args = type("Args", (), {})()
        verify_args.envelope = terminal_args.envelope
        verify_args.before = terminal_args.ledger
        verify_args.after = self.harness.write_text("f-after.md", terminal_ledger)
        verify_args.before_state = terminal_args.state
        verify_args.after_state = self.harness.write_json("f-after-state.json", after_state)
        verify_args.proposal = terminal_args.proposal
        verify_args.result = self.harness.path("f-verify.json")
        worker.verify(verify_args)
        verified = worker.read_json(verify_args.result)
        self.assertEqual("succeeded", verified["status"])
        self.assertTrue(verified["verification_evidence"]["unrelated_content_preserved"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
