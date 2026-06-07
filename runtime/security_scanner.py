from __future__ import annotations

import re
from pathlib import Path
from typing import List

# Plain substring markers (case-insensitive) that always indicate a committed secret.
_SUBSTRING_MARKERS = ["BEGIN PRIVATE KEY", "AWS_SECRET", "ANTHROPIC_API_KEY", "OPENAI_API_KEY"]

# Context-aware markers that need boundary/value checks to avoid false positives.
_REGEX_MARKERS = [
    # "sk-" key prefix, but not inside words like "disk-write".
    re.compile(r"(?<![a-z])sk-", re.IGNORECASE),
    # API_KEY assigned a literal value -- not an env-var reference such as
    # GEMINI_API_KEY=${GEMINI_API_KEY} or API_KEY=$VAR, and not an empty value.
    re.compile(r"API_KEY\s*=\s*[\"']?(?!\$)[^\s\"'$]", re.IGNORECASE),
]


def scan_text(text: str) -> List[str]:
    lowered = text.lower()
    found = [marker for marker in _SUBSTRING_MARKERS if marker.lower() in lowered]
    found += [marker.pattern for marker in _REGEX_MARKERS if marker.search(text)]
    return found


def scan_repo(root: str = ".") -> List[str]:
    findings: List[str] = []
    skip_dirs = {".git", "node_modules", ".next", "__pycache__"}
    skip_files = {
        "security_scanner.py",
        "verifier.py",
        "test_security_scanner.py",
        "package-lock.json",
    }
    for path in Path(root).rglob("*"):
        if not path.is_file() or any(part in skip_dirs for part in path.parts):
            continue
        if path.name in skip_files:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        markers = scan_text(text)
        if markers:
            findings.append(f"{path}: {','.join(markers)}")
    return findings
