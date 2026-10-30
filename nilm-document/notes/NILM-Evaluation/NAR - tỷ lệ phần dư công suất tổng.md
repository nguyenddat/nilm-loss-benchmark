---
type: metric
title: "NAR - tỷ lệ phần dư công suất tổng"
aliases: [Noise Aggregate Ratio]
tags: [nilm, metric, data-quality]
evidence_status: extracted
---

# NAR — tỷ lệ phần dư công suất tổng

NAR đo tỷ lệ sai khác giữa công suất tổng và tổng các kênh thiết bị đã đo, chuẩn hóa theo tổng công suất tổng:

$$
\mathrm{NAR}=\frac{\sum_t\left|y_t-\sum_i x_{i,t}\right|}{\sum_t y_t}.
$$

Tác giả diễn giải NAR như phần năng lượng tổng không được giải thích bởi các kênh công tơ thiết bị, gồm tải không đo và nhiễu. (Klemenjak và cộng sự, mục III.C, phương trình 2, PDF tr. 3; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

NAR không tách tải chưa đo khỏi sai số đo, không phải thước đo độ chính xác của mô hình và không đồng nghĩa với vi phạm [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|C3]]. Khi tính trên dữ liệu thực cần xác định căn chỉnh, đơn vị, chiều công suất và mặt nạ mẫu hợp lệ.

## Ví dụ REFIT

**Kết quả NAR trong REFIT:** Klemenjak và cộng sự báo NAR(P) cho các hộ REFIT được chọn; đây là số liệu từ hộ mẫu và giao thức bài báo. (Bảng I, PDF tr. 2; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

**Điều kiện đo bổ sung:** Murray và cộng sự mô tả sai số công tơ, độ lệch thời điểm IAM và ảnh hưởng điện mặt trời ở một số hộ. Đây là thông tin về chất lượng phép đo, không phải phép tính NAR mới. (Mục Household aggregate, PDF tr. 4; IAM, PDF tr. 5; [@murray2017refit].)
