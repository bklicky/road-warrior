# Road Warrior Context Routing Handoff Ledger

- Version: 1.0
- Status: Active V1 mechanism
- Date: 2026-08-12

## Purpose

Road Warrior uses this shared ledger when a conversation produces durable information that belongs to another project or context and should become available there later without requiring Bruce to remember and relay it manually.

Writing an entry proves only that Road Warrior recorded the handoff in this ledger. Cross-project delivery is not complete until the receiving project incorporates the information and marks the entry `Received`.

## V1 Boundary

- This ledger is intentionally simple and replaceable.
- V1 does not add software, database infrastructure, automation, APIs, or Obsidian integration for Context Routing.
- Structured records are required so a later mechanism can migrate them without depending on unstructured conversation history.
- Road Warrior remains the judgment and routing layer; the ledger records handoffs but does not create judgment.

## V1 Operating Model

```text
Road Warrior conversation
  → Judgment identifies durable project-relevant information
  → Determine target project
  → Write structured handoff entry
  → Receiving project reads entries addressed to it
  → Receiving project incorporates the information into its own context or work
  → Receiving project marks the handoff Received
```

## Ownership

- Road Warrior owns judging whether a handoff is warranted, determining the target project, and creating the entry.
- Each receiving project owns reading entries addressed to it, incorporating relevant information, and acknowledging receipt.
- Bruce is not the synchronization mechanism.

## How Road Warrior Writes Entries

1. Write an entry only when judgment identifies durable information that is relevant to another project or context.
2. Determine the target project with sufficient confidence. If the destination is materially uncertain, clarify rather than guess.
3. Append one entry using every field in the schema below.
4. Use an ID in the form `RW-HO-YYYYMMDD-NNN`, an ISO 8601 creation date, and `Pending` status.
5. Preserve enough context for the receiving project to understand the information without asking Bruce to reconstruct the originating conversation.
6. Do not claim that the receiving project has the information merely because the entry was written.

## How Receiving Projects Consume and Acknowledge Entries

1. Read `Pending` entries whose `Target Project` addresses the receiving project.
2. Incorporate the information into the project's own context or work as appropriate.
3. After incorporation, change `Status` to `Received` and set `Received` to the ISO 8601 date or timestamp of acknowledgment.
4. Do not mark an entry `Received` if it has not been incorporated.
5. Preserve the entry's other fields so the ledger remains auditable and suitable for later migration.

## Entry Schema

| Field | Requirement |
| --- | --- |
| ID | Unique handoff identifier using `RW-HO-YYYYMMDD-NNN`. |
| Created | ISO 8601 date or timestamp when Road Warrior created the entry. |
| Source | Originating Road Warrior context. |
| Target Project | Project or context responsible for receiving the handoff. |
| Type | Durable information type, such as `Story Seed`, `Decision`, `Observation`, or `Open Loop`. |
| Status | `Pending` or `Received`. |
| Summary | Concise statement of the information being handed off. |
| Context | Enough origin and intended-use context to make the summary useful. |
| Related Projects | Other relevant projects, or `None`. |
| Related People | Relevant people, or `None`. |
| Tags | Short retrieval and migration labels. |
| Received | ISO 8601 acknowledgment date or timestamp; `—` while pending. |

## Status Model

```text
Pending → Received
```

## Handoff Entries

### RW-HO-20260812-001

- **ID:** RW-HO-20260812-001
- **Created:** 2026-08-12
- **Source:** Road Warrior — initial Judgment Engine conversational reality testing
- **Target Project:** Instagram / O.G. Bruce trading-content project
- **Type:** Story Seed
- **Status:** Pending
- **Summary:** Trading strategies and methodologies can be analogous to different languages describing the same underlying market reality. A chair remains the same object whether called “chair” in English or “isu” in Japanese.
- **Context:** Story seed for future short-form trading-content development. The analogy may help explain how different methodologies can describe the same underlying market without requiring one vocabulary to invalidate another.
- **Related Projects:** Road Warrior
- **Related People:** Bruce
- **Tags:** `trading-content`, `story-seed`, `trading-methodologies`, `language-analogy`, `short-form-content`
- **Received:** —
