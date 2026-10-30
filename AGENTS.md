# Quy trình nhóm nghiên cứu

Repo có ba agent Codex trong `.codex/agents/`: `document`, `code` và `paper`. Giao các công việc đáng kể cho agent phụ trách đúng khu vực. Agent chính điều phối việc bàn giao và kiểm tra kết quả cuối. Nếu công việc chỉ thuộc một khu vực, hãy giao cho agent chuyên trách khi có thể. Với công việc liên khu vực, chỉ làm song song các phần có đầu vào đã ổn định; các phần phụ thuộc nhau phải theo chuỗi bằng chứng bên dưới. Các agent dùng chung workspace nên không cùng lúc sửa một file.

1. `document` quản lý vault Obsidian trong `nilm-document/`: ghi chú tài liệu đã xác minh, vị trí bằng chứng trong nguồn, tổng hợp và câu hỏi thí nghiệm.
2. `code` chuyển câu hỏi đã ghi thành giao thức, mã nguồn, kiểm tra và kết quả chạy có thể tái lập trong `nilm-code/`.
3. `paper` soạn và kiểm tra bản thảo trong `nilm-paper/` từ ghi chú đã rà soát và kết quả chạy đã xác minh.

Không chuyển một nhận định sang giai đoạn sau nếu thiếu bằng chứng: nhận định từ tài liệu cần nguồn và vị trí; nhận định thực nghiệm cần mã lần chạy, cấu hình, đầu ra gốc và trạng thái xác minh. Ghi rõ điều chưa biết. Agent chính giải quyết xung đột về phạm vi và quy trình, đồng thời báo phần bằng chứng còn thiếu thay vì điền nội dung có vẻ hợp lý.

Đọc `README.md` trong thư mục cần sửa trước khi làm việc. Giữ cấu trúc mẫu ghi chú Obsidian hiện có và phân biệt câu hỏi nghiên cứu được đề xuất với kết quả đã chứng minh. Mọi ghi chú, tài liệu hướng dẫn và file `AGENTS.md` trong repo phải bằng tiếng Việt có dấu; chỉ giữ nguyên tên riêng, thuật ngữ, ký hiệu, tên trường dữ liệu và cú pháp kỹ thuật khi cần. Ngôn ngữ của bản thảo công bố được quyết định riêng theo nơi nộp bài.

## Bài toán nghiên cứu hiện tại

Đề xuất hiện tại, “Beyond Accuracy: An Empirical Study of Loss Functions and Physical Constraint Violations in Non-Intrusive Load Monitoring”, hỏi việc chọn hàm mất mát ảnh hưởng thế nào đến dự đoán công suất thiết bị, hành vi theo thời gian và tính nhất quán vật lý trong một quy trình NILM được kiểm soát. Các ràng buộc dự kiến gồm công suất không âm, giới hạn công suất thiết bị khi có căn cứ độc lập, và giới hạn theo công suất tổng chỉ trên các mẫu có ngữ nghĩa đo lường phù hợp. REFIT là bộ dữ liệu thực được đề xuất làm nguồn chính; tín hiệu tổng hợp có kiểm soát là nguồn bổ sung. Đây là kế hoạch, chưa phải phát hiện hay thiết kế benchmark đã chốt. Đọc ghi chú đề xuất trong `nilm-document/` trước khi diễn giải hoặc thay đổi phạm vi nghiên cứu.

Mỗi khu vực có `AGENTS.md` riêng. Tuân theo file tương ứng về đầu ra và kiểm tra. Chuyển các quyết định giao thức chưa giải quyết về agent chính trước khi dùng chúng làm cơ sở cho kết quả hoặc nhận định trong paper.

Dùng môi trường `uv` ở gốc repo cho công cụ Python: `uv sync` để dựng `.venv/`, `uv run python ...` để chạy. Khi cần thư viện mới, thêm bằng `uv add` để cập nhật tệp khóa; không cài phụ thuộc chỉ trong môi trường cá nhân rồi quên khai báo.

## Cổng bàn giao từ tài liệu sang thí nghiệm

Đọc và tổng hợp tài liệu là phần việc chính của dự án, không phải bước chuẩn bị ngắn. Trước khi chốt giao thức benchmark, `document` phải xây dựng bản tổng quan có thể truy vết cho dữ liệu và cách đánh giá NILM, các họ mô hình, hàm mất mát, ràng buộc vật lý và độ vững trước dịch chuyển phân phối. Ghi rõ chiến lược tìm kiếm, tiêu chí chọn/loại, nguồn gốc và vị trí của từng nhận định, điểm đồng thuận hoặc mâu thuẫn, và khoảng trống nghiên cứu. Không đặt chỉ tiêu số bài cố định thay cho mức bao phủ bằng chứng.

`code` có thể kiểm tra khả năng truy cập và chất lượng dữ liệu trong lúc đọc tài liệu, nhưng chỉ khóa tổ hợp mô hình–loss, giả thuyết, thước đo và cách diễn giải khi bản tổng hợp liên quan đã được rà soát. `paper` chỉ dùng bằng chứng tài liệu đã rà soát và kết quả thực nghiệm đã xác minh. Lộ trình chi tiết nằm trong `nilm-document/synthesis/literature-review-plan.md`.

