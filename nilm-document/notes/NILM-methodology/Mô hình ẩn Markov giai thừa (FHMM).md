---
type: method
title: "Mô hình ẩn Markov giai thừa (FHMM)"
aliases: [Factorial Hidden Markov Model]
tags: [nilm, methodology, baseline]
evidence_status: extracted
---

# Mô hình ẩn Markov giai thừa (FHMM)

Mô hình ẩn Markov giai thừa biểu diễn công suất mỗi thiết bị như quan sát của một mô hình Markov ẩn; trạng thái ẩn tương ứng trạng thái thiết bị. Phân rã cần giải mã đồng thời trạng thái của nhiều thiết bị. (Batra và cộng sự, mục 3.5, PDF tr. 6; [@NILMTK].)

Với suy luận chính xác, bài báo nêu độ phức tạp `O(TK^(2N))`; vì vậy phương pháp còn khó mở rộng hơn CO trong phân tích của tác giả. Bài cũng lưu ý có thể dùng suy luận xấp xỉ hiệu quả hơn. (Batra và cộng sự, mục 3.5, PDF tr. 6.)

Trong bài về khả năng so sánh, FHMM tham gia các ví dụ REDD nhà 6 và DRED nhà 1 để cho thấy thước đo nhạy với phạm vi tập kiểm tra và mức nhiễu. Các thí nghiệm này không đánh giá lựa chọn hàm mất mát. (Klemenjak và cộng sự, mục IV.C, Bảng II–III, PDF tr. 4–5; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

## Giới hạn

Không suy rộng thứ hạng CO/FHMM từ các ví dụ này sang kiến trúc học sâu hoặc toàn bộ dữ liệu NILM. Phiên bản triển khai và môi trường chạy chưa được tái lập.
