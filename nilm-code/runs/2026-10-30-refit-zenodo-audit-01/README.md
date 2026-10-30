# Hồ sơ lần chạy: 2026-10-30-refit-zenodo-audit-01

Trạng thái: **exploratory (thăm dò)**  
Mã và phiên bản protocol: không có protocol — đây là kiểm tra truy cập và chất lượng dữ liệu được phép trước khi chốt giao thức (`AGENTS.md` gốc, mục “Cổng bàn giao”). Đầu vào: `nilm-document/synthesis/NILM-Questions/Audit dữ liệu và mặt nạ C3.md` (trạng thái `proposed`).  
Mục đích và thay đổi so với protocol: mô tả dữ liệu REFIT bản làm sạch (khoảng thời gian, khoảng cách lấy mẫu, thiếu dữ liệu, cột `Issues`, tỷ lệ ΣIAM > Aggregate). Không chọn hộ, không loại mẫu, không chốt dung sai hay mặt nạ C3, không huấn luyện mô hình.  
Thời điểm bắt đầu/kết thúc và múi giờ: xem `env/start_utc.txt`, `env/end_utc.txt` (UTC).

## Nguồn gốc

- Phiên bản code: commit gốc `285dd3d` (xem `env/git_state.txt`); `nilm-code/audit/` **chưa commit**. SHA-256 của script, `pyproject.toml`, `uv.lock` tại thời điểm chạy nằm trong `env/code_sha256.txt`.
- Dataset: *REFIT: Electrical Load Measurements (Cleaned)*, Zenodo record 5063428, DOI [10.5281/zenodo.5063428](https://doi.org/10.5281/zenodo.5063428), giấy phép CC BY 4.0, truy cập mở; ngày công bố ghi trên Zenodo 2016-06-16, record tạo 2021-07-03. Truy cập ngày 2026-10-30. **Chỉ gồm 6 hộ: 1, 2, 3, 4, 5, 11** (6 tệp `CLEAN_House*.csv`, tổng 2.220.373.115 byte). Kích thước, SHA-256, MD5 và kết quả đối chiếu MD5 với Zenodo: `outputs/data_manifest.json` (6/6 khớp).
- Quan hệ với bản trên kho Strathclyde: chưa xác minh. Hồ sơ Strathclyde của bản sạch (DOI 10.15129/9ab14b0e-19ac-4279-938f-27f643078cec) liệt kê `Processed_Data_CSV.7z` (489 MB), `CLEAN_REFIT_081116.7z` (490 MB), `REFIT_Readme.txt`, `CLEAN_READ_ME_081116.txt`, `MetaData_Tables.xlsx`, đều CC BY 4.0, nhưng tải tự động bị chặn bởi trang thử thách chống bot nên không tải. Ngày 2016-06-16 trùng ngày gửi bản `Processed_Data_CSV`, nhưng không có checksum để khẳng định bản Zenodo là bản nào; bản `081116` (11/2016) có thể khác.
- Cấu hình/định nghĩa: không có mô hình/loss. Định nghĩa thống kê nằm trong docstring `nilm-code/audit/refit_audit.py` và `outputs/definitions.json`.
- Seed: không dùng ngẫu nhiên. Môi trường: `env/environment.txt` (uv 0.12.7, Python 3.14.7, Windows 11), `env/pip_freeze.txt` (pandas 3.1.0, pyarrow 26.0.0, numpy 2.5.4).
- Lệnh tái lập (chạy tại gốc repo):

```bash
uv sync
# Tải dữ liệu (mỗi hộ một tệp; URL chính thức của Zenodo)
mkdir -p nilm-code/data/raw/refit/zenodo-5063428
for h in 1 2 3 4 5 11; do
  curl -L -o nilm-code/data/raw/refit/zenodo-5063428/CLEAN_House$h.csv \
    "https://zenodo.org/api/records/5063428/files/CLEAN_House$h.csv/content"
done
R=nilm-code/runs/2026-10-30-refit-zenodo-audit-01
uv run python -I nilm-code/audit/refit_manifest.py --data-dir nilm-code/data/raw/refit/zenodo-5063428 \
  --zenodo-record 5063428 --out $R/outputs/data_manifest.json
uv run python -I nilm-code/audit/refit_audit.py --data-dir nilm-code/data/raw/refit/zenodo-5063428 \
  --out-dir $R/outputs
```

> Chú thích sau (2026-10-30, không thuộc bản ghi gốc): `nilm-code/audit/refit_manifest.py` đã bị dời khỏi `audit/` (bản trùng SHA-256 được tìm thấy ở `nilm-code/data/refit_manifest.py`), và cả hai script đã được thay bằng cấu trúc `nilm-code/src/`; lệnh tương đương mới (tại `nilm-code/`): `uv run python -m src.experiments.e000_refit_data_audit.run --run-id <run-id>` rồi `uv run python -m src.experiments.e000_refit_data_audit.analyze --run-id <run-id>`; đối chiếu đầu ra ở run `2026-10-30-refit-zenodo-audit-02`.

## Tệp đầu ra

- Log và mã thoát: `manifest.log`, `audit.log` (cả hai `exit 0`).
- Đầu ra theo mẫu: không lưu (chỉ thống kê mô tả).
- Thống kê gốc (sinh bởi script, không sửa tay), trong `outputs/`:
  - `per_house_summary.csv` — một dòng/hộ: khoảng thời gian, số dòng, phân vị `dt`, khoảng trống, NaN, Aggregate âm/bằng 0, IAM âm, ΣIAM > Aggregate và độ lớn vượt, đối chiếu cột `Issues`, cờ `solar_affected_murray2017`.
  - `sampling_interval_bins.csv` — phân bố `dt` theo khoảng.
  - `excess_threshold_sensitivity.csv` — tỷ lệ vượt ở nhiều ngưỡng tuyệt đối/tương đối (thăm dò).
  - `per_channel.csv` — theo kênh: NaN, tỷ lệ 0, âm, > 4000 W, trung bình, max, q99.
  - `monthly_excess.csv`, `hourly_excess.csv` — tỷ lệ vượt theo tháng (Unix, UTC) và theo giờ của cột `Time`.
  - `definitions.json`, `summary_table.md` (bảng tóm tắt sinh tự động), `data_manifest.json`.
- Checkpoint: không áp dụng.

## Xác minh và diễn giải

- Kiểm tra đã thực hiện: (1) MD5 6/6 tệp khớp metadata Zenodo (`outputs/data_manifest.json`); (2) script được chạy lại lần hai trên cùng máy vào thư mục tạm, 8/8 tệp đầu ra trùng byte (`rerun_check.log`); (3) cột `Issues` được tính lại theo định nghĩa của `IssuesHighlight.m` (kho GitHub David-Murray/REFIT, commit `6683601`, đọc dạng văn bản, không chạy) — số mẫu lệch giữa `Issues` và phép tính lại là 0 ở cả 6 hộ.
- Tái lập độc lập: **chưa** (chỉ tái chạy cùng máy, cùng môi trường). Vì vậy run giữ trạng thái thăm dò.
- Giới hạn và điều chưa biết:
  - Chỉ có 6/20 hộ; hộ 21 (nhiễu điện mặt trời theo Murray 2017) **không có** trong bản này.
  - Chưa có README/metadata kèm bản dữ liệu: tên thiết bị của `Appliance1..9` theo hộ và lịch đổi thiết bị chưa biết. Bảng 3 của bài báo chỉ liệt kê loại thiết bị theo hộ, không cho ánh xạ kênh.
  - Bản sạch đã điền NaN (điền tiến < 2 phút, gán 0 nếu dài hơn) và đặt IAM > 4000 W về 0 (theo mô tả trên hồ sơ Strathclyde và `GapFilling.m`, `SpikeRemoval.m`). Do đó `frac_any_nan = 0` không chứng minh không có dữ liệu thiếu; khoảng thiếu xuất hiện dưới dạng khoảng nhảy `dt` hoặc giá trị 0 không phân biệt được với thiết bị tắt.
  - Cột `Time` trùng với `Unix` diễn giải theo UTC ở mọi dòng (`time_minus_unix_offset_hours_counts`); việc cột `Time` là UTC hay giờ địa phương đã chỉnh BST chưa được xác minh với README.
  - `dt` có phân vị 1%–99% từ 1 đến 14–16 s, trung vị 7 s (chu kỳ danh nghĩa 8 s): dấu thời gian không đều; chưa áp dụng căn chỉnh nào. Độ lệch đến 7 s giữa IAM và tổng (Murray 2017) chưa được xử lý.
  - Aggregate có giá trị cực đại 24–66 kW và hàng nghìn đến hàng chục nghìn mẫu > 4000 W mỗi hộ (`per_channel.csv`); chưa đánh giá là đỉnh bất thường hay tải thật.
- Nhận định được run này hỗ trợ: chỉ là thống kê mô tả của 6 tệp nói trên dưới các định nghĩa đã ghi. Không phải phát hiện nghiên cứu và không phải mặt nạ C3.
