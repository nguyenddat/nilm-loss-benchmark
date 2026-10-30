---
type: synthesis
status: draft
title: "Taxonomy phương pháp NILM"
aliases: [Taxonomy phương pháp NILM tần số thấp, Cây phân nhóm phương pháp NILM]
tags: [nilm, synthesis, taxonomy, literature-review, top-down]
---

# Taxonomy phương pháp NILM (tần số thấp) — cây phân nhóm do dự án dựng từ ba review

> [!warning] Cây phân nhóm là đề xuất của dự án
> Không review nào trong ba review đã rà soát đề xuất đúng cây này; Huber và cộng sự còn ghi rõ nhóm màu trong hình tổng quan của họ “không nên hiểu là taxonomy” ([@huber2021review], Hình 1, tr. 10). Cây dưới đây là cách dự án sắp xếp lại các trục mà review dùng. Mọi locator của review đã được đối chiếu với PDF (2026-10-30). Nhãn **[R]** (liên quan trực tiếp bài toán: loss, C1–C3, độ vững) là **suy luận của dự án**. Nhãn **[L]** đánh dấu nút hoặc nhánh dựng từ bài lá, **chưa có review nào xác nhận**. Bài lá chưa `reviewed` chỉ được nêu tên để định hướng đọc, không làm bằng chứng.

## Câu hỏi và phạm vi

Các review gần đây chia không gian phương pháp NILM tần số thấp thế nào, và những nhánh nào chứa bằng chứng cho bài toán của dự án: lựa chọn loss, ràng buộc vật lý trên dự đoán và độ vững dưới dịch chuyển phân phối? Khái niệm liên quan: [[notes/NILM-Definitions/Phát biểu bài toán NILM|Phát biểu bài toán NILM]], [[notes/NILM-Evaluation/Ràng buộc C1 - không âm|C1 - không âm]], [[notes/NILM-Evaluation/Ràng buộc C2 - công suất cực đại thiết bị|C2 - công suất cực đại thiết bị]], [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|C3 - giới hạn công suất tổng]], [[notes/NILM-Evaluation/NAR - tỷ lệ phần dư công suất tổng|NAR]], [[notes/NILM-methodology/Học có giám sát|Học có giám sát]], [[notes/NILM-methodology/Chỉ dùng công suất tổng|Chỉ dùng công suất tổng]], [[notes/literature-matrix|Ma trận bằng chứng]].

Ngoài phạm vi: NILM tần số cao (dạng sóng, V-I), phương pháp chỉ phát hiện sự kiện, ứng dụng thương mại/công nghiệp.

## Nguồn đã đọc

| Review | Khóa | Phiên bản và locator | Phạm vi đọc | Trạng thái |
| --- | --- | --- | --- | --- |
| Huber và cộng sự 2021, Energies 14(9):2390 | `huber2021review` | Bản xuất bản, 34 tr.; trang tạp chí | Toàn văn mục 1–6; dòng Bảng 2 chưa trích | reviewed |
| Kaselimi và cộng sự 2022, Sensors 22(15):5872 | `kaselimi2022trustworthy` | arXiv:2207.02009v1, 22 tr.; **locator theo arXiv v1**, chưa đối chiếu bản Sensors | Toàn văn mục I–VIII | reviewed |
| Saleem và cộng sự 2025, Applied Intelligence 55(15):1020 | `saleem2025review` | Bản xuất bản Springer, 36 tr.; trang bài | Phần lời mục 1–7; dòng Bảng 2–3, Hình 3–7 chưa trích | reviewed |

Ghi chú nguồn: `papers/2021-huber-dnn-low-frequency-nilm-review.md`, `papers/2022-kaselimi-trustworthy-nilm-review.md`, `papers/2025-saleem-ml-dl-nilm-review.md`. Các review 2023–2026 khác đã xác minh metadata nhưng chưa đọc (danh sách trong kế hoạch: `synthesis/search-log`, lượt 2); vì vậy cây này **thiếu góc nhìn 2023–2026** ngoài Saleem 2025, và phạm vi bài của Saleem theo lời tác giả là 2009–2023 ([@saleem2025review], mục 3.2, tr. 17).

## Cây phân nhóm đề xuất

Viết tắt locator: H = Huber 2021 (trang tạp chí); K = Kaselimi 2022 (trang arXiv v1); S = Saleem 2025 (trang bài).

### A. Họ mô hình (trục “dùng gì để tách”)

- **A1. Phương pháp thời kỳ đầu, không DNN:** CO, phân loại SVM/DT, DTW, GSP, HMM và biến thể, phân rã ma trận (K mục III.A, tr. 4); KNN, SVM, DT trong nhóm *Supervised ML* (S mục 2.1.1, tr. 5; Bảng 2, tr. 6). H loại khỏi phạm vi, chỉ nhắc lịch sử dựa trên sự kiện và HMM (H mục 1, tr. 2).
  - Lá đã `reviewed`: `kolter2012approximate` (AFAMAP), `zhong2014signal` (SAC). **[R] cho C3** (suy luận): đây là nơi phần dư/tổng xuất hiện tường minh trong mô hình sinh; SAC ràng buộc tổng năng lượng theo thiết bị, khác C3 (xem [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|C3]]).
- **A2. DNN có giám sát:** DAE, RNN/LSTM/GRU, CNN, seq2point/seq2seq (K mục III.B, tr. 4–5); GAN, transformer, UNet-NILM đa nhiệm (K mục III.C, tr. 5); các khối kiến trúc trong Bảng 2 (H mục 3.4.1, tr. 15–16); nhóm *Supervised DL* (S Bảng 2, tr. 6–7) và các nhóm mô hình cải biên (S Bảng 3, tr. 9–13).
- **A3. Không giám sát / bán giám sát / tự giám sát:** K mục V.A.3, tr. 8; H mục 4.5.1, tr. 23–24 (bán giám sát như hướng xử lý khan hiếm nhãn); S nhóm *Unsupervised* (Bảng 2, tr. 6–7), mục 6.2, tr. 27; Hình 2, tr. 14 (“Advance learning techniques”).
- **A4. Học chuyển giao / thích nghi miền:** appliance transfer và cross-domain transfer, DANN (S mục 2.2.3, tr. 13–14; nhóm *Generative, Representation, Federated, and Transfer Learning* ở Bảng 3, tr. 11–13; Hình 2, tr. 14), DA tổng hợp→thực và source-free DA (S mục 6.5, tr. 28), transfer với transformer (S mục 6.8, tr. 29); kịch bản cross-domain transfer (H mục 3.2.1, tr. 12). **[R] cho độ vững.**
- **A5. Học liên kết, ensemble, lai:** S nhóm *Hybrid Architectures and Ensemble Learning* (Bảng 3, tr. 9–10), mục 6.1, 6.7, tr. 27–28; K mục VI.F, tr. 12 (federated cho riêng tư); H mục 5, tr. 25 (federated như kịch bản tương lai). Ngoài phạm vi trực tiếp.

### B. Lựa chọn thiết kế (trục “thế lưỡng nan” — K mục V.A, tr. 7–10; “bậc tự do” — H Hình 1, tr. 10)

- **B1. Hồi quy / phân loại / đa nhiệm kết hợp:** K mục V.A.1, tr. 6–7; H mục 2.1, tr. 9–10 và mục 3.5, tr. 16–17. **[R]** (suy luận): loss đa nhiệm (hồi quy + cross-entropy) là một nhánh loss.
  - Lá chưa `reviewed`: `shin2019subtask` (SGN, `extracted`); Liu & Fan 2026, MATNilm 2023 (`screened`).
- **B2. Đơn đích / đa đích:** K mục V.A.2, tr. 7–8; H mục 3.5, tr. 17 (ký hiệu đầu ra nhiều thiết bị). **[R] cho C3** (suy luận): C3 chỉ đo được trên tổng nhiều thiết bị.
  - Lá chưa `reviewed`: UNet-NILM (K [49], H [46]); Buddhahai & Makonin 2021 (K [80]); MATNilm; RAPC-Net 2026 (`queued`, nội dung chưa xác minh).
- **B3. Đầu vào/đầu ra cửa sổ:** seq2point / seq2seq / seq2subseq; nhân quả / phi nhân quả; một / nhiều chiều (K mục V.A.4–7, tr. 8–10); hình dạng, đặc trưng đầu vào và đầu ra (H mục 3.3, tr. 14–15; mục 3.5, tr. 16–17). Ít liên quan trực tiếp; là biến kiểm soát của benchmark.
  - Lá đã `reviewed`: `zhang2018sequence` (Seq2Point).
- **B4. Hàm mục tiêu / loss:** chỉ H có mục riêng (H mục 3.4.2, tr. 16); K không có mục loss, chỉ nhắc huấn luyện đối kháng của GAN (K mục III.C, tr. 5); S chỉ khuyến nghị loss cho mất cân bằng (S mục 5.1, tr. 25). **[R] trung tâm.**
  - B4a. MAE/MSE (+ cross-entropy cho bật/tắt) — H mục 3.4.2, tr. 16.
  - B4b. Quantile/pinball — UNet-NILM [46], PB-NILM [59] (H mục 3.4.2, tr. 16); PB-NILM bị loại khỏi danh sách đọc theo quyết định người dùng.
  - B4c. Loss đối kháng (GAN) — H [34, 35, 39, 43], mục 3.4.2, tr. 16; H mục 4.1, tr. 19 xếp GAN vào yếu tố lặp lại ở nhóm kết quả tốt (so sánh khác giao thức).
  - B4d. Loss ghép MSE + KL + soft-margin + MAE — BERT4NILM, H [55], mục 3.4.2, tr. 16.
  - B4e. Focal / có trọng số lớp cho mất cân bằng — S mục 5.1, tr. 25 (chỉ khuyến nghị).
  - **B4f. [L] Loss nhất quán với aggregate / phạt ước lượng quá:** không review nào trong ba review nêu nhánh này. Gần nhất: H mô tả [59] học thêm đích `P_total` và `P_rest` (H mục 3.5, tr. 17) — đó là đa nhiệm, không phải ràng buộc. Lá chưa `reviewed`: Liu & Fan 2026, RAPC-Net 2026.
- **B5. Đầu ra và hậu xử lý:** trung bình/trung vị cửa sổ chồng, lọc kích hoạt ngắn, mạng thứ hai (H mục 3.5.1, tr. 17); clip giá trị **đo** vượt định mức công tơ khi tiền xử lý (H mục 3.2.2, tr. 13). **[R] cho C1/C2** (suy luận): nơi tự nhiên của clip/ReLU; không review nào bàn ràng buộc trên **dự đoán**.
- **B6. Xử lý dữ liệu:** lấy mẫu lại, chuẩn hóa, cân bằng kích hoạt, tăng cường dữ liệu (H mục 3.2.2–3.2.4, tr. 12–14); hai loại mất cân bằng, lấy mẫu lại và dữ liệu thiếu (K mục IV.A, tr. 5–6); nhiễu dữ liệu, gán nhãn, mất cân bằng (S mục 5.1, tr. 25).

### C. Kịch bản đánh giá và độ vững (trục “đánh giá thế nào”)

- **C-a. Observed vs synthetic (noised/denoised):** chỉ H định nghĩa (H mục 3.2.1, tr. 11–12; dữ liệu “dn” ở mục 3.2.4, tr. 14). **[R] cho C3** (suy luận): chỉ kịch bản observed có phần dư tải không đo; trên synthetic C3 gần như chặt.
  - Lá chưa `reviewed`: Klemenjak và cộng sự 2021, real vs denoised (`screened`, đã đọc toàn văn, chưa có ghi chú).
- **C-b. Seen / unseen / cross-domain:** H mục 3.2.1, tr. 11–12 (cross-domain chỉ 5 bài); K mục V.A.3, tr. 8 và mục VI.A, VI.C, tr. 11–12; S mục 3.4.2, tr. 20, mục 5.2, tr. 26, mục 6.5, tr. 28. **[R] cho độ vững.**
  - Lá chưa `reviewed`: D'Incecco 2020 (`screened`; S [125], H [91]); Murray 2019 (K [19]); Liu UDA TII 2022; Chang KDD'23; NILMBench2026; thước đo chuyển giao của Klemenjak (H [145]); Shin 2019 về số hộ (H [75]).
- **C-c. Thước đo:** MAE và F1 là phổ biến nhất (H mục 3.6, tr. 17); đề xuất MAE + F1 tối thiểu và giao thức chuẩn (H mục 4.1, tr. 20); thước đo phân loại vs hồi quy, cấp hộ vs cấp thiết bị (K mục VII.B, tr. 13–14; mục VIII.C, tr. 15–16); F1 dùng nhiều nhất, đề xuất thước đo chuẩn theo nhiệm vụ (S mục 3.4.2, tr. 20; mục 5.2, tr. 26). Không review nào có thước đo vi phạm ràng buộc vật lý.
- **C-d. Khía cạnh tin cậy** (độ tin cậy, mở rộng, vững, giải thích, công bằng, an toàn/riêng tư) — K mục VI, tr. 10–12. Chỉ “độ vững” liên quan trực tiếp.
- **C-e. Nhiễu và thay đổi điều kiện đo:** dữ liệu tổng nhiễu làm giảm hiệu năng (K mục II.B, tr. 3); nhiễu dữ liệu (sai số đo, thiếu, ngoại lai) chưa được nghiên cứu kỹ (S mục 5.1, tr. 25). Về PV: K chỉ nêu sự có mặt tấm PV như một biến đầu vào bổ sung (K mục VIII.A, tr. 15); S nêu một case study tách cả DER như PV và xe điện [185] (S mục 4.1, tr. 23). **[L]** Ảnh hưởng của PV sau công tơ tới ngữ nghĩa công suất tổng và C3 không được review nào bàn; lá chưa `reviewed`: Chen & Ardakanian 2022, DualNILM.

## Bằng chứng đối chiếu

| Nhận định hẹp | Nguồn | Bằng chứng + vị trí | Điều kiện | Mức chắc chắn |
| --- | --- | --- | --- | --- |
| Loss phổ biến nhất là MAE/MSE + cross-entropy | huber2021review | Mục 3.4.2, tr. 16 | DNN tần số thấp đến 11/2020; định tính | Trung bình–cao |
| Theo hiểu biết tác giả, chưa có so sánh loss có hệ thống cho DNN-NILM | huber2021review | Mục 3.4.2, tr. 16; mục 4.4, tr. 22 | Đến 11/2020; K và S không có mục loss nên không xác nhận hay bác bỏ | Cao trong phạm vi Huber |
| Đa số DNN huấn luyện một mô hình cho mỗi thiết bị | huber2021review; kaselimi2022trustworthy | H mục 3.5, tr. 17; K mục V.A.2, tr. 7–8 | Mô tả xu hướng, không đếm | Trung bình–cao |
| Đơn đích có thể ước lượng quá/thiếu tổng | kaselimi2022trustworthy | Mục V.A.2, tr. 8; Hình 3, tr. 7 | Lập luận định tính, dẫn He và cộng sự 2019 (bị loại khỏi danh sách đọc) | Thấp–trung bình |
| Cross-domain hiếm được đánh giá | huber2021review | Mục 3.2.1, tr. 12 | 5 bài trên 99 | Cao trong phạm vi Huber |
| Kết quả công bố khó so sánh vì thiếu chuẩn thước đo/cách báo cáo | huber2021review; kaselimi2022trustworthy; saleem2025review | H mục 4.1, tr. 18–20; K mục VII.B, tr. 13; S mục 5.2, tr. 26 | Lời tác giả, ba review | Trung bình–cao |
| Khái quát sang hộ chưa thấy cần dữ liệu từ nhiều hộ | huber2021review; kaselimi2022trustworthy | H mục 4.5.1, tr. 23 (dẫn [75]); K mục VI.C, tr. 11–12 | Lời tác giả; H dựa trên một nghiên cứu và trình bày của Net2Grid | Trung bình |
| Tải không đo phụ lớn và không Gauss | huber2021review | Mục 2.1, tr. 9 | Lập luận, không số liệu | Trung bình |

> [!example] Cách đọc bảng
> **Điểm chung:** ba review cùng cho rằng khác biệt về thước đo và cách báo cáo khiến kết quả giữa các bài khó so sánh ([@huber2021review], mục 4.1, tr. 18–20; [@kaselimi2022trustworthy], mục VII.B, tr. 13; [@saleem2025review], mục 5.2, tr. 26).
>
> **Bổ sung riêng:** chỉ Huber nêu thiếu so sánh loss có hệ thống ([@huber2021review], mục 3.4.2, tr. 16); chỉ Kaselimi nêu rủi ro ước lượng quá/thiếu tổng của mô hình đơn đích ([@kaselimi2022trustworthy], mục V.A.2, tr. 8).

## Khả năng so sánh

Ba review khác phạm vi: Huber chỉ DNN tần số thấp đến 11/2020 và mô tả chiến lược tìm (H mục 1.3, tr. 9); Kaselimi trải từ 1995 đến 2022, Bảng 1 chỉ gồm 12 bài có giám sát và không mô tả chiến lược tìm; Saleem gồm cả ML cổ điển, phạm vi 2009–2023 theo lời tác giả (S mục 3.2, tr. 17), thiên về F1 và không mô tả chiến lược tìm. Không review nào chạy thí nghiệm; mọi bảng số (H Hình 3–4, K Bảng 3, S Bảng 2–3) là kết quả tự báo cáo, khác giao thức.

## Điểm thống nhất, khác biệt và giới hạn

- **Thống nhất:** kết quả công bố khó so sánh vì thiếu chuẩn thước đo/cách báo cáo (ba review, locator ở bảng trên). Đa số DNN-NILM là mô hình một thiết bị (H mục 3.5, tr. 17; K mục V.A.2, tr. 7–8).
- **Cùng chủ đề nhưng không cùng nhận định (không gọi là đồng thuận):** cả ba nói về khái quát sang hộ/miền mới, nhưng mỗi review nêu khía cạnh khác — K coi đây là thách thức 1 (K mục II.B, tr. 3); H nêu cross-domain hiếm được đánh giá (H mục 3.2.1, tr. 12) và nhu cầu dữ liệu nhiều hộ (H mục 4.5.1, tr. 23); S nêu đánh giá tập trung vào vài hộ và đề xuất transfer/thích nghi miền (S mục 3.4.2, tr. 20; mục 5.2, tr. 26).
- **Khác biệt về cách phân nhóm:** Huber tổ chức theo “bậc tự do” và nói rõ không phải taxonomy (H Hình 1, tr. 10); Kaselimi theo giai đoạn lịch sử + thế lưỡng nan thiết kế (K mục III, V.A); Saleem theo nhóm thuật toán (S Bảng 2–3) và “khái niệm chính” (S Hình 2, tr. 14).
- **Khác biệt về hướng xử lý hộ chưa thấy:** Kaselimi cho rằng phương pháp không giám sát “có thể là lựa chọn tốt hơn” (K mục V.A.3, tr. 8); Saleem đề xuất transfer liên miền và thích nghi miền (S mục 5.2, tr. 26; mục 6.5, tr. 28); Huber nhấn mạnh dữ liệu nhiều hộ và học bán giám sát (H mục 4.5.1, tr. 23–24). Không bên nào có thực nghiệm đối chứng.
- **Khác biệt về mô hình đo:** Huber tách tải không đo phụ khỏi nhiễu đo (H phương trình 1, tr. 9); Kaselimi gộp chung vào nhiễu cộng ε (K phương trình 1, tr. 3); Saleem không nêu phương trình. Điểm này quan trọng cho C3.
- **Giới hạn:** không review nào trong ba review bàn ràng buộc vật lý trên dự đoán (C1–C3) hay thước đo vi phạm (tìm toàn văn từng review, xem ghi chú nguồn). Nhánh B4f và phần PV của C-e chỉ dựng từ bài lá **[L]**.

## Giả thuyết và thí nghiệm đề xuất

**Suy luận / đề xuất:** benchmark cần cố định các nút B3, B5, B6 làm biến kiểm soát và chỉ thay B4; C3 cần báo riêng theo C-a (observed/synthetic) và theo B2 (tổng nhiều mô hình đơn đích hay một mô hình đa đích). Đây là đề xuất, chưa phải giao thức.

## Nhận định có thể dùng và điều kiện

- Có thể dùng (kèm phạm vi): “theo hiểu biết của Huber và cộng sự, tính đến 11/2020 chưa có so sánh loss có hệ thống cho DNN-NILM tần số thấp” ([@huber2021review], mục 3.4.2, tr. 16). Hai review sau không có mục loss nên không cập nhật được nhận định này cho 2021–2026.
- Có thể dùng: ba review đã rà soát không bàn ràng buộc vật lý trên dự đoán — đây là quan sát về ba review, không phải bằng chứng vắng mặt trong toàn lĩnh vực.
- Chưa dùng được: mọi nhận định về đo vi phạm C1–C3 từ bài lá (RAPC-Net, Liu & Fan, MATNilm) — chưa `reviewed`.
- Chưa dùng được: P_max độc lập cho C2 — chưa có nguồn học thuật.

## Việc tiếp theo

- [ ] Rà soát cây phân nhóm này (agent chính / người dùng); hiện `status: draft`.
- [ ] Đọc thêm 1–2 review 2023–2026 để kiểm tra nhánh **[L]** (B4f, PV trong C-e).
- [ ] Đối chiếu Kaselimi 2022 bản Sensors với arXiv v1.
- [ ] Danh sách bài lá ưu tiên đọc nằm trong kế hoạch tổng quan (kế hoạch: `synthesis/literature-review-plan`, mục “Bài lá ưu tiên theo taxonomy”).
