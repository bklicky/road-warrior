#!/usr/bin/env python3
"""Deterministic V1.5 Obligation Worker proof.

This worker never interprets user language and never calls Google Drive itself.
It validates an already-judged envelope, prepares one exact ledger mutation from
a fresh adapter-provided snapshot, and verifies an independent readback.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CONTRACT_VERSION = "1.0"
TARGET_RESOURCE_ID = "1sy1jB1MECL-DTDdd4s7Q7K2_cgTnWT94"
REQUIRED_FORBIDDEN_ACTIONS = {
    "calendar_write",
    "gmail_write",
    "scheduled_task_write",
    "handoff_write",
    "delete_ledger_record",
    "modify_unrelated_content",
    "human_communication",
    "priority_change",
    "governance_change",
}
CREATE_SIDE_EFFECT = "append_exact_obligation_record"
TERMINAL_SIDE_EFFECT = "transition_exact_test_record_to_terminal"
REQUIRED_VERIFICATION_EVIDENCE = {
    "stable_resource_id",
    "exact_record_once",
    "transaction_marker_once",
    "idempotency_marker_once",
    "unrelated_content_preserved",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(value)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


def write_json(path: Path, value: dict[str, Any]) -> None:
    write_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def marker_count(ledger: str, label: str, value: str) -> int:
    return ledger.count(f"- {label}: {value}")


def record_span(ledger: str, record_id: str) -> tuple[int, int, str] | None:
    pattern = re.compile(
        rf"(?m)^## {re.escape(record_id)}\r?\n(?P<body>.*?)(?=^## |\Z)",
        re.DOTALL,
    )
    match = pattern.search(ledger)
    if not match:
        return None
    return match.start(), match.end(), match.group(0)


def base_result(envelope: dict[str, Any], state: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "status": "failed",
        "transaction_id": envelope.get("transaction_id"),
        "idempotency_key": envelope.get("idempotency_key"),
        "target_resource_id": envelope.get("target_resource_id"),
        "before_state": state,
        "after_state": None,
        "per_step_result": [],
        "verification_evidence": {},
        "retry_count": 0,
        "typed_error": None,
        "requires_judgment": False,
        "user_facing_notification_required": None,
        "notification_decision_owner": "Road Warrior",
        "worker_generated_user_prose": False,
        "recorded_at": utc_now(),
    }


def add_step(result: dict[str, Any], step: str, status: str, evidence: Any = None) -> None:
    item: dict[str, Any] = {"step": step, "status": status}
    if evidence is not None:
        item["evidence"] = evidence
    result["per_step_result"].append(item)


def fail(
    result: dict[str, Any],
    code: str,
    message: str,
    *,
    status: str = "blocked",
    requires_judgment: bool = False,
    retryable: bool = False,
) -> dict[str, Any]:
    result["status"] = status
    result["typed_error"] = {"code": code, "message": message, "retryable": retryable}
    result["requires_judgment"] = requires_judgment
    add_step(result, "refuse_mutation", "passed", code)
    return result


def validate_envelope(envelope: dict[str, Any]) -> list[str]:
    required = [
        "contract_version",
        "transaction_id",
        "idempotency_key",
        "intent_type",
        "accepted_responsibility",
        "authority",
        "operations",
        "payload",
        "resource_ids",
        "operation",
        "obligation_text",
        "context",
        "timing",
        "target_resource_id",
        "target_record_id",
        "allowed_side_effects",
        "forbidden_actions",
        "completion_condition",
        "required_verification_evidence",
        "expiry",
        "retry_policy",
        "closure_policy",
        "preconditions",
        "captured_at",
    ]
    missing = [name for name in required if name not in envelope or envelope[name] in (None, "", [])]
    preconditions = envelope.get("preconditions")
    if isinstance(preconditions, dict):
        for name in ("content_sha256", "revision_id", "modified_time"):
            if preconditions.get(name) in (None, ""):
                missing.append(f"preconditions.{name}")
    else:
        missing.append("preconditions")
    return sorted(set(missing))


def validate_contract(envelope: dict[str, Any], state: dict[str, Any], result: dict[str, Any]) -> dict[str, Any] | None:
    missing = validate_envelope(envelope)
    if missing:
        return fail(
            result,
            "MISSING_MATERIAL_FIELD",
            "Missing material field(s): " + ", ".join(missing),
            requires_judgment=True,
        )
    if envelope["contract_version"] != CONTRACT_VERSION:
        return fail(result, "UNSUPPORTED_CONTRACT_VERSION", "Only contract version 1.0 is supported.")
    if envelope["target_resource_id"] != TARGET_RESOURCE_ID:
        return fail(result, "TARGET_NOT_AUTHORIZED", "The transaction targets an unauthorized resource.")
    if state.get("resource_id") != TARGET_RESOURCE_ID:
        return fail(result, "STABLE_ID_MISMATCH", "The adapter snapshot is not the authoritative ledger.")
    if envelope["timing"].lower() != "untimed":
        return fail(result, "TIMED_OBLIGATION_FORBIDDEN", "This proof accepts untimed obligations only.")
    if not REQUIRED_FORBIDDEN_ACTIONS.issubset(set(envelope["forbidden_actions"])):
        return fail(result, "FORBIDDEN_ACTION_BOUNDARY_INCOMPLETE", "The transaction omits required forbidden actions.")
    operation = envelope["operation"]
    if operation not in {"create", "terminalize"}:
        return fail(result, "OPERATION_NOT_AUTHORIZED", "Only create and terminalize are supported by this proof.")
    expected_side_effect = CREATE_SIDE_EFFECT if operation == "create" else TERMINAL_SIDE_EFFECT
    if envelope["allowed_side_effects"] != [expected_side_effect]:
        return fail(result, "SIDE_EFFECT_SCOPE_MISMATCH", "Allowed side effects are not the exact proof operation.")
    if envelope["operations"] != [expected_side_effect]:
        return fail(result, "OPERATION_SCOPE_MISMATCH", "Ordered operations are not the exact proof operation.")
    if envelope["accepted_responsibility"] != envelope["obligation_text"]:
        return fail(result, "RESPONSIBILITY_MISMATCH", "Accepted responsibility differs from the exact obligation.")
    expected_payload = {
        "obligation_text": envelope["obligation_text"],
        "context": envelope["context"],
        "timing": envelope["timing"],
        "target_record_id": envelope["target_record_id"],
    }
    if envelope["payload"] != expected_payload:
        return fail(result, "PAYLOAD_MISMATCH", "Payload is not the exact resolved proof payload.")
    if envelope["resource_ids"] != {
        "obligation_ledger": TARGET_RESOURCE_ID,
        "obligation_record": envelope["target_record_id"],
    }:
        return fail(result, "RESOURCE_SCOPE_MISMATCH", "Resource IDs are not the exact authorized targets.")
    authority = envelope["authority"]
    if not isinstance(authority, dict) or authority.get("authorized_by") != "Bruce/ChatGPT" or not authority.get("scope"):
        return fail(result, "AUTHORITY_INVALID", "Proof authority is absent or outside the approved source.", requires_judgment=True)
    if envelope["retry_policy"] != {"max_retries": 0, "retryable_errors": []}:
        return fail(result, "RETRY_POLICY_MISMATCH", "This proof permits no automatic retries.")
    if envelope["closure_policy"] != {"decision_owner": "Road Warrior", "worker_may_communicate": False}:
        return fail(result, "CLOSURE_POLICY_MISMATCH", "Road Warrior must retain all human-facing closure authority.")
    try:
        expiry = datetime.fromisoformat(envelope["expiry"].replace("Z", "+00:00"))
        if expiry.tzinfo is None or expiry.astimezone(timezone.utc) <= datetime.now(timezone.utc):
            raise ValueError("expired")
    except (TypeError, ValueError):
        return fail(result, "TRANSACTION_EXPIRED", "Transaction expiry is invalid or has passed.", requires_judgment=True)
    if not REQUIRED_VERIFICATION_EVIDENCE.issubset(set(envelope["required_verification_evidence"])):
        return fail(result, "VERIFICATION_BOUNDARY_INCOMPLETE", "The transaction omits required verification evidence.")
    expected_intent = "record_untimed_obligation" if operation == "create" else "terminalize_test_obligation"
    if envelope["intent_type"] != expected_intent:
        return fail(result, "INTENT_TYPE_MISMATCH", "Intent type does not match the exact operation.")
    add_step(result, "validate_contract", "passed")
    return None


def state_with_hash(state: dict[str, Any], ledger: str) -> dict[str, Any]:
    value = dict(state)
    value["content_sha256"] = sha256(ledger)
    return value


def check_preconditions(envelope: dict[str, Any], state: dict[str, Any], ledger: str, result: dict[str, Any]) -> dict[str, Any] | None:
    observed = state_with_hash(state, ledger)
    result["before_state"] = observed
    expected = envelope["preconditions"]
    mismatches = {
        name: {"expected": expected[name], "observed": observed.get(name)}
        for name in ("content_sha256", "revision_id", "modified_time")
        if expected[name] != observed.get(name)
    }
    if mismatches:
        result["verification_evidence"]["precondition_mismatches"] = mismatches
        return fail(result, "STALE_STATE", "Authoritative state changed after judgment; re-read before any write.")
    add_step(result, "validate_preconditions", "passed", observed)
    return None


def build_create_record(envelope: dict[str, Any]) -> str:
    return (
        f"## {envelope['target_record_id']}\n\n"
        "- Status: Open (Test-Only)\n"
        f"- Obligation: {envelope['obligation_text']}\n"
        f"- Context: {envelope['context']}\n"
        "- Timing: Untimed\n"
        "- External surfacing: None; Calendar explicitly forbidden for this proof.\n"
        f"- Captured: {envelope['captured_at']} — controlled governed-worker proof authorized by Bruce/ChatGPT.\n"
        f"- Transaction ID: {envelope['transaction_id']}\n"
        f"- Idempotency key: {envelope['idempotency_key']}\n"
        "- Test scope: Disposable audit evidence; retain and transition to a terminal test status.\n"
    )


def append_record(ledger: str, record: str) -> tuple[str, str]:
    separator = "" if ledger.endswith("\n\n") else "\n" if ledger.endswith("\n") else "\n\n"
    patch = separator + record
    return ledger + patch, patch


def build_terminal_candidate(envelope: dict[str, Any], ledger: str) -> tuple[str, str, str] | None:
    span = record_span(ledger, envelope["target_record_id"])
    if span is None:
        return None
    start, end, record = span
    expected_status = "- Status: Open (Test-Only)"
    if record.count(expected_status) != 1:
        return None
    terminal_lines = (
        f"- Terminalized: {envelope['captured_at']} — controlled proof cleanup; historical evidence retained.\n"
        f"- Terminal transaction ID: {envelope['transaction_id']}\n"
        f"- Terminal idempotency key: {envelope['idempotency_key']}\n"
    )
    updated_record = record.replace(expected_status, "- Status: Canceled (Test-Only)", 1)
    updated_record = updated_record.rstrip("\r\n") + "\n" + terminal_lines
    candidate = ledger[:start] + updated_record + ledger[end:]
    return candidate, record, updated_record


def idempotency_status(envelope: dict[str, Any], ledger: str, result: dict[str, Any], ambiguous: bool) -> dict[str, Any] | None:
    operation = envelope.get("operation")
    label = "Idempotency key" if operation == "create" else "Terminal idempotency key"
    transaction_label = "Transaction ID" if operation == "create" else "Terminal transaction ID"
    count = marker_count(ledger, label, str(envelope.get("idempotency_key")))
    if count == 0:
        return None
    if count != 1:
        return fail(result, "IDEMPOTENCY_MARKER_CONFLICT", "Idempotency marker is not unique.", requires_judgment=True)
    span = record_span(ledger, str(envelope.get("target_record_id")))
    if span is None or f"- Obligation: {envelope.get('obligation_text')}" not in span[2]:
        return fail(result, "IDEMPOTENCY_KEY_CONFLICT", "Idempotency key exists on a conflicting record.", requires_judgment=True)
    transaction_count = marker_count(ledger, transaction_label, str(envelope.get("transaction_id")))
    if transaction_count != 1 or f"- {transaction_label}: {envelope.get('transaction_id')}" not in span[2]:
        return fail(result, "IDEMPOTENCY_KEY_CONFLICT", "Idempotency key exists with a conflicting transaction marker.", requires_judgment=True)
    status = "already_applied_after_ambiguous_outcome" if ambiguous else "already_applied"
    result["status"] = status
    result["verification_evidence"] = {
        "record_id": envelope["target_record_id"],
        "record_count": ledger.count(f"## {envelope['target_record_id']}"),
        "idempotency_marker_count": count,
        "transaction_marker_count": transaction_count,
        "authoritative_content_sha256": sha256(ledger),
        "retry_performed": False,
    }
    add_step(result, "check_idempotency", "passed", status)
    return result


def prepare(args: argparse.Namespace, *, ambiguous: bool = False) -> int:
    envelope = read_json(args.envelope)
    state = read_json(args.state)
    ledger = read_text(args.ledger)
    result = base_result(envelope, state_with_hash(state, ledger))
    for path in (args.candidate, args.proposal):
        if path.exists():
            path.unlink()

    contract_failure = validate_contract(envelope, state, result)
    if contract_failure:
        write_json(args.result, contract_failure)
        return 0

    applied = idempotency_status(envelope, ledger, result, ambiguous)
    if applied:
        write_json(args.result, applied)
        return 0

    if ambiguous:
        outcome = fail(
            result,
            "AMBIGUOUS_OUTCOME_UNRESOLVED",
            "Authoritative readback does not show the transaction; retry is prohibited pending Road Warrior judgment.",
            status="outcome_unknown",
            requires_judgment=True,
        )
        outcome["verification_evidence"]["retry_performed"] = False
        write_json(args.result, outcome)
        return 0

    stale = check_preconditions(envelope, state, ledger, result)
    if stale:
        write_json(args.result, stale)
        return 0

    operation = envelope["operation"]
    if operation == "create":
        if record_span(ledger, envelope["target_record_id"]):
            output = fail(result, "RECORD_ID_CONFLICT", "Target record ID already exists.", requires_judgment=True)
            write_json(args.result, output)
            return 0
        record = build_create_record(envelope)
        candidate, patch = append_record(ledger, record)
        proposal_extra = {"authorized_patch": patch, "before_record": None, "after_record": record}
    else:
        terminal = build_terminal_candidate(envelope, ledger)
        if terminal is None:
            output = fail(result, "TERMINAL_PRECONDITION_FAILED", "Exact open test record is unavailable.", requires_judgment=True)
            write_json(args.result, output)
            return 0
        candidate, before_record, after_record = terminal
        proposal_extra = {"authorized_patch": None, "before_record": before_record, "after_record": after_record}

    proposal = {
        "operation": operation,
        "write_required": True,
        "transaction_id": envelope["transaction_id"],
        "idempotency_key": envelope["idempotency_key"],
        "target_resource_id": TARGET_RESOURCE_ID,
        "target_record_id": envelope["target_record_id"],
        "before_content_sha256": sha256(ledger),
        "candidate_content_sha256": sha256(candidate),
        "before_state": state_with_hash(state, ledger),
        **proposal_extra,
    }
    write_text(args.candidate, candidate)
    write_json(args.proposal, proposal)
    result["status"] = "prepared"
    result["verification_evidence"] = {
        "candidate_content_sha256": proposal["candidate_content_sha256"],
        "authorized_record_id": envelope["target_record_id"],
        "write_required": True,
    }
    add_step(result, "check_idempotency", "passed", "not_applied")
    add_step(result, "prepare_exact_mutation", "passed", proposal["candidate_content_sha256"])
    write_json(args.result, result)
    return 0


def verify(args: argparse.Namespace) -> int:
    envelope = read_json(args.envelope)
    before_state = read_json(args.before_state)
    after_state_raw = read_json(args.after_state)
    proposal = read_json(args.proposal)
    before = read_text(args.before)
    after = read_text(args.after)
    result = base_result(envelope, state_with_hash(before_state, before))
    after_state = state_with_hash(after_state_raw, after)
    result["after_state"] = after_state
    errors: list[str] = []

    if before_state.get("resource_id") != TARGET_RESOURCE_ID or after_state_raw.get("resource_id") != TARGET_RESOURCE_ID:
        errors.append("stable target identity changed")
    if sha256(before) != proposal["before_content_sha256"]:
        errors.append("before content does not match proposal")
    if sha256(after) != proposal["candidate_content_sha256"]:
        errors.append("after content does not match exact candidate")

    before_span = record_span(before, envelope["target_record_id"])
    after_span = record_span(after, envelope["target_record_id"])
    if after_span is None:
        errors.append("target record missing")
    else:
        if after.count(f"## {envelope['target_record_id']}") != 1:
            errors.append("target record is not unique")
        label = "Idempotency key" if envelope["operation"] == "create" else "Terminal idempotency key"
        transaction_label = "Transaction ID" if envelope["operation"] == "create" else "Terminal transaction ID"
        if marker_count(after, label, envelope["idempotency_key"]) != 1:
            errors.append("idempotency marker is not unique")
        if marker_count(after, transaction_label, envelope["transaction_id"]) != 1:
            errors.append("transaction marker is not unique")
        if f"- Obligation: {envelope['obligation_text']}" not in after_span[2]:
            errors.append("exact obligation text missing")

    if envelope["operation"] == "create":
        patch = proposal["authorized_patch"]
        if after != before + patch:
            errors.append("content outside the exact append changed")
        unrelated_before = before
        unrelated_after = after[: len(before)] if after.startswith(before) else ""
    else:
        if before_span is None or after_span is None:
            errors.append("terminal record boundary unavailable")
            unrelated_before = before
            unrelated_after = after
        else:
            unrelated_before = before[: before_span[0]] + before[before_span[1] :]
            unrelated_after = after[: after_span[0]] + after[after_span[1] :]
            if after_span[2] != proposal["after_record"]:
                errors.append("terminal record differs from exact proposal")
            if "- Status: Canceled (Test-Only)" not in after_span[2]:
                errors.append("terminal test status missing")
    unrelated_preserved = unrelated_before == unrelated_after
    if not unrelated_preserved:
        errors.append("unrelated ledger content changed")

    result["verification_evidence"] = {
        "stable_resource_id_preserved": after_state_raw.get("resource_id") == TARGET_RESOURCE_ID,
        "exact_record_exists_once": after.count(f"## {envelope['target_record_id']}") == 1,
        "exact_obligation_text_present": f"- Obligation: {envelope['obligation_text']}" in after,
        "idempotency_marker_present_once": marker_count(
            after,
            "Idempotency key" if envelope["operation"] == "create" else "Terminal idempotency key",
            envelope["idempotency_key"],
        )
        == 1,
        "transaction_marker_present_once": marker_count(
            after,
            "Transaction ID" if envelope["operation"] == "create" else "Terminal transaction ID",
            envelope["transaction_id"],
        )
        == 1,
        "unrelated_content_preserved": unrelated_preserved,
        "unrelated_before_sha256": sha256(unrelated_before),
        "unrelated_after_sha256": sha256(unrelated_after),
        "candidate_sha256_verified": sha256(after) == proposal["candidate_content_sha256"],
        "before_revision_id": before_state.get("revision_id"),
        "after_revision_id": after_state_raw.get("revision_id"),
    }
    if errors:
        output = fail(
            result,
            "READBACK_VERIFICATION_FAILED",
            "; ".join(errors),
            status="outcome_unknown",
            requires_judgment=True,
        )
        write_json(args.result, output)
        return 0

    result["status"] = "succeeded"
    add_step(result, "verify_stable_identity", "passed", TARGET_RESOURCE_ID)
    add_step(result, "verify_exact_record", "passed", envelope["target_record_id"])
    add_step(result, "verify_unrelated_content", "passed", sha256(unrelated_before))
    add_step(result, "verify_idempotency_marker", "passed", envelope["idempotency_key"])
    add_step(result, "verify_transaction_marker", "passed", envelope["transaction_id"])
    write_json(args.result, result)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "reconcile"):
        command = subparsers.add_parser(name)
        command.add_argument("--envelope", type=Path, required=True)
        command.add_argument("--ledger", type=Path, required=True)
        command.add_argument("--state", type=Path, required=True)
        command.add_argument("--candidate", type=Path, required=True)
        command.add_argument("--proposal", type=Path, required=True)
        command.add_argument("--result", type=Path, required=True)

    command = subparsers.add_parser("verify")
    command.add_argument("--envelope", type=Path, required=True)
    command.add_argument("--before", type=Path, required=True)
    command.add_argument("--after", type=Path, required=True)
    command.add_argument("--before-state", type=Path, required=True)
    command.add_argument("--after-state", type=Path, required=True)
    command.add_argument("--proposal", type=Path, required=True)
    command.add_argument("--result", type=Path, required=True)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "prepare":
        return prepare(args)
    if args.command == "reconcile":
        return prepare(args, ambiguous=True)
    if args.command == "verify":
        return verify(args)
    parser.error("Unsupported command")
    return 2


if __name__ == "__main__":
    sys.exit(main())
