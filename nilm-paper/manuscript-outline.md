---
title: "Đề cương bản thảo: Beyond Accuracy: An Empirical Study of Loss Functions and Physical Constraint Violations in Non-Intrusive Load Monitoring"
status: proposal
type: manuscript-outline
tags: [nilm, paper, proposal]
---

# Đề cương bản thảo

> [!warning] Mới là đề xuất
> Chưa có kết quả thí nghiệm hay kết luận nào được ghi nhận. Giữ trạng thái `proposal` cho đến khi quy trình và cơ sở bằng chứng sẵn sàng.

## Tiêu đề và tóm tắt

- Tiêu đề làm việc: như trên; xem xét lại khi bằng chứng làm rõ phạm vi thực tế của bài.
- Chỉ viết tóm tắt sau khi kết quả được xác minh. Nêu bài toán, quy trình, phát hiện đo được chính và giới hạn.

## 1. Giới thiệu

- Động lực: độ chính xác dự đoán có thể chưa phản ánh đầy đủ tính nhất quán theo thời gian và vật lý.
- Định nghĩa bài toán NILM và phạm vi thiết bị mục tiêu dựa trên nguồn đã xác minh cùng quy trình cuối cùng.
- Trình bày khoảng trống có bằng chứng; chưa tuyên bố tính mới trước khi rà soát phần tổng hợp tài liệu.
- Liệt kê câu hỏi nghiên cứu và đóng góp đã chốt. RQ1–RQ4 hiện vẫn là đề xuất.

## 2. Nghiên cứu liên quan

- Mục tiêu huấn luyện NILM và sự khác biệt giữa huấn luyện có giám sát với chỉ dùng tín hiệu tổng.
- Chỉ số đánh giá NILM và khả năng so sánh giữa các quy trình.
- Ràng buộc vật lý hoặc phép đo tính nhất quán trong các công trình trước.
- Mọi nhận định cần có ghi chú đã rà soát và vị trí chính xác trong nguồn gốc.

## 3. Thiết kế bộ chuẩn đánh giá và phương pháp

- Họ mô hình và kiến trúc cụ thể.
- Định nghĩa hàm mất mát, hệ số, phép gộp và thông tin huấn luyện được cung cấp cho từng phương pháp.
- Tách riêng các nhánh có giám sát và chỉ dùng tín hiệu tổng.
- Mô hình đối chứng và các kiểm soát để bảo đảm công bằng.

## 4. Bộ dữ liệu và tiền xử lý

- Phiên bản REFIT, giấy phép, hộ gia đình/thiết bị được chọn, căn chỉnh dấu thời gian, xử lý dữ liệu thiếu và bất thường.
- Bộ tạo tín hiệu tổng hợp, giả định và cách xây dựng nhãn chuẩn.
- Tần số lấy mẫu, chia cửa sổ, chuẩn hóa và ranh giới các tập dữ liệu.

## 5. Quy trình đánh giá

- MAE, RMSE, SAE, F1 sự kiện: công thức chính xác, đơn vị, cách tổng hợp, ngưỡng, dung sai ghép sự kiện và cách xử lý mẫu số bằng không.
- C1 không âm và C2 cận trên công suất thiết bị: định nghĩa, nguồn/cơ sở của giới hạn và dung sai nếu có.
- C3 cận công suất tổng: giả định, mặt nạ mẫu đủ điều kiện, căn chỉnh thời gian, xử lý phát điện/nhiễu và số lượng mẫu đủ điều kiện.
- Hạt giống ngẫu nhiên, ngân sách dò siêu tham số, tài nguyên tính toán và cách ước lượng độ bất định.

## 6. Kết quả

- Hiệu năng dự đoán tổng thể và theo từng thiết bị.
- Phân tích chẩn đoán quanh thời điểm chuyển trạng thái và vùng công suất thấp.
- Tỷ lệ và độ lớn vi phạm ràng buộc vật lý.
- Độ bền vững trước nhiễu có kiểm soát và dịch chuyển giữa các hộ.
- Chỉ tạo bảng và hình từ tệp kết quả lần chạy đã xác minh.

## 7. Thảo luận

- Sự đánh đổi giữa độ chính xác, tính nhất quán và diễn biến theo thời gian.
- Phân biệt mối liên hệ quan sát được với khẳng định nhân quả.
- Chế độ lỗi và mức độ liên quan ngoài các thiết lập đã thử nghiệm.

## 8. Hạn chế và nguy cơ đối với tính hợp lệ

- Tính đại diện của bộ dữ liệu, thời điểm cảm biến, độ bao phủ thiết bị không đầy đủ, khoảng cách giữa dữ liệu tổng hợp và thực tế, độ nhạy của chỉ số và ngân sách tính toán.

## 9. Kết luận

- Chỉ tóm tắt kết luận có kết quả hỗ trợ và nêu rõ phạm vi của nghiên cứu.

## Tuyên bố khả năng tái lập

- Phiên bản mã, phiên bản và cách truy cập dữ liệu, cấu hình, hạt giống ngẫu nhiên, lệnh chạy, tệp kết quả và giới hạn giấy phép.

## Tài liệu tham khảo

- Chỉ điền từ hồ sơ trích dẫn đã xác minh; không tự tạo BibTeX theo phỏng đoán.

## Hình và bảng

- Duy trì danh sách đầu ra và lệnh tạo lại trong `claim-ledger.md` hoặc hồ sơ lần chạy.

