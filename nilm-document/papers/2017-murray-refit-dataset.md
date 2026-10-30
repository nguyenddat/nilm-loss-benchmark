---
type: paper
status: reviewed
title: "An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study"
authors: [David Murray, Lina Stankovic, Vladimir Stankovic]
year: 2017
venue: "Scientific Data, 4, 160122"
doi: "10.1038/sdata.2016.122"
source_url: "https://strathprints.strath.ac.uk/58873/8/Murray_etal_SD_2016_An_electrical_load_measurements_dataset_of_United_Kingdom.pdf"
citation_key: "murray2017refit"
read_date: 2026-10-30
tags: [nilm, dataset, refit]
---

# Bộ dữ liệu điện hộ gia đình REFIT — ghi chú nguồn

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Murray, David, Lina Stankovic, và Vladimir Stankovic. “An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study.” *Scientific Data* 4, 160122 (2017). DOI: [10.1038/sdata.2016.122](https://doi.org/10.1038/sdata.2016.122).
- Khóa trích dẫn: `murray2017refit` trong `ref.bib`, đối chiếu tiêu đề/tác giả/tạp chí/tập/mã bài/năm/DOI với bài báo gốc và hồ sơ dataset chính thức.
- Toàn văn đã đối chiếu: [PDF 12 trang trên kho University of Strathclyde](https://strathprints.strath.ac.uk/58873/8/Murray_etal_SD_2016_An_electrical_load_measurements_dataset_of_United_Kingdom.pdf); DOI bài báo [10.1038/sdata.2016.122](https://doi.org/10.1038/sdata.2016.122).
- Bộ dữ liệu: [Hồ sơ REFIT của University of Strathclyde](https://pureportal.strath.ac.uk/en/datasets/refit-electrical-load-measurements/); bài báo liên kết bản thô và bản sạch trong kho dữ liệu PURE (Data Records, PDF tr. 8).
- Mã thu thập và kiểm tra dữ liệu được tác giả công bố: [kho REFIT trên GitHub](https://github.com/David-Murray/REFIT) (Code availability, PDF tr. 7); chưa kiểm tra phiên bản mã hoặc tái chạy.
- Phạm vi đã đọc: toàn bài 12 trang gồm thiết kế lấy mẫu hộ, chọn thiết bị, thiết bị đo, dữ liệu và làm sạch, các lỗi đã biết, xác thực kỹ thuật, giới hạn và thông tin trích dẫn. Trạng thái `reviewed` áp dụng cho ghi chú đối với bài báo; README, metadata và tệp dữ liệu cụ thể của phiên bản dự án định dùng vẫn cần kiểm tra riêng.

## 2. Tóm tắt điều hành

- REFIT ghi nhận công suất tổng hộ gia đình và số đo của chín thiết bị riêng cho mỗi hộ, theo chu kỳ 8 giây, trên 20 hộ ở Vương quốc Anh trong khoảng hai năm (tóm tắt, PDF tr. 1; Background & Summary, PDF tr. 2–3).
- Số đo công suất tổng được lấy từ cảm biến kẹp dòng điện. Bài báo cho biết cảm biến không đo điện áp lưới và dẫn một thử nghiệm với sai số tương đối khoảng 6% (mục Household aggregate, PDF tr. 4).
- Sáu hộ có pin mặt trời. Ở hộ 3, 11 và 21, điện mặt trời vẫn xuất hiện trong số đo công suất tổng; do cảm biến không phân biệt được chiều công suất, nó bị ghi nhận như mức tiêu thụ tăng thêm và gây nhiễu liên quan đến thời tiết (mục Household aggregate, PDF tr. 4).
- Số đo IAM không đồng bộ với công suất tổng. Thời điểm ghi được gán theo mẫu công suất tổng, còn số đo thiết bị có thể cũ hơn đến 7 giây (mục Individual appliance monitors, PDF tr. 5; mục Code availability, PDF tr. 7).
- Cột ghi chú trong bộ dữ liệu đã làm sạch đánh dấu mẫu mà tổng số đo IAM lớn hơn công suất tổng (Technical Validation, PDF tr. 8). Điều này ảnh hưởng trực tiếp đến cách diễn giải C3.
- Bài ghi nhận uptime trung bình của các hộ là 88%; hộ 2 thấp nhất 76%, hộ 18 cao nhất 94%. Bản dữ liệu thô có 6,4% giá trị NaN; tài liệu diễn giải chúng là giá trị không đổi hoặc IAM không phản hồi (Hình 3; Data Records / Technical Validation, PDF tr. 6–8).
- Trong bản làm sạch, bài mô tả sửa thời gian do BST, xóa spike IAM trên 4.000 W, điền tiến giá trị trước cho gap ngắn hơn 2 phút, gán 0 cho gap dài hơn, và ghép lại các chuỗi khi IAM được chuyển giữa ổ cắm. Các phép xử lý này có thể ảnh hưởng thống kê hoạt động và sai số nên phải ghi lại khi chọn bản dữ liệu (Data Records, Algorithm 1, PDF tr. 7–8).

Đây là các nhận định của nguồn, không phải kết quả thí nghiệm mới của dự án.

## 3. Bài toán, động lực và đóng góp

Tác giả lập luận cần dữ liệu kiểu công tơ thông minh được thu trong sinh hoạt thật để phát triển/kiểm tra các dịch vụ năng lượng, trong đó có NILM. Đóng góp của bài là mô tả thiết kế và chất lượng bộ dữ liệu REFIT, cách làm sạch/đánh nhãn và cách sử dụng dữ liệu (Tóm tắt; Background & Summary, PDF tr. 1–2). Đây là bài mô tả bộ dữ liệu, không báo cáo so sánh mô hình hoặc hàm loss.

## 4. Phương pháp và loss

Không áp dụng: nguồn này mô tả bộ dữ liệu, không so sánh loss. Cách thu thập/làm sạch được trích ở mục 5; quy trình dataset cụ thể của dự án vẫn phải kiểm tra README và bản dữ liệu.

## 5. Bộ dữ liệu và thiết lập thu thập

| Thành phần | Thông tin trong nguồn | Vị trí |
| --- | --- | --- |
| Hộ gia đình và phép đo | Công suất tổng cùng chín phép đo thiết bị; 20 hộ; lấy mẫu mỗi 8 giây | Tóm tắt, PDF tr. 1; Background & Summary, tr. 2–3 |
| Cảm biến công suất tổng | Kẹp dòng điện; không đo điện áp; sai số tương đối khoảng 6% theo thử nghiệm được dẫn | Household aggregate, PDF tr. 4 |
| Thời gian IAM | Số đo thiết bị có thể cũ hơn thời điểm ghi công suất tổng đến 7 giây | Mục IAM, PDF tr. 5; Code availability, PDF tr. 7 |
| Điện mặt trời | Hộ 3, 11, 21 còn nhiễu điện mặt trời trong công suất tổng; cảm biến ghi nhận thành mức tiêu thụ tăng thêm | Household aggregate, PDF tr. 4 |
| Cờ báo C3 không khớp | Bản dữ liệu đã làm sạch ghi chú mẫu có tổng IAM vượt công suất tổng | Technical Validation, PDF tr. 8 |
| Cách chọn hộ | 57 hộ phản hồi; chọn dựa trên mức quen ICT và cơ cấu hộ; có hộ bị loại vì vấn đề kết nối | Methods, Selection methodology, PDF tr. 2 |
| Chọn thiết bị | Chọn các thiết bị có tiêu thụ cao và/hoặc dùng thường xuyên theo HES; mỗi hộ tối đa 9 IAM; hộ dùng gas làm sưởi chính và không có HVAC khác | Methods, PDF tr. 2; mục IAM, PDF tr. 4 |
| Độ phủ | Uptime trung bình 88%; hộ 2 là 76%, hộ 18 là 94%; các khoảng mất dữ liệu >1/4 ngày được thể hiện trên Hình 3 | Data Records, Hình 3, PDF tr. 8 |
| Phần năng lượng được đo phụ | Bảng 5 ghi tỷ lệ đo phụ theo hộ; ví dụ 22% ở hộ 8 và 55% ở hộ 18; hộ có điện mặt trời là N/A | Technical Validation, Bảng 5, PDF tr. 10 |
| Bản dữ liệu và giấy phép | Bài dẫn tệp CSV thô và sạch trên kho PURE; hồ sơ Strathclyde hiện ghi dữ liệu CC BY 4.0 | Data Records, PDF tr. 8; hồ sơ dữ liệu chính thức, Access Dataset |

Hộ được tuyển tình nguyện và thiết bị ưu tiên theo tiêu thụ/tần suất, không phải mẫu ngẫu nhiên đại diện toàn bộ hộ UK. Do đó kết quả chỉ trên REFIT không tự khái quát cho mọi hộ. (Methods, Selection methodology, PDF tr. 2.)

## 6. Kết quả mô tả và xác thực dữ liệu

Nguồn không báo cáo kết quả của mô hình hoặc hàm loss nào. Trong phần xác thực, bài so sánh điện năng đo công tơ tiện ích với tổng từ dữ liệu giám sát trên các khoảng ghi được (Bảng 4, PDF tr. 10); tác giả cũng tổng hợp phần công suất được thiết bị IAM ghi nhận theo hộ (Bảng 5) và số lượt sử dụng/năng lượng theo loại thiết bị (Bảng 6, PDF tr. 10). Bảng 5 cho thấy mức đo phụ thay đổi giữa hộ (ví dụ 22%–55% ở các hàng được trích) và để N/A cho hộ có điện mặt trời; đây không phải tỷ lệ lỗi dự đoán hay kiểm định C3.

Bảng 6 ghi nhận sự khác biệt lớn về tần suất sử dụng loại thiết bị: ví dụ tủ lạnh/freezer có rất nhiều lần sử dụng, máy giặt có 6.865 lượt và dishwasher 4.250 lượt toàn tập; pond pump/vivarium được xếp loại dùng liên tục. (Technical Validation, Bảng 6, PDF tr. 10.) Những thống kê mô tả này nhắc rằng số sự kiện và mức hoạt động khác nhau giữa thiết bị; chúng không tương đương với event-F1 hoặc độ khó dự đoán đã được kiểm định.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng và điều kiện | Vị trí | Mức chắc chắn |
| --- | --- | --- | --- |
| REFIT là ứng viên để khảo sát có giám sát cấp thiết bị. | Có kênh aggregate và IAM trên 20 hộ ở chu kỳ 8 giây. | Tóm tắt, PDF tr. 1; Bảng 1, PDF tr. 3 | Cao về cấu trúc; mức phù hợp với câu hỏi benchmark vẫn cần audit dữ liệu |
| Không thể giả định C3 đúng ở mọi mẫu. | Bản dữ liệu đã làm sạch đánh dấu mẫu mà tổng IAM vượt công suất tổng. | Technical Validation, PDF tr. 8 | Cao |
| Số đo không đồng bộ có thể ảnh hưởng so sánh tại từng thời điểm. | IAM có thể cũ hơn thời điểm ghi công suất tổng đến 7 giây. | Mục IAM và Code availability, PDF tr. 5 và 7 | Cao |
| Một số hộ có vấn đề đo đã biết do điện mặt trời. | Ở hộ 3, 11, 21, điện mặt trời bị ghi nhận như mức tiêu thụ tăng thêm và gây nhiễu liên quan thời tiết. | Household aggregate, PDF tr. 4 | Cao |
| Dữ liệu thiếu và làm sạch có thể ảnh hưởng phân tích thời gian. | 6,4% NaN ở dữ liệu thô; gap <2 phút điền tiến, gap dài hơn điền 0. | Technical Validation/Data Records, PDF tr. 7–8 | Cao |
| Mức quan sát được thay đổi giữa hộ và thiết bị. | Uptime trung bình 88%, hộ 2 thấp nhất 76%; tỷ lệ submetering theo hộ trong Bảng 5; số lượt sử dụng theo appliance trong Bảng 6. | Hình 3 và Bảng 5–6, PDF tr. 8–10 | Cao trong tập REFIT được mô tả |

## 8. Phân biệt điều nguồn nói và điều nguồn chứng minh

### Tác giả tuyên bố gì?

Bài báo mô tả cách đo REFIT, giới hạn cảm biến, thời điểm lấy mẫu, nhiễu điện mặt trời và quy trình làm sạch/xác thực tại các vị trí đã nêu.

### Bằng chứng trực tiếp

Bộ dữ liệu có phép đo công suất tổng và IAM; bài báo đồng thời ghi nhận khả năng lệch thời gian giữa các luồng và cờ trong dữ liệu đã làm sạch cho một số mẫu IAM/công suất tổng không khớp.

### Suy luận / đề xuất của dự án

Chỉ đánh giá C3 trên các mẫu đáp ứng giả định căn chỉnh và điện mặt trời đã chọn. Báo cáo riêng các cửa sổ bị gắn cờ không khớp hoặc loại chúng theo quy tắc đặt trước. Đo ảnh hưởng của cách căn chỉnh và chốt cách xử lý hộ 3, 11, 21 trước khi khóa quy trình. Đây là đề xuất, không phải kết quả trong nguồn.

## 9. Hạn chế và khả năng tái lập

- Đã rà soát toàn bài báo 12 trang; chưa kiểm tra README/metadata cụ thể của bản dataset thô/sạch sẽ dùng trong dự án.
- Sai số tương đối khoảng 6% được quy cho một thử nghiệm mà bài báo dẫn lại; cần xem nguồn đó và định nghĩa sai số trước khi diễn giải.
- Ghi chú chưa chốt dùng bản dữ liệu thô hay bản làm sạch, cách mã hóa cờ sai khác, hoặc chính sách căn chỉnh cụ thể.
- Chưa chạy lệnh tái lập hay kiểm tra dữ liệu cục bộ.

## 10. Liên hệ với benchmark loss NILM

**Suy luận / cách dùng dự kiến:** REFIT có thể hỗ trợ phần đánh giá có giám sát trong đề xuất nghiên cứu, với điều kiện chọn thiết bị/hộ, xác minh phiên bản, kiểm tra căn chỉnh và dữ liệu thiếu, đồng thời xử lý C3 rõ ràng. Nguồn này chưa giải quyết quy trình cho huấn luyện chỉ dùng công suất tổng hoặc nhiễu tổng hợp có kiểm soát.

## 11. Việc cần kiểm tra tiếp

- [x] Đọc hết bài gốc và đối chiếu vị trí nguồn cho các thông tin trích xuất trong ghi chú.
- [ ] Kiểm tra README, metadata và cột ghi chú của bản dữ liệu thô và bản đã làm sạch.
- [ ] Xác minh việc đổi thiết bị gắn với monitor và mức độ sẵn có của các thiết bị/hộ được chọn.
- [ ] Định nghĩa cách căn chỉnh thời điểm ghi và quy tắc chọn/loại mẫu cho C3.
- [x] Thêm nguồn vào bảng tổng quan tài liệu sau khi rà soát.

## 12. Trích dẫn

Murray, David, Lina Stankovic, và Vladimir Stankovic. “An electrical load measurements dataset of United Kingdom households from a two-year longitudinal study.” *Scientific Data* 4, 160122 (2017). https://doi.org/10.1038/sdata.2016.122.
