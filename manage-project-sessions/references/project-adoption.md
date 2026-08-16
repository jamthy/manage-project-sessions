# Project adoption

## Purpose

Make two-layer operation the default for complex projects. Treat the personal skill as the method owner and the applicable project instruction as the checkpoint-invocation owner; do not copy the full skill into the repository.

The default includes an automatic read-only adoption audit at the first substantial project checkpoint. It does not include background monitoring or silent project-file writes.

## Authorization boundary

Installing or updating the personal skill authorizes automatic read-only inspection of applicable project instructions during in-scope work. It does not authorize editing every project.

Modify a project instruction only when the user explicitly asks to adopt, install, enable, update, or remove the two-layer policy for the current project or explicitly names the target instruction file. That authorization covers only the bounded local instruction change, not project truth, source code, Git history, task operations, or external effects.

## Audit the default project layer

At the first substantial checkpoint in a complex project:

1. Discover the effective instruction hierarchy for the current working scope.
2. Inspect session, task-boundary, handoff, and `$manage-project-sessions` rules.
3. Classify the project layer as exactly one state:
   - **adopted**: one effective policy or equivalent rule invokes the skill proactively and preserves all required semantics;
   - **missing**: no effective project-layer checkpoint rule exists, or an existing non-conflicting rule omits one or more required meanings;
   - **conflicting**: duplicate, overridden, or contradictory rules could produce inconsistent behavior;
   - **unverified**: the effective owner or override chain cannot be inspected reliably.
4. Cache the result in the current task context. Re-audit only after the instruction hierarchy changes, the working scope moves under another override, a handoff/resume occurs, or evidence contradicts the cached state.

Handle the result proportionally:

- **adopted**: operate in two-layer mode and stay quiet when the boundary result is **continue here**.
- **missing**: report the adoption gap once for the current task scope, propose the exact owner, and request authorization before writing unless the current request already grants it. Continue safe bounded work when possible.
- **conflicting**: name the conflict and affected scope. Do not claim project-layer enforcement is active; block only the governance action that depends on the conflict.
- **unverified**: state that project-layer enforcement is unverified and identify the missing evidence. Do not invent an owner.

## Discover the instruction owner

1. Locate the applicable `AGENTS.md` hierarchy or the repository's established equivalent.
2. Read the instructions that govern the intended project scope.
3. Search for an existing session, task-boundary, handoff, or `$manage-project-sessions` rule.
4. Select the narrowest established owner that covers the project work. Do not create a second root or competing constitution.
5. Preserve unrelated instructions and user changes.

If no instruction owner exists, propose the repository root `AGENTS.md` only when that convention is appropriate. Create it only after authorization. Otherwise ask for the exact owner instead of inventing one.

## Choose the managed prose language

Select the output language before drafting or updating a managed block. Apply this order exactly and stop at the first available signal:

1. Use the language explicitly requested by the user for this instruction change.
2. Otherwise, when the selected instruction owner already contains prose, use the dominant language of the surrounding instructions.
3. Otherwise, use the language of the current user conversation.
4. Otherwise, use the dominant language of the active project documentation.
5. If no signal resolves the choice, use Chinese.

The asset is a semantic source, not a language authority. Translate every managed heading, sentence, list item, and outcome label into the selected language. Never paste English prose into a Chinese instruction owner, Chinese prose into an English instruction owner, or preserve a stale managed block in the wrong language. If an existing owner is materially mixed and has no dominant language, use the current conversation language instead of copying the asset language.

Keep only machine-sensitive or identity-sensitive text unchanged: the two marker lines, `$manage-project-sessions`, filenames, command names, code identifiers, and established product names such as `Codex`, `Git`, and `AGENTS.md`. Language adaptation must not change policy meaning.

## Apply the managed policy

Use [../assets/agents-session-policy.md](../assets/agents-session-policy.md) as the semantic source. Preserve these marker lines exactly so adoption is detectable and idempotent:

```text
<!-- manage-project-sessions-policy:v1:start -->
<!-- manage-project-sessions-policy:v1:end -->
```

Use the selected prose language and adapt the heading level to the existing file, while preserving these meanings:

- invoke `$manage-project-sessions` at evidence-backed checkpoints without waiting for the user to mention sessions;
- include a checkpoint when work needs another topic's result, work, decision, writable owner, or other cross-topic collaboration, even before another stage or owner change occurs;
- keep ordinary bounded work quiet when the result is to continue;
- never use message count alone as a switch rule;
- surface one recommendation only when user attention is needed;
- require a verified handoff before unsafe switching;
- never create, hand off, resume, switch or navigate to, rename, archive, or delete tasks without explicit user authorization for the concrete action;
- treat the policy as invocation guidance, not as permission to edit project truth or execute external effects.

If a managed block already exists, update it in place. If an equivalent unmarked rule exists, merge with it or replace it only within the authorized scope; do not leave competing rules.

## Validate adoption

After editing:

1. Read back the effective instruction from the project scope.
2. Confirm exactly one start marker and one end marker exist in the selected owner.
3. Confirm the block names `$manage-project-sessions` and all required meanings remain present.
4. Confirm all managed prose uses the selected language; ignore the exact markers, `$manage-project-sessions`, filenames, commands, code identifiers, and established product names when checking this.
5. Search the applicable instruction hierarchy for contradictory or duplicate session rules.
6. Report the exact project scope now covered and any narrower directories that override it.

Do not claim background monitoring. The project instruction makes the check part of Codex's normal project turns; it cannot wake a task when no user or system turn occurs.

## Remove or change adoption

Require an explicit request for the exact project scope. Remove or replace only the marked block, preserve surrounding instructions, and read back the result.
