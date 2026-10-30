---
type: research-questions
status: proposed
tags: [nilm, research-questions]
---

# Câu hỏi nghiên cứu

**Trạng thái: đề xuất, chưa được tổng quan tài liệu hoặc thực nghiệm kiểm chứng.** Các câu hỏi này được chuyển từ research-proposal. Cần điều chỉnh sau khi sàng lọc tài liệu và chốt quy trình đánh giá.

| ID | Câu hỏi | Bằng chứng hoặc chi tiết thiết kế cần xác lập |
| --- | --- | --- |
| RQ1 — Hiệu năng | Các tổ hợp mô hình–loss khác nhau đạt kết quả ra sao trên từng thiết bị, hộ gia đình và bộ dữ liệu? | Xác định so sánh chính, cách tổng hợp theo thiết bị/hộ, tính tương thích giữa bộ dữ liệu, thước đo và độ bất định. |
| RQ2 — Hành vi của loss | Từng thành phần loss ảnh hưởng thế nào đến sai số dự đoán, nhất là tại thời điểm bật/tắt và vùng công suất thấp? | Định nghĩa cửa sổ chuyển trạng thái, nhóm công suất thấp, phép ablation thành phần và cách kiểm soát mô hình/ngân sách huấn luyện. |
| RQ3 — Tính nhất quán vật lý | Các mô hình hiện có vi phạm tính không âm, giới hạn công suất thiết bị và ràng buộc công suất tổng ở mức nào? | Định nghĩa mẫu đủ điều kiện, giới hạn đã biết, căn chỉnh thời điểm đo, thước đo vi phạm và cách xử lý nhiễu điện mặt trời/công tơ. |
| RQ4 — Độ vững | Các hành vi này nhạy đến đâu với nhiễu đo và dịch chuyển phân phối giữa các hộ? | Định trước phân phối/mức nhiễu và cách chia hộ huấn luyện/kiểm tra; định lượng biến thiên giữa các hộ và hạt giống ngẫu nhiên. |

## Quyết định cần chốt trước khi khóa quy trình

- Bộ dữ liệu và phiên bản: REFIT bản thô hay bản làm sạch; tập thiết bị/hộ cụ thể; bộ sinh tín hiệu tổng hợp và trạng thái được kiểm soát.
- Cách chia và khả năng khái quát: giữ lại khoảng thời gian, giữ lại hộ chưa thấy hoặc cả hai; ngăn rò rỉ giữa thời gian và hộ.
- Thông tin huấn luyện: tách riêng trường hợp có giám sát và chỉ dùng công suất tổng; nêu rõ mỗi phương pháp được dùng nhãn nào.
- Họ mô hình và mô hình đối chứng: xác định hồi quy đơn giản, mạng nơ-ron theo thời gian và mô hình tối ưu hóa lồi với giả định đầu vào/nhãn có thể so sánh.
- Định nghĩa hàm mất mát: cách gộp thành giá trị loss (reduction), chuẩn hóa, trọng số và hệ số chính xác cho MSE/MAE thiết bị, tái tạo công suất tổng, L1/L2, total variation và các tổ hợp.
- Chỉ số: định nghĩa, đơn vị, ngưỡng, quy tắc ghép sự kiện và cách tổng hợp cho MAE, RMSE, SAE, F1 sự kiện, tái tạo công suất tổng, tần suất/mức độ vi phạm.
- Giới hạn vật lý: nguồn và độ bất định của từng `P_i^max`; cách biểu diễn giới hạn không biết hoặc thay đổi.
- Điều kiện C3: các luồng REFIT không căn thời gian hoàn toàn; nhiễu điện mặt trời còn ở hộ 3, 11, 21; dữ liệu đã làm sạch đánh dấu mẫu có tổng IAM vượt công suất tổng. Xem [@murray2017refit]. Nêu rõ các cửa sổ đó sẽ được căn chỉnh, loại trừ hay phân tích riêng.
- Độ vững: nhiễu đo có kiểm soát và quy trình xác định dịch chuyển giữa các hộ.
- Ngân sách và suy luận: ngân sách tìm tham số cố định, hạt giống ngẫu nhiên, quy tắc dừng, cách tóm tắt độ bất định và tiêu chí để xem hiệu ứng là đáng kể.
- Phạm vi: giới hạn số tổ hợp để có thể chạy và diễn giải được, không tuyên bố quan hệ nhân quả ngoài những gì so sánh có kiểm soát hỗ trợ.

## Bước tiếp theo

Dùng ma trận bằng chứng để ghi các quy trình và bằng chứng trước đây có thể so sánh. Không xem đóng góp kỳ vọng trong đề xuất nghiên cứu là kết quả. Sau khi giải quyết các quyết định, bàn giao cho thư mục mã nguồn một mô tả thí nghiệm có dẫn nguồn.
