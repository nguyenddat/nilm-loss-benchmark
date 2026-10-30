---
type: paper
status: reviewed
title: "Approximate Inference in Additive Factorial HMMs with Application to Energy Disaggregation"
authors: [J. Zico Kolter, Tommi Jaakkola]
year: 2012
venue: "Proceedings of the 15th International Conference on Artificial Intelligence and Statistics (AISTATS 2012), PMLR 22"
doi: "không nêu"
source_url: "https://proceedings.mlr.press/v22/zico12.html"
citation_key: "kolter2012approximate"
read_date: 2026-10-30
tags: [nilm, literature, afhmm, total-variation, robust-loss, convex-optimization]
---

# AFAMAP — Kolter & Jaakkola (2012)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Kolter, J. Z., Jaakkola, T. "Approximate Inference in Additive Factorial HMMs with Application to Energy Disaggregation." AISTATS 2012, PMLR 22:1472–1482. Tiêu đề, tác giả, hội nghị, tập và trang khớp `ref.bib` (`kolter2012approximate`) và chân trang PDF.
- Toàn văn / phiên bản / tài liệu bổ sung: PDF PMLR `https://proceedings.mlr.press/v22/zico12/zico12.pdf` (11 trang, tải 2026-10-30). Trang đầu PDF vẫn ghi “Volume XX of JMLR: W&CP XX”. Bài nói mã MATLAB cho thí nghiệm tổng hợp đi kèm bài (chú thích 4, tr. 1477); chưa kiểm tra.
- Tệp nguồn cục bộ: `papers/Approximate Inference in Additive Factorial HMMs with Application to Energy Disaggregation.pdf`. Locator dùng số trang kỷ yếu in ở chân trang (PDF tr. 1 = tr. 1472, …, PDF tr. 11 = tr. 1482).
- Mục tiêu đọc / RQ liên quan: chủ đề 2 (TV, loss bền vững/Huber), chủ đề 3 (mô hình hóa phần dư công suất tổng), chủ đề 5 (tối ưu lồi, chỉ dùng công suất tổng); RQ2, RQ3.
- Trạng thái `reviewed` (rà soát 2026-10-30): đối chiếu lại toàn bộ ký hiệu phương trình 1–16 và 33–35 trên ảnh render trang PDF (PyMuPDF), số liệu Bảng 1, chú thích 4–5 và mọi locator. Đã sửa: dạng prior ở phương trình 3, hệ số Σ^{1/2}, vị trí Huber (Δz_t trong mô hình hiệu), định nghĩa NDE có căn bậc hai, λ và Σ cùng được chỉnh trên một ngày. Chưa tái lập thực nghiệm.

## 2. Tóm tắt điều hành

- Bài đề xuất AFAMAP, suy luận MAP gần đúng **lồi** cho additive FHMM, kết hợp: mô hình tổng (additive), mô hình hiệu tín hiệu (difference), thành phần hỗn hợp “robust” và điều kiện chỉ một chuỗi đổi trạng thái mỗi lúc (one-at-a-time). (Tóm tắt, tr. 1472; mục 3.3 và Hình 3, tr. 1476.)
- Thành phần robust `z_t ∈ R^n` giải thích phần tín hiệu tổng không được thiết bị nào mô hình hóa; prior là **total variation 1D** (chuẩn ℓ1 của hiệu tín hiệu), khuyến khích `z_t` hằng từng đoạn; `z_t` được nhân với Σ^{1/2} trong trung bình của quan sát. (Mục 2.2, phương trình 3–4, tr. 1474.)
- Trong **mô hình hiệu**, tại các bước không chuỗi nào đổi trạng thái, tối ưu giải tích theo `Δz_t` của số hạng bình phương cộng phạt `λ‖Δz_t‖_1` cho **hàm Huber** `D(y, λ)` thay cho sai số bình phương. (Mục 3.2, phương trình 14, tr. 1476; Phụ lục B, phương trình 33–35, tr. 1481–1482.)
- Thiết lập **không giám sát**: dữ liệu cấp mạch chỉ dùng để kiểm định, không dùng huấn luyện mô hình. (Mục 1, tr. 1473; mục 5, tr. 1478.)
- Dữ liệu thật: công suất tổng một hộ trong hai tuần ghi bằng thiết bị A/D độ phân giải cao, kèm đo cấp mạch; 9 motif thiết bị, 7 mạch; λ và Σ chỉnh trên một ngày dữ liệu. AFAMAP đạt precision/recall tổng 87,2%/60,3% so với SMF 35,5%/45,1%. (Mục 5, tr. 1478; Bảng 1, tr. 1479.)
- Năng lượng “chưa gán” được coi là hợp lệ khi thiết bị không có mô hình, nên recall không kỳ vọng đạt 100% và tác giả nhấn mạnh precision. (Mục 5, tr. 1478.)

## 3. Bài toán, động lực và đóng góp

FHMM có biểu diễn mạnh nhưng suy luận chính xác không khả thi và các phương pháp gần đúng (block Gibbs, structured mean field) dễ rơi vào cực trị địa phương. Tác giả khai thác cấu trúc cộng tính để có bài toán lồi, không có vấn đề cực trị địa phương, tính toán gần tuyến tính theo số HMM, xử lý được nhiễu cộng không IID. (Tóm tắt, tr. 1472; mục 1, tr. 1472.) Với NILM, đóng góp theo tác giả: xét thiết lập không giám sát (không biết trước thiết bị trong nhà); dùng được mô hình thiết bị phức tạp hơn; nối hai hướng (trạng thái thiết bị và tín hiệu quá độ) trong một mô hình. (Mục 1, tr. 1473.)

## 4. Phương pháp và loss

Ký hiệu dưới đây đã đối chiếu với ảnh render trang PDF.

- Kiến trúc / đầu vào / đầu ra: additive FHMM — N HMM độc lập; `x_t^(i) ∈ {1,…,m_i}`; quan sát `ȳ_t | x_t^(1:N) ~ N(Σ_{i=1}^N μ^(i)_{x_t^(i)}, Σ)`, `ȳ_t ∈ R^n` (phương trình 1, tr. 1473). Difference FHMM: `Δȳ_t | x_t^(1:N), x_{t−1}^(1:N) ~ N(Σ_i (μ_{x_t^(i)} − μ_{x_{t−1}^(i)}), Σ)`, ký hiệu `Δμ_{j,k} = μ_j − μ_k` (phương trình 2, tr. 1473). Đầu ra: `ŷ_t^(i) = Σ_j μ_j^(i) Q(x_t^(i))_j` (Hình 3, tr. 1476).
- Thành phần robust, mô hình tổng: prior `p(z_{1:T}) = (1/Z(λ,T)) exp{−λ Σ_{t=1}^{T−1} ‖z_{t+1} − z_{t−1}‖_1}` **như in ở phương trình 3** (tr. 1474); trong mục tiêu (9) và Hình 3 số hạng tương ứng là `λ Σ_t ‖z_t − z_{t−1}‖_1`. Văn bản mô tả prior là “ℓ1 norm of the signal differences” (mục 2.2, tr. 1474). Chỉ số `t+1, t−1` trong phương trình 3 không khớp với (9): bài không giải thích; **suy luận của người rà soát**: nhiều khả năng là lỗi in, nhưng chưa xác minh. Likelihood: `ȳ_t | x_t^(1:N), z_t ~ N(Σ_i μ^(i)_{x_t^(i)} + Σ^{1/2} z_t, Σ)`; Σ^{1/2} được dùng để một hệ số λ chung có đơn vị tương thích với `ȳ_t` (phương trình 4, tr. 1474).
- Thành phần robust, mô hình hiệu: prior ℓ1 trực tiếp `exp{−λ Σ_t ‖Δz_t‖_1}` và trung bình `Σ_i Δμ + Σ^{1/2} Δz_t` (phương trình 5–6, tr. 1474).
- Mục tiêu tối ưu: MAP được viết thành MIQP gồm `½ Σ_t ‖ȳ_t − Σ^{1/2} z_t − Σ_{i,j} μ_j^(i) Q(x_t^(i))_j‖²_{Σ^{−1}}`, số hạng `Σ Q(·)_{j,k}(−log P^(i)_{k,j})` và `λ Σ_t ‖z_t − z_{t−1}‖_1` (phương trình 9, tr. 1475); dạng tương tự cho mô hình hiệu (phương trình 10, tr. 1475). Ràng buộc: Q thuộc local marginal polytope L (phương trình 8, tr. 1475) và tập one-at-a-time O: `Σ_{i,j,k≠j} Q(x_{t−1}^(i), x_t^(i))_{j,k} ≤ 1` (phương trình 13, tr. 1476).
- Loss bền vững: với ràng buộc O, khi một chuỗi đổi trạng thái thì `Δz_t = 0`; khi không chuỗi nào đổi, số hạng `‖Δȳ_t − Σ^{1/2}Δz_t‖²_{Σ^{−1}}` cộng `λ‖Δz_t‖_1` tối ưu giải tích cho Huber. Phương trình 14 in `D(y, λ) = min_z {‖y − z‖²_2 + λ‖z‖_1} = Σ_ℓ min{½ y_ℓ², max{λ|y_ℓ| − λ²/2, λ²/2}}` (tr. 1476); Phụ lục B suy ra từ `½‖y − z‖²_2 + λ‖z‖_1` với nghiệm soft-thresholding (phương trình 33–35, tr. 1481–1482). Hệ số ½ trong vế min của (14) và (34) khác nhau; bài không bình luận. Kết quả là MILP (phương trình 15, tr. 1476), nới lỏng thành LP.
- AFAMAP: kết hợp mô hình tổng (Σ_1, λ_1) và mô hình hiệu (Σ_2, λ_2) sau khi nới lỏng nguyên, ràng buộc posterior trạng thái hai mô hình khớp nhau; `z` không buộc khớp. Là QP lồi; giải xen kẽ: CPLEX cho Q với `z` cố định, bộ giải TV proximal (Barbero & Sra 2011) cho `z` với Q cố định; dự đoán bằng trung bình đầu ra, không làm tròn. (Mục 3.3, Hình 3, tr. 1476; tr. 1477.)
- Reduction / trọng số / đơn vị: tổng theo t, i, j, k; λ_1, λ_2 ∈ R+ và Σ_1, Σ_2 là tham số (Hình 3, tr. 1476). Đơn vị W trong thí nghiệm năng lượng (Hình 7, tr. 1479).
- Mất cân bằng / bật-tắt / chuẩn hóa: không nêu. Ràng buộc không âm cho đầu ra: không nêu tường minh.
- Tiền xử lý tín hiệu: dùng biến thể tham lam của TV để xấp xỉ công suất thành hằng từng đoạn nhằm giảm kích thước tín hiệu, trước khi trích motif (mục 5, tr. 1478) — đây là bước tiền xử lý, khác với TV trên `z_t` trong mục tiêu.

## 5. Bộ dữ liệu và thiết lập thực nghiệm

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Bộ dữ liệu / phiên bản / thiết bị / hộ | Tổng hợp: N HMM “cyclic”, mặc định N = 4, m = 4, n = 4, T = 500; trạng thái đầu đều; `P_jj ∝ 30`; trung bình `(μ_j^(i))_ℓ ~ U[0, 2]`; nhiễu N(0, 0,01I). Thật: một hộ, hai tuần công suất tổng (thiết bị A/D độ phân giải cao) + đo cấp mạch; chú thích ghi “All data is available at redd.csail.mit.edu” nhưng không nêu số hộ REDD; 9 motif thiết bị, 7 mạch | Chú thích 4, tr. 1477; mục 5 và chú thích 5, tr. 1478; Bảng 1, tr. 1479 |
| Tần suất lấy mẫu / tiền xử lý / cửa sổ | Tần suất không nêu bằng con số; xấp xỉ hằng từng đoạn bằng TV tham lam; trích đoạn bật–tắt vượt ngưỡng (ngưỡng không nêu), dựng HMM “thực nghiệm”, gom cụm phổ trên đồ thị k láng giềng gần nhất để chọn motif | Mục 5, tr. 1478 |
| Tập huấn luyện / xác thực / kiểm tra | Không giám sát; λ và Σ của mọi phương pháp chỉnh trên một ngày; đánh giá trên toàn bộ hai tuần. Bài không nêu ngày dùng để chỉnh có bị loại khỏi phần đánh giá hay không | Mục 5, tr. 1478 |
| Hạt giống ngẫu nhiên / số lần chạy | Không nêu | — |
| Siêu tham số / tìm kiếm / ngân sách | Tổng hợp: tham số chính quy “on the order of” tham số của mô hình thật. Thật: λ và Σ chỉnh trên một ngày; SMF được tác giả chỉnh “substantially”; SMF dùng annealing trong mọi thí nghiệm | Chú thích 4, tr. 1477; mục 4, tr. 1477; mục 5, tr. 1478–1479 |
| Phần cứng / thời gian chạy | Không nêu | — |

## 6. Mô hình đối chứng, thước đo và kết quả

Thước đo trên dữ liệu tổng hợp: normalized disaggregation error `sqrt( Σ_{t,i} ‖y_t^(i) − ŷ_t^(i)‖²_2 / Σ_{t,i} ‖y_t^(i)‖²_2 )` — **có căn bậc hai** (phương trình 16, tr. 1477); thấp hơn là tốt hơn. Lưu ý: NDE của Zhong và cộng sự 2014 (phương trình 8) không lấy căn; hai con số không so sánh trực tiếp được.

| Thiết lập / bộ dữ liệu / cách chia | Mô hình đối chứng / loss | Thước đo / định nghĩa / đơn vị / chiều tốt hơn | Kết quả / độ biến thiên | Vị trí nguồn |
| --- | --- | --- | --- | --- |
| Tổng hợp, thay đổi số HMM / số trạng thái / số chiều đầu ra (2–10) | Exact MAP; SMF; AFAMAP bỏ mô hình hiệu (Σ_2 = ∞); AFAMAP bỏ mô hình tổng (Σ_1 = ∞); Prior (phân phối dừng) | NDE có căn (phương trình 16), thấp hơn tốt hơn | AFAMAP tốt hơn mọi phương pháp gần đúng (trừ exact MAP khi chạy được); dùng cả hai mô hình tốt hơn từng mô hình riêng (chỉ có đồ thị, không có bảng số) | Phương trình 16, Hình 4, tr. 1477 |
| Tổng hợp + nhiễu random walk `w_t ~ N(w_{t−1}; σ²I)`, σ từ 0 đến 0,1 | AFAMAP và Exact MAP, có/không thành phần robust; Prior | Như trên | Theo tác giả, mục tiêu lồi của AFAMAP ước lượng được thành phần nhiễu; exact MAP với robust dùng tối đa hóa xen kẽ gặp vấn đề như SMF (chỉ có đồ thị) | Hình 5, tr. 1478 |
| Một hộ, hai tuần, cấp mạch | AFAMAP vs SMF | Precision/recall năng lượng theo mạch, % | Tổng: AFAMAP 87,2% / 60,3%; SMF 35,5% / 45,1%. In đậm (khác biệt có ý nghĩa thống kê trên cả hai thước đo): Microwave 97,5%/66,1%, Bath GFI 82,7%/70,8%, Furnace 91,7%/70,8% và Total. Wash/Dryer 98,8%/73,6% không in đậm | Bảng 1, tr. 1479 |

Ghi chú: precision/recall là theo năng lượng gán cho mạch, không phải F1 sự kiện; một mạch có thể chứa nhiều thiết bị (chú thích Bảng 1, tr. 1479). Bài không nêu kiểm định thống kê nào được dùng cho phần in đậm. Văn bản nói 5/9 thiết bị có precision > 90% (mục 5, tr. 1478–1479), trong khi Bảng 1 chỉ có 3/7 mạch vượt 90% (Microwave, Furnace, Wash/Dryer); bài không cho bảng theo thiết bị nên không đối chiếu được con số 5/9.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| Phần dư không được mô hình hóa được biểu diễn bằng một thành phần riêng với prior TV | `z_t` trong mô hình tổng, nhân Σ^{1/2}, phạt ℓ1 của hiệu | Mục 2.2, phương trình 3–4, tr. 1474 | Tuyên bố/định nghĩa của tác giả; cao |
| TV ở đây chính quy hóa thành phần phần dư, không phải đầu ra thiết bị | Đầu ra thiết bị là `Σ_j μ_j Q_j`; TV chỉ áp lên `z` | Phương trình 3–4, tr. 1474; Hình 3, tr. 1476 | Cao (đọc trực tiếp cấu trúc) |
| Sai số bình phương + ℓ1 trên `Δz_t` tương đương Huber trên tín hiệu hiệu đã chuẩn hóa `Σ^{−1/2}Δȳ_t`, ở các bước không chuỗi nào đổi trạng thái | Tối ưu giải tích theo `Δz_t` dưới ràng buộc O | Phương trình 14–15, tr. 1476; phương trình 33–36, tr. 1481–1482 | Cao |
| AFAMAP vượt SMF trên một hộ hai tuần | Không giám sát; precision/recall năng lượng theo mạch; tham số chỉnh trên một ngày | Bảng 1, tr. 1479; mục 5, tr. 1478 | Quan sát trong một hộ; không tổng quát hóa |
| Năng lượng chưa gán là hợp lệ khi thiết bị không có mô hình | Lý do đặt trọng tâm vào precision | Mục 5, tr. 1478 | Tuyên bố của tác giả |
| Xác suất vi phạm one-at-a-time là O(Δt) và tăng theo bậc hai của số HMM | Mệnh đề 1 và chứng minh | Mục 3.2, phương trình 11–12, tr. 1475; Phụ lục A, phương trình 28, tr. 1481 | Kết quả lý thuyết dưới giả định chuỗi Markov liên tục rời rạc hóa |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

AFAMAP lồi, hiệu quả, không có cực trị địa phương, tốt hơn nhiều so với các phương pháp hiện có và tách gần hoàn hảo nhiều thiết bị chỉ từ tín hiệu tổng. (Tóm tắt, tr. 1472; mục 5, tr. 1479.)

### Thí nghiệm thực sự chứng minh gì?

Trên dữ liệu tổng hợp với tham số đã biết, AFAMAP có lỗi chuẩn hóa thấp hơn SMF và các biến thể bỏ thành phần (Hình 4–5, tr. 1477–1478; chỉ có đồ thị). Trên dữ liệu thật, bằng chứng chỉ từ **một hộ, hai tuần**, đánh giá cấp mạch, so với một đối chứng (SMF) đã được chỉnh thủ công (Bảng 1, tr. 1479). “Gần hoàn hảo” dựa vào precision > 90% của 5 thiết bị và quan sát trực quan (mục 5, tr. 1479; Hình 7, tr. 1479).

### Bài báo chưa giải quyết gì?

- Không xét loss huấn luyện có giám sát; không so sánh các dạng loss ngoài việc Huber xuất hiện như hệ quả của suy luận.
- Không nêu ràng buộc không âm hay ràng buộc tổng theo mẫu; `z_t` “can take on arbitrary values” (mục 2.2, tr. 1474), nên dấu của phần dư không bị ràng buộc.
- Tác giả nêu hướng tương lai: kết hợp học và suy luận, lặp trên phần năng lượng “unassigned” để học thêm thiết bị, hard EM (mục 6, tr. 1479).
- Tác giả lưu ý xác suất vi phạm one-at-a-time tăng theo bình phương số HMM, có thể cần tần suất lấy mẫu khá cao (Phụ lục A, tr. 1481).
- Suy luận của người rà soát: ngày dùng để chỉnh λ, Σ nằm trong hai tuần được đánh giá, và bài không nêu có loại ra hay không — đây là nguy cơ lạc quan nhỏ trong đánh giá, không phải điều tác giả thừa nhận.

## 9. Hạn chế và khả năng tái lập

- Mã nguồn / dữ liệu / giấy phép / phiên bản hoặc mã commit: mã MATLAB cho thí nghiệm tổng hợp được nói là đi kèm bài (chú thích 4, tr. 1477); dữ liệu thật chỉ dẫn tới trang REDD (chú thích 5, tr. 1478). Chưa kiểm tra.
- Lệnh tái lập do tác giả cung cấp: không nêu.
- Chi tiết còn thiếu / nguy cơ ảnh hưởng tính hợp lệ: tần suất lấy mẫu, số hộ REDD, ngưỡng trích motif, giá trị λ/Σ cuối, kiểm định thống kê của Bảng 1, số lần chạy; đối chứng duy nhất trên dữ liệu thật; một hộ.
- Đã tự chạy lại chưa? Chưa.

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc:**

- Có thể dùng trực tiếp: cách tách rõ “phần dư công suất tổng” thành một biến có prior riêng là một cách làm tường minh giả định về tải chưa đo — phù hợp với cảnh báo của dự án rằng không suy ra C3 vô điều kiện (xem ghi chú C3 trong `notes/NILM-Evaluation/`).
- Có thể dùng trực tiếp: Huber xuất hiện như loss bền vững trước phần dư thưa; là ứng viên có cơ sở để thêm vào nhóm loss bền vững (chủ đề 2), nhưng bối cảnh gốc là suy luận AFHMM trên tín hiệu hiệu, không phải huấn luyện mạng.
- Cần điều chỉnh: “total variation” trong dự án (làm trơn đầu ra thiết bị) khác vị trí áp TV ở bài này (trên phần dư và trong tiền xử lý). Khi định nghĩa loss TV phải nêu áp lên đại lượng nào.
- Cần điều chỉnh: nếu dùng NDE, phải nêu có lấy căn hay không (bài này có căn, Zhong 2014 không).
- Khoảng trống nghiên cứu: không có số liệu nào về vi phạm C1–C3; không có thiết lập có giám sát.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Kiểm tra dữ liệu thật thuộc hộ nào của REDD (bài không nêu số hộ) và tải mã MATLAB nếu còn.
- Phương trình 3 (`z_{t+1} − z_{t−1}`) có phải lỗi in không — chỉ xác minh được nếu có errata hoặc mã gốc.
- Câu hỏi thí nghiệm (đề xuất): với mô hình nơ-ron, thay MSE bằng Huber có làm thay đổi sai số ở vùng chuyển trạng thái (RQ2) không?

## 12. Trích dẫn

Khóa BibTeX `kolter2012approximate` trong `ref.bib` (đã đối chiếu tiêu đề, tác giả, hội nghị, tập 22, trang 1472–1482 với PDF). Kolter, J. Z., & Jaakkola, T. (2012). Approximate Inference in Additive Factorial HMMs with Application to Energy Disaggregation. In *Proceedings of the Fifteenth International Conference on Artificial Intelligence and Statistics*, PMLR 22, 1472–1482.
