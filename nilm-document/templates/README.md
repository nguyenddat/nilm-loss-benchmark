# Hướng dẫn dùng mẫu ghi chú

## Bảng Markdown và wikilink

Trong ô bảng, dấu `|` dùng để chia cột. Nếu wikilink cần bí danh, phải escape dấu `|` bên trong liên kết bằng dấu gạch chéo ngược; nếu không cần bí danh, dùng wikilink chỉ có đích.

```markdown
| Ghi chú | Bí danh |
| --- | --- |
| [[notes/NILM-Datasets/REFIT\|REFIT]] | [[notes/NILM-Datasets/REFIT]] |
```

Trong tài liệu hiện tại, chỉ các note ở `notes/` được wikilink với nhau. Không dùng ví dụ wikilink trong mẫu để tạo liên kết từ `papers/`, `synthesis/` hoặc `templates/`.

Sau khi thêm hoặc sửa bảng, kiểm tra mọi hàng có cùng số cột và xem trong Reading view để chắc chắn dấu `|` trong bí danh không làm bảng vỡ.

## Các mẫu

- `concept-note.md`: ghi chú khái niệm hạt nhân trong `notes/`.
- `synthesis-note.md`: tổng hợp tri thức liên nguồn; lưu kết quả trong `notes/`.
- `paper-note.md`: trích xuất bằng chứng từ một bài báo trong `papers/`.
