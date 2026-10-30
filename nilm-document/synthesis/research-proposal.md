---
type: research-proposal
status: proposed
title: "Beyond Accuracy: An Empirical Study of Loss Functions and Physical Constraint Violations in Non-Intrusive Load Monitoring"
research_type: empirical-benchmark
tags:
  - nilm
  - proposal
  - loss-functions
  - physical-consistency
---

# Đề xuất nghiên cứu

> [!warning] Trạng thái đề xuất
> Ghi chú này lưu một nghiên cứu đang được đề xuất. Câu hỏi, phương pháp và đóng góp dưới đây chưa phải phát hiện. Chưa có tổng quan tài liệu hay kết quả thực nghiệm nào được ghi nhận làm bằng chứng cho chúng.

**Tiêu đề đề xuất:** Beyond Accuracy: An Empirical Study of Loss Functions and Physical Constraint Violations in Non-Intrusive Load Monitoring  
**Loại nghiên cứu:** Đánh giá thực nghiệm / nghiên cứu so sánh

## 1. Bối cảnh và động lực

Non-Intrusive Load Monitoring (NILM) nhằm ước lượng mức tiêu thụ điện của từng thiết bị từ phép đo công suất tổng của hộ gia đình.

Các mô hình NILM hiện dùng nhiều hàm mục tiêu, gồm loss tái tạo, loss hồi quy ở cấp thiết bị và các thành phần chính quy hóa. Tuy nhiên, độ chính xác dự đoán chưa mô tả đầy đủ liệu mô hình có tạo ra ước lượng công suất nhất quán về mặt vật lý và đáng tin cậy hay không.

Nghiên cứu này khảo sát ảnh hưởng của lựa chọn hàm loss đến hiệu năng ở cấp thiết bị, hành vi theo thời gian và vi phạm các ràng buộc vật lý.

## 2. Mục tiêu nghiên cứu

Mục tiêu chính là đánh giá có hệ thống mối liên hệ giữa **hàm loss, hiệu năng dự đoán và tính nhất quán vật lý** trên một số họ mô hình NILM tiêu biểu.

Nghiên cứu đặt ra bốn câu hỏi:

- **RQ1 — Hiệu năng:** Các tổ hợp mô hình–loss khác nhau đạt kết quả ra sao trên từng thiết bị, hộ gia đình và bộ dữ liệu?
- **RQ2 — Hành vi của loss:** Từng thành phần loss ảnh hưởng thế nào đến sai số dự đoán, nhất là tại thời điểm bật/tắt và vùng công suất thấp?
- **RQ3 — Tính nhất quán vật lý:** Các mô hình hiện có vi phạm tính không âm, giới hạn công suất thiết bị và ràng buộc công suất tổng ở mức nào?
- **RQ4 — Độ vững:** Các hành vi này nhạy đến đâu với nhiễu đo và dịch chuyển phân phối giữa các hộ?

Xem research-questions để biết cách diễn đạt câu hỏi hiện tại và các quyết định còn mở.

## 3. Phương pháp

### 3.1. Thiết kế bộ đánh giá so sánh

	Đánh giá các họ mô hình NILM tiêu biểu theo một quy trình thực nghiệm chuẩn hóa, gồm mô hình đối chứng hồi quy đơn giản, mô hình mạng nơ-ron theo thời gian và mô hình đối chứng tối ưu hóa lồi.

So sánh những cấu hình loss phù hợp:

- MSE và MAE ở cấp thiết bị.
- Loss tái tạo dựa trên công suất tổng.
- Chính quy hóa L1/L2.
- Total variation theo thời gian.
- Một số tổ hợp và phép ablation được chọn.

Đánh giá riêng phương pháp có giám sát và phương pháp chỉ dùng công suất tổng để tránh so sánh thiếu công bằng do khác biệt về thông tin huấn luyện.

### 3.2. Ràng buộc vật lý

Gọi \(P_t\) là công suất tổng quan sát và \(y_{i,t}\) là công suất dự đoán của thiết bị. Đánh giá ba ràng buộc:

$$
\begin{aligned}
\text{C1: }&y_{i,t}\geq0\\
\text{C2: }&y_{i,t}\leq P_i^{\max}\quad\text{(khi đã biết)}\\
\text{C3: }&\sum_{i=1}^{n}y_{i,t}\leq P_t
\end{aligned}
$$

Chỉ đánh giá C3 khi phép đo công suất tổng biểu diễn mức tiêu thụ không âm và các giả định cần thiết về nhiễu, nguồn phát điện và căn chỉnh phép đo được thỏa mãn.

### 3.3. Bộ dữ liệu và đánh giá

**Bộ dữ liệu:** REFIT là bộ đánh giá thực tế chính; bổ sung tín hiệu tổng hợp có trạng thái thiết bị và nhiễu đo được kiểm soát.

**Chỉ số hiệu năng:** MAE, RMSE, SAE và F1 dựa trên sự kiện.

**Chỉ số nhất quán vật lý:** Tần suất vi phạm ràng buộc, mức vi phạm trung bình, mức vi phạm lớn nhất và sai số tái tạo công suất tổng.

**Kiểm soát thực nghiệm:** Dùng tiền xử lý, cách chia dữ liệu, tần suất lấy mẫu và ngân sách tìm tham số nhất quán; dùng nhiều hạt giống ngẫu nhiên khi phù hợp.

### 3.4. Phân tích chẩn đoán

Thực hiện ablation có kiểm soát và phân tích theo nhóm thiết bị, trạng thái hoạt động, dải công suất và thời điểm chuyển trạng thái.

Khảo sát đánh đổi giữa độ chính xác dự đoán, tính nhất quán vật lý và cường độ chính quy hóa. Phân biệt mối liên hệ quan sát được với kết luận nhân quả.

## 4. Đóng góp kỳ vọng

1. Một bộ đánh giá có thể tái lập, nối các cấu hình hàm mất mát trong NILM với hiệu năng cấp thiết bị và tính nhất quán vật lý.
2. Mô tả có hệ thống các kiểu lỗi gắn với những hàm mục tiêu và điều kiện hoạt động khác nhau.
3. Bằng chứng thực nghiệm về đánh đổi giữa độ chính xác, hành vi theo thời gian và mức thỏa mãn ràng buộc.
4. Một quy trình thực nghiệm mở và bộ mã nguồn phục vụ nghiên cứu lý thuyết tiếp theo.

Đây là đóng góp dự kiến, chưa phải kết quả đã được xác lập.

## 5. Phạm vi và sản phẩm dự kiến

Nghiên cứu tập trung vào **đánh giá thực nghiệm**, không tuyên bố có bảo đảm lý thuyết mới và không đề xuất kiến trúc NILM mới.

Sản phẩm dự kiến gồm kho bộ đánh giá có quản lý phiên bản, quy trình đánh giá chuẩn hóa, kết quả so sánh, nghiên cứu loại bỏ thành phần và bài báo nghiên cứu.

**Nghiên cứu tiếp nối:** Dùng các kiểu lỗi quan sát được để hình thành giả thuyết toán học về tính lồi, khả định, tính duy nhất và bảo đảm khôi phục; sau đó phân tích lý thuyết và có thể đề xuất phương pháp mới.

## 6. Kiểm tra nguồn ban đầu: REFIT

Hồ sơ dữ liệu của University of Strathclyde mô tả REFIT là dữ liệu công suất tiêu thụ điện có dấu thời gian, ở cấp công suất tổng và thiết bị, tính bằng oát, gồm 20 hộ và lấy mẫu mỗi 8 giây. Hồ sơ nêu khoảng thời gian dữ liệu từ tháng 10/2013 đến tháng 6/2015, đồng thời liên kết đến bài mô tả bộ dữ liệu gốc. Hồ sơ có cả dữ liệu thô và dữ liệu đã làm sạch, theo giấy phép CC BY 4.0. Xem [hồ sơ REFIT chính thức](https://pureportal.strath.ac.uk/en/datasets/refit-electrical-load-measurements/), phần mô tả và tệp dữ liệu.

Phần tóm tắt của bài mô tả dữ liệu nêu phép đo công suất tổng của cả nhà và chín thiết bị riêng cho mỗi hộ, lấy mẫu mỗi 8 giây trong hai năm trên 20 hộ. Bài viết nói dữ liệu phân phối đã được làm sạch để loại phép đo không hợp lệ, gán nhãn đúng cho dữ liệu thiết bị và lấp các khoảng thiếu ngắn. Xem Murray, Stankovic & Stankovic (2017), phần tóm tắt, [hồ sơ Strathprints](https://strathprints.strath.ac.uk/58873/), DOI [10.1038/sdata.2016.122](https://doi.org/10.1038/sdata.2016.122).

Bài dữ liệu gốc cũng nêu các giới hạn quan trọng cho đề xuất này: cảm biến công suất tổng không đo điện áp lưới và có sai số tương đối khoảng 6% (mục Household aggregate, PDF tr. 4); phép đo IAM có thể cũ hơn thời điểm ghi công suất tổng đến 7 giây (mục Individual appliance monitors, PDF tr. 5; Code availability, PDF tr. 7); các hộ 3, 11 và 21 còn nhiễu do điện mặt trời, được cảm biến ghi nhận như mức tiêu thụ tăng thêm (mục Household aggregate, PDF tr. 4). Bản dữ liệu đã làm sạch bổ sung cột ghi chú cho mẫu mà tổng công suất IAM lớn hơn công suất tổng (mục Data Records / Technical Validation, PDF tr. 7). Vì vậy, C3 cần quy định rõ cách căn chỉnh và tiêu chí chọn mẫu. Xem [@murray2017refit] để biết bằng chứng và các việc còn cần kiểm tra.

Kiểm tra ban đầu này cho thấy REFIT là một ứng viên để đánh giá có giám sát ở cấp thiết bị. Tuy nhiên, nó chưa chứng minh phép đo công suất tổng thỏa C3 tại mọi thời điểm hoặc mọi thiết bị, hộ và cách chia dữ liệu đều phù hợp. Trước khi chốt quy trình, cần kiểm tra README dữ liệu, định nghĩa kênh đo, vị trí công tơ, dữ liệu thiếu và bất thường, cùng ý nghĩa căn chỉnh thời điểm đo. Kiểm tra giả định C3 trên từng bản ghi được chọn; loại riêng hoặc báo cáo riêng những cửa sổ không thỏa giả định. Đánh giá mức phù hợp vẫn là sơ bộ cho đến khi hoàn thành việc kiểm tra này.

## 7. Quyết định cần chốt trước khi khóa quy trình

- Chọn thiết bị, hộ gia đình, phiên bản REFIT và khoảng thời gian nào?
- Tập kiểm tra khái quát hóa sẽ giữ lại khoảng thời gian trong cùng hộ, giữ lại các hộ chưa thấy, hay dùng cả hai? Mỗi cách chia trả lời RQ nào?
- So sánh phương pháp chỉ dùng công suất tổng với phương pháp có giám sát thế nào để không nhập nhằng ảnh hưởng của nhãn và họ mô hình?
- Định nghĩa chính xác, ngưỡng, quy tắc ghép sự kiện, đơn vị và mức tổng hợp nào được dùng cho SAE, F1 sự kiện, vùng công suất thấp, thời điểm bật/tắt và từng chỉ số vi phạm?
- Lấy \(P_i^{\max}\) từ nguồn nào, và biểu diễn giới hạn chưa biết hoặc thay đổi ra sao?
- Dùng mô hình và mức nhiễu nào; tạo hoặc đo dịch chuyển giữa các hộ như thế nào?
- Làm thế nào để mô hình đối chứng tối ưu hóa, ngân sách huấn luyện, tìm tham số, hạt giống ngẫu nhiên và quy tắc dừng có thể so sánh?
- Chọn những tổ hợp loss và ablation nào để tránh ma trận mô hình × loss × hộ × seed quá lớn, khó chạy và khó diễn giải?
- Bằng chứng nào đủ để kết luận có đánh đổi, và sẽ báo cáo độ bất định giữa các hộ, seed ra sao?

## 8. Ghi chú vault liên quan

- research-questions — cách diễn đạt câu hỏi hiện tại và các quyết định còn mở.
- ma trận bằng chứng — bảng bằng chứng sẽ cập nhật sau khi đọc nguồn.
- Hàng đợi đọc — thêm nguồn liên quan trước khi trích xuất.
- Mẫu ghi chú bài báo — trích xuất phương pháp và bằng chứng từ từng nguồn.
- Mẫu tổng hợp — tổng hợp các nghiên cứu có thể so sánh.
