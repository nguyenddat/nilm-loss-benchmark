# Benchmark hàm mất mát cho NILM

Workspace lưu bằng chứng tài liệu, thí nghiệm có thể tái lập và bản thảo paper cho nghiên cứu về hàm mất mát và vi phạm ràng buộc vật lý trong Non-Intrusive Load Monitoring (NILM).

## Quy trình

1. Tìm, đọc, đối chiếu và tổng hợp tài liệu trong [vault Obsidian](nilm-document/README.md) theo [lộ trình tổng quan](nilm-document/synthesis/literature-review-plan.md). [Đề xuất nghiên cứu](nilm-document/synthesis/research-proposal.md) mô tả phạm vi dự kiến, chưa phải kết quả.
2. Khi bằng chứng đã đủ để biện minh cho lựa chọn mô hình, hàm mất mát và cách đánh giá, thiết kế giao thức, hiện thực và xác minh thí nghiệm trong [workspace mã nguồn](nilm-code/README.md).
3. Viết [bản thảo paper](nilm-paper/README.md) từ ghi chú đã rà soát và các lần chạy đã xác minh.

Ba agent Codex được cấu hình trong [.codex/](.codex/README.md). Xem [quy tắc điều phối](AGENTS.md) và `AGENTS.md` trong từng workspace trước khi giao việc.

## Môi trường Python

Dự án dùng `uv` và môi trường ảo `.venv/` ở gốc repo. Chạy `uv sync` để cài các thư viện đã khóa trong `uv.lock`; chạy công cụ Python bằng `uv run python ...`. Hiện môi trường chỉ khai báo PyMuPDF để đọc và chuyển đổi PDF. Khi thí nghiệm cần thêm thư viện, dùng `uv add <ten-goi>` để cập nhật cả `pyproject.toml` và `uv.lock`. Không đưa `.venv/` vào Git.

