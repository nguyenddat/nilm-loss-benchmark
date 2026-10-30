---
type: experimental-question
title: "Thiết kế cách chia và độ vững"
tags: [nilm, experimental-design, robustness, domain-shift]
status: proposed
---

# Thiết kế cách chia và độ vững

Đây là kế hoạch trả lời RQ4 về độ nhạy với nhiễu đo và dịch chuyển giữa hộ (câu hỏi nghiên cứu (kế hoạch: `synthesis/research-questions`)). Bằng chứng về độ bao phủ tập kiểm tra và cách chia minh họa được ghi tại note chia tập, còn đề xuất hiện tại chưa ấn định protocol.

## Câu hỏi cần giải quyết

- Chia theo thời gian trong hộ, giữ lại hộ chưa thấy, hay báo cáo cả hai như hai mục tiêu khác nhau?
- Làm thế nào ngăn rò rỉ giữa cửa sổ, chuẩn hóa, dò siêu tham số và các đoạn thời gian gần nhau?
- Mức/kiểu nhiễu tổng hợp được xác định thế nào, và có lưu hạt giống ngẫu nhiên để tái lập không?
- Cần bao nhiêu hạt giống ngẫu nhiên và ngân sách dò siêu tham số đồng đều để mô tả độ bất định? Nguồn hiện có chưa chốt con số.
- Báo cáo hiệu năng theo từng hộ hay phân phối giữa hộ ra sao?

## Đầu ra cho code

Định nghĩa cách chia và đại lượng đích ước lượng; danh sách hộ/đoạn tập kiểm tra; quy tắc chống rò rỉ; cấu hình nhiễu và hạt giống ngẫu nhiên; ngân sách dò siêu tham số; cách tóm tắt độ biến thiên. Chưa kết luận quan hệ nhân quả nếu thiết kế chưa hỗ trợ.
