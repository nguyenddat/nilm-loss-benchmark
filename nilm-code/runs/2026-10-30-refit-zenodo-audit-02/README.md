# Hồ sơ lần chạy: 2026-10-30-refit-zenodo-audit-02

Trạng thái: **exploratory (thăm dò)**  
Mã và phiên bản protocol: không có protocol — kiểm tra truy cập và chất lượng dữ liệu trước khi chốt giao thức (`AGENTS.md` gốc, mục “Cổng bàn giao”). Experiment: `src/experiments/e000_refit_data_audit/`.  
Mục đích và thay đổi so với protocol: kiểm chứng việc tái cấu trúc `audit/refit_manifest.py` + `audit/refit_audit.py` (run `2026-10-30-refit-zenodo-audit-01`) sang `src/data/refit/` và `src/experiments/e000_refit_data_audit/` **không đổi hành vi**. Cùng dữ liệu, định nghĩa, ngưỡng và môi trường như run 01. Không chọn hộ, không loại mẫu, không chốt mặt nạ C3, không huấn luyện mô hình.  
Thời điểm bắt đầu/kết thúc và múi giờ: `env/start_utc.txt`, `env/end_utc.txt` (UTC).

## Nguồn gốc

- Phiên bản code: commit gốc `285dd3d` (`env/git_state.txt`); `nilm-code/src/` **chưa commit**. SHA-256 của mọi tệp `.py` trong `src/`, `pyproject.toml`, `uv.lock` lúc chạy: `env/code_sha256.txt` (`pyproject.toml`, `uv.lock` trùng run 01).
- Dataset: REFIT bản làm sạch, Zenodo record 5063428 (DOI 10.5281/zenodo.5063428, CC BY 4.0), 6 hộ 1, 2, 3, 4, 5, 11; cùng 6 tệp CSV như run 01 (SHA-256 trong `data_manifest.json` trùng, MD5 6/6 khớp Zenodo). Chi tiết nguồn và giới hạn: xem README run 01.
- Cấu hình: `src/experiments/e000_refit_data_audit/config.py` (danh sách hộ, ngưỡng thăm dò, `DEFINITIONS`). Định nghĩa thống kê: docstring `src/data/refit/quality.py` và `definitions.json`.
- Seed: không dùng ngẫu nhiên. Môi trường: `env/environment.txt` (uv 0.12.7, Python 3.14.7, Windows 11), `env/pip_freeze.txt` (trùng run 01).
- Lệnh tái lập (tải dữ liệu như README run 01; sau đó chạy tại `nilm-code/`):

```bash
uv sync
cd nilm-code
uv run python -m src.experiments.e000_refit_data_audit.run --run-id 2026-10-30-refit-zenodo-audit-02
uv run python -m src.experiments.e000_refit_data_audit.analyze --run-id 2026-10-30-refit-zenodo-audit-02
```

`run.py` từ chối ghi vào thư mục đầu ra đã có tệp; khi chạy lại hãy dùng run ID mới. Không dùng `-I` vì `-m src...` cần thư mục làm việc `nilm-code/` trên `sys.path`; thư mục này chỉ chứa mã của repo, không chứa dữ liệu tải về.

## Tệp đầu ra

- Log và mã thoát: `run.log` (`run exit 0`), `analyze.log` (`analyze exit 0`).
- Đầu ra gốc: `nilm-code/outputs/experiments/e000_refit_data_audit/2026-10-30-refit-zenodo-audit-02/` — `data_manifest.json`, `per_house_summary.csv`, `sampling_interval_bins.csv`, `excess_threshold_sensitivity.csv`, `per_channel.csv`, `monthly_excess.csv`, `hourly_excess.csv`, `definitions.json` (sinh bởi `run.py`); `summary_table.md` (sinh bởi `analyze.py` từ `per_house_summary.csv`).
- Đầu ra theo mẫu, checkpoint: không áp dụng.

## Xác minh và diễn giải

- So sánh với run 01 (`compare_with_run01.log`, `cmp` từng byte, cùng 9 tệp, không thừa/thiếu tệp):
  - Trùng byte 7/9: `definitions.json`, `excess_threshold_sensitivity.csv`, `hourly_excess.csv`, `monthly_excess.csv`, `per_channel.csv`, `per_house_summary.csv`, `sampling_interval_bins.csv`.
  - `data_manifest.json`: khác đúng một dòng `generated_utc` (thời điểm lập manifest). Các trường còn lại, gồm `data_dir`, metadata Zenodo, SHA-256/MD5 và kết quả đối chiếu, trùng.
  - `summary_table.md`: khác đúng dòng chú thích đầu (`refit_audit.py` → `src/experiments/e000_refit_data_audit/analyze.py`, tên script sinh tệp). Các dòng bảng trùng; bảng hiện được dựng lại từ `per_house_summary.csv` đã lưu thay vì từ DataFrame trong bộ nhớ.
  - Bảng in ra trong `analyze.log` trùng bảng trong `audit.log` của run 01.
- Kết luận: tái cấu trúc tương đương run 01 về mọi thống kê. Đây vẫn là chạy lại trên cùng máy, cùng môi trường, nên chưa phải tái lập độc lập; run giữ trạng thái thăm dò.
- Giới hạn và điều chưa biết: như run 01 (6/20 hộ, chưa có metadata ánh xạ kênh, múi giờ cột `Time` chưa xác minh, dữ liệu thiếu bị che bởi bước làm sạch, chưa căn chỉnh thời gian).
- Nhận định được run này hỗ trợ: mã mới cho cùng thống kê mô tả như run 01. Không phải phát hiện nghiên cứu và không phải mặt nạ C3.
