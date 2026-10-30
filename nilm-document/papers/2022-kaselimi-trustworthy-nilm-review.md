---
type: paper
status: reviewed
title: "Towards Trustworthy Energy Disaggregation: A Review of Challenges, Methods, and Perspectives for Non-Intrusive Load Monitoring"
authors: [Maria Kaselimi, Eftychios Protopapadakis, Athanasios Voulodimos, Nikolaos Doulamis, Anastasios Doulamis]
year: 2022
venue: "Sensors 22(15):5872"
doi: "10.3390/s22155872"
source_url: "https://arxiv.org/abs/2207.02009"
citation_key: "kaselimi2022trustworthy"
read_date: 2026-10-30
tags: [nilm, literature, review, trustworthy, generalization, imbalance, evaluation]
---

# Review “NILM đáng tin cậy” — Kaselimi và cộng sự (2022)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Kaselimi, M., Protopapadakis, E., Voulodimos, A., Doulamis, N., Doulamis, A. "Towards Trustworthy Energy Disaggregation: A Review of Challenges, Methods, and Perspectives for Non-Intrusive Load Monitoring." Sensors 22(15):5872, 2022. DOI `10.3390/s22155872` (đối chiếu Crossref 2026-10-30: 5 tác giả theo thứ tự trên, Sensors 22(15), bài 5872, xuất bản 5/8/2022; OpenAlex: gold OA). Metadata khớp mục `kaselimi2022trustworthy` trong `ref.bib`.
- Toàn văn / phiên bản đã đọc: **arXiv:2207.02009v1** (5/7/2022), 22 trang, định dạng IEEE (“VOLUME 4, 2022”). Bản Sensors chính thức **chưa đối chiếu** (trang MDPI chặn tải tự động); bố cục, số trang và có thể nội dung khác. **Mọi locator dưới đây theo trang PDF arXiv v1**, không dùng cho bản Sensors.
- Tệp nguồn cục bộ: `papers/Towards trustworthy Energy Disaggregation - review (arXiv 2207.02009v1).pdf`.
- Mục tiêu đọc: lượt top-down — phân nhóm phương pháp, thách thức khái quát/độ vững, mất cân bằng, thước đo; RQ1, RQ3, RQ4.
- Phạm vi đọc: toàn văn mục I–VIII (tr. 1–16); Bảng 1 (tr. 11), Bảng 2 (tr. 13), Bảng 3 (tr. 14) đã đọc; danh mục tham khảo tra theo số khi cần.
- Rà soát (2026-10-30): đối chiếu từng nhận định, con số và locator với PDF arXiv v1; tìm toàn văn phần thân bài các từ khóa loss, objective, constraint, negative, physical, conservation, search, criteria. Sửa: locator mục VII.B (tr. 14 → tr. 13–14); Bảng 3 gồm cả AMPds; năm của Pereira & Nunes (2018 → 2017, theo danh mục [132]); xác định [52] = Klemenjak và cộng sự 2020 và [79] = He và cộng sự 2019; mở rộng mục VII từ “đọc lướt” sang toàn văn.

## 2. Tóm tắt điều hành

- NILM được phát biểu là **bài toán ngược đặt không chỉnh** (inverse ill-posed): ước lượng thành phần từ tổng `p(t) = Σ_m p_m(t) + ε(t)` (mục II.A, phương trình 1, tr. 3). Mô hình này gộp mọi phần còn lại vào một “additive noise” `ε(t)`, không tách tải không đo khỏi nhiễu.
- Cấu trúc trình bày của review gồm ba lớp: (i) **giai đoạn lịch sử**: thời kỳ đầu 1995–2014 (CO, phân loại SVM/DT, DTW, GSP, HMM và biến thể, phân rã ma trận), học sâu 2015–2019 (DAE, RNN/LSTM/GRU, CNN, seq2point/seq2seq), tiến bộ hiện tại 2020– (GAN, transformer, đa nhiệm UNet-NILM, XAI) (mục III, tr. 4–5); (ii) **bảy “thế lưỡng nan” thiết kế**: phân loại/hồi quy, đa đích/đơn đích, có/không giám sát, tích chập/hồi quy (recurrent), nhân quả/phi nhân quả, seq2point/seq2seq, một/nhiều chiều (mục V.A, tr. 7–10; Hình 2–7, tr. 6–9; Bảng 1, Hình 8, tr. 11); (iii) **sáu khía cạnh tin cậy**: độ tin cậy, khả năng mở rộng, độ vững, khả năng giải thích, công bằng, an toàn/riêng tư (mục VI, tr. 10–12).
- Năm thách thức: khái quát/độ vững với hộ chưa thấy và dữ liệu nhiễu; mô hình lai có phản hồi người dùng và học liên tục; giải thích; công bằng; riêng tư (mục II.B, tr. 3–4).
- Liên quan C3: mô hình **đơn đích** “có thể ước lượng thiếu hoặc quá đáng kể” tổng công suất vì không tối thiểu hóa chênh lệch giữa tổng đo và tổng các ước lượng thiết bị, do mỗi mô hình được huấn luyện độc lập với thiết bị khác, dẫn [79] (mục V.A.2, tr. 8; cũng ở ô “Cons” của Hình 3, tr. 7). Đây là nhận định định tính, không có số đo trong review.
- Mất cân bằng: hai loại — chênh lệch thời gian bật/tắt, và chênh lệch số lượng đo giữa các loại thiết bị (mục IV.A.1, tr. 5–6).
- Thước đo: “chưa có hiểu biết chung hay định dạng được chấp nhận” về cách báo độ chính xác NILM (dẫn [52]); chia thành thước đo phân loại (sự kiện bật/tắt) và thước đo ước lượng công suất; khuyến nghị báo cả cấp hộ và cấp thiết bị (mục VII.B, tr. 13–14); khuyến nghị báo cả thước đo phân loại lẫn hồi quy và chuẩn hóa kết quả (mục VIII.C, tr. 15–16).
- Review **không** có mục về hàm loss hay ràng buộc vật lý ở đầu ra; không mô tả chiến lược tìm kiếm/tiêu chí chọn bài (tìm toàn văn mục I–VIII: “loss” chỉ xuất hiện một lần, nói về gradient biến mất của RNN, tr. 8; “constraint” chỉ nói ràng buộc do bộ dữ liệu, tr. 12).

## 3. Bài toán, động lực và đóng góp

Tác giả cho rằng sự quan tâm đã chuyển từ công thức hóa toán học bài toán NILM sang NILM thực tế; hiện là giai đoạn “mature NILM” khi độ phức tạp, khả năng chuyển giao, độ tin cậy, tính thực tiễn và nói chung tính đáng tin trở thành trọng tâm (Tóm tắt, tr. 1; Hình 1, tr. 2). Đóng góp: tổng quan ngắn phương pháp NILM cho thiết bị dân dụng, các thế lưỡng nan nghiên cứu, thách thức và triển vọng theo khung “đáng tin cậy” (Tóm tắt, tr. 1; mục I, tr. 2–3).

## 4. Phương pháp và loss (nội dung được review tổng hợp)

- **Phân loại vs hồi quy:** hồi quy “tự nhiên” từ dữ liệu có đo phụ; phân loại cần ngưỡng/phát hiện sự kiện, và kết quả phụ thuộc bước tiền xử lý này; ưu nhược điểm ở Hình 2 (mục V.A.1, tr. 6–7).
- **Đơn đích vs đa đích:** đơn đích là xu hướng chính của DNN; hồi quy đa đích “chưa được nghiên cứu kỹ”; UNet-NILM [49] là ví dụ đa đích phân loại + hồi quy với quantile regression đa đích; [80] Buddhahai & Makonin đề xuất hồi quy đa đích bằng random forest (mục III.C, tr. 5; mục V.A.2, tr. 7–8). Tác giả ghi nhận quan tâm gia tăng tới mô hình đa đích (mục V.B, tr. 10).
- **Có giám sát vs không giám sát:** có giám sát tốt trên hộ đã huấn luyện nhưng “không phải lúc nào cũng chuyển được” sang hộ chưa thấy, dẫn [81]; với hộ chưa thấy, “không giám sát có thể là lựa chọn tốt hơn” (mục V.A.3, tr. 8; Hình 4, tr. 8). Đây là nhận định của tác giả, không kèm thực nghiệm.
- **Loss:** review không có mục riêng; chỉ nhắc các nghiên cứu GAN “phần lớn khai thác tính vững trước nhiễu” mà huấn luyện đối kháng đạt được (mục III.C, tr. 5).
- **Tiền xử lý:** cân bằng dữ liệu, lấy mẫu lại, xử lý khoảng thiếu; tác giả viết “đã được chứng minh thực nghiệm” rằng lấy mẫu lại/làm sạch/cân bằng cải thiện đáng kể độ chính xác và khái quát, dẫn [52] = Klemenjak và cộng sự 2020 (khóa `klemenjak2020comparabilitynonintrusiveloadmonitoring`) (mục IV, tr. 5). Chưa đối chiếu nhận định này với [52].

## 5. Bộ dữ liệu và thiết lập (mức review)

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Bộ dữ liệu | Bảng 2 liệt kê 18 bộ; REFIT, DEDDIAG, IDEAL có thời lượng dài nhất; REFIT ghi 2 năm, công suất tác dụng, 8 s | Mục VII.A, tr. 12; Bảng 2, tr. 13 |
| Thước đo | Phân loại: accuracy, precision, recall, F1; hồi quy: MAE, RMSE | Mục VII.B.1–2, tr. 14 |
| So sánh MAE | Bảng 3: MAE (W) cho 5 thiết bị phổ biến trên REDD/UK-DALE/REFIT/AMPds, lấy từ các bài khác nhau; có cột đánh dấu kiểm tra hộ chưa thấy | Bảng 3, tr. 14 |

## 6. Mô hình đối chứng, thước đo và kết quả

Review không có thí nghiệm. Bảng 3 (tr. 14) tổng hợp MAE tự báo cáo; tác giả kết luận “không thể khẳng định có một cách tiếp cận tổng thể ‘tốt nhất’ cho mọi loại thiết bị” (mục VIII.B, tr. 15). Không dùng Bảng 3 để xếp hạng vì giao thức khác nhau.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn (arXiv v1) | Mức chắc chắn |
| --- | --- | --- | --- |
| Mô hình đơn đích có thể ước lượng quá/thiếu tổng công suất vì không tối thiểu hóa chênh lệch tổng | Lập luận tác giả, dẫn [79] He và cộng sự 2019 (IEEE TSG 10(6)) | Mục V.A.2, tr. 8; Hình 3, tr. 7 | Thấp–trung bình: định tính; [79] đã bị loại khỏi danh sách đọc theo quyết định người dùng |
| Có giám sát giảm hiệu năng ở hộ chưa thấy | Lời tác giả, dẫn [81] Khazaei và cộng sự | Mục V.A.3, tr. 8 | Trung bình (thứ cấp) |
| Hai loại mất cân bằng trong NILM | Phân loại khái niệm | Mục IV.A.1, tr. 5–6 | Cao (định nghĩa) |
| Dữ liệu từ nhiều hộ giúp khái quát; đa dạng mẫu thiết bị cùng loại không được dữ liệu mở bao phủ | Lời tác giả | Mục VI.C, tr. 11–12 | Trung bình (thứ cấp) |
| Chưa có hiểu biết chung về cách báo độ chính xác NILM | Lời tác giả, dẫn [52] Klemenjak 2020 | Mục VII.B, tr. 13 | Trung bình–cao (lời tác giả; [52] là nguồn đã `reviewed` trong vault) |
| Không bàn loss hay ràng buộc vật lý; không nêu chiến lược tìm | Tìm toàn văn mục I–VIII | Toàn bài, tr. 1–16 | Cao (vắng mặt trong review này) |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

NILM cần chuyển sang khung đáng tin cậy (tin cậy, mở rộng, vững, giải thích, công bằng, riêng tư); chưa có phương pháp tốt nhất cho mọi thiết bị; cần chọn thước đo cẩn thận và báo cả thước đo phân loại lẫn hồi quy (Tóm tắt, tr. 1; mục VI, tr. 10–12; mục VIII, tr. 15–16).

### Thí nghiệm thực sự chứng minh gì?

Không có thí nghiệm. Bảng 1 và Hình 8 chỉ thống kê lựa chọn thiết kế của **12 bài có giám sát** được chọn (Bảng 1, tr. 11) — mẫu nhỏ, không phải khảo sát hệ thống.

### Bài báo chưa giải quyết gì?

- Không mô tả chiến lược tìm kiếm/tiêu chí chọn → không biết độ bao phủ.
- Không bàn loss hay ràng buộc vật lý ở đầu ra; “robustness” chủ yếu là dữ liệu nhiễu, thiết bị lạ và hộ mới, không có định nghĩa đo.
- Bản đã đọc là arXiv v1; chưa đối chiếu bản Sensors.

## 9. Hạn chế và khả năng tái lập

Không áp dụng (review, không có mã). Nguy cơ: một số nhận định dẫn chủ yếu công trình của chính nhóm tác giả ([18], [37], [44], [103]).

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc:**

- Trục “đơn đích vs đa đích” quyết định cách đo C3: C3 chỉ kiểm được khi có dự đoán cho nhiều thiết bị cùng lúc (hoặc tổng các mô hình đơn đích). Benchmark phải nêu rõ C3 đo trên tổng các mô hình đơn đích hay một mô hình đa đích.
- Nhận định “đơn đích có thể ước lượng quá tổng” (tr. 8) là giả thuyết có thể kiểm bằng tỷ lệ mẫu `Σ ŷ > x` — chưa có số liệu.
- “Độ vững” trong review rộng (nhiễu, thiết bị lạ, hộ mới) → dự án cần định nghĩa hẹp và đo được.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Đối chiếu bản Sensors 22(15):5872 (bố cục, số trang, nội dung mục V.A.2 và VII.B).
- [81] (giảm hiệu năng hộ chưa thấy), [53] De Baets và cộng sự 2017 (kỹ thuật cân bằng), [80] Buddhahai & Makonin 2021 (hồi quy đa đích) là ứng viên lá; [79] đã bị loại theo quyết định người dùng.

## 12. Trích dẫn

```bibtex
@article{kaselimi2022trustworthy,
    title   = {Towards Trustworthy Energy Disaggregation: A Review of Challenges, Methods, and Perspectives for Non-Intrusive Load Monitoring},
    author  = {Kaselimi, Maria and Protopapadakis, Eftychios and Voulodimos, Athanasios and Doulamis, Nikolaos and Doulamis, Anastasios},
    journal = {Sensors},
    volume  = {22},
    number  = {15},
    pages   = {5872},
    year    = {2022},
    doi     = {10.3390/s22155872},
    note    = {Bản đã đọc: arXiv:2207.02009v1}
}
```
