---
type: paper
status: reviewed
title: "Towards Comparability in Non-Intrusive Load Monitoring: On Data and Performance Evaluation"
authors: [Christoph Klemenjak, Stephen Makonin, Wilfried Elmenreich]
year: 2020
venue: "Bản thảo arXiv:2001.07708v1; bản hội nghị IEEE ISGT 2020 được ghi chú trên PDF"
doi: "10.48550/arXiv.2001.07708"
source_url: "https://arxiv.org/abs/2001.07708"
citation_key: "klemenjak2020comparabilitynonintrusiveloadmonitoring"
read_date: 2026-10-30
tags: [nilm, literature, comparability, evaluation, dataset]
---

# Khả năng so sánh trong NILM — Klemenjak và cộng sự (2020)

## Phạm vi và nguồn

- Bản phân tích dựa trên arXiv v1 nộp ngày 20-01-2020; bản PDF ghi dự kiến xuất bản tại IEEE ISGT 2020. Không giả định các phiên bản có nội dung hoàn toàn giống nhau.
- Nguồn gốc: [arXiv:2001.07708](https://arxiv.org/abs/2001.07708), DOI arXiv `10.48550/arXiv.2001.07708`.
- Bản toàn văn tiếng Việt: `papers/md/2020-klemenjak-comparability-fulltext.md`; PDF gốc: `papers/Towards Comparability in Non-Intrusive Load Monitoring On Data and Performance Evaluation.pdf`.
- Mã nghiên cứu được bài dẫn: [kho comparability](https://github.com/klemenjak/comparability). Chưa kiểm tra commit, môi trường hoặc tái chạy kết quả.
- PDF cục bộ là arXiv:2001.07708v1 [eess.SP], 5 trang; trang 1 ghi bản chính thức sẽ đăng tại 2020 IEEE PES Innovative Smart Grid Technologies Conference (ISGT). Số trang trong ghi chú là trang PDF của bản arXiv này; chưa đối chiếu bản IEEE.
- Metadata khớp `ref.bib` (tiêu đề, ba tác giả, năm 2020, eprint 2001.07708, eess.SP). `ref.bib` không có trường DOI; DOI arXiv `10.48550/arXiv.2001.07708` theo quy ước DataCite của arXiv.
- Bài định nghĩa “tần suất thấp” là 1–60 mẫu/phút, bao gồm hai đầu; toàn bộ mã được nêu là tương thích NILMTK. (Mục I, PDF tr. 1.)
- Trạng thái `reviewed` (rà soát 2026-10-30): đã đối chiếu từng con số, phương trình, bảng và locator trực tiếp với PDF (không dựa vào bản chuyển ngữ); đã tách lời tác giả, kết quả quan sát và suy luận dự án. Chưa tái lập thực nghiệm.

## Tóm tắt điều hành

- **WHY:** Tác giả nêu thiếu chuẩn hóa và đồng thuận về quy trình đánh giá khiến tái lập và so sánh “cực kỳ khó”; dẫn các nghiên cứu trước cho rằng do đa dạng dữ liệu và phương pháp luận, so sánh khách quan gần như không thể. (Tóm tắt và Mục I, PDF tr. 1.)
- **WHAT:** Bài phân tích sự khác biệt giữa một số bộ dữ liệu NILM tần suất thấp, đề xuất báo cáo mức nhiễu và độ bao phủ tập kiểm tra, rồi minh họa bằng các thử nghiệm CO/FHMM trên REDD và DRED. Đây là nghiên cứu về đánh giá và dữ liệu, không phải nghiên cứu so sánh hàm loss. (Mục I–V, PDF tr. 1–5.)
- Mô hình hóa tín hiệu tổng là tổng tín hiệu thiết bị cộng số dư `ε_t`; số dư gồm nhiễu đo và tải không được đo. Suy luận của người đọc: phương trình bài viết **không** khẳng định tổng tải đã đo bằng công suất tổng, cũng không cho phép suy ra C3 đúng vô điều kiện. (Mục II, phương trình 1, PDF tr. 1.)
- Dữ liệu khác nhau về thời lượng, số hộ, số công tơ, tần suất, loại công suất, số sự kiện và phần tải không quan sát. Các đại lượng này còn biến thiên giữa hộ trong cùng một dataset. (Mục III, PDF tr. 1–3; Bảng I, PDF tr. 2.)
- Trong ví dụ REDD nhà 6, cùng tập huấn luyện nhưng các tập kiểm tra có TSR 25,9%, 17,1%, 8,5%; cả 10 chuỗi RMSE (5 thiết bị × CO/FHMM) giảm đơn điệu khi TSR giảm. (Mục IV.C, Bảng II, PDF tr. 4.)
- Trong ví dụ DRED nhà 1, tập kiểm tra TSR 35,2%; RMSE trên tổng thiết bị đã đo (NAR 0%) thấp hơn so với aggregate thực tế có NAR 31,4%, với chênh lệch tối đa được báo cáo 14,2 W cho CO và 9,3 W cho FHMM. (Mục IV.C, Bảng III, PDF tr. 5.)
- **Không phải** chứng cứ trực tiếp về loss, ràng buộc C1–C3, hay dữ liệu REFIT; bài mô tả ba hộ REFIT trong Bảng I nhưng không dùng REFIT trong hai minh họa RMSE.

## 1. WHY — Vì sao khả năng so sánh quan trọng?

Tác giả nêu chưa có đồng thuận về thước đo hoặc định dạng báo cáo chung; đa dạng dữ liệu và phương pháp luận gây khó cho so sánh khách quan. Họ cũng đặt vấn đề rằng thuộc tính nào của dữ liệu quyết định độ khó NILM vẫn chưa được hiểu/định lượng đầy đủ. Đây là chẩn đoán của tác giả tại thời điểm công bố, không phải khảo sát hiện trạng toàn lĩnh vực vào năm nay. (Mục I và IV.A, PDF tr. 1, 3.)

Tác giả cho rằng dữ liệu thực tế không nhất thiết tương đương nhau: lượng dữ liệu, hoạt động hộ, chiến dịch đo và số lượng thiết bị được đo đều khác. Nếu kiểm tra trên khoảng thời gian ngắn hoặc đã khử nhiễu, kết quả có thể trông thuận lợi hơn. Hai nghiên cứu trường hợp được dùng để minh họa tính nhạy với lựa chọn đánh giá, không phải để chứng minh một thuật toán luôn tốt hơn thuật toán khác. (Mục III–IV.C, PDF tr. 1–5.)

## 2. WHAT — Bài toán và đóng góp

NILM được viết dưới dạng ước lượng công suất các thiết bị từ công suất tổng:

$$
y_t = \epsilon_t + \sum_{i=1}^{M} x_t^{(i)}
\tag{1}
$$

Trong đó `ε_t` là sai khác giữa phép đo tổng và tổng các kênh thiết bị được đo; bài định nghĩa nó gồm nhiễu đo và tải chưa đo. (Mục II, phương trình 1, PDF tr. 1.)

Các đóng góp của bài là phân tích dataset và thước đo, khuyến nghị báo cáo NAR/TSR/EVR, và nêu nhu cầu có thước đo độ phức tạp dataset thống nhất. Bài minh họa một số hệ quả qua CO và FHMM của NILMTK. Bài **không** đưa ra loss mới, thử nghiệm loss ablation, giới hạn công suất thiết bị độc lập, hay bảo đảm vật lý. (Tóm tắt; Mục IV–V, PDF tr. 1, 3–5.)

## 3. Phương pháp, mô hình và hàm mất mát

- **Kiến trúc/đầu vào/đầu ra:** bài không đề xuất kiến trúc mới; diễn giải NILM theo phương trình (1) và dùng CO/FHMM có sẵn trong NILMTK cho hai ví dụ. (Mục II, PDF tr. 1; Mục IV.C, PDF tr. 4–5.)
- **Hàm loss:** không nghiên cứu hoặc so sánh loss huấn luyện. RMSE là thước đo lỗi đánh giá ở cấp thiết bị, không phải objective mới được khảo sát. (Mục IV.C, phương trình 4, PDF tr. 4.)
- **Cách chia:** REDD nhà 6 dùng cùng tập huấn luyện cho ba tập test với TSR khác nhau; DRED nhà 1 có TSR 35,2% và so sánh aggregate thật với aggregate tổng hợp từ các kênh thiết bị đã đo. Bài **không nêu**: kích thước/khoảng thời gian của tập huấn luyện, vị trí thời gian của các tập test và việc chúng có lồng nhau không, tần suất/tiền xử lý dùng cho ví dụ, siêu tham số CO/FHMM, seed hay số lần chạy; không có đánh giá liên hộ. (Mục IV.C, PDF tr. 4–5.)
- **Tái lập:** bài dẫn kho mã nguồn; commit, môi trường và lệnh tái chạy chưa xác minh.

## 4. Bằng chứng về khác biệt dữ liệu

### Các chiều được báo cáo

Bảng I so sánh một số hộ được chọn trong AMPds2, COMBED, DRED, ECO, iAWE, REDD, REFIT và UK-DALE: thời lượng, số công tơ, chu kỳ lấy mẫu mains/submeter, loại đại lượng AC, số sự kiện tối thiểu/trung bình mỗi ngày và NAR khi có thể tính. BLUED bị loại vì thiếu công suất đo phụ, Tracebase và GREEND vì thiếu công suất tổng hộ. Đây là các hộ được chọn, không phải thống kê đại diện đầy đủ cho toàn dataset. (Mục III, PDF tr. 2; Bảng I, PDF tr. 2.)

Ví dụ Bảng I: REFIT hộ 1/20, 8/20, 17/20 lần lượt có thời lượng 638, 555, 443 ngày; 9 công tơ; chu kỳ ghi 7 giây ở cột mains và submeter; sự kiện trung bình/ngày 320, 229, 379; NAR(P) 65%, 78%, 45%. Bảng này ghi 7 giây, trong khi bài dataset REFIT của Murray và cộng sự mô tả chu kỳ 8 giây; Klemenjak không giải thích chênh lệch. Không gộp hai mô tả này thành cùng một phép đo nếu chưa xác minh quy tắc thời gian. (Bảng I, PDF tr. 2; đối chiếu [@murray2017refit], tóm tắt, PDF tr. 1.) Bảng I chỉ báo NAR(P) cho REFIT; cột NAR(S) để trống.

Số sự kiện ở Bảng I là số chuyển giữa hai trạng thái công suất đại diện, ước lượng cho từng thiết bị bằng thống kê, lọc và phân cụm; chi tiết phương pháp nằm trong tài liệu bổ sung (chưa đọc). Tác giả nêu giả thuyết số sự kiện có ảnh hưởng đáng kể tới hiệu năng phân rã — chưa được kiểm nghiệm trong bài. **Đây không phải event-F1**: đó là đặc tính đếm sự kiện dùng để mô tả hoạt động hộ, không phải điểm precision/recall/F1. Nhiều hộ có mức tối thiểu 0 sự kiện/ngày; tác giả diễn giải là có thiết bị hoàn toàn không được dùng trong chiến dịch đo nên công tơ chỉ ghi nhiễu. (Mục III.B, PDF tr. 2–3.)

### NAR: diễn giải và giới hạn

$$
\mathrm{NAR}=\frac{\sum_{t=1}^{T}\left|y_t-\sum_{i=1}^{M}x_t^{(i)}\right|}{\sum_{t=1}^{T} y_t}
\tag{2}
$$

NAR được tác giả lấy từ thước đo percent-noisy measure (%-NM) của Makonin & Popowich (tài liệu [18] trong bài). Tác giả dùng NAR để biểu thị phần năng lượng aggregate không được giải thích bởi các kênh submeter đã có, gồm tải không đo và nhiễu; NAR tính được cho mọi loại công suất AC khi có cả aggregate và submeter. NAR 0,25 được diễn giải là 25% tổng năng lượng đến từ tải không đo/nhiễu. Tác giả nhận xét nhiều submeter thường cho NAR thấp (ví dụ AMPds2), và một số hộ có NAR trên 50%, nghĩa là hiểu biết về thành phần aggregate rất hạn chế. (Mục III.C, phương trình 2, PDF tr. 3.)

Trong REFIT, công thức này chỉ nên dùng sau khi thống nhất chiều công suất, đơn vị, thời gian và mẫu hợp lệ giữa mains với các IAM. NAR là phần dư theo aggregate đã quan sát, không tách riêng nhiễu cảm biến khỏi tải thực chưa đo; không phải thước đo trực tiếp của C3 và không chứng minh mô hình dự đoán vi phạm C3. Đây là suy luận từ định nghĩa phương trình 1–2 và vấn đề căn chỉnh REFIT được mô tả trong [@murray2017refit].

## 5. Thước đo bao phủ tập kiểm tra

Tác giả đề xuất:

$$
\mathrm{TSR}=\frac{\text{thời lượng tập kiểm tra}}{\text{tổng thời lượng}},\qquad
\mathrm{EVR}=\frac{\text{số sự kiện trong tập kiểm tra}}{\text{tổng số sự kiện}}
\tag{3}
$$

Khi có khoảng thiếu lớn, thời lượng dùng ở TSR được tính bằng tổng thời lượng của các khoảng còn dữ liệu. TSR và EVR mô tả độ bao phủ theo thời lượng và số sự kiện; chúng không tự bảo đảm test đại diện hoặc dễ/khó tương đương. (Mục IV.C, phương trình 3, PDF tr. 4.)

### Ví dụ REDD

Tác giả huấn luyện CO/FHMM bằng cùng tập huấn luyện và trích ba test từ REDD nhà 6 với TSR lần lượt 25,9%, 17,1%, 8,5%. Bảng II cho thấy cả 10 chuỗi RMSE giảm đơn điệu khi TSR giảm; ví dụ điều hòa CO: 231,3 → 74,2 → 41,2; FHMM: 227,6 → 65,3 → 44,1. Bảng II **không ghi đơn vị**; RMSE theo phương trình 4 có đơn vị của công suất thiết bị (nhiều khả năng W, như văn bản dùng W cho Bảng III) — chưa xác minh. Tác giả lập luận các đoạn dữ liệu không tương đương nhau (có đoạn chứa sự kiện khó phát hiện) nên nên kiểm tra trên nhiều đoạn thay vì “cherry-picking”. Suy luận của người đọc: vì ba tập test khác nhau cả về nội dung lẫn kích thước, ví dụ không tách được tác động của kích thước test khỏi tác động của đoạn được chọn; con số này không phải bằng chứng về tính tổng quát hay hiệu quả loss. (Mục IV.C, phương trình 4 và Bảng II, PDF tr. 4.)

### Ví dụ DRED: dữ liệu thực và tổng hợp đã khử nhiễu

Trên DRED nhà 1, tác giả báo TSR=35,2%, huấn luyện CO/FHMM trên DRED, rồi đánh giá trên aggregate thực và aggregate dựng bằng tổng các thiết bị đã đo. Hai điều kiện có NAR lần lượt 31,4% và 0%. Bảng III cho thấy RMSE nhỏ hơn ở NAR=0 cho cả 12 cặp (6 thiết bị × CO/FHMM), cột chênh lệch khớp với hiệu hai cột; ví dụ microwave CO 68,2 W so với 54,0 W, FHMM 60,7 W so với 51,4 W. Tác giả báo chênh lệch lớn nhất 14,2 W và 9,3 W tương ứng. Tác giả dẫn thêm tài liệu trước ([18], [21]) rằng kiểm tra đã khử nhiễu thường cho độ chính xác cao hơn và không phản ánh thực tế. Suy luận của người đọc: ví dụ minh họa thay đổi cấu tạo tín hiệu đầu vào làm thay đổi kết quả, nhưng không tách riêng quan hệ nhân quả giữa NAR với lỗi và không đại diện cho REFIT. (Mục IV.C, PDF tr. 4–5; Bảng III, PDF tr. 5.)

## 6. Thước đo độ chính xác và khuyến nghị đánh giá

Tác giả phân biệt thước đo phát hiện sự kiện với thước đo ước lượng năng lượng, nhắc rằng cần chọn metric cẩn thận để tránh diễn giải sai. Họ cho rằng đánh giá phải gồm cả hiệu năng phân loại lẫn ước lượng năng lượng, khuyến nghị dùng thước đo chuẩn hóa để so sánh thiết bị công suất thấp với công suất lớn, và yêu cầu mô tả chính xác mọi thao tác trên dữ liệu (lấy mẫu lại, làm sạch, cân bằng). Họ cũng nêu câu hỏi liệu đánh giá có nên vượt ra ngoài độ chính xác, gồm khả năng khái quát, khả năng mở rộng và bảo vệ quyền riêng tư, và cho rằng hiệu năng trên kịch bản chưa thấy nên được đánh giá. (Mục IV.B, PDF tr. 3–4; Mục IV.C, PDF tr. 4.)

Trong ví dụ thực nghiệm, metric là RMSE cấp thiết bị (phương trình 4); Bảng II–III không ghi đơn vị, văn bản dùng W cho chênh lệch ở Bảng III. Bài không cung cấp F1 cho các ví dụ REDD/DRED. Suy luận của dự án: không dùng số sự kiện/ngày trong Bảng I thay cho F1 sự kiện của proposal; cần định nghĩa event-F1 độc lập về ngưỡng ON/OFF, ghép sự kiện và dung sai thời gian. (Mục III.B, IV.C, PDF tr. 2–5.)

## 7. Kết luận tác giả và phạm vi chứng minh

### Tác giả kết luận/khuyến nghị

- Cần lựa chọn dataset cẩn thận, mô tả tiền xử lý/làm sạch và báo cáo kết quả thống nhất; coi các dataset là thay thế được cho nhau khi đánh giá có thể gây hiểu lầm. (Tóm tắt, PDF tr. 1; Mục IV.A, PDF tr. 3; Mục IV.B–V, PDF tr. 3–5.)
- Báo cáo NAR để phân biệt dữ liệu aggregate thực với aggregate đã khử nhiễu; báo cáo TSR và EVR để chỉ rõ lượng thời gian và số sự kiện nằm trong test. (Mục IV.C–V, phương trình 2–3, PDF tr. 3–5.)
- Phát triển thước đo độ phức tạp độc lập với thuật toán, vì độ khó giữa dataset/hộ chưa được định lượng đầy đủ. (Mục IV.A, PDF tr. 3; Mục V, PDF tr. 5.)

### Thực nghiệm trực tiếp hỗ trợ điều gì?

Hai nghiên cứu trường hợp cho thấy trong các cấu hình được báo cáo (mỗi cấu hình một kết quả, không báo độ biến thiên) rằng RMSE thay đổi theo phạm vi test và việc dùng aggregate đã khử nhiễu thay cho aggregate thực. Chúng không chứng minh một protocol phổ quát, không kiểm nghiệm loss, không so sánh liên hộ đủ rộng, và không kiểm nghiệm ràng buộc vật lý. (Mục IV.C, Bảng II–III, PDF tr. 4–5.)

### Hạn chế / chưa được giải quyết

Các ý dưới đây là nhận xét của người đọc về phạm vi bài, không phải hạn chế do tác giả tự nêu.


- Ví dụ RMSE là CO/FHMM trên REDD nhà 6 và DRED nhà 1; không dùng các ví dụ đó để xếp hạng trực tiếp với NILMTK hoặc REFIT.
- Bảng I chỉ mô tả một số hộ được chọn; không phải kiểm định thống kê đại diện toàn dataset.
- Bài không nghiên cứu loss, C1–C3, độ bất định giữa nhiều seed, hay xác thực chéo hộ cho câu hỏi dự án.
- Bài định nghĩa `ε_t` nhưng không đưa ra dấu hay cận cho phần dư; suy luận: tổng IAM có thể lớn hơn hoặc nhỏ hơn mains tùy thiết bị, sai số và căn chỉnh.
- REFIT trong Bảng I có NAR(P) cao ở các hộ mẫu, nhưng đó không thay thế kiểm tra cờ, lệch thời gian và điện mặt trời theo bản dữ liệu mà dự án thực sự dùng.

## 8. Liên hệ với nghiên cứu hiện tại

**Suy luận / đề xuất, chưa phải kết quả:**

- Cùng kiến trúc và split, thay loss là phép đối chiếu phù hợp hơn so sánh điểm số lấy từ các bài khác nhau. Giữ cố định dữ liệu, xử lý thiếu, cách căn chỉnh, mô hình, thông tin nhãn và ngân sách.
- Ghi TSR, EVR, số hộ, số cửa sổ/sự kiện và thời lượng dùng được cho mọi kết quả; nếu split theo hộ thì bổ sung số hộ kiểm tra và phân phối theo hộ.
- Báo cáo NAR hoặc chỉ số phần dư chỉ khi các kênh được đồng bộ/đơn vị tương thích. Báo cáo riêng số mẫu REFIT bị gắn cờ hoặc không đủ điều kiện; không dùng NAR thay cho mức vi phạm mô hình.
- Đánh giá C3 tách khỏi chất lượng dataset: trên mặt nạ mẫu đủ điều kiện, so sánh tổng dự đoán thiết bị với mains có cùng timestamp/đơn vị; báo cáo tỷ lệ mẫu hợp lệ, tần suất vi phạm, mức vượt trung bình/lớn nhất và dung sai đo lường đã chọn.
- C1 có thể kiểm tra theo đầu ra không âm; C2 chỉ khi nguồn giới hạn `P_i^max` độc lập, theo thiết bị/hộ/điều kiện; NAR không cung cấp giới hạn C2.
- Đánh giá event-F1 cần đặc tả event matcher; không tái dùng event count/day hoặc FTE/F-score khác định nghĩa mà không đối chiếu công thức.

## 9. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| Dữ liệu không đồng nhất ở thời lượng, hộ, tần suất, loại công suất và mức tải chưa đo. | Dataset/hộ được chọn trong bảng so sánh | Mục III, PDF tr. 1–3; Bảng I, PDF tr. 2 | Cao cho các trường được báo cáo; không đại diện toàn dataset |
| Số event/day là mô tả số chuyển trạng thái, không phải event-F1. | Định nghĩa event và thống kê số sự kiện tối thiểu/trung bình | Mục III.B, PDF tr. 2–3 | Cao |
| Phần dư aggregate gồm tải không đo và nhiễu. | Định nghĩa `ε_t` | Mục II, phương trình 1, PDF tr. 1 | Cao |
| RMSE nhạy với phần trăm/loại dữ liệu kiểm tra trong ví dụ. | REDD H6, TSR 25,9/17,1/8,5%, cùng train; RMSE (Bảng II không ghi đơn vị) | Mục IV.C, Bảng II, PDF tr. 4 | Cao trong phạm vi ví dụ |
| Aggregate khử nhiễu cho sai số thấp hơn trong ví dụ DRED. | DRED H1, TSR 35,2%, NAR 31,4% so với 0%, CO/FHMM | Mục IV.C, Bảng III, PDF tr. 5 | Cao trong phạm vi ví dụ |
| NAR không chứng minh C3. | NAR đo sai khác tín hiệu tổng và tổng kênh đã đo; không tách lỗi đo khỏi tải không đo | Mục II–III.C, phương trình 1–2, PDF tr. 1–3 | Suy luận trực tiếp từ định nghĩa |

## 10. Trích dẫn

Klemenjak, Christoph, Stephen Makonin, và Wilfried Elmenreich. “Towards Comparability in Non-Intrusive Load Monitoring: On Data and Performance Evaluation.” arXiv:2001.07708v1, 2020. DOI: [10.48550/arXiv.2001.07708](https://doi.org/10.48550/arXiv.2001.07708). Xem khóa trong `ref.bib`.
