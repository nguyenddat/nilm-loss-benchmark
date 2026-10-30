# Mã nguồn NILM

Lưu phần chuẩn bị dữ liệu, hiện thực loss, script huấn luyện/đánh giá, cấu hình và đầu ra thí nghiệm có thể tái lập tại đây.

Trước khi thêm thí nghiệm, ghi phiên bản dataset, cách chia tập, seed, định nghĩa metric và lệnh cần dùng để tái lập từng kết quả. Chỉ dùng đầu ra thăm dò làm bằng chứng cho paper sau khi đã tái lập được.

## Bắt đầu một thí nghiệm

1. Đọc [AGENTS.md](AGENTS.md), bản đề xuất và ghi chú đã review liên quan trong `../nilm-document/`.
2. Sao chép [mẫu protocol](templates/experiment-protocol.md) vào `protocols/` và chốt những lựa chọn cần thiết cho phép so sánh công bằng.
3. Hiện thực và kiểm tra code dữ liệu, mô hình, loss và đánh giá cần thiết. Ghi lệnh tái lập và nguồn gốc.
4. Tạo `runs/<run-id>/` cho mỗi lần chạy và điền [hồ sơ run](templates/run-record.md), giữ liên kết truy xuất giữa cấu hình, log, đầu ra thô và bảng tổng hợp.
5. Xác minh kết quả trước khi bàn giao cho `../nilm-paper/`; giữ cả các run thất bại và thăm dò kèm trạng thái.

## Cấu trúc hiện có

Quy ước đầy đủ: mục “Cấu trúc mã nguồn” trong [AGENTS.md](AGENTS.md).

- `src/core/`: đường dẫn dùng chung.
- `src/data/refit/`: đọc CSV REFIT bản làm sạch (`load.py`), manifest kích thước + SHA-256/MD5 đối chiếu Zenodo (`manifest.py`), thống kê chất lượng theo hộ (`quality.py`).
- `src/experiments/e000_refit_data_audit/`: audit thăm dò REFIT (không huấn luyện mô hình). Chạy tại `nilm-code/`:
  `uv run python -m src.experiments.e000_refit_data_audit.run --run-id <run-id>` rồi `uv run python -m src.experiments.e000_refit_data_audit.analyze --run-id <run-id>`.
- `data/raw/refit/zenodo-5063428/`: CSV REFIT bản làm sạch từ Zenodo (CC BY 4.0), git bỏ qua. Không đặt hay chạy code trong `data/`.
- `outputs/experiments/<experiment_id>/<run-id>/`: đầu ra gốc của từng run.
- `runs/<run-id>/`: hồ sơ lần chạy theo `templates/run-record.md`. Run `2026-10-30-refit-zenodo-audit-01` (script cũ, đầu ra nằm trong hồ sơ) là bản ghi lịch sử; run `...-02` chạy bằng cấu trúc mới và đối chiếu với run 01.

Chỉ tạo `protocols/`, `docs/`, `src/methods/`, `src/metrics/` khi có nhu cầu thực tế. Các mẫu chỉ hỗ trợ lập kế hoạch và không chứa kết quả thực nghiệm.
