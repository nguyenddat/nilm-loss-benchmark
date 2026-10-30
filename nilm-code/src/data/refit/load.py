"""Đọc CSV REFIT bản làm sạch (`CLEAN_House<N>.csv`) và các hằng số mô tả dataset.

Chỉ đọc tệp dữ liệu; không thực thi gì từ thư mục dữ liệu.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

IAM_COLS = [f"Appliance{i}" for i in range(1, 10)]
EXPECTED_COLS = ["Time", "Unix", "Aggregate", *IAM_COLS, "Issues"]
# Hộ chịu ảnh hưởng điện mặt trời theo Murray và cộng sự 2017 (mục Household aggregate, PDF tr. 4).
SOLAR_HOUSES_MURRAY2017 = {3, 11, 21}
# Ngưỡng đỉnh IAM mà bản làm sạch đặt về 0 (SpikeRemoval.m, hồ sơ Strathclyde).
IAM_SPIKE_LIMIT_W = 4000


def house_id(path: Path) -> int:
    m = re.search(r"House(\d+)", path.stem)
    if not m:
        raise ValueError(f"Không đọc được số hộ từ tên tệp {path.name}")
    return int(m.group(1))


def house_csv(data_dir: Path, house: int) -> Path:
    path = data_dir / f"CLEAN_House{house}.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy {path}")
    return path


def load(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, engine="pyarrow")
    missing = [c for c in EXPECTED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"{path.name}: thiếu cột {missing}; có {list(df.columns)}")
    for c in ["Unix", "Aggregate", *IAM_COLS, "Issues"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("float64")
    df["Time"] = pd.to_datetime(df["Time"], errors="coerce")
    return df
