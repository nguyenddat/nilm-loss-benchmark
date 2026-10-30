"""Thống kê mô tả chất lượng dữ liệu cho một hộ REFIT bản làm sạch.

Chỉ mô tả dữ liệu; không chọn hộ, không loại mẫu, không chốt dung sai hay mặt nạ C3.

Định nghĩa (đơn giản, có chủ ý):
- Một "mẫu" là một dòng của tệp CSV như được công bố; không lấy mẫu lại, không căn chỉnh lại.
- dt = hiệu liên tiếp của cột `Unix` (giây) theo thứ tự dòng trong tệp.
- S_t = Appliance1 + ... + Appliance9 (NaN được tính như thiếu: nếu có NaN thì S_t là NaN).
- excess_t = S_t - Aggregate_t (W). "ΣIAM > aggregate" nghĩa là excess_t > 0 (so sánh chặt,
  khớp với IssuesHighlight.m của tác giả: Issues = (Aggregate - ΣIAM) < 0).
- Các ngưỡng (khoảng dt, ngưỡng tuyệt đối/tương đối, ngưỡng khoảng trống, phân vị) do experiment
  truyền vào; chúng chỉ để thăm dò, KHÔNG phải dung sai đã chốt.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import pandas as pd

from src.data.refit.load import IAM_COLS, IAM_SPIKE_LIMIT_W, SOLAR_HOUSES_MURRAY2017, house_id, load


def qdict(s: pd.Series, prefix: str, quantiles: Sequence[float]) -> dict:
    s = s.dropna()
    if s.empty:
        return {f"{prefix}_q{int(q * 100):02d}": np.nan for q in quantiles}
    vals = s.quantile(quantiles).to_numpy()
    return {f"{prefix}_q{int(q * 100):02d}": float(v) for q, v in zip(quantiles, vals)}


def audit_house(
    path: Path,
    *,
    dt_bins: Sequence[float],
    dt_labels: Sequence[str],
    abs_thresholds_w: Sequence[float],
    rel_thresholds: Sequence[float],
    gap_thresholds_s: Sequence[float],
    quantiles: Sequence[float],
) -> dict[str, pd.DataFrame | dict]:
    """Trả về `summary` (dict một dòng) và các bảng `dt`, `thr`, `ch`, `monthly`, `hourly` cho một hộ."""
    h = house_id(path)
    df = load(path)
    n = len(df)
    unix = df["Unix"]
    dts = unix.diff().iloc[1:]
    span_s = float(unix.max() - unix.min()) if n else np.nan

    # Lệch giữa cột Time (chuỗi không kèm múi giờ) và Unix diễn giải theo UTC, làm tròn theo giờ.
    unix_dt = pd.to_datetime(unix, unit="s", errors="coerce")
    offset_h = ((df["Time"] - unix_dt).dt.total_seconds() / 3600).round()
    offset_counts = offset_h.value_counts(dropna=False).sort_index()

    agg = df["Aggregate"]
    iam = df[IAM_COLS]
    s_iam = iam.sum(axis=1, min_count=9)  # NaN nếu bất kỳ IAM nào là NaN
    excess = s_iam - agg
    valid = s_iam.notna() & agg.notna()
    nv = int(valid.sum())
    exc_pos = excess[valid & (excess > 0)]
    issues = df["Issues"]
    recomputed = (excess > 0) & valid

    summary = {
        "house": h,
        "file": path.name,
        "solar_affected_murray2017": h in SOLAR_HOUSES_MURRAY2017,
        "n_rows": n,
        "time_first": str(df["Time"].min()),
        "time_last": str(df["Time"].max()),
        "unix_first": float(unix.min()),
        "unix_last": float(unix.max()),
        "span_days": span_s / 86400,
        "n_time_unparsed": int(df["Time"].isna().sum()),
        "n_unix_nan": int(unix.isna().sum()),
        "n_dt_nonpositive": int((dts <= 0).sum()),
        "n_dt_zero_duplicate_unix": int((dts == 0).sum()),
        "n_dt_negative": int((dts < 0).sum()),
        "unix_monotonic_increasing": bool(unix.is_monotonic_increasing),
        **qdict(dts, "dt_s", quantiles),
        "rows_per_8s_of_span": n / (span_s / 8) if span_s else np.nan,
        "time_minus_unix_offset_hours_counts": json.dumps(
            {str(k): int(v) for k, v in offset_counts.items()}),
        "n_any_nan": int(df[["Aggregate", *IAM_COLS]].isna().any(axis=1).sum()),
        "frac_any_nan": float(df[["Aggregate", *IAM_COLS]].isna().any(axis=1).mean()),
        "n_agg_nan": int(agg.isna().sum()),
        "n_agg_negative": int((agg < 0).sum()),
        "n_agg_zero": int((agg == 0).sum()),
        "frac_agg_zero": float((agg == 0).mean()),
        "n_rows_all_zero": int(((agg == 0) & (iam == 0).all(axis=1)).sum()),
        "n_iam_negative_any": int((iam < 0).any(axis=1).sum()),
        f"n_iam_gt_{IAM_SPIKE_LIMIT_W}_any": int((iam > IAM_SPIKE_LIMIT_W).any(axis=1).sum()),
        "n_valid_for_excess": nv,
        "n_excess_gt0": int(len(exc_pos)),
        "frac_excess_gt0": len(exc_pos) / nv if nv else np.nan,
        "excess_gt0_mean_w": float(exc_pos.mean()) if len(exc_pos) else np.nan,
        **qdict(exc_pos, "excess_gt0_w", quantiles),
        "issues_values": json.dumps(
            {str(k): int(v) for k, v in issues.value_counts(dropna=False).sort_index().items()}),
        "n_issues_eq1": int((issues == 1).sum()),
        "n_issues1_and_recomputed": int(((issues == 1) & recomputed).sum()),
        "n_issues1_not_recomputed": int(((issues == 1) & ~recomputed).sum()),
        "n_issues0_but_recomputed": int(((issues != 1) & recomputed).sum()),
    }
    for g in gap_thresholds_s:
        big = dts[dts > g]
        summary[f"n_gaps_gt_{g}s"] = int(len(big))
        summary[f"gap_time_gt_{g}s_frac_of_span"] = float(big.sum() / span_s) if span_s else np.nan

    # Bảng phân bố dt
    binned = pd.cut(dts, bins=list(dt_bins), labels=list(dt_labels))
    dt_tab = binned.value_counts(sort=False).rename("n").reset_index()
    dt_tab.columns = ["dt_bin_s", "n"]
    dt_tab["frac"] = dt_tab["n"] / max(len(dts), 1)
    dt_tab.insert(0, "house", h)

    # Độ nhạy theo ngưỡng (thăm dò)
    rows = []
    for t in abs_thresholds_w:
        k = int((valid & (excess > t)).sum())
        rows.append({"house": h, "kind": "abs_w", "threshold": t, "n": k, "frac": k / nv if nv else np.nan})
    pos_agg = valid & (agg > 0)
    npa = int(pos_agg.sum())
    for r in rel_thresholds:
        k = int((pos_agg & (excess > r * agg)).sum())
        rows.append({"house": h, "kind": "rel_of_agg_where_agg_gt0", "threshold": r, "n": k,
                     "frac": k / npa if npa else np.nan, "denominator": npa})
    thr = pd.DataFrame(rows)

    # Theo kênh
    ch_rows = []
    for c in ["Aggregate", *IAM_COLS]:
        x = df[c]
        ch_rows.append({
            "house": h, "channel": c, "n_nan": int(x.isna().sum()),
            "frac_zero": float((x == 0).mean()), "n_negative": int((x < 0).sum()),
            f"n_gt_{IAM_SPIKE_LIMIT_W}": int((x > IAM_SPIKE_LIMIT_W).sum()), "mean_w": float(x.mean()),
            "max_w": float(x.max()), "q99_w": float(x.quantile(0.99)),
        })
    ch = pd.DataFrame(ch_rows)

    # Theo tháng (Unix diễn giải UTC) và theo giờ của cột Time (múi giờ chưa xác minh)
    month = unix_dt.dt.to_period("M").astype(str)
    g = pd.DataFrame({"month": month, "excess_gt0": recomputed, "valid": valid,
                      "issues1": issues == 1, "agg_zero": agg == 0})
    monthly = g.groupby("month").agg(n_rows=("valid", "size"), n_valid=("valid", "sum"),
                                     n_excess_gt0=("excess_gt0", "sum"),
                                     n_issues1=("issues1", "sum"), n_agg_zero=("agg_zero", "sum"))
    monthly["frac_excess_gt0"] = monthly["n_excess_gt0"] / monthly["n_valid"]
    monthly = monthly.reset_index()
    monthly.insert(0, "house", h)

    hour = df["Time"].dt.hour
    gh = pd.DataFrame({"hour_of_time_col": hour, "excess_gt0": recomputed, "valid": valid})
    hourly = gh.groupby("hour_of_time_col").agg(n_valid=("valid", "sum"), n_excess_gt0=("excess_gt0", "sum"))
    hourly["frac_excess_gt0"] = hourly["n_excess_gt0"] / hourly["n_valid"]
    hourly = hourly.reset_index()
    hourly.insert(0, "house", h)

    return {"summary": summary, "dt": dt_tab, "thr": thr, "ch": ch,
            "monthly": monthly, "hourly": hourly}
