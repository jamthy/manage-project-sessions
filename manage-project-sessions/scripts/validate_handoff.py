#!/usr/bin/env python3
"""Validate the structure of a project-session handoff Markdown file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REQUIRED_SECTIONS = {
    "identity": ("交接标识", "handoff identity"),
    "goal": ("当前目标与边界", "current goal and boundaries", "current goal and scope"),
    "status": ("事实状态", "factual status", "current status"),
    "decisions": ("已确认与已否决决策", "decisions"),
    "entrypoints": ("关键入口与变更", "key entry points and changes", "entry points and changes"),
    "evidence": ("验证证据", "validation evidence", "verification evidence"),
    "unresolved": ("未解决问题与未验证项", "unresolved and unverified", "open questions and unverified"),
    "volatile": ("易变现场快照", "volatile state snapshot", "runtime snapshot"),
    "next": ("下一步安全动作", "next safe action"),
    "prompt": ("新会话开场提示", "new task opening prompt", "new session opening prompt"),
}

PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}")
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def normalize_heading(value: str) -> str:
    value = re.sub(r"[`*_]", "", value).strip().casefold()
    return re.sub(r"\s+", " ", value)


def collect_sections(text: str) -> dict[str, str]:
    matches = list(HEADING_RE.finditer(text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        level = len(match.group(1))
        end = len(text)
        for following in matches[index + 1 :]:
            if len(following.group(1)) <= level:
                end = following.start()
                break
        sections[normalize_heading(match.group(2))] = text[start:end].strip()
    return sections


def find_section(sections: dict[str, str], aliases: tuple[str, ...]) -> str | None:
    normalized_aliases = {normalize_heading(alias) for alias in aliases}
    for heading, body in sections.items():
        if heading in normalized_aliases:
            return body
    return None


def check_local_links(text: str, document: Path) -> list[str]:
    errors: list[str] = []
    for raw_target in LINK_RE.findall(text):
        target = raw_target.strip().strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        path_text = unquote(target.split("#", 1)[0])
        if not path_text:
            continue
        linked = Path(path_text)
        if not linked.is_absolute():
            linked = document.parent / linked
        if not linked.exists():
            errors.append(f"missing local link target: {target}")
    return errors


def validate(document: Path, verify_links: bool) -> list[str]:
    errors: list[str] = []
    try:
        text = document.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["file is not valid UTF-8"]

    if not text.strip():
        return ["file is empty"]

    sections = collect_sections(text)
    for section_id, aliases in REQUIRED_SECTIONS.items():
        body = find_section(sections, aliases)
        if body is None:
            errors.append(f"missing required section: {section_id} ({aliases[0]})")
        elif not body.strip():
            errors.append(f"required section is empty: {section_id} ({aliases[0]})")

    placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
    if placeholders:
        preview = ", ".join(placeholders[:5])
        suffix = " ..." if len(placeholders) > 5 else ""
        errors.append(f"unresolved template placeholders: {preview}{suffix}")

    if verify_links:
        errors.extend(check_local_links(text, document))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff_file", type=Path)
    parser.add_argument(
        "--check-local-links",
        action="store_true",
        help="fail when a relative or absolute local Markdown link target is missing",
    )
    args = parser.parse_args()

    document = args.handoff_file.expanduser().resolve()
    if not document.is_file():
        print(f"FAIL: handoff file does not exist: {document}", file=sys.stderr)
        return 2

    errors = validate(document, args.check_local_links)
    if errors:
        print(f"FAIL: {document}", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    link_note = " and local links" if args.check_local_links else ""
    print(f"PASS: handoff structure{link_note} validated: {document}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
