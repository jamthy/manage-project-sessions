# Project task model

## Principle

Keep chats replaceable and project truth durable. Use tasks to isolate bounded reasoning and execution; use the project workspace, active documentation, source, tests, decisions, and current runtime evidence to preserve continuity.

## Establish current truth

Identify authority by concern instead of assuming one global file order:

- Follow `AGENTS.md` and equivalent files for repository-working instructions.
- Use the active product/requirements owner for intended behavior.
- Use architecture or decision records for accepted boundaries and reasons.
- Use compiled source, active call paths, configuration, tests, and current runtime evidence for implemented behavior.
- Use Git state for tracked change history and uncommitted scope when Git exists.
- Treat a handoff as a dated snapshot and navigation aid; verify its claims against current owners.

When owners conflict, stop the affected action, describe the conflict, and resolve or escalate it before declaring continuity.

## Task types

### Project-control task

Use one when a long-running project needs continuing direction and coordination.

Own:

- current stage and priority;
- the next bounded topic;
- cross-topic dependencies and accepted decisions;
- whether a topic has enough evidence to close;
- which durable owner must be updated.

Do not own:

- bulk implementation;
- prolonged debugging;
- detailed design that belongs to a dedicated topic;
- duplicate copies of product or architecture truth.

### Topic task

Give it one primary outcome, one semantic boundary, and one stop condition. Examples include requirements review, architecture of one subsystem, an implementation slice, acceptance of one release boundary, or diagnosis of one reproducible failure.

Keep work in the same topic task while fixes, tests, and clarification serve the same outcome and owner. Start another topic only when the boundary actually changes.

## Topology rules

- Create tasks on demand, never as an empty future hierarchy.
- Prefer one active writer for any code or truth owner.
- Avoid parallel tasks that can edit the same owner or make competing decisions.
- Keep project control lightweight; link to topic outcomes and durable truth.
- Return a completed topic to project control with evidence and the next decision, not a transcript dump.
- Do not assume every project needs a project-control task. A short or single-owner project may stay in one bounded task.

## Establishment output

When proposing a structure, provide only the tasks currently justified. For each, state:

```text
Title
Purpose
Inputs or truth owners
Allowed scope
Stop condition
Returns to
```

Mark future possible topics as future boundaries, not as tasks to create now.
