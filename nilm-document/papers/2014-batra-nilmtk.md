---
type: paper
status: reviewed
title: "NILMTK: An Open Source Toolkit for Non-intrusive Load Monitoring"
authors: [Nipun Batra, Jack Kelly, Oliver Parson, Haimonti Dutta, William Knottenbelt, Alex Rogers, Amarjeet Singh, Mani Srivastava]
year: 2014
venue: "Proceedings of the 5th International Conference on Future Energy Systems (ACM e-Energy)"
doi: "10.1145/2602044.2602051"
source_url: "http://dx.doi.org/10.1145/2602044.2602051"
citation_key: "NILMTK"
read_date: 2026-10-30
tags: [nilm, literature, reproducibility, evaluation, dataset]
---

# NILMTK: An Open Source Toolkit for Non-intrusive Load Monitoring

## Phạm vi và trạng thái đọc

Ghi chú ưu tiên **WHY** (vì sao cần NILM và hạ tầng so sánh) và **WHAT** (bài toán, mục tiêu, đóng góp), đồng thời trích xuất bằng chứng, kết quả, giới hạn và cơ hội tái sử dụng. Đây không phải hướng dẫn thao tác. Số trang dưới đây là số trang PDF của tệp cục bộ, tính từ trang tiêu đề.

- PDF gốc: `papers/NILMTK An Open Source Toolkit for Non-intrusive Load Monitoring.pdf`. Tệp này là bản arXiv:1404.3878v1 [stat.AP], ngày 15-04-2014, 14 trang (10 trang nội dung, tài liệu tham khảo, phụ lục), ghi “To appear in ... ACM e-Energy, Cambridge, UK. 2014” (PDF tr. 1). Số trang trong ghi chú là của bản arXiv này, **không phải** số trang 265–276 của bản ACM; chưa đối chiếu nội dung với bản ACM chính thức.
- Bản toàn văn Markdown: `papers/md/2014-batra-nilmtk-fulltext.md` (chỉ dùng để tra cứu; mọi số liệu dưới đây đã đối chiếu trực tiếp với PDF).
- Trích dẫn: khóa `NILMTK` trong `ref.bib`. Tiêu đề, tác giả, năm và hội nghị khớp PDF; DOI, nhà xuất bản và trang 265–276 lấy từ `ref.bib`/bản ACM, không kiểm được từ tệp arXiv cục bộ (Klemenjak và cộng sự 2020, tài liệu tham khảo [8], cũng ghi tr. 265–276 — nguồn thứ cấp).
- Trạng thái `reviewed` (rà soát 2026-10-30): đã đối chiếu từng con số, công thức, bảng và locator với PDF bản arXiv v1; đã tách lời tác giả, kết quả quan sát và suy luận dự án. Chưa tái lập thực nghiệm; chưa so với bản ACM.
- Sáu bộ dữ liệu đánh giá trong bài không gồm REFIT; các con số không phải bằng chứng trực tiếp trên REFIT.

## Tóm tắt điều hành

- **WHY lĩnh vực:** NILM phân rã phép đo điện tổng thành mức tiêu thụ thiết bị. Tác giả nêu ba lợi ích kỳ vọng: giúp hộ gia đình nhận biết và giảm tiêu thụ; cung cấp phản hồi tiết kiệm theo thiết bị; hỗ trợ dời tải linh hoạt sang thời điểm điện rẻ hơn hoặc ít carbon hơn. Đây là động lực ứng dụng, không phải lợi ích được kiểm nghiệm trong thí nghiệm của bài. (Giới thiệu, PDF tr. 1.)
- **WHY bài báo:** theo mô tả năm 2014, so sánh NILM bị cản trở bởi khác biệt dữ liệu/hộ/thời đoạn, thiếu hiện thực đối chứng chung và khác biệt metric; vì thế kết quả khó đặt cạnh nhau hoặc đánh giá khả năng khái quát. (Giới thiệu, PDF tr. 1–2; mục 2.1–2.3, PDF tr. 2–3.)
- **WHAT bài toán:** ước lượng công suất thật của từng thiết bị tại thời điểm t từ công suất tổng hộ; nhiều thuật toán biểu diễn trạng thái thiết bị rời rạc như tắt, bật hoặc trung gian. (Mục 2.5, PDF tr. 4.)
- **WHAT NILMTK:** hạ tầng nghiên cứu mã nguồn mở gồm định dạng dữ liệu chung, nhập dữ liệu, thống kê/chẩn đoán, tiền xử lý, hai thuật toán đối chứng và các metric. Đóng góp là hỗ trợ phân tích, so sánh nhất quán; không phải kiến trúc mới. (Tóm tắt, PDF tr. 1; mục 3; kết luận, PDF tr. 10.)
- Bài báo nhập sáu bộ dữ liệu (REDD, Smart*, Pecan Street, iAWE, AMPds, UK-DALE); loại BLUED, Tracebase và HES vì lý do dữ liệu/thời gian. (Mục 3.1, PDF tr. 4.)
- Bằng chứng thực nghiệm minh họa dị biệt dữ liệu và metric, cũng như CO/FHMM; không kiểm nghiệm loss, ràng buộc vật lý, nhiễu có kiểm soát hay dịch chuyển hộ theo benchmark hiện tại. (Mục 4.1–4.5, PDF tr. 7–10.)
- Hai hộ Pecan Street có tỷ lệ năng lượng đo phụ trên 100%, được tác giả giải thích là kênh đo chồng lấn. Điều này liên quan đến điều kiện dữ liệu để đánh giá C3, nhưng không phải đánh giá trực tiếp C3. (Mục 4.1, Bảng 2, PDF tr. 7.)

## 1. WHY — Động lực và vấn đề nghiên cứu

### Vì sao NILM có ích theo bài báo?

Ba ứng dụng tác giả nêu: thông tin mức dùng giúp cư dân hành động giảm tiêu thụ; phản hồi theo thiết bị có thể lượng hóa lợi ích tài chính khi thay thiết bị kém hiệu quả; nhận biết thời điểm dùng có thể giúp khuyến nghị dời tải sang giờ điện rẻ hoặc ít phát thải carbon. Đây là lập luận động lực, không phải kết quả đánh giá người dùng hay tiết kiệm năng lượng của NILMTK; chỉ lợi ích thứ nhất được gắn trích dẫn [2] (Darby 2006), hai lợi ích sau không kèm nguồn. (Giới thiệu, PDF tr. 1.)

### Vì sao cần công cụ đánh giá chung?

Tác giả nêu ba điểm nghẽn (Giới thiệu, PDF tr. 1–2; mục 2.1–2.3, PDF tr. 2–3):

1. **Dữ liệu không đồng nhất:** mục tiêu, định dạng, thiết bị đo, số hộ, thời lượng và tần số lấy mẫu khác nhau. Theo hiểu biết của tác giả, mỗi đóng góp đến thời điểm đó chỉ được đánh giá trên một bộ dữ liệu, nên khó biết phương pháp có khái quát sang hộ mới không; nhiều bài còn chọn tập con hộ/thiết bị/thời đoạn khiến khó tái lập.
2. **Đối chứng không thống nhất:** phương pháp mới dùng benchmark khác nhau; thiếu hiện thực tham chiếu công khai khiến đánh giá lại tốn công hoặc không thể thực hiện.
3. **Metric không thống nhất:** nghiên cứu nhắm các trường hợp sử dụng khác nhau nên báo cáo thước đo khác nhau. Mục 2.3 nêu ví dụ bốn biến thể metric cùng nhóm “energy correctly assigned” trên REDD có định nghĩa khác nhau (chuẩn hóa theo lát thời gian và có thể âm; theo từng thiết bị; theo toàn chuỗi để sai số thừa/thiếu bù trừ nhau; đếm kép năng lượng gán nhầm), nên không so sánh số được. (Mục 2.3, PDF tr. 3.)

**Diễn giải của người đọc:** luận điểm không chỉ là giảm công lập trình. Muốn kết quả có ý nghĩa liên nghiên cứu, cần biết dữ liệu, metric và đối chứng; nếu thiếu, chênh lệch số không thể được diễn giải như chênh lệch năng lực thuật toán. Đây là mô tả bối cảnh năm 2014, không phải xác nhận hiện trạng NILM ngày nay.

## 2. WHAT — Bài toán và loại đóng góp

Bài báo ký hiệu công suất thật thiết bị n tại thời điểm t là $y_t^{(n)}$, dự đoán là $\hat y_t^{(n)}$, trạng thái thật/dự đoán là $x_t^{(n)}$, $\hat x_t^{(n)}$, và công suất tổng là $\bar y_t$. Mục tiêu NILM là ước lượng công suất thiết bị từ phép đo tổng; nhiều thuật toán dùng trạng thái rời rạc. (Mục 2.5, PDF tr. 4.)

Các nhóm đóng góp NILMTK gồm: biểu diễn chung cho dữ liệu/metadata; thống kê và chẩn đoán; tiền xử lý khác biệt đo lường; hai thuật toán đối chứng CO và FHMM; metric phát hiện và phân rã năng lượng; khả năng thêm dữ liệu và thuật toán. Tác giả nói rõ CO/FHMM được đưa vào để tạo đối chứng, không nhằm công bố kết quả trạng thái nghệ thuật (mục 3.5, PDF tr. 5). Bài dùng bản phát hành NILMTK v0.1.0 (chú thích 3, PDF tr. 2). (Tóm tắt, PDF tr. 1; mục 3.1–3.7, PDF tr. 4–7; kết luận, PDF tr. 10.)

## 3. Dữ liệu: khác biệt, chọn và loại

Bảng 1 tổng hợp chín nguồn theo địa điểm, thời lượng, số hộ và tần số đo (PDF tr. 3). Chu kỳ lấy mẫu trải từ 2 hoặc 10 phút (HES) tới 12–16 kHz (BLUED, UK-DALE); tác giả quy đổi dải tần số thiết bị là 0,008 Hz tới 16 kHz (mục 3.4, PDF tr. 5). Số hộ từ một tới 251 (HES); thời lượng mỗi hộ từ 3 ngày (REDD 3–19 ngày) tới 17 tháng (UK-DALE 3–17 tháng). Khác biệt mục tiêu và định dạng tạo rào cản kỹ thuật, còn đánh giá trên một bộ/hộ hạn chế khả năng khái quát (mục 2.1, PDF tr. 2–3).

| Bộ dữ liệu | Vai trò và đặc trưng trong bài |
| --- | --- |
| REDD | Tích hợp và so sánh; MIT, Massachusetts; 6 hộ; 3–19 ngày; thiết bị 3 giây, mains 1 giây và 15 kHz. (Bảng 1, PDF tr. 3.) |
| Smart* | Tích hợp và so sánh; UMass; 3 hộ; 3 tháng; kênh 1 giây. Chỉ một hộ có dữ liệu đo phụ (mục 2.1, PDF tr. 2), và Bảng 2 xử lý Smart* như một hộ. (Bảng 1, PDF tr. 3; Bảng 2, PDF tr. 7.) |
| Pecan Street / Sample | Tích hợp và so sánh; Austin, Texas; 10 hộ; 7 ngày; kênh 1 phút. (Bảng 1, PDF tr. 3.) |
| iAWE | Tích hợp và so sánh; IIIT Delhi; 1 hộ; 73 ngày; thiết bị 1 hoặc 6 giây, mains 1 giây. (Bảng 1, PDF tr. 3.) |
| AMPds | Tích hợp và so sánh; British Columbia; 1 hộ; 1 năm; kênh 1 phút. (Bảng 1, PDF tr. 3.) |
| UK-DALE | Tích hợp và so sánh; London; 4 hộ; 3–17 tháng; thiết bị 6 giây, mains 1–6 giây và 16 kHz. (Bảng 1, PDF tr. 3.) |
| BLUED | Không tích hợp: thiếu công suất đo phụ; Bảng 1 mô tả nhãn chuyển trạng thái. (Mục 3.1, PDF tr. 4; Bảng 1, tr. 3.) |
| Tracebase | Không tích hợp: thiếu công suất tổng hộ. (Mục 3.1, PDF tr. 4.) |
| HES | Không tích hợp do giới hạn thời gian. (Mục 3.1, PDF tr. 4.) |

Sáu tập dùng trong so sánh **không gồm REFIT**. UK-DALE không phải REFIT và không thay thế bằng chứng trên REFIT.

### Chẩn đoán và tiền xử lý có ý nghĩa gì?

Tác giả cho rằng không bộ dữ liệu nào hoàn hảo nên cần khảo sát đặc tính dữ liệu trước khi đánh giá; ví dụ nhiều thuật toán giả định kênh cảm biến liên tục, nhưng giả định này sai khi cảm biến tắt hoặc lỗi. Chẩn đoán (mục 3.2) gồm phát hiện khoảng trống (gap: hai mẫu liên tiếp cách nhau quá một ngưỡng định trước), dropout rate, dropout rate bỏ qua gap và up-time; tỷ lệ năng lượng đo phụ là một thống kê (mục 3.3), được tính sau khi che các gap của kênh mains khỏi kênh đo phụ, và giả định dữ liệu đo phụ thiếu thêm là do công tơ/tải tắt. (Mục 3.2–3.3, PDF tr. 5.)

Bảng 2 báo giá trị min/median/max qua các hộ khi có nhiều hộ; mỗi cột lấy min/median/max riêng (PDF tr. 7): REDD có 9/16/23 thiết bị, tỷ lệ năng lượng đo phụ 58/71/89%, dropout bỏ qua gap 0/10/16% và tỷ lệ up-time 8/40/79%; UK-DALE có 4/12/53 thiết bị, đo phụ 19/48/82%, dropout 0/7/22%, up-time 73/84/100%; Smart* có 25 thiết bị, 86% đo phụ, dropout 0%, up-time 96%; iAWE có 10 thiết bị, 48% đo phụ, dropout 8%, up-time 93%; AMPds có 20 thiết bị, 97% đo phụ, dropout 0%, up-time 100%; Pecan Street có 13/14/22 thiết bị, đo phụ 75/87/150%, dropout 0%, up-time 100%. Cột “Mains up-time per house (days)” không được chép ở đây.

**Cảnh báo ngữ nghĩa đo:** hai hộ Pecan Street vượt 100% năng lượng đo phụ; tác giả diễn giải là một số kênh chồng lấn/thiết bị bị đo bởi nhiều kênh và đề xuất metadata về đấu nối điện. Đây là quan sát cấu trúc dữ liệu, không phải phát hiện về dự đoán mô hình. (Mục 4.1, Bảng 2, PDF tr. 7.)

Bài còn nêu dao động điện áp khác nhau giữa các bộ dữ liệu (iAWE 180–250 V, Smart* 118–123 V) có thể tác động công suất, và NILMTK chuẩn hóa theo công thức Hart với số mũ 2 (công thức 1, mục 3.4, PDF tr. 5). Chuẩn hóa làm phân phối công suất toaster (tải điện trở tuyến tính) hẹp hơn rõ, ít tác động lên tải công suất hằng (máy giặt-sấy, đèn LED), còn với điều hòa phi tuyến thì phương sai tăng; tác giả dẫn dạng tổng quát số mũ β của Hart (β = 2 cho tải tuyến tính, β = 0,7 cho tủ lạnh) và cho rằng lợi ích chuẩn hóa phụ thuộc tỷ lệ tải điện trở trong hộ. Do đó một bước chuẩn hóa không mặc định cải thiện mọi thiết bị. (Mục 4.3, Hình 4, công thức 17, PDF tr. 8–9.)

## 4. Metric: định nghĩa và cạm bẫy

Bài báo lập luận cần nhiều metric vì ứng dụng NILM khác nhau (mục 2.3, PDF tr. 3; mục 3.7, PDF tr. 6–7). Cột “Cạm bẫy” là suy luận của người đọc, không phải lời tác giả.

| Metric | Ý nghĩa trong bài | Cạm bẫy khi diễn giải |
| --- | --- | --- |
| Sai số tổng năng lượng gán | Trị tuyệt đối chênh lệch giữa tổng thật và tổng dự đoán của thiết bị n trên toàn tập: $\lvert\sum_t y_t^{(n)}-\sum_t \hat y_t^{(n)}\rvert$ (công thức 3). | Lấy trị tuyệt đối nên mất chiều thừa/thiếu; sai số thừa và thiếu ở các lát khác nhau bù trừ nhau; bài không nêu đơn vị hay hệ số thời gian lấy mẫu. |
| FTE | Độ chồng lấp giữa tỷ trọng năng lượng thật và dự đoán của từng thiết bị (công thức 4). | Đo phân bổ năng lượng toàn chuỗi, không phải độ chính xác mỗi lát thời gian. Công thức in trong PDF có tử số $\sum_n y_t^{(n)}$ (tổng theo n) trong khi mô tả bằng lời là tỷ trọng năng lượng của từng thiết bị (tổng theo t); nhiều khả năng là lỗi ký hiệu, chưa xác minh với bản ACM hoặc mã v0.1.0. |
| NEP | Tổng sai lệch công suất tuyệt đối theo thiết bị, chuẩn hóa theo tổng năng lượng thật của thiết bị (công thức 5). | Nhạy với mẫu số/năng lượng thiết bị; thấp hơn là tốt hơn. |
| RMS error | Căn trung bình bình phương sai số công suất (công thức 6). | Phạt mạnh sai số lớn; không đo vi phạm ràng buộc vật lý. |
| Precision, recall, F-score | TP/FP/FN khi phân loại ON/OFF tại từng lát thời gian; F-score là trung bình điều hòa precision và recall (công thức 7–15). Câu mô tả precision bằng lời trong PDF ghi nhầm “actually off”, công thức 13 là TP/(TP+FP). | **Không phải event-F1 ghép onset/offset.** Bài không nêu quy tắc/ngưỡng chuyển công suất thành trạng thái ON/OFF trong định nghĩa metric. |
| Hamming loss | Sai phân loại trạng thái trên thiết bị và thời gian (công thức 16). | Đếm lỗi trạng thái, không đo watt hoặc vi phạm tổng. |

Theo tác giả, NEP thấp và FTE/F-score cao là tốt; FTE/F-score trong [0,1], NEP không âm. (Mục 4.4, PDF tr. 9.) Không đồng nhất metric của bài với metric dự án khi chưa đối chiếu công thức, đơn vị, threshold, mask dữ liệu thiếu và cách gộp.

## 5. Minh họa thực nghiệm và số liệu

### So sánh CO/FHMM liên bộ dữ liệu

Đây là minh họa trong bài, không phải tái lập độc lập. Tác giả dùng **hộ đầu tiên** của sáu bộ; nửa đầu chuỗi để huấn luyện, nửa sau để phân rã; chỉ mô hình hóa thiết bị đóng góp trên 5%; mỗi thiết bị hai trạng thái. REDD, UK-DALE, Smart* và iAWE được giảm mẫu về 1 phút; gap nhỏ được nội suy, vùng thiếu mains hoặc thiết bị bị bỏ qua. AMPds và Pecan Street không cần tiền xử lý nêu trên. Ba metric NEP, FTE, F-score được chọn vì được dùng nhiều nhất trong nghiên cứu trước. Chạy trên laptop i7 2,3 GHz, RAM 8 GB, Linux; seed cố định, chi tiết trên GitHub dự án. (Mục 4.4, PDF tr. 9.) Suy luận của người đọc: kết quả không đại diện cho mọi hộ/thiết bị, đặc biệt thiết bị nhỏ.

Bảng 3 báo thời gian huấn luyện, thời gian phân rã, NEP, FTE và F-score (PDF tr. 9). Các cặp dưới đây theo thứ tự CO; FHMM. NEP là metric không thứ nguyên; thấp hơn là tốt hơn. Hai cột thời gian trong bảng gốc lần lượt là giây huấn luyện và giây phân rã, không phải NEP.

| Tập / phạm vi | NEP (không thứ nguyên) | FTE | F-score | Ghi chú theo metric |
| --- | ---: | ---: | ---: | --- |
| REDD, hộ đầu, thiết bị >5%, nửa sau kiểm tra | 1,61; 1,35 | 0,77; 0,83 | 0,31; 0,31 | FHMM có NEP thấp hơn; FTE cao hơn; F-score bằng nhau. |
| Smart*, cùng giao thức | 3,10; 2,71 | 0,50; 0,66 | 0,53; 0,61 | FHMM tốt hơn theo cả NEP, FTE và F-score. |
| AMPds, cùng giao thức | 2,23; 0,96 | 0,44; 0,84 | 0,55; 0,71 | FHMM tốt hơn theo cả ba metric; dữ liệu kéo dài một năm. |
| iAWE, cùng giao thức | 0,91; 0,91 | 0,89; 0,89 | 0,73; 0,73 | Ba metric bằng nhau. |
| Pecan Street, cùng giao thức | 0,68; 0,75 | 0,99; 0,87 | 0,77; 0,77 | CO có NEP thấp hơn và FTE cao hơn; F-score bằng nhau. |
| UK-DALE, cùng giao thức | 3,66; 3,67 | 0,81; 0,80 | 0,38; 0,38 | CO có NEP thấp hơn nhẹ; FHMM có FTE thấp hơn nhẹ; F-score bằng nhau. |

Tác giả viết FHMM vượt CO theo cả ba metric ở REDD, Smart* và AMPds, nhưng Bảng 3 ghi REDD F-score bằng 0,31 cho cả hai. Ghi rõ sai khác và ưu tiên số trong bảng. Đối chiếu đúng cột NEP cho thấy FHMM thấp hơn CO ở REDD, Smart* và AMPds; NEP bằng nhau ở iAWE; CO thấp hơn ở Pecan Street và UK-DALE. Đây chỉ là kết quả minh họa theo giao thức đã nêu. (Mục 4.4, Bảng 3, PDF tr. 9.)

Tác giả viết CO “tương tự” FHMM ở iAWE, Pecan Street và UK-DALE theo mọi metric, dù Bảng 3 ghi FTE Pecan Street 0,99 (CO) so với 0,87 (FHMM). Họ cho rằng điều này có thể do rất ít thiết bị vượt ngưỡng 5% ở các hộ được chọn; sưởi/làm mát chiếm phần lớn (khoảng 60% cho một điều hòa 2,7 kW ở Pecan Street; khoảng 35% cho hai điều hòa 1,8 kW và 1,6 kW ở iAWE) và tải HVAC công suất lớn dễ phân rã hơn điện tử/chiếu sáng; máy giặt ở UK-DALE (một thiết bị vượt 5%) làm metric giảm ở cả hai thuật toán. Đây là giải thích của tác giả cho cấu hình cụ thể, không phải kiểm định. (Mục 4.4, PDF tr. 9.)

Thời gian huấn luyện (giây) CO; FHMM trong Bảng 3: REDD 3,67; 22,81 — Smart* 3,40; 46,34 — Pecan Street 1,72; 2,83 — AMPds 5,92; 298,49 — iAWE 1,68; 8,90 — UK-DALE 1,06; 11,42. Thời gian phân rã (giây): REDD 0,14; 1,21 — Smart* 0,39; 1,85 — Pecan Street 0,02; 0,12 — AMPds 3,08; 22,58 — iAWE 0,07; 0,38 — UK-DALE 0,10; 0,52. Tác giả cho rằng thời gian xác nhận CO nhanh hơn FHMM theo cấp hàm mũ, gợi ý CO có thể đáng dùng ở các hộ như Pecan Street/iAWE, và nêu thời gian AMPds lớn vì dữ liệu dài một năm (so với một tuần ở Pecan Street). (Mục 4.4, Bảng 3, PDF tr. 9–10.)

### Chẩn đoán theo thiết bị

Phân tích iAWE dùng sáu thiết bị tiêu thụ lớn, vẫn mô hình hai trạng thái; iAWE được chọn vì có metadata như nhiệt độ đặt điều hòa. Bảng 4 (CO; FHMM): điều hòa 1 NEP 0,3; 0,3, F-score 0,9; 0,9; điều hòa 2 NEP 1,0; 1,0, F-score 0,7; 0,7; entertainment unit NEP 4,2; 4,1, F-score 0,3; 0,3; tủ lạnh NEP 0,5; 0,5, F-score 0,8; 0,8; laptop NEP 1,7; 1,8, F-score 0,3; 0,2; máy giặt NEP 130,1; 125,1, F-score 0,0; 0,0. Đây là số của một hộ iAWE theo giao thức bài. (Mục 4.5, Bảng 4, PDF tr. 10.)

Tác giả quan sát máy giặt và thiết bị dùng nguồn xung (laptop, entertainment unit) kém hơn nhiều so với điều hòa ở cả hai metric, và dẫn tài liệu trước [32] rằng thiết bị phức tạp như máy giặt khó mô hình hóa; bài không gắn riêng kết quả thiết bị điện tử với số trạng thái. Điều hòa 2 được vận hành ở 26°C khi ngoài trời khoảng 30–35°C nên có nhiều thời gian ở trạng thái trung gian (quạt chạy, máy nén tắt). Mô hình hai trạng thái dự đoán khoảng 1,1 kW so với công suất định mức khoảng 1,6 kW; tác giả suy đoán mô hình ba trạng thái có thể khắc phục nhưng tăng chi phí tính toán/bộ nhớ. Đây là giải thích và giả thuyết của tác giả, không phải kiểm định nhân quả. (Mục 4.5, Bảng 4, Hình 8, PDF tr. 10.)

## 6. Giới hạn và hướng tiếp theo

- So sánh liên bộ dữ liệu dùng hộ đầu tiên và chỉ mô hình hóa thiết bị đóng góp >5% (tác giả nêu lý do là độ phức tạp hàm mũ của CO/FHMM). Suy luận của người đọc: một hộ mỗi bộ không phải mẫu đại diện, và ngưỡng 5% bỏ nhiều thiết bị nhỏ. (Mục 4.4, PDF tr. 9.)
- CO/FHMM đặt hai trạng thái dù có thể dùng nhiều hơn; tác giả nói thí nghiệm nhằm so sánh công bằng hai thuật toán đối chứng, không phải phiên bản tối ưu hóa đầy đủ của từng phương pháp. (Mục 4.4, PDF tr. 9; mục 4.5, PDF tr. 10.)
- Bài không đánh giá loss học sâu, nhiều seed, chia chéo hộ, nhiễu tổng hợp hay vi phạm ràng buộc vật lý. Đây nằm ngoài mục tiêu, không phải bằng chứng các vấn đề ấy không quan trọng (nhận xét của người đọc).
- Tác giả nêu seed cố định, chi tiết trên GitHub dự án, và bản phát hành NILMTK v0.1.0 được dùng cho bài; ghi chú này chưa xác minh tag v0.1.0, môi trường và chưa chạy lại kết quả. (Mục 4.4, PDF tr. 9; chú thích 3, PDF tr. 2.)
- Sáu tập so sánh không gồm REFIT; giao thức và metric có thể không tương thích với benchmark hiện tại.

Hướng tiếp theo tác giả nêu: bổ sung thuật toán/bộ dữ liệu (có thể gồm HES), so sánh học không giám sát không cần công suất đo phụ, duy trì wiki metadata thiết bị và đưa mô phỏng hộ vào để mở rộng kịch bản. Đây là đề xuất tương lai, không phải kết quả đã hoàn thành. (Kết luận, PDF tr. 10.)

## 7. Bảng bằng chứng có vị trí nguồn

| Nhận định / dữ kiện | Loại bằng chứng và điều kiện | Vị trí PDF |
| --- | --- | --- |
| Ba lợi ích ứng dụng | Động lực tác giả, dẫn nguồn trước; không phải kết quả thực nghiệm | Giới thiệu, tr. 1 |
| Ba trở ngại so sánh | Lập luận trong bối cảnh 2014 | Giới thiệu, tr. 1–2; mục 2.1–2.3, tr. 2–3 |
| Định nghĩa NILM theo công suất tổng và trạng thái | Định nghĩa/ký hiệu | Mục 2.5, tr. 4 |
| Chín tập được tổng hợp, sáu tập nhập, ba tập loại | Mô tả phạm vi và lý do lựa chọn | Bảng 1, tr. 3; mục 3.1, tr. 4 |
| Khác biệt thiết bị đo, năng lượng đo phụ, dropout, uptime | Chẩn đoán min/median/max qua hộ | Mục 4.1, Bảng 2, tr. 7 |
| Pecan Street có hai hộ đo phụ vượt 100% | Tác giả diễn giải là chồng lấn kênh; không nói về dự đoán | Mục 4.1, Bảng 2, tr. 7 |
| F-score là ON/OFF tại từng lát thời gian | Định nghĩa TP/FP/FN; khác event-F1 | Mục 3.7, công thức 7–15, tr. 6–7 |
| So sánh CO/FHMM | Hộ đầu; chia nửa; thiết bị >5%; hai trạng thái; tiền xử lý theo tập | Mục 4.4, Bảng 3, tr. 9 |
| REDD có F-score CO=FHMM=0,31 | Số trong bảng với giao thức cụ thể | Bảng 3, tr. 9 |
| Khác biệt iAWE theo thiết bị và trạng thái điều hòa | Sáu thiết bị lớn; mô hình hai trạng thái | Mục 4.5, Bảng 4, Hình 8, tr. 10 |
| Hướng nghiên cứu tiếp theo | Đề xuất tác giả | Kết luận, tr. 10 |

## 8. Hàm ý cho benchmark loss và ràng buộc vật lý

**Toàn mục này là suy luận / đề xuất của dự án, không phải lời tác giả.**

### Có thể tái sử dụng

1. **Mô tả dữ liệu và split:** ghi dataset/version, hộ, mask mẫu hợp lệ, tần số, cách chia và tiêu chí thiết bị. Đây là suy luận từ chẩn đoán bài, chưa phải protocol chốt.
2. **Không dùng một metric làm toàn bộ kết luận:** phân biệt sai số công suất, phân bổ năng lượng, trạng thái ON/OFF, event detection và physical consistency; định nghĩa theo câu hỏi dự án.
3. **Kiểm tra ngữ nghĩa đo trước C3:** Pecan Street cho thấy tổng nhãn đo phụ có thể chồng lấn. C3 chỉ có thể áp dụng khi xác minh phép đo không âm, đồng bộ, không chồng lấn đáng kể và giả định về phát điện/nhiễu phù hợp. Đây là suy luận; bài không thử C3.
4. **Báo cáo theo thiết bị/điều kiện:** kết quả máy giặt, laptop và điều hòa khác nhau; trình bày theo thiết bị, dải công suất, trạng thái và vùng chuyển tiếp bên cạnh số tổng hợp.
5. **Phân biệt metric trạng thái với metric sự kiện:** F-score NILMTK tính theo lát thời gian; event-F1 cần quy tắc ghép onset/offset riêng.
6. **Theo dõi biểu diễn trạng thái:** mô hình hai trạng thái có thể không phù hợp thiết bị nhiều trạng thái; khi so sánh loss cần cố định khả năng biểu diễn hoặc ghi rõ tương tác.

### Bài báo không hỗ trợ kết luận sau

- Không chứng minh MSE, MAE, reconstruction loss, regularization hay total variation tốt hơn loss khác.
- Không đo tỷ lệ/độ lớn vi phạm không âm, giới hạn công suất thiết bị hoặc công suất tổng.
- Không xác nhận REFIT phù hợp làm dữ liệu chính; REFIT không nằm trong sáu tập đánh giá.
- Không đánh giá nhiễu có kiểm soát hay cross-household shift.
- Không cho phép so sánh trực tiếp Bảng 3 với benchmark dự án nếu chưa đồng bộ metric, thiết bị, split, tiền xử lý và protocol.

## 9. Đầu vào cho nhóm code và câu hỏi còn mở

Có thể chuyển tiếp như nguyên tắc tài liệu: checklist sampling/gap/dropout/uptime/tỷ lệ đo phụ/cấu trúc mạch; phân biệt nhóm metric; kiểm tra ngữ nghĩa trước C3; giữ bảng kết quả theo thiết bị. Chưa chốt loss hay protocol từ riêng nguồn này.

Còn cần xác minh: REFIT có metadata để lập mask hợp lệ cho C3 không; các nhãn có thể chồng lấn hoặc bỏ sót tải nào; định nghĩa mask, ngưỡng ON/OFF, đồng bộ và cách gộp metric nào phù hợp; tổng quan đã bao phủ dữ liệu, loss, mô hình, ràng buộc và robustness theo kế hoạch tổng quan (kế hoạch: `../synthesis/literature-review-plan`) chưa?

## 10. Trích dẫn

Batra, Nipun, Jack Kelly, Oliver Parson, Haimonti Dutta, William Knottenbelt, Alex Rogers, Amarjeet Singh, và Mani Srivastava. “NILMTK: An Open Source Toolkit for Non-intrusive Load Monitoring.” *Proceedings of the 5th International Conference on Future Energy Systems (ACM e-Energy)*, 2014, tr. 265–276. DOI: [10.1145/2602044.2602051](https://doi.org/10.1145/2602044.2602051). Khóa BibTeX: `NILMTK`. Bản đã đọc: arXiv:1404.3878v1 (locator theo bản này); trang ACM lấy từ `ref.bib`, chưa kiểm trên bản ACM.
