# Road Warrior Context Routing Protocol

- Version: 2.0
- Status: Operational protocol and authoritative-location pointer
- Date: 2026-08-18

This file is not a live handoff ledger. It defines the V1 protocol and points to the one authoritative operational ledger. Do not append handoff entries here.

## Authoritative Live Ledger

- **Name:** `ROAD_WARRIOR_HANDOFFS`
- **Location:** Google Drive, root-level `RoadWarrior` folder
- **Drive file ID:** `1U4YvjjmwGAbspYwKo5dwlXd4NHbvSlnMdbWPPQYCGHc`
- **Stable link:** `https://docs.google.com/document/d/1U4YvjjmwGAbspYwKo5dwlXd4NHbvSlnMdbWPPQYCGHc/edit?usp=drivesdk`

The Drive artifact is authoritative for live entries and receipt state. This repository is authoritative for the protocol, durable decisions, and evidence. Git history preserves the former repository-ledger snapshot; it is not a second operational queue.

## Purpose and Boundary

Context Routing lets Road Warrior move durable, project-relevant information to the context where it belongs without requiring Bruce to remember and relay it manually.

- Road Warrior remains the judgment and routing layer.
- The ledger records transfers; it does not create judgment.
- V1 uses a simple, human-readable, replaceable shared ledger.
- There is no claimed background monitoring or polling.
- A write proves only that a handoff was recorded. Delivery is complete only after verified incorporation and acknowledgment by the receiving project.

## Ownership

- **Road Warrior:** judge whether a handoff is warranted, resolve the target, and create a complete `Pending` entry.
- **Receiving project:** retrieve entries addressed to it, deduplicate, incorporate the information into its own durable artifact, verify that write by readback, and acknowledge receipt.
- **Bruce:** remains the final human authority but is not the courier, ledger administrator, or acknowledgment mechanism.

## Producer Protocol

1. Create a handoff only for durable information relevant to another approved project or context.
2. Resolve the target with sufficient confidence; ask the smallest clarifying question rather than guessing.
3. Write one structured entry to the authoritative Drive ledger with a unique ID and `Pending` status.
4. Preserve enough origin and intended-use context for the receiving project to act without asking Bruce to reconstruct the conversation.
5. Independently read back the new entry before reporting that it was recorded.
6. Do not claim delivery, incorporation, or receipt from the producer write.

## Consumer Protocol

1. On the first user message in a participating project each calendar day, retrieve the exact ledger by Drive file ID before responding.
2. Consider only `Pending` entries unambiguously addressed to that project.
3. Deduplicate and incorporate the handoff into the receiving project's authoritative durable artifact.
4. Independently read back and verify the receiving-project write.
5. Only after successful verification, update the handoff to `Received` and record the receipt timestamp, receiving project, and destination artifact identity.
6. Verify the acknowledgment write. If either write cannot be verified, leave the handoff `Pending` and report the boundary honestly.
7. After a successful daily check, do not check again that calendar day unless Bruce explicitly asks for another check.

## Required Entry Fields

| Field | Requirement |
| --- | --- |
| ID | Unique handoff identifier. Preserve the live ledger's established ID format. |
| Created | ISO 8601 date or timestamp. |
| Source | Originating Road Warrior context. |
| Target Project | Unambiguous receiving project or context. |
| Type | Durable information type. |
| Status | `Pending` or `Received`. |
| Summary | Concise statement of the information being transferred. |
| Context | Enough origin and intended-use context for independent incorporation. |
| Related Projects / People | Relevant relationships, or `None`. |
| Tags | Short retrieval and migration labels. |
| Receipt | Timestamp, receiving project, and destination artifact identity; empty while pending. |

## Status and Verification Rule

```text
Producer write + readback -> Pending
Receiving durable write + readback -> acknowledgment write + readback -> Received
```

No planned action, attempted write, tool response, or producer-only record is sufficient evidence for `Received`.
