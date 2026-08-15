---
name: manage-project-sessions
description: "Proactively preserve continuity across Codex tasks in complex software projects by deciding when to continue the current task, create a project-control or topic task, hand off and switch, or resume from verified project truth. Default to a two-layer strategy: use this personal skill as the decision layer and automatically audit the applicable project instruction as the checkpoint-enforcement layer at the first substantial project checkpoint. Use explicitly for task/session structure, boundary assessment, handoff, resume, or project-policy adoption requests. Also use proactively even when the user does not mention sessions whenever ongoing project work starts or completes a substantial task, changes project stage or semantic owner, enters prolonged diagnosis, begins independent review or acceptance, prepares a release, shows context drift, changes person/model, or resumes later. Keep ordinary bounded work quiet when no real boundary or adoption action exists."
---

# Manage Project Sessions

Keep project continuity in durable project truth, not in chat history. Treat a task as a bounded workspace for thinking and execution, never as the authoritative project database.

## Operating boundaries

- Inspect before recommending. Follow the repository's existing instructions, documentation layout, source ownership, Git state, tests, and runtime evidence.
- Adapt to existing truth owners. Do not require files named `PROJECT.md`, `PRD.md`, or `DECISIONS.md` when the project uses other owners.
- Keep one writable owner for each fact. Link to durable product, architecture, decision, and validation truth instead of copying it into a second project database.
- Default to two-layer operation: this personal skill owns boundary decisions, and the applicable project instruction owns repeatable checkpoint invocation.
- At the first substantial checkpoint in a complex project, audit the project layer read-only even when the user does not ask about sessions. Keep adopted-and-continue results internal when no user action is needed.
- Recommend task changes proactively, but never create, rename, navigate to, archive, or delete a task unless the user explicitly requests that action and the host supports it.
- Treat a new task as a context boundary, not as permission to implement, change project files, commit, push, deploy, or touch live state.
- Preserve user state. Re-check live processes, configuration, logs, services, scheduled jobs, connected systems, and other volatile facts read-only before acting on them.

## Core workflow

1. Classify the request as one of six operations:
   - audit the default two-layer state;
   - run a proactive boundary checkpoint;
   - establish a task structure;
   - assess the current task;
   - hand off and switch;
   - resume from a handoff.
2. Inspect the smallest useful current truth: current goal, project stage, semantic owner, active project truth, actual changed state, validation evidence, Git state when present, and relevant live state.
3. Read [references/session-model.md](references/session-model.md) when establishing or revising project/task topology.
4. Read [references/switch-gates.md](references/switch-gates.md) whenever running a proactive checkpoint or deciding whether to continue, split, or switch.
5. Read [references/handoff-contract.md](references/handoff-contract.md) before producing or consuming a handoff.
6. Read [references/project-adoption.md](references/project-adoption.md) at the first substantial project checkpoint and whenever applying, auditing, updating, or removing the project layer.
7. Recommend exactly one next task action in plain language when a boundary or missing closeout needs user attention. Explain the evidence, what must happen first, and the risk of switching incorrectly.
8. If the proactive result is **continue here**, do not add session-management ceremony to an otherwise normal development response unless a short notice materially helps.
9. If a new task is warranted, provide a concise suggested title, bounded purpose, required inputs, stop condition, and copyable opening prompt. Create it only after an explicit user request.
10. If durable project truth must change, name the existing owner and request or rely on authorization for that exact edit. Do not hide project-truth edits inside a session-management action.
11. Verify every handoff artifact structurally and re-read it. Report volatile or unavailable evidence as unverified.

## Decision outcomes

Choose one outcome; do not return a menu when evidence supports a recommendation.

- **Continue here**: keep the current task because the goal, owner, acceptance boundary, and useful context remain coherent.
- **Create a topic task**: establish one new bounded task because an independent goal or owner needs focused work; keep the project-control task lightweight.
- **Hand off and switch**: close the current boundary, write back durable truth, prepare a verified handoff, then enter a new task.
- **Resume from handoff**: reconcile the handoff snapshot with current project and runtime truth before continuing.
- **Do not switch yet**: finish the minimum closeout needed to prevent loss or contradiction before moving.

## Project-control and topic tasks

Use a project-control task only for direction, stage placement, priorities, cross-topic coordination, and deciding the next bounded task. Do not use it for bulk coding or prolonged debugging.

Use a topic task for one bounded outcome with one clear completion boundary, such as requirements review, architecture decision, one implementation slice, acceptance, or diagnosis of one failing boundary. Do not create empty future tasks in advance.

When useful, suggest titles in these forms without forcing renames:

```text
<项目名>｜项目总控
<项目名>｜<专题>｜<阶段或目标>
```

## Default two-layer operation

Use this personal skill as the decision engine. Use a project-scoped `AGENTS.md` or the repository's existing equivalent instruction owner as the checkpoint enforcement layer.

For every complex project in scope:

1. Inspect the applicable instruction hierarchy and existing session or handoff rules read-only at the first substantial checkpoint.
2. Classify the project layer as **adopted**, **missing**, **conflicting**, or **unverified** using [references/project-adoption.md](references/project-adoption.md).
3. If adopted, continue in two-layer mode. Stay quiet when the boundary result is **continue here** and no user action is needed.
4. If missing, name the exact proposed instruction owner and recommend installing the managed policy. Continue safe bounded work when possible; do not repeatedly interrupt the same task after the user defers.
5. If conflicting or unverified, explain the affected scope and do not claim that proactive enforcement is active. Continue unrelated safe work when the conflict does not block it.
6. Before any authorized project-instruction write, apply the deterministic language-selection rules in [references/project-adoption.md](references/project-adoption.md). Never treat the asset's source language as the output language, and never insert prose in a language different from the selected language.
7. When authorized to adopt, reuse or update the existing owner, adapt [assets/agents-session-policy.md](assets/agents-session-policy.md), and verify exactly one effective managed policy block.

Automatic auditing is read-only. Do not modify a project's instruction merely because this personal skill was invoked. An explicit request to adopt, install, enable, update, or remove the two-layer policy for the current project authorizes only that bounded local instruction change; otherwise show the target and obtain authorization before writing.

## Handoff artifacts

Use [assets/session-handoff-template.md](assets/session-handoff-template.md) as a starting shape, then adapt it to the project. Do not copy it unchanged or invent missing facts.

After writing a handoff file, run:

```text
python <skill-root>/scripts/validate_handoff.py <handoff-file> --check-local-links
```

If local links intentionally point outside the available checkout, omit `--check-local-links` and report link validation as unverified. Structural validation never proves that project claims are true.

## Communication

Keep normal advice compact:

- recommended action;
- evidence for it;
- required closeout, if any;
- suggested task title and opening prompt, when applicable;
- facts that must be revalidated.

Do not expose an internal scorecard or force the user to choose project-management jargon. Ask only when different answers change the visible scope, durable write location, or external/task-management action.
