"""Đường dẫn dùng chung của workspace `nilm-code/` (suy ra từ vị trí tệp, không phụ thuộc thư mục làm việc)."""

from __future__ import annotations

from pathlib import Path

CODE_ROOT = Path(__file__).resolve().parents[2]  # nilm-code/
REPO_ROOT = CODE_ROOT.parent
DATA_RAW = CODE_ROOT / "data" / "raw"
OUTPUTS = CODE_ROOT / "outputs"
RUNS = CODE_ROOT / "runs"


def repo_relative(path: Path) -> str:
    """Đường dẫn dạng POSIX tính từ gốc repo, dùng khi ghi vào đầu ra để không lộ đường dẫn tuyệt đối."""
    return path.resolve().relative_to(REPO_ROOT).as_posix()
