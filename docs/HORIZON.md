# Road Warrior Horizon

- Version: 0.3
- Status: Captured; not designed
- Date: 2026-08-18

The Horizon records future possibilities without designing them.

- Continuous or always-available access across environments.
- Ambient availability with explicit participation boundaries.
- Event-driven skill and agent handoffs.
- Continuous project contribution and reconciliation outside driving.
- Connectors, MCPs, APIs, webhooks, and orchestration across other systems.
- Calendar, Gmail, Google Docs, GitHub, task systems, and other integrations.
- Delegated execution.
- Coordination with specialized AIs and existing workflows.
- Road Warrior should prefer orchestration over recreating existing systems.

## Context Engine

Future research only.

### Questions

- Representing contexts.
- Multiple contexts.
- Ranking contexts.
- Contextual opportunities.
- Delayed clarification.
- Learned contexts with explicit permission.
- Orchestration opportunities.
- Privacy considerations.

## Richer Bidirectional Cross-Project Context Sharing

Later architecture and research only. This is not August 21 scope.

Research how relevant context and information could move in both directions among Road Warrior and approved projects without Bruce acting as the courier. The V1 shared Drive handoff ledger remains the current operational mechanism, governed by the repository-root protocol.

### Deferred V2 Local-First Recommendation

The recommended V2 direction is a local-first routing plane with:

- one shared local Markdown handoff ledger as the inspectable operational record;
- one repository-scoped routing skill that applies the same producer, consumer, target-filtering, deduplication, and acknowledgment rules across participating projects;
- verified receipts that identify the receiving project and destination artifact and are written only after independent readback;
- an optional watcher or bridge for event detection and transport, without moving judgment or authority into the watcher; and
- Google Drive/mobile fallback for access when the local workspace is unavailable.

V2 should preserve a single logical ledger, deterministic ownership, human readability, and replaceability. It must not create simultaneous local and Drive authorities without an explicit synchronization and conflict model. This is a recommendation for later design and reality testing, not permission to implement V2 now.

## Relational Knowledge Layer — V3/V4 Research

Research a human-readable relational knowledge layer, such as Obsidian, combined with semantic retrieval to support cross-project relationships and interconnected concepts.

- Road Warrior remains the judgment and routing layer.
- The knowledge layer provides relational memory; it does not create judgment.
- Human readability and inspectability are preferred.
- A graph database should be introduced only if later relationship complexity earns the additional infrastructure.
- This is a research direction, not an implementation decision.

## Judgment-Driven Personal OS / Dynamic Mission Control — V3

Road Warrior and the Judgment Engine may become the cognitive prioritization layer above Personal OS. Personal OS may become a dynamic presentation and action surface informed by projects, calendar, tasks, investments, trades, communications, and other approved signals.

The surface should present judgment already formed from relevant context rather than require Bruce to create that judgment by manually managing static lists or Kanban classifications.

**Principle:** “The dashboard should display judgment, not create it.”

The approved governed-worker direction provides a future-compatible boundary without selecting a dashboard design:

- workers may gather verified state and maintain derived projections;
- Road Warrior alone determines salience, priority, meaning, and what deserves Bruce's attention;
- the dashboard may display projections of that judged state;
- dashboard actions return to Road Warrior as new intent; and
- the dashboard must not independently redefine priorities or write authoritative obligation or handoff state.

This is a V3 brainstorm and design direction, not a Prototype 1 requirement.
