# Câu hỏi nghiên cứu ban đầu

**Trạng thái: đề xuất định hướng đọc, chưa được kiểm chứng.** Điều chỉnh sau khi có bằng chứng trong [bảng literature review](literature-matrix.md).

| ID | Câu hỏi | Thông tin cần trích xuất |
| --- | --- | --- |
| RQ1 | Lựa chọn loss ảnh hưởng thế nào đến chất lượng dự đoán công suất và phát hiện trạng thái thiết bị? | Công thức loss, metric regression/event, ngưỡng trạng thái và đơn vị. |
| RQ2 | Kết quả có thay đổi theo tần suất hoạt động, loại thiết bị và phân bố công suất không? | Phân bố on/off, thiết bị, chuẩn hóa, sampling rate và cách tổng hợp metric. |
| RQ3 | Hiệu ứng của loss có còn khi giữ cố định mô hình và protocol huấn luyện không? | Kiến trúc, split, seed, hyperparameter search, ngân sách và ablation. |
| RQ4 | Kết quả có khái quát sang nhà hoặc dataset khác không? | Chia train/validation/test theo nhà/thời gian, leakage, domain shift và đánh giá ngoài miền. |
| RQ5 | Những chi tiết nào còn thiếu để tái lập một benchmark loss công bằng? | Phiên bản dữ liệu/code, preprocessing, cấu hình, seed, phần cứng và độ biến thiên. |

## Quyết định còn mở

- Dataset và điều kiện truy cập.
- Danh sách loss, mô hình và baseline.
- Metric chính, protocol, ngân sách và tiêu chí so sánh.

Chốt các quyết định bằng nguồn hoặc thí nghiệm được ghi lại; chưa coi danh sách này là thiết kế benchmark chính thức.
