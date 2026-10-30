"""Manifest tệp REFIT cục bộ: kích thước, SHA-256, MD5 và đối chiếu với metadata Zenodo.

Định dạng đầu ra giữ nguyên như `data_manifest.json` của run 2026-10-30-refit-zenodo-audit-01.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import urllib.request
from pathlib import Path


def hash_file(path: Path, chunk: int = 1 << 22) -> tuple[str, str]:
    sha = hashlib.sha256()
    md5 = hashlib.md5()
    with path.open("rb") as fh:
        while block := fh.read(chunk):
            sha.update(block)
            md5.update(block)
    return sha.hexdigest(), md5.hexdigest()


def fetch_zenodo(record: str) -> dict:
    url = f"https://zenodo.org/api/records/{record}"
    with urllib.request.urlopen(url, timeout=60) as resp:  # noqa: S310 - URL cố định
        return json.load(resp)


def build_manifest(data_dir: Path, data_dir_label: str, zenodo_record: str | None) -> dict:
    """Lập manifest cho mọi `*.csv` trong `data_dir`; `data_dir_label` là chuỗi đường dẫn ghi vào đầu ra."""
    remote: dict[str, dict] = {}
    record_meta = None
    if zenodo_record:
        rec = fetch_zenodo(zenodo_record)
        record_meta = {
            "id": rec.get("id"),
            "doi": rec.get("doi"),
            "conceptdoi": rec.get("conceptdoi"),
            "title": rec["metadata"].get("title"),
            "publication_date": rec["metadata"].get("publication_date"),
            "license": rec["metadata"].get("license"),
            "access_right": rec["metadata"].get("access_right"),
            "creators": [c.get("name") for c in rec["metadata"].get("creators", [])],
            "updated": rec.get("updated"),
            "api_url": f"https://zenodo.org/api/records/{zenodo_record}",
        }
        for f in rec.get("files", []):
            remote[f["key"]] = {"size": f["size"], "checksum": f.get("checksum")}

    files = []
    for path in sorted(data_dir.glob("*.csv")):
        sha, md5 = hash_file(path)
        entry = {
            "file": path.name,
            "size_bytes": path.stat().st_size,
            "sha256": sha,
            "md5": md5,
        }
        if path.name in remote:
            r = remote[path.name]
            entry["zenodo_size_bytes"] = r["size"]
            entry["zenodo_checksum"] = r["checksum"]
            entry["size_matches_zenodo"] = r["size"] == entry["size_bytes"]
            entry["md5_matches_zenodo"] = r["checksum"] == f"md5:{md5}"
        files.append(entry)

    return {
        "generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "data_dir": data_dir_label,
        "zenodo_record": record_meta,
        "remote_files_not_present_locally": sorted(set(remote) - {f["file"] for f in files}),
        "files": files,
    }


def write_manifest(manifest: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
