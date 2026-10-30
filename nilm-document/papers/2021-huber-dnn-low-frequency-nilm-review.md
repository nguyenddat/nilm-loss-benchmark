---
type: paper
status: reviewed
title: "Review on Deep Neural Networks Applied to Low-Frequency NILM"
authors: [Patrick Huber, Alberto Calatroni, Andreas Rumsch, Andrew Paice]
year: 2021
venue: "Energies 14(9):2390"
doi: "10.3390/en14092390"
source_url: "https://doi.org/10.3390/en14092390"
citation_key: "huber2021review"
read_date: 2026-10-30
tags: [nilm, literature, review, deep-learning, low-frequency, loss, evaluation]
---

# Review DNN cho NILM tần số thấp — Huber và cộng sự (2021)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Huber, P., Calatroni, A., Rumsch, A., Paice, A. "Review on Deep Neural Networks Applied to Low-Frequency NILM." Energies 14(9):2390, 2021. DOI `10.3390/en14092390` (đối chiếu Crossref 2026-10-30; OpenAlex: gold OA, CC BY). Có bản preprint `10.20944/preprints202104.0421.v1` — không dùng. Metadata khớp mục `huber2021review` trong `ref.bib`.
- Toàn văn / phiên bản: bản xuất bản Energies, 34 trang; trang 1 ghi Received 9/2/2021, Accepted 16/4/2021, Published 23/4/2021, CC BY 4.0. Tải từ kho của HSLU (trang MDPI chặn truy cập tự động trong môi trường agent).
- Tệp nguồn cục bộ: `papers/Review on Deep Neural Networks Applied to Low-Frequency NILM (Energies 2021).pdf`. Locator theo số trang tạp chí (“x of 34”), trùng số trang PDF.
- Mục tiêu đọc: lượt top-down — nắm phân nhóm thiết kế DNN-NILM, loss được dùng, kịch bản đánh giá, khoảng trống; RQ1–RQ4.
- Phạm vi đọc: toàn văn mục 1–6 (tr. 1–3, 9–25). Bảng 2 (tr. 4–8, 99 bài theo Bảng 1) chỉ đọc chú thích và cấu trúc cột, **chưa trích từng dòng**. Hình 1 (tr. 10) đã xem trên ảnh render; giá trị trong Hình 3–4 (tr. 18–19) không trích.
- Chất lượng trích xuất: PyMuPDF; công thức (1)–(5) ngắn, đã đối chiếu văn bản.
- Rà soát (2026-10-30): đối chiếu lại mọi nhận định, con số và locator của ghi chú với PDF; tìm toàn văn các từ khóa constraint, non-negative, negative, physical, conservation, aggregate, loss. Sửa: thêm ngày Accepted; diễn đạt lại chú thích Hình 1; sửa suy luận về kịch bản synthetic và C3 (mục 10); ghi rõ phạm vi câu “chưa có so sánh loss có hệ thống”; bổ sung locator mục 4.1 (tr. 18–20) và 4.5.1 (tr. 23–24).

## 2. Tóm tắt điều hành

- Phạm vi: DNN huấn luyện bằng lan truyền ngược trên dữ liệu **tần số thấp** (lấy mẫu thấp hơn tần số cơ bản AC), tài liệu đến cuối 11/2020; loại mạng nông một lớp ẩn (Tóm tắt, tr. 1; mục 1.2, tr. 3). Chiến lược tìm: rà kỷ yếu International NILM Workshop 2016–2020 và BuildSys 2015–2020, tìm từ khóa trên Google Scholar/IEEE Xplore, truy vết tài liệu tham khảo; lượt tìm cuối vào cuối 11/2020 (mục 1.3, tr. 9).
- Tác giả **không** đề xuất taxonomy: Hình 1 minh họa “các bậc tự do chính” của nghiên cứu DNN-NILM (Datasets, Data Processing & Input, DNNs & Output, Metrics, Appliances); chú thích viết màu chỉ là “nhóm lỏng” và “không nên hiểu là taxonomy” (Hình 1, tr. 10).
- Loss: đa số dùng MAE hoặc MSE cho hồi quy công suất và cross-entropy cho bật/tắt; một số dùng quantile regression ([46], [59]), loss GAN ([34, 35, 39, 43]) và loss bốn thành phần của BERT4NILM ([55]). Câu kết đoạn: “To our knowledge, a systematic comparison of loss functions for DNN-NILM approaches has not been published.” (mục 3.4.2, tr. 16).
- Kịch bản đánh giá: phân biệt *observed vs synthetic* (tương đương noised/denoised) và *seen vs unseen vs cross-domain transfer*; cross-domain chỉ thấy ở 5 bài [39, 42, 63, 71, 91] (mục 3.2.1, tr. 11–12).
- Các yếu tố lặp lại ở nhóm kết quả tốt nhất (so sánh kết quả tự báo cáo, khác giao thức): khoảng lấy mẫu ≤ 10 s, trường nhìn lớn, loss GAN, học đa nhiệm, hậu xử lý (Tóm tắt, tr. 1; mục 4.1, tr. 18–20).
- Khoảng trống được nêu: thiếu nghiên cứu tham số có hệ thống (tần số lấy mẫu × cửa sổ, chuẩn hóa, cân bằng kích hoạt, tăng cường dữ liệu, hậu xử lý, **loss**), thiếu giao thức đánh giá chuẩn, khan hiếm dữ liệu gán nhãn (mục 4.1, tr. 20; mục 4.4, tr. 22; mục 4.5.1, tr. 23–24).
- Review **không** bàn ràng buộc vật lý trên đầu ra (không âm, cận công suất thiết bị, tổng ≤ công suất tổng): tìm toàn văn không có “constraint”, “non-negative”, “physical”, “conservation”; điểm gần nhất là cắt (clip) giá trị **đo** vượt định mức công tơ khi tiền xử lý (mục 3.2.2, tr. 13).

## 3. Bài toán, động lực và đóng góp

Mô hình đo (phương trình 1, tr. 9): `x^a_t = Σ_m y^m_t + Σ_k w^k_t + ε_t`, với `e_t = Σ_k w^k_t + ε_t`. Tác giả tách riêng tải không đo phụ `Σ_k w^k_t` khỏi nhiễu thiết bị đo `ε_t` vì “bản chất khác nhau”: nhiễu đo có thể giả định “well behaved”, xấp xỉ “a standard distribution” và nhỏ so với tín hiệu; còn tải không đo phụ “thường chiếm phần lớn” `x^a_t` và có phân phối **không Gauss** (mục 2.1, tr. 9). Đây là lập luận của tác giả, không kèm số liệu.

Suy luận của người đọc: lập luận này cho thấy giả định nhiễu Gauss (cơ sở xác suất của MSE) không mô tả phần dư `x − Σ y` của kịch bản observed; review không kiểm nghiệm điều này.

Đóng góp tác giả nêu: tổng quan có cấu trúc + Bảng 2; thảo luận so sánh hiệu năng, đặc trưng đầu vào, đa nhiệm, nghiên cứu tham số, khoảng trống triển khai (mục 1.1, tr. 3).

## 4. Phương pháp và loss (nội dung được review tổng hợp)

- **Hồi quy vs phân loại:** mục tiêu chính là công suất (hồi quy) hoặc trạng thái bật/tắt (phân loại nhị phân) (mục 2.1, tr. 9–10); 4 bài [33, 61, 68, 118] chuyển hồi quy thành phân loại theo cụm công suất (mục 3.5, tr. 16–17).
- **Loss:** MAE/MSE (hồi quy), cross-entropy (bật/tắt); quantile regression ở [46] UNet-NILM và [59] PB-NILM — “[59] thấy loss đề xuất tăng hiệu năng hai mô hình state-of-the-art so với MSE”; loss GAN ở [34, 35, 39, 43] (bộ phân biệt đầu ra thật/giả, kỳ vọng làm đầu ra thực tế hơn, nhất là khi dữ liệu ít); loss bốn thành phần MSE + KL + soft-margin + MAE ở [55] BERT4NILM (mục 3.4.2, tr. 16). Đây là **mô tả thứ cấp**; PB-NILM không được đọc toàn văn (người dùng quyết định bỏ qua 2026-10-30).
- **Đầu ra / đa nhiệm:** s2s, s2sub, s2p; đa số huấn luyện một mô hình cho mỗi thiết bị; đa nhiệm công suất + bật/tắt ở [35, 63, 97, 106]; [59] học ba đích: công suất tổng `P_total`, công suất thiết bị `P_app` và hiệu `P_rest`; [46] học cả bật/tắt và công suất của nhiều thiết bị (mục 3.5, tr. 16–17).
- **Hậu xử lý:** trung bình hoặc trung vị các dự đoán chồng lấp; [21] thấy mạng ước lượng thấp khi kích hoạt chỉ nằm một phần trong cửa sổ nên đề xuất trung vị; lọc kích hoạt quá ngắn ([37], [36] — [36] báo cải thiện 28–54% tùy thước đo); mạng thứ hai để loại kích hoạt giả ([58, 89]) (mục 3.5.1, tr. 17).
- **Mất cân bằng:** nhiều bài cân bằng mẫu có/không có kích hoạt; đa số không xử lý; chỉ [34] khảo sát tỷ lệ cân bằng (mục 3.2.3, tr. 13–14).
- **Tiền xử lý:** lấy mẫu lại, lấp tiến khoảng thiếu ngắn (thường ≤ 3 phút, [14]), cắt giá trị đo vượt định mức công tơ; chuẩn hóa z-score hoặc min–max theo tập huấn luyện/hộ/cửa sổ; chỉ hai bài báo cáo ảnh hưởng của cách chuẩn hóa (mục 3.2.2, tr. 12–13).
- **Tăng cường dữ liệu / synthetic:** một số bài huấn luyện và kiểm tra hoàn toàn trên dữ liệu synthetic (ký hiệu “dn” ở Bảng 2); một số cộng thêm kích hoạt đo phụ vào aggregate đo; tác giả không biết nghiên cứu nào so sánh các chiến lược tăng cường (mục 3.2.4, tr. 14).

## 5. Bộ dữ liệu và thiết lập (mức review)

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Tập dữ liệu hay dùng | UK-DALE (~40 bài), REDD (~30), AMPds, REFIT, Dataport (~10 mỗi bộ), ECO (3) | Mục 3.1, tr. 11 |
| REFIT trong Bảng 3 | GBR, 20 hộ, 177 thiết bị, 8 s cho aggregate và thiết bị | Bảng 3, tr. 11 |
| Thiết bị hay dùng | rửa bát, tủ lạnh, vi sóng, máy giặt, ấm đun… | Mục 3.1, tr. 11 |
| Tần số lấy mẫu | 1/3600 Hz đến 10 Hz; phần lớn 1/60 Hz hoặc 1–1/10 Hz | Mục 3.2.2, tr. 12 |
| Kịch bản đánh giá | observed/synthetic; seen/unseen/cross-domain | Mục 3.2.1, tr. 11–12; Hình 2, tr. 12 |
| Số bài theo năm | 2015: 2; 2016: 6; 2017: 4; 2018: 21; 2019: 36; 2020: 30 (đến cuối 11/2020) | Bảng 1, tr. 2 |

## 6. Mô hình đối chứng, thước đo và kết quả

| Thiết lập | Nội dung | Thước đo | Kết quả | Vị trí nguồn |
| --- | --- | --- | --- | --- |
| So sánh kết quả **tự báo cáo**, chỉ kịch bản observed + unseen, chỉ mô hình đề xuất (không baseline) | MAE nhỏ nhất và F1 lớn nhất theo bộ dữ liệu × thiết bị; lấy 1/4 kết quả tốt nhất mỗi thiết bị để tìm yếu tố chung | MAE (W), F1 | Ấm đun và vi sóng tốt hơn và ít phân tán hơn thiết bị đa trạng thái; tác giả cảnh báo kết quả đến từ quy trình “wildly different” | Mục 4.1, Hình 3–4, tr. 18–20 |
| Học đa nhiệm | Tổng hợp bằng chứng từ [91], [107], [35, 37, 63, 97] vs [49] | — | Tác giả kết luận đa nhiệm có lợi; chỉ [49] báo giảm hiệu năng | Mục 4.3, tr. 22 |

Ghi chú: review không chạy thí nghiệm; mọi so sánh là so sánh kết quả công bố, khác dữ liệu/chia/tiền xử lý.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| Theo hiểu biết của tác giả, chưa có so sánh có hệ thống các loss cho DNN-NILM | Lời tác giả; phạm vi: DNN-NILM tần số thấp, tài liệu đến cuối 11/2020 (mục 1.3, tr. 9); mục 4.4 xếp loss vào danh sách lựa chọn cần so sánh có hệ thống | Mục 3.4.2, tr. 16; mục 4.4, tr. 22 | Cao cho phạm vi review; không bao phủ 2021–2026 |
| MAE/MSE + cross-entropy là lựa chọn phổ biến nhất | Tổng hợp review (“vast majority”), không đếm | Mục 3.4.2, tr. 16 | Trung bình–cao (định tính) |
| Tải không đo phụ thường lớn và không Gauss | Lời tác giả | Mục 2.1, tr. 9 | Trung bình (lập luận, không số liệu) |
| Synthetic: `Σ w^k_t = 0`, chỉ còn nhiễu đo; observed: phần dư gồm tải không đo phụ | Định nghĩa của tác giả; synthetic = denoised | Mục 3.2.1, tr. 11–12 | Cao (định nghĩa) |
| Cross-domain transfer hiếm được đánh giá | 5 bài: [39, 42, 63, 71, 91] | Mục 3.2.1, tr. 12 | Cao cho phạm vi review |
| Đề xuất báo MAE và F1 làm thước đo chuẩn tối thiểu; cần giao thức đánh giá chuẩn | Khuyến nghị tác giả, dựa trên mức phổ biến | Mục 4.1, tr. 20 | Khuyến nghị, không phải kết quả |
| Không bàn ràng buộc vật lý trên dự đoán | Tìm toàn văn; chỉ có clip giá trị đo khi tiền xử lý | Mục 3.2.2, tr. 13 | Cao (vắng mặt trong review này) |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

Kết quả tốt nhất thường có lấy mẫu ≤ 10 s, trường nhìn lớn, loss GAN, đa nhiệm, hậu xử lý; đa nhiệm có lợi cho DNN-NILM; cần nghiên cứu tham số, giao thức chuẩn, chia sẻ mã và mô hình (Tóm tắt, tr. 1; mục 4.1–4.4, tr. 18–22).

### Thí nghiệm thực sự chứng minh gì?

Không có thí nghiệm mới. Các “yếu tố của cách tiếp cận tốt nhất” là quan sát trên kết quả tự báo cáo không cùng giao thức; tác giả tự nêu giới hạn này (mục 4.1, tr. 20).

### Bài báo chưa giải quyết gì?

- Ràng buộc vật lý ở đầu ra (C1–C3) không được bàn; không có thước đo vi phạm (tìm toàn văn, xem mục 2).
- Suy luận của người đọc: review không phân biệt loss huấn luyện với thước đo đánh giá về đơn vị/reduction.
- Phạm vi chỉ đến 11/2020; không gồm các họ mô hình mới hơn.

## 9. Hạn chế và khả năng tái lập

- Bảng 2 có bản Excel; dữ liệu và mã cho Hình 3–4 ở `github.com/ihomelab/dnn4nilm_overview` (chú thích Bảng 2, tr. 4; Supplementary Materials, tr. 25) — chưa kiểm tra.
- Thiên lệch chọn bài: dựa vào hai hội nghị chính + Google Scholar/IEEE Xplore + truy vết; tác giả thừa nhận có thể sót vài bài gần đây (mục 1.3, tr. 9).

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc:**

- Có thể dùng trực tiếp: câu “chưa có so sánh có hệ thống các loss” là bằng chứng khoảng trống cho RQ2, **chỉ trong phạm vi DNN-NILM tần số thấp đến 11/2020** và theo hiểu biết của tác giả; cần lượt tìm cập nhật 2021–2026 trước khi dùng trong paper.
- Danh sách lớp loss cần xem xét: MSE, MAE, quantile/pinball, loss tổ hợp (BERT4NILM), loss đa nhiệm công suất + trạng thái, loss đối kháng (GAN). Loss GAN thay đổi cả quy trình huấn luyện → có thể không so sánh công bằng với loss điểm — cần quyết định phạm vi.
- Phân biệt observed/synthetic là trục bắt buộc khi đo C3. Trên synthetic, nhãn thỏa `Σ y ≈ x` (chỉ còn nhiễu đo) nên không có “khoảng trống” do tải không đo: C3 trên dự đoán gần như chặt, và mọi ước lượng quá ở một thiết bị phải được bù bằng ước lượng thiếu ở thiết bị khác. Trên observed, phần dư lớn làm C3 lỏng hơn. Kết quả C3 vì vậy không chuyển trực tiếp giữa hai kịch bản.
- Hậu xử lý (lọc kích hoạt, trung vị) là biến gây nhiễu khi so sánh loss — phải cố định.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Trích Bảng 2: lọc các bài có loss khác MSE/MAE, các bài dùng REFIT, các bài cross-domain.
- [46] UNet-NILM (quantile đa nhiệm) và [55] BERT4NILM là ứng viên lá cho nhánh loss; [59] PB-NILM chỉ qua nguồn thứ cấp.
- Đọc [145] Klemenjak và cộng sự (thước đo khả năng chuyển giao, arXiv:1912.06200); [75] Shin và cộng sự 2019 (Energies 12:1696, số hộ huấn luyện).

## 12. Trích dẫn

```bibtex
@article{huber2021review,
    title   = {Review on Deep Neural Networks Applied to Low-Frequency {NILM}},
    author  = {Huber, Patrick and Calatroni, Alberto and Rumsch, Andreas and Paice, Andrew},
    journal = {Energies},
    volume  = {14},
    number  = {9},
    pages   = {2390},
    year    = {2021},
    doi     = {10.3390/en14092390}
}
```
