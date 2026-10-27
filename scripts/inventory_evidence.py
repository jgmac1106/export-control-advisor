#!/usr/bin/env python3
"""Inventory user-supplied exports without parsing, changing, or uploading them."""
import argparse
import hashlib
import json
import os
import stat
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0.0"
FIELDS = ("source_system", "tenant", "collected_at", "period_start", "period_end",
          "query_or_method", "collector_version", "collected_by", "data_handling",
          "collection_status")

def inventory(root, output, engagement, metadata=None):
    root = Path(root).resolve(strict=True)
    output = Path(output).resolve()
    if not root.is_dir():
        raise ValueError("Input must be a directory")
    if output == root or root in output.parents:
        raise ValueError("Output must be outside the input directory")
    if output.exists():
        raise ValueError("Output already exists; choose a new run directory")
    if not isinstance(engagement, str) or not engagement.strip():
        raise ValueError("Engagement identifier must not be empty")
    metadata = {} if metadata is None else metadata
    if not isinstance(metadata, dict):
        raise ValueError("Metadata must be an object keyed by relative file path")
    for key, value in metadata.items():
        if not isinstance(key, str) or not isinstance(value, dict):
            raise ValueError("Each metadata entry must be an object")
        if Path(key).is_absolute() or ".." in Path(key).parts or "\\" in key:
            raise ValueError("Metadata paths must be relative POSIX paths")
        if set(value) - set(FIELDS):
            raise ValueError("Unknown metadata fields for " + key)
        if any(v is not None and not isinstance(v, str) for v in value.values()):
            raise ValueError("Metadata values must be strings or null")
        if value.get("collection_status") not in (None, "complete", "partial", "failed", "unknown"):
            raise ValueError("Invalid collection_status for " + key)
    entries, issues = [], []
    def walk_error(error):
        issues.append({"path": str(Path(error.filename).relative_to(root)), "reason": "directory_unreadable"})
    for base, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        dirs.sort(); files.sort()
        for name in list(dirs):
            path = Path(base) / name
            if path.is_symlink():
                dirs.remove(name)
                issues.append({"path": path.relative_to(root).as_posix(), "reason": "symlink_skipped"})
        for name in files:
            path = Path(base) / name
            rel = path.relative_to(root).as_posix()
            try:
                info = path.lstat()
                if not stat.S_ISREG(info.st_mode):
                    issues.append({"path": rel, "reason": "nonregular_file_skipped"}); continue
                digest = hashlib.sha256()
                # O_NOFOLLOW prevents following a file symlink swapped after lstat on supported OSs.
                fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
                with os.fdopen(fd, "rb") as stream:
                    before = os.fstat(stream.fileno())
                    if not stat.S_ISREG(before.st_mode):
                        raise ValueError("not_regular")
                    for block in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(block)
                    after = os.fstat(stream.fileno())
                if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                    issues.append({"path": rel, "reason": "changed_during_read"}); continue
            except (OSError, ValueError):
                issues.append({"path": rel, "reason": "unreadable_or_changed"}); continue
            supplied = metadata.get(rel, {})
            entry = {"evidence_id": "EV-" + hashlib.sha256(rel.encode()).hexdigest()[:16],
                     "relative_path": rel, "sha256": digest.hexdigest(), "size_bytes": after.st_size,
                     "provenance": {field: supplied.get(field) for field in FIELDS},
                     "provenance_status": "user_reported" if supplied else "not_provided",
                     "review_status": "not_assessed", "mappings": []}
            entries.append(entry)
    seen = {e["relative_path"] for e in entries}
    for key in sorted(set(metadata) - seen):
        issues.append({"path": key, "reason": "metadata_without_inventoried_file"})
    manifest = {"schema_version": "1.0", "engagement_id": engagement,
                "inventory_created_at": datetime.now(timezone.utc).isoformat(),
                "inventory_tool_version": VERSION, "entries": entries, "issues": issues,
                "inventory_status": "with_issues" if issues else "complete"}
    output.mkdir(parents=True, exist_ok=False)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    gaps = [{"evidence_id": e["evidence_id"], "missing_provenance": [k for k,v in e["provenance"].items() if not v]}
            for e in entries if any(not v for v in e["provenance"].values())]
    (output / "intake-gaps.json").write_text(json.dumps(gaps, indent=2) + "\n", encoding="utf-8")
    (output / "run-summary.md").write_text(
        "# Evidence inventory\n\n" + str(len(entries)) + " files inventoried; " + str(len(issues)) + " collection issues.\n\n"
        "Content and controls have not been assessed. Hashes identify bytes at intake; they do not authenticate the source. "
        "Inventory time is not source collection time. Consult manifest.json and intake-gaps.json.\n", encoding="utf-8")
    return manifest

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--engagement", required=True, help="Non-sensitive engagement identifier")
    parser.add_argument("--metadata", help="Optional JSON object keyed by relative file path")
    args = parser.parse_args()
    try:
        metadata = json.loads(Path(args.metadata).read_text(encoding="utf-8")) if args.metadata else None
        result = inventory(args.input, args.output, args.engagement, metadata)
    except (OSError, ValueError) as error:
        parser.exit(2, "Inventory failed: " + str(error) + "\n")
    print(str(len(result["entries"])) + " files inventoried; " + str(len(result["issues"])) + " issues")
    return 1 if result["issues"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
