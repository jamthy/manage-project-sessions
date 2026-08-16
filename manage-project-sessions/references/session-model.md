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

## Project-control orchestration

Apply this protocol when host metadata, an originating delegation, a verified handoff, or current user direction identifies the current task as project control or as a topic expected to return to project control. A missing or unreachable control route is handled below; it does not let the topic take over orchestration. Do not impose this topology on a short or single-owner project that remains coherent in one bounded task.

### Identify the roles and route

Treat a task as project control only when the relationship is explicit in host task metadata, an originating delegation, a verified handoff, or current user direction. Treat a title such as `<project> | project control`, a matching repository, or a plausible recent task as a discovery hint, never as identity proof.

Before a topic reports or requests coordination, resolve the established project-control route from one of those explicit sources. Use the host's task-messaging capability with the exact host-provided task identifier and host identifier when the host requires both. Never guess, derive, or substitute a task ID from a title, project path, repository, or task list position.

If project control does not exist, cannot be identified, is unavailable, or cannot receive the report, stop at the current topic boundary. Preserve the minimum closeout, tell the user which route is missing, and ask them to establish or restore project control. Do not create a replacement, select a likely task, or route the work to another topic.

### Topic responsibilities at a boundary

While the goal, owner, stage, and acceptance boundary remain unchanged, continue ordinary topic work without status ceremony. Do not report every edit, test, clarification, or small failure.

At any of these real boundary events, stop expanding the topic and return control to project control:

- the topic reaches its stop condition or completes its current stage;
- progress needs another topic's result, work, decision, or writable owner;
- the semantic owner, primary deliverable, project stage, or acceptance boundary must change;
- the topic needs another topic to be created, handed off, resumed, switched to, or otherwise coordinated;
- the user asks inside the topic to create or switch to another project topic.

Send project control a compact return report using [handoff-contract.md](handoff-contract.md#topic-return-report). Include actual status, changes, validation, unresolved or unverified items, and one recommended next decision. When the user requested a task operation, include the exact requested operation and the available authorization evidence. A report is a decision input, not permission for the topic to continue into the next phase.

A topic must not create, hand off, resume, switch, direct, or coordinate another project topic. It must not turn a cross-topic dependency into direct topic-to-topic instructions. After reporting, wait for project control or the user to return an in-boundary action; do not infer the next topic or broaden scope.

### Project-control responsibilities and authorization

Project control owns project-wide topic orchestration: place the report in the current project stage, reconcile cross-topic dependencies, choose the next bounded owner, and decide whether the correct outcome is to continue, close, create, hand off, resume, or switch.

This orchestration role grants no task-operation authority by itself. Before project control creates, hands off, resumes, switches, navigates to, renames, archives, or deletes a task, require the user's explicit authorization for that concrete action. If the authorization was given in a topic task, project control must verify the exact source request through host-visible task history or another reliable user-authored record; a topic's paraphrase alone is not authorization. If that evidence is unavailable or the requested target or action changed, ask the user again.

Keep task-operation authorization separate from implementation and external-effect authorization. Creating or resuming a topic does not authorize project-file changes, commits, pushes, releases, deployments, or destructive actions.

## Topology rules

- Create tasks on demand, never as an empty future hierarchy.
- Prefer one active writer for any code or truth owner.
- Avoid parallel tasks that can edit the same owner or make competing decisions.
- Keep project control lightweight; link to topic outcomes and durable truth.
- When project control exists, return completed topics and cross-topic boundary decisions through the project-control orchestration protocol above, not directly to another topic.
- Do not assume every project needs a project-control task. A short or single-owner project may stay in one bounded task.

## Codex-mode gate before code

Apply this gate immediately before the first formal code write in the current project session. Re-run it after a task switch, handoff, resume, or any reported host-mode change. This gate does not replace normal authorization, owner, test, or validation checks.

1. Determine the current session's backing mode from host-provided task metadata or another explicit host signal. Confirm the gate only when the host identifies the current session as a **Codex** task or Codex coding mode.
2. Do not infer Codex mode from the model name, the presence of a Git repository or workspace, available shell commands, apparent file-edit capability, or the fact that the conversation discusses code.
3. Treat the mode as not confirmed when the host identifies the session as ChatGPT, ChatGPT Work, ordinary chat, or another non-Codex backing kind, or when the host exposes no reliable current-session mode signal.
4. When mode is not confirmed, stop before any code mutation. Do not apply a patch, generate code into the project, run a formatter or generator that rewrites code, or begin an implementation step. Tell the user:

```text
当前会话不是 Codex 模式，或无法确认其为 Codex 模式。请先切换到 Codex 模式；切换后告诉我继续，我会重新检查后再开始写代码。
```

5. If the host mode remains unknown and the user explicitly states that they have switched the current session to Codex mode, accept that statement as confirmation for the current session and allow implementation to continue. Record that the gate passed by user confirmation rather than host confirmation. This fallback does not override an explicit current host signal that identifies the session as non-Codex.

For this gate, a formal code write includes source code, tests, executable scripts, and build or configuration changes that alter executable behavior. Read-only inspection, diagnosis, planning, handoff preparation, and ordinary prose-document edits may continue without passing this gate, but they must not be used to stage or conceal code changes.

## Project workspace selection

Apply this flow only after the user has explicitly authorized creation of a project topic task. It selects where that task runs; it does not authorize the task or broaden its write scope.

1. List the host's saved projects, resolve the current project, and use its returned project ID. Do not infer an ID from a repository path or name.
2. Default to the current project's **Local** working directory. This skill intentionally overrides a host default that may prefer a Worktree merely because the project is a Git repository.
3. Use a **Worktree** only when either exception is established:
   - the user explicitly requests parallel isolation for this topic task; or
   - current evidence shows a real write-conflict risk.
4. Treat write-conflict risk as established only when another active or deliberately overlapping task, person, or process is expected to write the same checkout concurrently and at least one concrete collision surface is identified, such as overlapping files or truth owners, incompatible branch/base requirements, or build, generated-output, dependency, or configuration state that cannot safely be shared. Name the competing writer and collision surface. A vague possibility of future edits is not evidence.
5. Do not use a Worktree solely because the project uses Git, the task is long or substantial, the semantic topic differs, another task is read-only, or read-only work runs in parallel. An active task with no concurrent write plan is not by itself a conflict.
6. Tell the user which environment will be used and why before or alongside creation. For a Worktree, name whether the reason is the user's explicit isolation request or the identified writer/collision evidence. For Local, state that no Worktree exception was found when the distinction is material.
7. Call the host task-creation tool with an explicit environment:

```text
Local:    target = { type: "project", projectId: <resolved-id>, environment: { type: "local" } }
Worktree: target = { type: "project", projectId: <resolved-id>, environment: { type: "worktree" } }
```

For a Worktree, omit `startingState` unless the user explicitly requests a particular Git state; never invent a branch or ref. If isolation is required but the selected project or host cannot create a Worktree, stop and report that no safe isolated creation path is available instead of silently falling back to Local.

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
