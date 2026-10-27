# NILM document vault

Mở thư mục `nilm-document` bằng **Obsidian → Open folder as vault**. Có thể đọc và sửa trực tiếp bằng trình soạn thảo Markdown; không cần plugin cộng đồng.

## Bắt đầu

1. Ghi paper mới vào [hàng đợi đọc](inbox/reading-queue.md), kèm DOI hoặc URL nguồn.
2. Sao chép [mẫu đọc paper](templates/paper-note.md) vào `papers/`, đặt tên `nam-tacgia-tu-khoa.md`. Thay các trường trong dấu `<…>` và ghi `không nêu` nếu nguồn thiếu thông tin.
3. Sau khi đọc, thêm liên kết ghi chú vào [danh mục paper](papers/index.md) và [bảng literature review](synthesis/literature-matrix.md).
4. Đối chiếu với [câu hỏi nghiên cứu](synthesis/research-questions.md). Dùng [mẫu tổng hợp](templates/synthesis-note.md) khi đã có nhiều nguồn phù hợp.

## Cấu trúc

- `inbox/`: hàng đợi và thông tin nguồn chưa xử lý.
- `papers/`: ghi chú có bằng chứng cho từng paper.
- `synthesis/`: so sánh liên bài, câu hỏi và giả thuyết cần kiểm tra.
- `templates/`: mẫu để sao chép thủ công, không cần plugin.
- `assets/`: chỉ tạo khi có PDF, hình hoặc tệp đính kèm thực tế; giữ nguyên bản nguồn và đặt tên gắn với paper.

## Quy ước bằng chứng

- Mỗi nhận định quan trọng cần nguồn và vị trí: trang, section, bảng hoặc hình. Nếu số trang PDF khác trang in, ghi rõ loại trang.
- Tách **tác giả tuyên bố**, **thí nghiệm chứng minh** và **suy luận/đề xuất của người đọc**.
- Giữ ngữ cảnh cho số liệu: dataset, split, thiết bị, đơn vị, metric, preprocessing và protocol. Không xếp hạng trực tiếp kết quả khác protocol.
- Mức chắc chắn: **Cao** (nêu trực tiếp và có số liệu hỗ trợ), **Trung bình** (bằng chứng hạn chế), **Suy luận** (diễn giải của người đọc).
- Trạng thái đọc: `queued` → `screened` → `reading` → `extracted` → `reviewed`; dùng `excluded` kèm lý do nếu ngoài phạm vi.
- Chỉ đánh dấu `reviewed` sau khi kiểm tra nguồn, locator, số liệu và phần suy luận. Không dùng đầu ra khám phá làm bằng chứng cho manuscript.
- Chỉ ghi citation/BibTeX đã xác minh; không tự điền DOI, tác giả hay kết quả khi chưa đọc nguồn.

Chưa có paper hoặc kết quả thực nghiệm được nhập. Các câu hỏi khởi tạo là đề xuất để định hướng đọc, chưa phải kết luận nghiên cứu.
