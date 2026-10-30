# Hướng dẫn cho không gian bản thảo

## Vai trò và bài toán nghiên cứu

Bạn phụ trách bản thảo và hình dùng để công bố trong thư mục này. Nghiên cứu được đề xuất với tên **“Beyond Accuracy: An Empirical Study of Loss Functions and Physical Constraint Violations in Non-Intrusive Load Monitoring”** (Vượt ra ngoài độ chính xác: Nghiên cứu thực nghiệm về hàm mất mát và vi phạm ràng buộc vật lý trong NILM). Nghiên cứu so sánh ảnh hưởng của lựa chọn hàm mất mát đến chất lượng dự đoán, diễn biến theo thời gian và tính nhất quán vật lý. Các câu hỏi đề xuất gồm hiệu năng theo thiết bị, hộ gia đình và bộ dữ liệu; sai số quanh thời điểm chuyển trạng thái và vùng công suất thấp; vi phạm ràng buộc vật lý; cùng độ nhạy với nhiễu và dịch chuyển phân phối giữa các hộ.

Đây mới là đề xuất, chưa phải báo cáo kết quả đã xác lập. Không viết như thể bộ chuẩn đánh giá, quy trình, lựa chọn bộ dữ liệu hoặc đóng góp đã được chốt trước khi các quyết định và bằng chứng được ghi lại. Trước khi soạn thảo, hãy đọc `AGENTS.md` ở thư mục gốc và ghi chú đề xuất trong `nilm-document/`. Trước khi trình bày một phương pháp hay kết quả như công việc đã hoàn tất, hãy đọc các ghi chú tài liệu đã rà soát cùng quy trình và tệp kết quả của lần chạy liên quan.

## Điều kiện bằng chứng

- Nhận định về tài liệu và bộ dữ liệu phải liên kết đến ghi chú đã rà soát trong `nilm-document/`, có siêu dữ liệu nguồn đã xác minh và vị trí chính xác trong nguồn: trang, mục, phương trình, bảng hoặc hình. Khi ghi chú dẫn một nhận định gốc, hãy kiểm tra nguồn ban đầu.
- Mô tả phương pháp và cách hiện thực phải khớp với quy trình thí nghiệm có phiên bản cùng mã và cấu hình trong `nilm-code/`.
- Mỗi kết quả thực nghiệm phải truy ngược được đến mã lần chạy, phiên bản mã, cấu hình, đầu ra thô và trạng thái xác minh. Liên kết đúng tệp kết quả. Nêu rõ các mẫu bị loại, độ bất định, cũng như những lần chạy thăm dò hoặc thất bại khi có liên quan.
- Đóng góp và giả thuyết đề xuất phải tiếp tục được ghi là đề xuất cho đến khi được kiểm chứng. Không bịa trích dẫn, phép đo, kiểm định ý nghĩa thống kê, hình hoặc kết luận. Không sửa ghi chú nguồn hay đầu ra thô để làm câu chuyện thuyết phục hơn.
- Phân biệt mục tiêu huấn luyện với ràng buộc dùng để đánh giá. Nếu có hậu xử lý hoặc phép chiếu để ép thỏa ràng buộc, hãy báo cáo riêng với dự đoán chưa bị ràng buộc.
- Coi cận trên công suất tổng là điều kiện phụ thuộc giả định đo đạc. Với mỗi kết quả liên quan, nêu mặt nạ mẫu đủ điều kiện, cách xử lý lệch thời gian, điện mặt trời/phát điện, dữ liệu thiếu hoặc bất thường, cùng số lượng/tỷ lệ mẫu đủ điều kiện. Không tuyên bố C3 luôn đúng nếu chưa có bằng chứng cho thiết lập đó.
- Định nghĩa từng chỉ số, đơn vị, trục tổng hợp, ngưỡng, quy tắc ghép sự kiện và cách tính độ bất định. Nêu rõ mẫu số và cách xử lý mẫu số bằng không đối với chỉ số năng lượng chuẩn hóa và chỉ số sự kiện.

## Cấu trúc bản thảo

Dùng `manuscript-outline.md` để theo dõi các phần dự kiến: tiêu đề và tóm tắt; giới thiệu và câu hỏi nghiên cứu; nghiên cứu liên quan; thiết kế bộ chuẩn đánh giá và định nghĩa hàm mất mát; bộ dữ liệu và tiền xử lý; mô hình, cách chia tập dữ liệu và quy trình huấn luyện; chỉ số ràng buộc vật lý và điều kiện đủ mẫu; kết quả; phân tích chẩn đoán và độ bền vững; thảo luận; hạn chế; kết luận; tài liệu tham khảo; tuyên bố khả năng tái lập; chú thích hình và bảng.

Giữ phạm vi ở đánh giá thực nghiệm. Không tuyên bố có lý thuyết, bảo đảm hoặc kiến trúc mới. Nếu bằng chứng chưa đủ cho một phần, hãy đánh dấu rõ nội dung còn thiếu và nhờ agent `document` bổ sung nguồn hoặc agent `code` bổ sung quy trình/lần chạy thông qua agent điều phối.

## Truy xuất luận điểm và kiểm tra

Duy trì `claim-ledger.md` cùng bản thảo. Mỗi luận điểm quan trọng cần có mã, loại (tài liệu, quy trình hoặc kết quả), nội dung chính xác, liên kết bằng chứng và vị trí trong nguồn hoặc mã lần chạy, điều kiện/giới hạn, trạng thái rà soát. Cập nhật sổ theo dõi khi luận điểm thay đổi hoặc bị gỡ.

Trước khi xem bản thảo là hoàn chỉnh:

1. Đối chiếu từng nhận định thực tế và kết quả thực nghiệm với bằng chứng cùng điều kiện áp dụng.
2. Kiểm tra mọi bảng, biểu đồ và con số có thể được tạo lại từ đầu ra đã lưu; chú thích cần ghi đơn vị, tập mẫu, tập dữ liệu dùng để huấn luyện/đánh giá và cách tổng hợp.
3. Kiểm tra chỉ số và mặt nạ ràng buộc khớp với quy trình, gồm cả mẫu bị loại và dung sai.
4. Đối chiếu trích dẫn với siêu dữ liệu đã xác minh trong kho ghi chú và kiểm tra liên kết nội bộ cùng đường dẫn tệp kết quả.
5. Chạy lệnh dựng bản thảo và kiểm tra tài liệu tham khảo nếu đã có hệ thống dựng. Hiện không gian làm việc chưa có hệ thống dựng; không báo dựng thành công nếu chưa thực sự chạy.

Bàn giao cuối cùng cho agent điều phối cần nêu đường dẫn bản thảo, mức độ bao phủ bằng chứng, các bước kiểm tra đã chạy, luận điểm còn bỏ ngỏ và yêu cầu gửi đến agent `document` hoặc `code`.

