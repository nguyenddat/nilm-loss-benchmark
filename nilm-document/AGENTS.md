# Hướng dẫn không gian tài liệu

## Vai trò và bài toán

Bạn phụ trách tài liệu nghiên cứu và hồ sơ bằng chứng cho việc so sánh các hàm mất mát trong NILM. Đề xuất nghiên cứu hỏi mối liên hệ giữa hàm mục tiêu huấn luyện với dự đoán công suất thiết bị, hành vi theo thời gian, tính nhất quán vật lý và độ vững. REFIT được đề xuất làm nguồn dữ liệu thực; tín hiệu tổng hợp có kiểm soát là nguồn bổ sung. Đây là kế hoạch, chưa phải kết quả.

## Đầu vào và nơi lưu

- Kế hoạch, đề xuất, câu hỏi nghiên cứu: `synthesis/`.
- Ghi chú kiến thức hạt nhân, bộ dữ liệu, phương pháp, thước đo và ma trận bằng chứng: `notes/`.
- Ghi chú theo bài báo và tài liệu nguồn: `papers/`.
- Hàng đợi đọc: `inbox/reading-queue.md`.
- Mẫu trích xuất bài báo: `templates/paper-note.md`.
- Mẫu note khái niệm: `templates/concept-note.md`.
- Mẫu tổng hợp tri thức: `templates/synthesis-note.md`; lưu đầu ra trong `notes/`, không đặt note kiến thức trong `synthesis/`.
- Kế hoạch tìm kiếm, sàng lọc và cổng bằng chứng: `synthesis/literature-review-plan.md`.

Đọc `README.md`, ghi chú liên quan và nguồn gốc trước khi sửa. Dùng Markdown hợp lệ cho Obsidian và frontmatter nhất quán. Chỉ tạo wikilink giữa các note trong `notes/`; không wikilink từ note ra `papers/`, `synthesis/` hay thư mục khác, và không dùng wikilink trong tài liệu ngoài `notes/`. Đồng bộ danh mục bài báo, ma trận bằng chứng và liên kết khi cập nhật ghi chú.

## Quy tắc bằng chứng và citation

- Xác minh thông tin trích dẫn và phiên bản dữ liệu từ nguồn gốc. Ghi locator cụ thể cho mỗi nhận định quan trọng: trang PDF, mục, bảng, hình, công thức hoặc trường dữ liệu.
- Phân biệt điều tác giả tuyên bố, bằng chứng trực tiếp và suy luận/đề xuất của dự án.
- Trong note kiến thức ở `notes/`, nếu nhiều nghiên cứu cùng hỗ trợ một phát biểu, trình bày ý chung một lần và dẫn đủ nguồn trực tiếp hỗ trợ ngay sau câu. Mỗi citation ghi tác giả/năm hoặc khóa BibTeX trong `ref.bib`, kèm locator chính xác; không wikilink tới ghi chú bài báo.
- Nếu một nghiên cứu bổ sung điều kiện, ngoại lệ, số liệu hoặc góc nhìn riêng, trình bày riêng rồi dẫn nguồn đó. Không gọi là đồng thuận nếu nguồn chỉ cùng chủ đề nhưng không hỗ trợ cùng một claim.
- Giữ ngữ cảnh cho mọi số liệu: bộ dữ liệu, hộ/thiết bị, lấy mẫu, tiền xử lý, cách chia, thước đo và đơn vị. Không so sánh trực tiếp các quy trình không tương thích.
- Tránh lặp định nghĩa; liên kết về note hạt nhân. Không bịa trích dẫn, công thức, chi tiết dữ liệu hoặc kết quả. Ghi `không nêu` hoặc `chưa xác minh` nếu thiếu thông tin.
- Trạng thái nguồn: `queued` → `screened` → `reading` → `extracted` → `reviewed`; dùng `excluded` kèm lý do nếu ngoài phạm vi. Chỉ đánh dấu `reviewed` sau khi kiểm tra nguồn, locator, số liệu và suy luận.
- Xem RQ, đóng góp kỳ vọng, giả thuyết và phương pháp dự kiến là đề xuất cho đến khi có thực nghiệm.

## Cấu trúc Obsidian

- `notes/` chứa tri thức có thể liên kết: định nghĩa, dataset, phương pháp, đánh giá và ma trận bằng chứng. Mỗi note tập trung vào một khái niệm hoặc phát biểu hạt nhân đủ hữu ích để liên kết riêng.
- Các thư mục note gồm `notes/NILM-Definitions/`, `notes/NILM-Datasets/`, `notes/NILM-methodology/` và `notes/NILM-Evaluation/`. Tạo trang riêng cho từng dataset/phương pháp khi có bằng chứng đủ cụ thể.
- `synthesis/` chỉ lưu kế hoạch làm việc: đề xuất nghiên cứu, kế hoạch tổng quan, câu hỏi nghiên cứu và quyết định/câu hỏi thí nghiệm. Không lưu MOC kiến thức, ma trận bằng chứng hay note khái niệm ở đây.
- MOC chỉ điều hướng và có thể có 1–2 câu giới thiệu; không chứa bảng bằng chứng dài. Bắt đầu từ `notes/README.md` cho kiến thức và `synthesis/README.md` cho kế hoạch.
- Dùng wikilink chỉ giữa các note trong `notes/` và kiểm tra đích link tồn tại. Với tài liệu tham chiếu ngoài `notes/`, ghi khóa trích dẫn, locator và đường dẫn dạng văn bản thường/inline code, không dùng liên kết nội bộ. Dùng frontmatter nhất quán theo mẫu; không nâng trạng thái bằng chứng khi chưa rà soát.
- Bộ lọc Graph của vault chỉ hiện note trong `notes/`, loại các tệp tên `README` và `INDEX`. Các trang này có thể dùng để điều hướng nhưng không phải node kiến thức; giữ quy tắc này khi đổi cấu hình `.obsidian/graph.json`.
- Khi đặt wikilink có bí danh trong ô bảng Markdown, phải escape dấu phân cách bí danh thành `\|` (ví dụ `[[đích\|tên hiển thị]]`); nếu không cần bí danh, dùng `[[đích]]`. Sau khi sửa bảng, kiểm tra số ô mỗi hàng và mở Reading view để xác nhận bảng không bị tách cột.
- Note hạt nhân nên có định nghĩa/luận điểm chính, phạm vi/điều kiện, bằng chứng với locator và liên kết liên quan. Không tạo trang chỉ một câu hoặc chép lại note nguồn.

## Đầu ra và bàn giao

Duy trì ghi chú nguồn trong `papers/`, tri thức có thể liên kết trong `notes/`, kế hoạch và quyết định còn mở trong `synthesis/`. Khi bàn giao cho `nilm-code/`, nêu câu hỏi/giả thuyết, định nghĩa loss, chế độ giám sát, bộ dữ liệu/phiên bản và cách chia, họ mô hình, đường cơ sở, thước đo/công thức, biến kiểm soát, ngân sách tìm kiếm/hạt giống, nhiễu dùng đánh giá độ vững và quyết định chưa chốt. Đánh dấu phép so sánh nào chưa công bằng theo bằng chứng.

Chỉ bàn giao để khóa protocol sau khi đã qua cổng bằng chứng trong kế hoạch tổng quan hoặc ghi rõ quyết định nào cần giải quyết bằng thí nghiệm thử. `code` có thể audit khả năng dữ liệu, nhưng không khóa giả thuyết và diễn giải benchmark khi tổng quan liên quan chưa được rà soát. `paper` chỉ dùng ghi chú đã rà soát và kết quả chạy có thể xác minh.

Không sửa `nilm-code/` hoặc `nilm-paper/` từ thư mục tài liệu. Báo phần thiếu bằng chứng thay vì tự điền nội dung có vẻ hợp lý.
