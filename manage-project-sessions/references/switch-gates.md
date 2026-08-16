# Continue, split, and switch gates

## Decision order

Inspect these facts before recommending a task change:

1. current bounded goal and non-goals;
2. project stage and next accepted outcome;
3. semantic owner and consumers;
4. actual implementation/documentation state;
5. current validation and unresolved failures;
6. Git and overlapping writer state when present;
7. volatile runtime or external state when relevant;
8. context health: stale assumptions, rejected paths, contradictions, and recoverability.

Do not switch based on message count or token length alone.

## Proactive checkpoint activation

Run a lightweight boundary checkpoint without waiting for session-management wording when project instructions require it or current evidence shows one of these events:

- begin a substantial task while the current stage, goal, or non-goals are unclear;
- finish a substantial task or reach its stop condition;
- move between requirements, architecture, implementation, verification, release, or another stage with a different acceptance boundary;
- change the semantic owner, subsystem, or primary deliverable;
- need another topic's result, work, decision, writable owner, or other cross-topic collaboration, even when the current stage and owner have not otherwise changed;
- enter prolonged diagnosis, repeat failed approaches, or accumulate rejected hypotheses that make context recovery harder;
- start an independent review, acceptance pass, release-preparation pass, takeover, or later-period continuation;
- detect contradictions among current chat assumptions, active project truth, code, Git, tests, or runtime evidence;
- approach a handoff, model/person change, or context compaction with work that cannot be reconstructed safely from durable truth.

Keep this check proportional. Inspect only the evidence needed to decide the boundary. If the result is **continue here** and no user action is needed, continue the requested work without a separate governance report. Surface the result when a switch, new topic, handoff, truth write-back, conflict, or missing closeout requires attention.

A long task or conversation raises the value of a checkpoint but never determines the result by itself.

## Topic-task escalation

When the current task is a topic under established project control, apply the role and routing protocol in [session-model.md](session-model.md#project-control-orchestration) after the checkpoint identifies a real boundary. Topic completion, a cross-topic dependency, a semantic-owner or stage change, or a request to create or switch topics requires a return report to project control and a stop on scope expansion. The topic does not execute or coordinate the next task operation.

Do not escalate ordinary work that remains inside the same goal, owner, stage, and acceptance boundary. A normal edit, test, clarification, or recoverable failure remains in the topic unless other boundary evidence exists.

## Continue here

Recommend continuing when all material conditions hold:

- the primary goal and completion boundary are unchanged;
- work remains inside the same semantic owner or stable contract;
- existing discussion is still useful and not dominated by stale conclusions;
- the next action can be verified inside the current task;
- no independent review or fresh-context boundary is required.

A normal error, test failure, clarification, or small follow-up is not by itself a switch reason.

## Create a topic task

Recommend a new bounded topic when at least one evidence-backed condition holds:

- the next outcome is independently completable and belongs to a different semantic owner;
- the project moves into a new stage with a different acceptance boundary;
- an independent review, acceptance pass, or fresh-context diagnosis would materially improve evidence;
- another developer, model, or later work period must take ownership;
- the current task is project control and the next work is substantial implementation or prolonged diagnosis;
- context contains enough rejected or contradictory paths that reliable continuation requires a clean boundary.

Do not create a new task when it would merely duplicate the same writer, goal, or unresolved problem.

## Hand off and switch

Allow switching only after the minimum closeout is available:

- actual completed and incomplete state is separated;
- accepted and rejected decisions are recorded in their durable owner when required;
- changed files or artifacts and validation evidence are named;
- unresolved failures and unverified planes are explicit;
- Git and volatile runtime snapshots are recorded when relevant;
- the next safe action and stop condition are clear;
- the new task can locate the authoritative sources.

If these conditions are not met, recommend **do not switch yet** and perform or request the smallest missing closeout. Do not demand unrelated documentation ceremony.

## Resume from handoff

Treat the handoff as a snapshot, not current truth:

1. record its date, source task, and intended next action;
2. read current repository instructions and named truth owners;
3. inspect current files and Git state;
4. re-check volatile processes, configuration, logs, services, jobs, connections, and external state read-only;
5. classify handoff claims as current, changed, stale, conflicted, or unverified;
6. resolve material conflicts before writing or executing;
7. restate the bounded goal and first safe action.

## Recommendation shape

Return one recommendation:

```text
Recommended action: continue | create topic | hand off and switch | resume | do not switch yet
Why: <current evidence>
Before moving: <minimum closeout or none>
Suggested title: <only when a new task is warranted>
Opening prompt: <copyable and bounded>
Revalidate: <volatile or missing facts>
```

Recommend first; create, hand off, resume, switch, rename, navigate, archive, or delete a task only after an explicit request for that exact action. In a project-control/topic topology, only project control performs project-wide topic orchestration, subject to the authorization rules in [session-model.md](session-model.md#project-control-responsibilities-and-authorization).
