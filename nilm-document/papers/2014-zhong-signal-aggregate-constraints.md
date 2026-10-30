---
type: paper
status: reviewed
title: "Signal Aggregate Constraints in Additive Factorial HMMs, with Application to Energy Disaggregation"
authors: [Mingjun Zhong, Nigel Goddard, Charles Sutton]
year: 2014
venue: "Advances in Neural Information Processing Systems 27 (NIPS 2014)"
doi: "không nêu"
source_url: "https://proceedings.neurips.cc/paper_files/paper/2014/file/bf64575b42486eb72efdfa0091be60a5-Paper.pdf"
citation_key: "zhong2014signal"
read_date: 2026-10-30
tags: [nilm, literature, physical-constraint, aggregate-constraint, afhmm]
---

# Signal Aggregate Constraints trong AFHMM — Zhong, Goddard & Sutton (2014)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Zhong, M., Goddard, N., Sutton, C. "Signal Aggregate Constraints in Additive Factorial HMMs, with Application to Energy Disaggregation." NIPS 2014, tr. 3590–3598. Tiêu đề, tác giả khớp `ref.bib` (`zhong2014signal`); trang kỷ yếu 3590–3598 không in trên PDF (chân trang đánh 1–9), lấy từ `ref.bib`; Seq2Point (Zhang et al. 2018, danh mục tham khảo, arXiv v3 tr. 7) cũng ghi 3590–3598 — nguồn thứ cấp.
- Toàn văn / phiên bản / tài liệu bổ sung: PDF kỷ yếu NeurIPS tại `source_url` (9 trang, tải 2026-10-30). Không có tài liệu bổ sung được xem.
- Tệp nguồn cục bộ: `papers/Signal Aggregate Constraints in Additive Factorial HMMs, with Application to Energy Disaggregation.pdf`. Locator theo số trang chân trang của PDF (trùng số trang PDF).
- Mục tiêu đọc / RQ liên quan: chủ đề 2–3 (ràng buộc tổng, chính quy hóa); RQ3 (phân biệt ràng buộc tổng năng lượng theo thiết bị với C3), RQ1 (định nghĩa NDE/SAE).
- Trạng thái `reviewed` (rà soát 2026-10-30): đối chiếu phương trình 1–9, Bảng 1–3, Hình 1–2 và locator trên ảnh render trang PDF (PyMuPDF). Đã sửa: tham số ràng buộc ở phương trình 4 là δ_i (không phải ε_i); cách ước lượng μ trạng thái (k-means, 3 trạng thái) có nêu trong bài; locator ví dụ máy nướng bánh; trả lời câu hỏi NTC/rò rỉ (mục 8). Chưa tái lập thực nghiệm.

## 2. Tóm tắt điều hành

- Bài đề xuất **signal aggregate constraints (SAC)**: khuyến khích tổng tín hiệu của mỗi nguồn (thiết bị) trên cả chuỗi gần một giá trị kỳ vọng biết trước μ_i0. (Tóm tắt, tr. 1; mục 4.2, tr. 3.)
- SAC được đưa vào AFHMM dưới dạng ràng buộc bất đẳng thức với δ_i (phương trình 4, tr. 4) và giải bằng dạng **phạt bậc hai** tương đương với hệ số λ_i (phương trình 5, tr. 4). Đây là ràng buộc **mềm** trong suy luận MAP, không phải loss huấn luyện mạng nơ-ron.
- Bài toán được nới lỏng thành quy hoạch bậc hai lồi (CQP) giải bằng CVX (mục 5, phương trình 6, tr. 4–5).
- Mô hình đo: `Y_t = Σ_i x_it + ε_t`, với `Y_t ∈ R+`, `x_it ∈ R+` và ε_t Gauss trung bình 0, phương sai σ_t² (mục 3, phương trình 1, tr. 2). Đây là giả định mô hình, không phải ràng buộc được kiểm tra trên dữ liệu.
- Dữ liệu HES (Anh), 2 hoặc 10 phút; hai thí nghiệm: 100 hộ với công suất tổng tự cộng từ thiết bị, và 9 hộ dùng công suất tổng đo thật (mục 7.2, tr. 6–7).
- Với 9 hộ có mains: NDE AFHMM 1,36 ± 0,75; AFAMAP 1,05 ± 0,29; AFHMM+SAC (NTC) 0,74 ± 0,34; AFHMM+SAC (TTC, oracle) 0,57 ± 0,28 (Bảng 3, tr. 8).
- SAE ở bài này chuẩn hóa theo **tổng công suất tổng** và lấy trung bình qua thiết bị (phương trình 9, tr. 6) — khác SAE của Seq2Point (chuẩn hóa theo năng lượng thiết bị). NDE ở bài này không lấy căn (phương trình 8, tr. 5), khác NDE của Kolter & Jaakkola 2012 (có căn). Không so sánh số giữa các bài.

## 3. Bài toán, động lực và đóng góp

Tác giả xem NILM là tách nguồn mù một kênh, vốn không định danh được; cần đưa tri thức miền vào để nguồn tách ra có ý nghĩa (tránh “franken-appliance”). (Mục 1, tr. 1.) Quan sát được dùng: tổng tín hiệu khác nhau nhiều giữa các nguồn và thường biết trước giá trị tổng kỳ vọng, ví dụ máy nướng bánh có thể dùng 50 Wh/ngày và rất khó dùng tới 1000 Wh. (Mục 1, tr. 2.) Giá trị μ_i0 “could be obtained from expert knowledge or by experiments”, ví dụ ước tính tiêu thụ trung bình toàn quốc của thiết bị. (Mục 4.2, tr. 3.)

Đóng góp do tác giả nêu: (a) đề xuất SAC cho tách nguồn mù; (b) CQP cho AFHMM nới lỏng có SAC; (c) đánh giá trên dữ liệu năng lượng thật. (Mục 1, tr. 2.) Tác giả cũng chỉ ra mục tiêu (5) có thể suy ra từ posterior regularization (mục 6, phương trình 7, tr. 5).

## 4. Phương pháp và loss

Ký hiệu dưới đây đã đối chiếu với ảnh render trang PDF.

- Kiến trúc / đầu vào / đầu ra: AFHMM; mỗi thiết bị là một chuỗi Markov với tập trạng thái hữu hạn, `x_it ≈ μ_it ∈ {μ_i1,…,μ_iK_i}`; đầu vào là chuỗi công suất tổng Y; đầu ra là trạng thái (biểu diễn one-hot S_it) và tín hiệu thiết bị `μ_i^T S_it`. Tham số θ (μ, xác suất khởi tạo π_i, xác suất chuyển P^(i)) được coi là đã biết khi suy luận. (Mục 4–4.1, tr. 3.) Trong thí nghiệm năng lượng, θ ước lượng từ 15–30 ngày dữ liệu của từng hộ; mọi thiết bị giả định 3 trạng thái; μ_i ước lượng bằng k-means trên tín hiệu thiết bị trong dữ liệu huấn luyện. (Mục 7.2, tr. 6.)
- Công thức mục tiêu: log-posterior AFHMM gồm số hạng khởi tạo `S_i1^T log π_i`, chuyển trạng thái `S_it^T log P^(i) S_i,t−1` và **sai số bình phương** `−(1/2) Σ_t σ_t^{−2} (Y_t − Σ_i S_it^T μ_i)^2` (phương trình 3, tr. 3). SAC: `(Σ_{t=1}^T μ_i^T S_it − μ_i0)^2 ≤ δ_i`, δ_i ≥ 0 là tham số điều chỉnh có vai trò như trong ridge/LASSO (phương trình 4, tr. 4); dạng phạt: `L(S) = log P(S|Y) − Σ_i λ_i (Σ_t μ_i^T S_it − μ_i0)^2`, λ_i ≥ 0 tương ứng một-một với δ_i (phương trình 5, tr. 4). Đơn vị theo dữ liệu (bài mô tả quan sát là năng lượng đo bằng Wh, mục 3, tr. 2); reduction: tổng theo t và i.
- Mở rộng: có thể đặt J ràng buộc cho từng khoảng `[t^a_ij, t^b_ij]` (ví dụ thiết bị hiếm dùng 2–5 giờ sáng); phần còn lại của bài chỉ dùng một SAC mỗi chuỗi. (Mục 4.2, tr. 4.)
- Hệ số: λ_i = 1 cho mọi thí nghiệm, kể cả dữ liệu năng lượng; tác giả ghi có thể chỉnh bằng kiểm định chéo nhưng không làm. (Mục 7.1, tr. 5.)
- Nguồn của μ_i0 trong thí nghiệm: NTC (“national total consumption”) và TTC (oracle) — chi tiết và câu hỏi rò rỉ ở mục 8.
- Mất cân bằng / bật-tắt / chuẩn hóa: không nêu.
- Ràng buộc vật lý: `x_it ∈ R+` là giả định miền giá trị trong phương trình 1 (tr. 2). Bài không nêu ràng buộc tổng theo từng mẫu kiểu `Σ_i x̂_it ≤ Y_t`.

## 5. Bộ dữ liệu và thiết lập thực nghiệm

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Bộ dữ liệu / phiên bản / thiết bị / hộ | Toy: 2 chuỗi, trạng thái (0, 24, 280) và (0, 300, 500), T = 100, σ² = 0,01, xác suất khởi tạo/chuyển sinh ngẫu nhiên. Thật: Household Electricity Survey (HES), 251 hộ Anh 05/2010–07/2011 (26 hộ đo cả năm, 225 hộ đo một tháng); thí nghiệm 1 dùng 100 hộ, thí nghiệm 2 dùng 9 hộ có mains, 15–25 thiết bị/hộ | Mục 7.1, tr. 5; mục 7.2, tr. 6; Bảng 2, tr. 8 |
| Tần suất lấy mẫu / tiền xử lý / cửa sổ | 2 hoặc 10 phút tùy hộ; thí nghiệm 1 dựng công suất tổng bằng cộng tín hiệu thiết bị (phần lớn hộ không có mains) | Mục 7.2–7.2.1, tr. 6 |
| Tập huấn luyện / xác thực / kiểm tra | Thí nghiệm 1: tham số ước lượng từ 15–26 ngày, kiểm tra 1 ngày mỗi hộ. Thí nghiệm 2: 15–30 ngày huấn luyện, 8–10 ngày kiểm tra mỗi hộ (cùng hộ). Không có tập xác thực; không có hộ chưa thấy | Mục 7.2.1, tr. 6–7; Bảng 2, tr. 8 |
| Hạt giống ngẫu nhiên / số lần chạy | Không nêu; kết quả mean ± std theo ngày | Bảng 1, tr. 7; Bảng 3, tr. 8 |
| Siêu tham số / tìm kiếm / ngân sách | λ_i = 1 cố định; 3 trạng thái/thiết bị; không tìm kiếm | Mục 7.1, tr. 5; mục 7.2, tr. 6 |
| Phần cứng / thời gian chạy | Thời gian chạy (giây) trong Bảng 1, 3; phần cứng không nêu | Bảng 1, tr. 7; Bảng 3, tr. 8 |

## 6. Mô hình đối chứng, thước đo và kết quả

Thước đo:

- NDE = `Σ_{i,t} (x̂_it − x_it)^2 / Σ_{i,t} x_it^2` (phương trình 8, tr. 5); không lấy căn; thấp hơn là tốt hơn.
- SAE = `(1/I) Σ_i |Σ_t x̂_it − Σ_t' x_it'| / Σ_t Y_t` (phương trình 9, tr. 6); thấp hơn là tốt hơn. Mẫu số là tổng công suất tổng.

| Thiết lập / bộ dữ liệu / cách chia | Mô hình đối chứng / loss | Thước đo / định nghĩa / đơn vị / chiều tốt hơn | Kết quả / độ biến thiên (mean ± std theo ngày) | Vị trí nguồn |
| --- | --- | --- | --- | --- |
| HES, 100 hộ, công suất tổng = tổng thiết bị, 1 ngày test/hộ | AFHMM; AFAMAP; AFHMM+SAC (NTC); AFHMM+SAC (TTC) | NDE, thấp hơn tốt hơn | 0,98 ± 0,68; 0,96 ± 0,42; 0,64 ± 0,37; 0,36 ± 0,28 | Bảng 1, tr. 7 |
| Như trên | Như trên | SAE, thấp hơn tốt hơn | 0,144 ± 0,067; 0,083 ± 0,004; 0,069 ± 0,004; 0,0015 ± 0,0089 | Bảng 1, tr. 7 |
| Như trên | Như trên | Thời gian (giây) | 206 ± 114; 325 ± 177; 356 ± 262; 260 ± 108 | Bảng 1, tr. 7 |
| HES, 9 hộ, mains đo thật, 8–10 ngày test/hộ | Như trên | NDE | 1,36 ± 0,75; 1,05 ± 0,29; 0,74 ± 0,34; 0,57 ± 0,28 | Bảng 3, tr. 8 |
| Như trên | Như trên | SAE | 0,069 ± 0,039; 0,043 ± 0,012; 0,030 ± 0,014; 0,001 ± 0,0048 | Bảng 3, tr. 8 |
| Như trên | Như trên | Thời gian (giây) | 1008 ± 269; 1327 ± 453; 1101 ± 342; 1276 ± 410 | Bảng 3, tr. 8 |

Tác giả báo SAC (NTC) cải thiện 33% NDE và 16% SAE so với AFAMAP trong thí nghiệm 1, với kiểm định t ghép cặp ở mức 5% (mục 7.2.1, tr. 7). Ở thí nghiệm 2, kiểm định t ghép cặp AFAMAP vs AFHMM+SAC (NTC) được làm cho từng hộ, khác biệt ở mức 5% (mục 7.2.2, tr. 7; Hình 2, tr. 8). Ở phần giới thiệu, tác giả nêu giảm 45% NDE so với AFHMM và 29% so với AFAMAP trên dữ liệu có mains (mục 1, tr. 2) — khớp với Bảng 3 (1,36 → 0,74; 1,05 → 0,74). Thí nghiệm toy: NDE và SAE tăng khi khoảng cách Euclid giữa μ_0 và tổng thật tăng (Hình 1, tr. 6). Với 9 hộ có mains, tác giả nêu công suất tổng còn gồm thiết bị không có trong dữ liệu huấn luyện, nên bài toán khó hơn nhưng thực tế hơn (mục 7.2.2, tr. 7).

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| SAC là phạt bậc hai trên độ lệch tổng năng lượng của từng thiết bị so với giá trị kỳ vọng | Phương trình 4–5 | Mục 4.2, tr. 3–4 | Tuyên bố của tác giả; cao |
| SAC là ràng buộc mềm trong suy luận MAP của AFHMM, không phải loss huấn luyện mạng | Tham số θ cố định, tối ưu trên trạng thái S | Mục 4.1, tr. 3; mục 5, tr. 4–5 | Cao |
| Mô hình đo giả định thiết bị không âm và công suất tổng = tổng thiết bị + nhiễu Gauss | Phương trình 1 | Mục 3, tr. 2 | Giả định mô hình; không kiểm chứng trên dữ liệu |
| Công suất tổng đo thật chứa thiết bị không được mô hình hóa | Tác giả nêu khi mô tả thí nghiệm 2 | Mục 7.2.2, tr. 7 | Tuyên bố của tác giả; không định lượng phần dư |
| SAC giảm NDE/SAE so với AFHMM và AFAMAP trên HES | 100 hộ không mains; 9 hộ có mains; λ = 1; NTC từ ngày huấn luyện | Bảng 1, tr. 7; Bảng 3, tr. 8 | Kết quả quan sát trong phạm vi HES, chia theo ngày cùng hộ |
| Hiệu quả SAC phụ thuộc độ chính xác của μ_0 | Thí nghiệm toy hai chuỗi | Hình 1, tr. 6 | Kết quả quan sát trên dữ liệu tổng hợp |
| NDE tăng khi chuyển từ công suất tổng tổng hợp sang mains đo thật | So Bảng 1 với Bảng 3 | tr. 7–8 | Quan sát; hai thí nghiệm khác hộ và số ngày nên không phải so sánh có kiểm soát |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

SAC giúp xử lý vấn đề không định danh được, cải thiện “dramatically” so với AFHMM và “significantly” so với AFAMAP; trên dữ liệu mô phỏng AFHMM+SAC “robust to errors in specification of the constraint value”. (Tóm tắt, tr. 1; mục 8, tr. 8.)

### Thí nghiệm thực sự chứng minh gì?

Trên HES với chia theo ngày trong cùng hộ, λ_i = 1 cố định và μ_0 lấy từ trung bình ngày huấn luyện, AFHMM+SAC đạt NDE/SAE trung bình thấp hơn hai mô hình đối chứng (Bảng 1, 3, tr. 7–8). Kết quả oracle TTC chỉ cho cận trên của lợi ích. Tuyên bố “vững trước sai số chỉ định” chỉ dựa trên thí nghiệm toy hai chuỗi (Hình 1, tr. 6), và hình đó cho thấy lỗi tăng theo độ lệch.

### NTC tính trên những dữ liệu nào? (câu hỏi rò rỉ)

- **Lời tác giả, thí nghiệm 1:** NTC “was the average consumption of each appliance over the training days across all households in the data set” (mục 7.2.1, tr. 7); chú thích Bảng 1 và Bảng 3: “average consumption of each appliance over the training days” (tr. 7, tr. 8). TTC là tổng thật “for that day and household in the test data” (tr. 7).
- **Lời tác giả, thí nghiệm 2:** “We computed the NTC by using the training data” (mục 7.2.2, tr. 7); bài **không nêu** NTC ở thí nghiệm này gộp 9 hộ hay tính riêng từng hộ.
- **Kết luận theo văn bản:** theo định nghĩa của tác giả, NTC chỉ dùng **ngày huấn luyện**; ngày kiểm tra không được nêu là góp vào NTC. Vì mỗi hộ vừa có ngày huấn luyện vừa có ngày kiểm tra, các hộ được kiểm tra **có** góp dữ liệu ngày huấn luyện của chính mình (và, ở thí nghiệm 1, của mọi hộ khác) vào NTC.
- **Không nêu:** bài không nói rõ ngày kiểm tra tách rời ngày huấn luyện (chỉ nêu số ngày mỗi loại), không nói cách chọn ngày kiểm tra.
- **Suy luận của người rà soát:** không có bằng chứng văn bản về rò rỉ dữ liệu **ngày kiểm tra** vào NTC. Tuy nhiên NTC dùng thông tin cùng hộ (và chéo hộ) nên chỉ hợp lệ cho giao thức chia theo ngày trong cùng hộ; tên “national” dễ gây hiểu nhầm là thống kê độc lập bên ngoài (như khảo sát quốc gia mà tác giả gợi ý ở mục 4.2, tr. 3 và tr. 7). Kết quả NTC không phải bằng chứng cho hộ chưa thấy. Nếu dự án dùng thành phần dạng SAC với chia theo hộ, μ_0 phải tính chỉ từ hộ huấn luyện.

### Bài báo chưa giải quyết gì?

- Không xét ràng buộc theo từng mẫu thời gian (tổng dự đoán so với công suất tổng tại t); không đo vi phạm vật lý.
- Không đánh giá trên hộ chưa thấy; λ không được chỉnh; không nêu seed.
- Tác giả nêu hướng tương lai: đưa SAC vào phương pháp không giám sát, dùng khảo sát quốc gia để ước lượng μ_0 (mục 7.2.1, tr. 7).

## 9. Hạn chế và khả năng tái lập

- Mã nguồn / dữ liệu / giấy phép / phiên bản hoặc mã commit: bài không nêu kho mã; dữ liệu HES chưa kiểm tra điều kiện truy cập.
- Lệnh tái lập do tác giả cung cấp: không nêu.
- Chi tiết còn thiếu / nguy cơ ảnh hưởng tính hợp lệ: không nêu cách chọn 100 hộ và thiết bị cho từng hộ trong thí nghiệm 1, cách chọn ngày kiểm tra, xử lý thiếu dữ liệu, σ_t dùng cho dữ liệu thật, NTC ở thí nghiệm 2 gộp hộ hay không; tần suất 2/10 phút khác REFIT (8 giây).
- Đã tự chạy lại chưa? Chưa.

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc:**

- Có thể dùng trực tiếp: phân biệt hai loại “ràng buộc tổng”: (i) SAC — tổng năng lượng **của một thiết bị theo thời gian** gần giá trị kỳ vọng; (ii) C3 của dự án — tổng **các thiết bị tại một thời điểm** không vượt công suất tổng. Hai khái niệm không thay thế nhau.
- Cần điều chỉnh: nếu đưa thành phần dạng SAC vào loss mạng nơ-ron, μ_0 phải lấy từ dữ liệu huấn luyện độc lập với test (với chia theo hộ: chỉ từ hộ huấn luyện); λ cần ngân sách chỉnh như các loss khác.
- Cần điều chỉnh: định nghĩa SAE phải ghi rõ mẫu số (công suất tổng như phương trình 9 hay năng lượng thiết bị như Seq2Point); NDE phải ghi có lấy căn hay không.
- Khoảng trống nghiên cứu: bài không cho bằng chứng về loss huấn luyện của mạng nơ-ron hay về tần suất vi phạm C1–C3.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Truy vết Zhong, Goddard & Sutton 2015 (latent Bayesian melding, dùng thống kê toàn cục) mà Seq2Point dẫn.
- Câu hỏi thí nghiệm (đề xuất, chưa kiểm chứng): một số hạng phạt tổng năng lượng theo cửa sổ có thay đổi SAE và tần suất vi phạm C3 của mô hình nơ-ron không?

## 12. Trích dẫn

Khóa BibTeX `zhong2014signal` trong `ref.bib`. Zhong, M., Goddard, N., & Sutton, C. (2014). Signal Aggregate Constraints in Additive Factorial HMMs, with Application to Energy Disaggregation. In *Advances in Neural Information Processing Systems 27*, 3590–3598.
