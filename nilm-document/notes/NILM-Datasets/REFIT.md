---
type: dataset
title: "REFIT"
aliases: [Bộ dữ liệu điện REFIT]
tags: [nilm, dataset, refit]
source_status: reviewed
---

# REFIT

REFIT ghi công suất tổng và tối đa chín thiết bị riêng trong 20 hộ tại Vương quốc Anh, với chu kỳ danh nghĩa 8 giây trong khoảng hai năm. Bài báo mô tả dữ liệu đã được thu trong sinh hoạt thường ngày. (Murray và cộng sự, tóm tắt PDF tr. 1; Background & Summary, PDF tr. 2–3; [@murray2017refit].)

## Đặc điểm liên quan đến đánh giá đối chiếu

- Cảm biến tổng dùng kẹp dòng và không đo điện áp; bài dẫn thử nghiệm sai số tương đối khoảng 6%. (Mục Household công suất tổng, PDF tr. 4.)
- Tín hiệu IAM có thể cũ đến 7 giây so với dấu thời gian công suất tổng. (Mục Individual appliance monitors, PDF tr. 5; Code availability, PDF tr. 7.)
- Một số hộ có pin mặt trời; ở hộ 3, 11 và 21, tác giả báo công suất phát xuất hiện như mức tiêu thụ tăng thêm do cảm biến không phân biệt chiều công suất. (Mục Household công suất tổng, PDF tr. 4.)
- Bản sạch đánh dấu trường hợp tổng IAM lớn hơn công suất tổng. Đây là cờ chất lượng đo, không phải vi phạm C3 của mô hình. (Technical Validation, PDF tr. 8.)
- Bài báo nêu 6,4% giá trị NaN trong dữ liệu thô, thời gian hoạt động trung bình 88%, và các quy tắc xử lý dấu thời gian, đỉnh bất thường, khoảng trống cùng việc chuyển IAM. (Data Records và Technical Validation, PDF tr. 6–8.)

## Giới hạn suy rộng

57 hộ phản hồi; việc chọn hộ dựa một phần vào mức quen ICT, cơ cấu hộ và khả năng kết nối. Thiết bị được chọn ưu tiên theo mức tiêu thụ hoặc tần suất sử dụng. Vì vậy tập này không phải mẫu ngẫu nhiên đại diện cho mọi hộ ở Vương quốc Anh. (Methods, Selection methodology, PDF tr. 2.)

## Câu hỏi kiểm tra trước khi dùng

Phiên bản dữ liệu thô/sạch, README, cờ chất lượng, thời điểm IAM và chính sách căn chỉnh của dự án vẫn cần kiểm tra. Không coi mô tả trong bài báo là bằng chứng cho trạng thái của một bản dữ liệu chưa kiểm tra.

## Liên kết

- [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|Ràng buộc C3 - giới hạn công suất tổng]]
- [[notes/NILM-Evaluation/NAR - tỷ lệ phần dư công suất tổng|NAR - tỷ lệ phần dư công suất tổng]]
- Audit dữ liệu và mặt nạ C3 (kế hoạch: `synthesis/NILM-Questions/Audit dữ liệu và mặt nạ C3`)
