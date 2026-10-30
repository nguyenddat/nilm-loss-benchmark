# Nhóm nghiên cứu Codex

Ba agent chuyên trách trong `agents/` tương ứng với ba giai đoạn nghiên cứu. Codex đọc cấu hình dự án ở `config.toml` và quy tắc điều phối ở `../AGENTS.md` khi mở repo này. Mọi ghi chú, tài liệu và file `AGENTS.md` trong repo phải viết bằng tiếng Việt có dấu.

| Agent | Mô hình | Trách nhiệm | Đầu ra bàn giao |
| --- | --- | --- | --- |
| `document` | `gpt-6-luna`, medium | Đọc, xác minh, ghi chú và tổng hợp tài liệu trong vault Obsidian `nilm-document/` | Câu hỏi/giả thuyết và đặc tả thí nghiệm có nguồn |
| `code` | `gpt-6.1-terra`, high | Hiện thực, kiểm tra, chạy và lưu thí nghiệm trong `nilm-code/` | Kết quả đã xác minh, cấu hình, lệnh tái lập, giới hạn |
| `paper` | `gpt-6-luna`, high | Viết và rà soát bản thảo trong `nilm-paper/` | Bản thảo với nhận định truy ngược được về nguồn và lần chạy |

Ví dụ yêu cầu: “Nhờ `document` đọc các bài báo về hàm mất mát cho NILM và cập nhật vault; sau đó `code` thiết kế và chạy benchmark từ các ghi chú đã rà soát; cuối cùng `paper` viết bản thảo từ kết quả đã xác minh.”

Giai đoạn đọc và tổng hợp tài liệu cần đủ bằng chứng trước khi khóa thiết kế benchmark; xem [lộ trình tổng quan tài liệu](../nilm-document/synthesis/literature-review-plan.md). Ba giai đoạn phụ thuộc vào nhau nên chỉ chạy song song các phần độc lập. Cấu hình cho phép tối đa hai subagent đồng thời và mặc định dùng Luna medium cho các subagent khác; nó không tự khởi chạy các thí nghiệm hoặc tạo nội dung nghiên cứu. Nếu workspace không cấp quyền dùng một model, đổi giá trị `model` trong file agent tương ứng sang model có sẵn trước khi giao việc.
