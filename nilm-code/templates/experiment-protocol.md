# Giao thức thí nghiệm: <tên>

Trạng thái: draft (bản nháp) / ready (sẵn sàng) / revised (đã sửa)  
Mã và phiên bản protocol: <mã, phiên bản>  
Câu hỏi nghiên cứu: <RQ trong đề xuất và câu hỏi cụ thể>  
Ghi chú đã review và vị trí nguồn liên quan: <đường dẫn, liên kết, vị trí>  
Giả thuyết và cơ sở: <đề xuất, chưa phải phát hiện>  
Quyết định còn mở: <danh sách hoặc không có>

## Dữ liệu và cách chia tập

- Dataset, phiên bản, nguồn, giấy phép và quyền truy cập: <chi tiết>
- Hộ, kênh thiết bị và tiêu chí chọn: <chi tiết>
- Lấy mẫu, căn chỉnh, khoảng thiếu, lọc, đơn vị và chuẩn hóa: <chi tiết; chỉ ước lượng phép biến đổi trên tập huấn luyện>
- Hộ hoặc khoảng thời gian train/validation/test và artifact mô tả cách chia: <chi tiết>
- Cách tạo cửa sổ và kiểm tra rò rỉ: <chi tiết>
- Tạo tín hiệu tổng hợp và thêm nhiễu nếu có: <mô hình, vị trí, mức độ, seed>

## Phương pháp và so sánh có kiểm soát

- Thông tin có sẵn lúc huấn luyện và suy luận: <dữ liệu tổng, nhãn thiết bị, metadata>
- Mô hình, kiến trúc, khởi tạo và mục tiêu dự đoán: <chi tiết>
- Công thức loss, đơn vị, phép gộp, tỷ lệ, trọng số và vị trí nguồn: <chi tiết>
- Regularization, ràng buộc cứng và hậu xử lý: <chi tiết>
- Baseline và khả năng tương thích mô hình–loss: <chi tiết; tách so sánh có giám sát và chỉ dùng dữ liệu tổng>
- Yếu tố giữ cố định và thay đổi trong từng phép so sánh: <chi tiết>
- Tối ưu, không gian và ngân sách tìm siêu tham số, quy tắc chọn, seed và ngân sách tính toán: <chi tiết>

## Đánh giá

- So sánh và metric chính: <định nghĩa, đơn vị, chiều tốt hơn>
- MAE, RMSE, SAE và event F1: <công thức, cách gộp, xử lý mẫu số, ngưỡng, cách ghép sự kiện>
- C1/C2/C3: <điều kiện áp dụng, cận và nguồn gốc, dung sai, mẫu hợp lệ, mẫu số tần suất, đơn vị độ lớn, đầu ra thô/sau xử lý>
- Điều kiện áp dụng C3 với REFIT: <cách căn chỉnh thời điểm, mặt nạ bất thường/chất lượng và dữ liệu thiếu, xử lý phát điện mặt trời hoặc phép đo ròng, lý do và số mẫu bị loại; mặt nạ độc lập với dự đoán>
- Tái dựng tổng và xử lý tải không được đo: <công thức, giả định, kiểm tra tính nhất quán của ground truth>
- Các nhóm phân tầng: <thiết bị, hộ, trạng thái on/off, giai đoạn công suất thấp, cửa sổ chuyển trạng thái>
- Độ bền vững: <điều kiện nhiễu và thiết kế giữa các hộ; phân biệt dữ liệu thực/tổng hợp>
- Đơn vị thống kê, cách tổng hợp, độ bất định và xử lý run thiếu/thất bại: <chi tiết>

## Chạy và xác minh

- Phiên bản code, môi trường, phần cứng và cách ghi dependency: <chi tiết>
- Ma trận run và mã định danh: <đường dẫn hoặc bảng>
- Lệnh chính xác và vị trí artifact: <lệnh và đường dẫn>
- Kiểm tra công thức, rò rỉ, metric và ràng buộc: <các kiểm tra>
- Quy trình tái lập và tiêu chí khớp: <chi tiết>
- Giới hạn và sai lệch đã biết: <chi tiết>
