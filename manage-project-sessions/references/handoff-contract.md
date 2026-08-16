# Handoff contract

## Purpose

Make a project task replaceable without pretending that chat history is project truth. Produce a compact, evidence-backed bridge to current owners and the next safe action.

## Required content

Include:

1. handoff identity: project, source task, timestamp/timezone, intended destination;
2. current goal, scope, non-goals, and stop condition;
3. factual status separated into completed, partial, blocked, not started, and explicitly not done;
4. accepted and rejected decisions with links to their durable owner when available;
5. important source, configuration, documentation, test, and architecture entry points;
6. changed/uncommitted artifacts and Git state when Git exists;
7. fresh validation evidence with commands or paths and exact results;
8. failures, unresolved questions, risks, and unverified planes;
9. volatile runtime/external snapshot with capture time and read-only re-check instructions;
10. one next safe action, its prerequisites, and its stop condition;
11. a copyable opening prompt for the destination task.

Use `不适用` with a reason when a section does not apply. Never invent evidence to make a section look complete.

## Stable and volatile facts

Link stable facts to their active project owners. Mark volatile facts explicitly, including process IDs, open ports, local configuration, logs, databases, services, scheduled jobs, connected shares, credentials, provider state, deployment state, and external task status.

Record the observation time and require revalidation. A prior PID, log result, passing test, task status, or provider response is not proof of current state.

## Write location

Use an existing project convention and index when one exists. A handoff should point to durable truth rather than become a second requirements, architecture, or decision database.

If the user requests a durable handoff but no established location exists, obtain or propose one explicit path before writing. Do not silently invent a new documentation root or modify `AGENTS.md` as part of handoff creation.

## Topic return report

Use a compact return report when a topic reaches a boundary and must give project control the evidence needed to decide what happens next. This report is not automatically a durable handoff artifact and does not need the full template unless the task itself will be replaced or its state cannot otherwise be reconstructed.

Include only:

1. actual status against the topic goal and stop condition;
2. changed files, artifacts, durable owners, and relevant Git state;
3. validation performed and exact results;
4. unresolved failures, dependencies, risks, and unverified planes;
5. one recommended next project-control decision;
6. when applicable, the user's exact requested task operation and where project control can verify that user-authored authorization.

Keep inherited claims separate from fresh evidence. Do not send a transcript dump, claim another topic's status without verification, or treat the return report as authority to create, hand off, resume, switch, or direct another topic.

## Opening prompt requirements

Write the destination prompt so a fresh Codex instance can:

- locate the project and handoff;
- read repository instructions first;
- reconcile the handoff with current source, Git, and runtime facts;
- preserve explicit non-goals and user state;
- perform only the named next action;
- stop on conflict or after the bounded outcome;
- report fresh evidence separately from inherited claims.

Do not paste the full handoff into the prompt. Point to the artifact and summarize only the starting contract.

## Structural validation

Run `scripts/validate_handoff.py` against a created artifact. Use `--check-local-links` when the complete checkout is available. Fix structural errors and broken in-scope links, then re-read the document.

Treat a passing validator as structural evidence only. Confirm status, decisions, source entry points, tests, Git, and live state independently.
