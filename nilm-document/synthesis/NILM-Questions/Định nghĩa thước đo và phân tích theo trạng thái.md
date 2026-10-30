---
type: experimental-question
title: "Định nghĩa thước đo và phân tích theo trạng thái"
tags: [nilm, experimental-design, metrics]
status: proposed
---

# Định nghĩa thước đo và phân tích theo trạng thái

Đây là kế hoạch chốt định nghĩa, đơn vị và cách tổng hợp các thước đo trước khi chạy. Phạm vi metric dự kiến nằm trong đề xuất nghiên cứu (kế hoạch: `synthesis/research-proposal`). Phân biệt F-score theo lát thời gian, event-F1, số sự kiện/ngày và RMSE được ghi trong note so sánh thước đo.

## Câu hỏi cần giải quyết

- Đơn vị, mặt nạ và cách gộp theo thời gian, thiết bị, hộ cho MAE/RMSE/SAE là gì?
- F1 theo sự kiện ghép sự kiện thế nào: ngưỡng bật/tắt, thời điểm bật/tắt, dung sai thời gian và trường hợp chồng lấn?
- Vùng công suất thấp và cửa sổ quanh chuyển trạng thái được định nghĩa từ nguồn nào, trên tập nào?
- Độ bao phủ tập kiểm tra theo TSR/EVR và NAR được báo riêng ra sao? Chúng là thước đo độ bao phủ/chất lượng dữ liệu, không phải độ chính xác dự đoán.
- C1–C3 được đo trên dự đoán hay nhãn? Báo tần suất, mức vi phạm và dung sai nào?

## Đầu ra cho code

Đặc tả thước đo có công thức, đơn vị, mặt nạ, ngưỡng/quy tắc ghép và cách gộp; bảng thước đo theo thiết bị/hộ; thống kê số sự kiện và độ bao phủ riêng; định nghĩa rõ ràng cho các phép đo C1–C3.
