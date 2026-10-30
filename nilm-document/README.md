# Kho tài liệu nghiên cứu NILM

Mở thư mục `nilm-document` trong Obsidian bằng lệnh **Open folder as vault** (Mở thư mục dưới dạng vault). Có thể đọc và sửa các ghi chú bằng Markdown; không cần plugin cộng đồng.

## Bắt đầu

1. Thêm bài báo mới vào hàng đợi đọc (`inbox/reading-queue.md`), kèm DOI hoặc URL nguồn.
2. Sao chép mẫu đọc bài báo (`templates/paper-note.md`) vào `papers/`, đặt tên `nam-tacgia-tu-khoa.md`. Ghi `không nêu` nếu nguồn không cung cấp thông tin.
3. Sau khi đọc, cập nhật danh mục bài báo (`papers/index.md`) và ma trận bằng chứng (`notes/literature-matrix.md`).
4. Theo dõi phạm vi và tiến độ ở kế hoạch nghiên cứu (kế hoạch: `synthesis/README`). Tạo note kiến thức theo mẫu note khái niệm (`templates/concept-note.md`); nếu cần tổng hợp một câu hỏi liên nguồn, dùng mẫu tổng hợp (`templates/synthesis-note.md`) và lưu kết quả trong `notes/`.

## Cấu trúc

- `inbox/`: hàng đợi đọc và nguồn chưa xử lý.
- `papers/`: ghi chú theo từng bài báo, PDF và bản toàn văn Markdown.
- `notes/`: ghi chú kiến thức hạt nhân, ma trận bằng chứng và trang điều hướng. Bắt đầu từ bản đồ ghi chú.
- `notes/NILM-Definitions/`: định nghĩa và phát biểu bài toán.
- `notes/NILM-Datasets/`: ghi chú riêng cho từng bộ dữ liệu.
- `notes/NILM-methodology/`: phương pháp, mô hình đối chứng và chế độ giám sát.
- `notes/NILM-Evaluation/`: thước đo, cách chia dữ liệu và ràng buộc.
- `synthesis/`: kế hoạch nghiên cứu, tổng quan tài liệu, câu hỏi và quyết định công việc. Bắt đầu từ bản đồ kế hoạch (kế hoạch: `synthesis/README`).
- `synthesis/NILM-Questions/`: câu hỏi thực nghiệm và đầu ra cần bàn giao cho code.
- `templates/`: mẫu note để sao chép thủ công.
- `assets/`: tệp đính kèm nếu cần; giữ nguyên nguồn và tên gắn với bài báo.

## Quy ước ghi chú và bằng chứng

- Mỗi note kiến thức tập trung vào một định nghĩa hoặc phát biểu hạt nhân đủ hữu ích để liên kết riêng. MOC chỉ điều hướng.
- Khi nhiều nghiên cứu cùng hỗ trợ một phát biểu, viết ý chung một lần và dẫn đủ nguồn ngay sau câu. Ý chỉ có trong một nghiên cứu được trình bày riêng rồi dẫn nguồn đó; không gộp nguồn chỉ vì cùng chủ đề.
- Mỗi citation trong `notes/` ghi tác giả/năm hoặc khóa BibTeX trong `ref.bib`, cùng locator cụ thể: trang PDF, mục, bảng, hình hoặc phương trình. Không wikilink sang `papers/`, `synthesis/` hay thư mục khác.
- Chỉ dùng wikilink giữa các ghi chú nằm trong `notes/`. Graph của vault dùng bộ lọc `path:notes/ -file:README -file:INDEX`: chỉ hiện note nội dung, ẩn các trang điều hướng `README`/`INDEX`. Bài báo và kế hoạch là tài liệu tham chiếu, không tham gia Graph.
- Phân biệt điều tác giả tuyên bố, bằng chứng trực tiếp và suy luận/đề xuất của dự án. Không trình bày câu hỏi hoặc đóng góp kỳ vọng như kết quả.
- Giữ ngữ cảnh cho mọi số liệu: bộ dữ liệu, hộ/thiết bị, cách chia, tiền xử lý, thước đo và đơn vị. Không xếp hạng kết quả từ các quy trình không tương thích.
- Trạng thái nguồn: `queued` → `screened` → `reading` → `extracted` → `reviewed`; dùng `excluded` kèm lý do nếu ngoài phạm vi. Chỉ đánh dấu `reviewed` sau khi đối chiếu nguồn, vị trí trích dẫn, số liệu và suy luận.
- Chỉ ghi DOI, tác giả, khóa BibTeX và kết quả đã xác minh; ghi `không nêu` hoặc `chưa xác minh` khi thiếu thông tin.

## Trạng thái hiện tại

Ghi chú REFIT đã rà soát toàn văn bài báo; README và phiên bản dữ liệu dự án còn cần audit. Ghi chú NILMTK và Comparability đang ở trạng thái trích xuất, chưa rà soát cuối. Chưa có kết quả thực nghiệm của dự án được xác minh.
