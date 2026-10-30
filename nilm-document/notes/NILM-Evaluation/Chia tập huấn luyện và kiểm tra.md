---
type: evaluation-design
title: "Chia tập huấn luyện và kiểm tra"
tags: [nilm, evaluation, data-split]
evidence_status: extracted
---

# Chia tập huấn luyện và kiểm tra

Cách chia dữ liệu xác định kiểu khái quát hóa được đo. Chia theo thời gian trong cùng hộ và giữ lại hộ hoàn toàn chưa thấy trả lời các câu hỏi khác nhau; cần báo rõ đơn vị chia, hộ, khoảng thời gian và cách ngăn rò rỉ.

**Ví dụ từ Klemenjak:** trên REDD nhà 6, cùng tập huấn luyện nhưng ba tập kiểm tra có độ bao phủ khác nhau và RMSE biến đổi. (Mục IV.C, Bảng II, PDF tr. 4; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

**Giao thức minh họa riêng của NILMTK:** tác giả dùng hộ đầu tiên mỗi bộ, nửa đầu để huấn luyện và nửa sau để đánh giá CO/FHMM. Đây không phải đề xuất cách chia tối ưu cho dự án. (Batra và cộng sự, mục 4.4, PDF tr. 9; [@NILMTK].)

## Quyết định còn mở

Đề tài cần xác định cách chia theo thời gian, cách chia giữ lại hộ, hoặc báo cáo cả hai như mục tiêu đánh giá riêng. Thiết kế cách chia và độ vững (kế hoạch: `synthesis/NILM-Questions/Thiết kế cách chia và độ vững`) liệt kê các câu hỏi cần giải quyết.
