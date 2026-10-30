---
type: experimental-question
title: "Audit dữ liệu và mặt nạ C3"
tags: [nilm, experimental-design, data-quality, constraint-c3]
status: proposed
---

# Audit dữ liệu và mặt nạ C3

Đây là kế hoạch kiểm tra tính sẵn sàng của dữ liệu REFIT trước khi khóa mặt nạ C3. Các đặc tính đo lường và locator trong bài gốc được ghi tại note REFIT; phiên bản dữ liệu cục bộ của dự án chưa được xác minh.

## Câu hỏi cần giải quyết

- Căn chỉnh công suất tổng/IAM bằng quy tắc nào? Báo số mẫu được ghép, loại và mất; xem bằng chứng về lệch thời gian trong note REFIT.
- Đánh giá C3 trên hộ nào và mặt nạ nào? Xử lý riêng hộ có pin mặt trời và mẫu được gắn cờ tổng IAM vượt công suất tổng ra sao?
- Cách đánh dấu khoảng thiếu, đỉnh bất thường, thay công tơ thiết bị và dấu thời gian không hợp lệ là gì? Có phân tích độ nhạy giữa bản thô và sạch không?
- Mức phủ dữ liệu/sự kiện trên tập kiểm tra là bao nhiêu? Báo khoảng thời gian hợp lệ và nguyên nhân loại mẫu.

## Đầu ra cho code

Danh mục dữ liệu có phiên bản/mã kiểm tra; bảng phủ theo hộ và thiết bị; quy tắc dấu thời gian/giá trị thiếu; mặt nạ mẫu C3 có lý do; thống kê tỷ lệ mẫu còn lại. Các quyết định vẫn mở cho đến khi kiểm tra dữ liệu thực tế.
