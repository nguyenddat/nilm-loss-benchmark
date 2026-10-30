---
type: experimental-question
title: "So sánh công bằng giữa hàm mất mát và mô hình"
tags: [nilm, experimental-design, loss]
status: proposed
---

# So sánh công bằng giữa hàm mất mát và mô hình

Đây là kế hoạch xác định các yếu tố cần cố định và thay đổi khi so sánh mô hình–loss; phạm vi câu hỏi nằm trong đề xuất nghiên cứu (kế hoạch: `synthesis/research-proposal`). Cơ sở về khả năng so sánh được lưu tại note khả năng so sánh, còn phân biệt hàm mất mát với thước đo ở note loss và metric.

## Câu hỏi cần giải quyết

- Nhóm nào có giám sát thiết bị, nhóm nào chỉ dùng công suất tổng? Không gộp chúng thành một bảng xếp hạng nếu thông tin huấn luyện khác.
- Trong mỗi nhóm, mô hình nào được giữ cố định khi đổi hàm mất mát? Kiến trúc, đầu vào/cửa sổ, tối ưu hóa, chuẩn hóa, ngân sách và tiêu chí dừng là gì?
- Thành phần nào được loại bỏ lần lượt để đo tác động: hàm mất mát thiết bị, tái tạo tổng, L1/L2 hay biến phân toàn phần? Cách gộp, đơn vị và trọng số được định nghĩa ra sao?
- Mô hình đối chứng tối ưu hóa lồi, hồi quy đơn giản và mô hình thời gian có đủ thông tin đầu vào/nhãn để so sánh không?

## Đầu ra cho code

Ma trận thí nghiệm ghi rõ nhóm giám sát, mô hình đối chứng, kiến trúc, hàm mất mát và từng hệ số, biến cố định/thay đổi, ngân sách dò siêu tham số và tiêu chí dừng. Danh sách này là câu hỏi thiết kế, chưa chứng minh bất kỳ hàm mất mát nào tốt hơn.
