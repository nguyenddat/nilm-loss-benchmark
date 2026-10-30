---
type: paper
status: reviewed
title: "A comprehensive review of machine learning and deep learning models for non-intrusive load monitoring: performance, analyses, practical insights, and emerging trends"
authors: [Muhammad Hammad Saleem, Muhammad Taha, Muhammad Asif Ali Rehmani, Shafiqur Rahman Tito, Snjezana Soltic, Pieter Nieuwoudt, Neel Pandey, Mollah Daud Ahmed]
year: 2025
venue: "Applied Intelligence 55(15):1020"
doi: "10.1007/s10489-025-06921-4"
source_url: "https://doi.org/10.1007/s10489-025-06921-4"
citation_key: "saleem2025review"
read_date: 2026-10-30
tags: [nilm, literature, review, machine-learning, transfer-learning, research-gaps]
---

# Review ML/DL cho NILM — Saleem và cộng sự (2025)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Saleem, M. H., Taha, M., Rehmani, M. A. A., Tito, S. R., Soltic, S., Nieuwoudt, P., Pandey, N., Ahmed, M. D. "A comprehensive review of machine learning and deep learning models for non-intrusive load monitoring: performance, analyses, practical insights, and emerging trends." Applied Intelligence 55(15):1020 (2025). DOI `10.1007/s10489-025-06921-4`. Crossref (kiểm lại 2026-10-30) liệt kê đủ 8 tác giả theo thứ tự trên, tập 55, số 15, bài 1020, bản in 10/2025 — khớp trang 1 PDF. OpenAlex: hybrid OA. `ref.bib` đã bổ sung `number = {15}`.
- Toàn văn: PDF Springer **36 trang** (“Page x of 36”), gồm cả danh mục tham khảo (tr. 30–36); trang 1 ghi Received 3/4/2024, Accepted 6/9/2025, Published online 13/10/2025, “© The Author(s) 2025”.
- Tệp nguồn cục bộ: `papers/A comprehensive review of ML and DL models for NILM (Applied Intelligence 2025).pdf`. Locator theo số trang bài, trùng số trang PDF.
- Mục tiêu đọc: lượt top-down — xu hướng, khoảng trống gần đây, nhánh transfer/thích nghi miền; RQ1, RQ2, RQ4.
- Phạm vi đọc (sau rà soát): toàn văn phần lời mục 1–7 (tr. 1–29). Bảng 1 (tr. 4) đã đọc; Bảng 2 (tr. 6–7) và Bảng 3 (tr. 9–13) đã đọc cột “Categories” và một số dòng, **chưa trích từng dòng**; Hình 2 (tr. 14) xem trên ảnh render; Hình 3–7 (tr. 16–23) và Bảng 4 (tr. 20) không trích giá trị.
- Rà soát (2026-10-30): đối chiếu mọi nhận định và locator với PDF; tìm toàn văn phần thân bài (tr. 1–29) các từ khóa loss, objective, constraint, negative, physical, conservation, aggregate, search, Scopus, PRISMA, inclusion, criteria. Sửa: số trang PDF (47 → 36); câu về Crossref (Crossref có đủ 8 tác giả); cấu trúc bảng mục 2 (Bảng 2 và Bảng 3 có nhóm “Categories” khác nhau, xem mục 2); vị trí Hình 6 (tr. 21); bổ sung phạm vi năm 2009–2023 (tr. 17).

## 2. Tóm tắt điều hành

- Review xoay quanh 5 câu hỏi: vấn đề NILM nào đã được ML/DL giải quyết và với F1/thời gian tính toán ra sao; mô hình nào được khám phá nhiều nhất và F1 trên các bộ dữ liệu; khả năng giải thích; yêu cầu thực tế; thách thức (Tóm tắt, tr. 1; mục 1.2, tr. 3–4).
- Phạm vi thời gian theo lời tác giả: “several prominent research from 2009 to 2023” (mục 3.2, tr. 17); mục 6 dẫn thêm một số bài 2024–2025 (ví dụ [130], [131], [212], [213]).
- Phân nhóm của review: Bảng 2 “mô hình nổi tiếng” chia *Supervised ML*, *Supervised DL*, *Unsupervised* (mục 2.1, tr. 5–8; Bảng 2, tr. 6–7); Bảng 3 “mô hình mới/cải biên” chia *Hybrid Architectures and Ensemble Learning*; *Temporal and attention-based models*; *Generative, Representation, Federated, and Transfer Learning*; *Fundamental Models-based Modified Versions* (mục 2.2.1–2.2.4, tr. 8–15; Bảng 3, tr. 9–13). Hình 2 tóm tắt sáu “khái niệm chính để đề xuất mô hình mới/cải biên”: ensemble; tăng cường dữ liệu (GAN, mô phỏng đa tác tử); transfer learning (thiết bị & liên miền; thích nghi miền sâu); kỹ thuật học nâng cao (liên kết; có/bán/không giám sát); trích tín hiệu thời gian (LSTM, autoencoder, TCN); **độ vững và khái quát** (DANN, mô hình attention) (Hình 2, tr. 14).
- Thước đo chủ đạo của review là **F1**; tác giả quan sát F1 là thước đo dùng nhiều nhất, rồi đến accuracy và MAE (mục 3.4.2, tr. 20). Tác giả nêu sự không nhất quán thước đo (MAE, F1, accuracy) làm khó so sánh, đề xuất thước đo chuẩn theo nhiệm vụ (nhận diện sự kiện, phân loại tải, ước lượng năng lượng) và thước đo chuẩn cho bộ nhớ/tính toán (mục 5.2, tr. 26).
- Khoảng trống về dữ liệu: thiếu nghiên cứu kỹ nhiễu trong dữ liệu NILM (sai số đo, thiếu, ngoại lai); mất cân bằng giữa thiết bị — **đề xuất** GAN/SMOTE hoặc focal loss / loss có trọng số lớp (mục 5.1, tr. 25). Đây là khuyến nghị, không có bằng chứng thực nghiệm kèm theo.
- Khoảng trống về đánh giá: REDD hộ 1 rồi UK-DALE hộ 2 là các tập được khám phá nhiều nhất → “khoảng trống lớn” về kiểm chứng trên hộ khác và bộ dữ liệu khác (mục 3.4.2, tr. 20; Hình 6, tr. 21).
- Khoảng trống về mô hình: độ chính xác thấp khi đổi môi trường/thiết bị → đề xuất transfer liên miền và thích nghi miền (huấn luyện đối kháng, attention) (mục 5.2, tr. 26). Mục 6.5 nêu hai ví dụ thích nghi miền gần đây: tổng hợp→thực dựa trên tái tạo đặc trưng [212] và thích nghi miền không cần nguồn dựa trên che–phục hồi chuỗi [213] (tr. 28).
- Không có mục về **ràng buộc vật lý** hay **so sánh loss có kiểm soát**; không mô tả chiến lược tìm kiếm/tiêu chí chọn bài (tìm toàn văn tr. 1–29 không ra kết quả liên quan). “Loss” chỉ xuất hiện ở ba chỗ: một bài U-Net/GAN “tránh hàm loss” (tr. 7), “performance (accuracy or loss)” (tr. 17), khuyến nghị focal/class-weighted (tr. 25).

## 3. Bài toán, động lực và đóng góp

Tác giả nêu các review trước chưa trả lời đầy đủ 5 câu hỏi trên (mục 1.2, tr. 3) và tóm tắt 10 review trước trong Bảng 1 (mục 1.1, tr. 2–3; Bảng 1, tr. 4), trong đó có Huber 2021 ([36] trong bài; Bảng 1 ghi phát hiện: nên so sánh các cách tiếp cận, đặc trưng ngoài P và đa nhiệm có lợi) và Kaselimi 2022 ([42] trong bài; mô tả theo các giai đoạn và các cặp lựa chọn phân loại/hồi quy, có/không giám sát, tích chập/hồi quy, nhân quả/phi nhân quả, seq2seq/seq2point, tr. 3).

## 4. Phương pháp và loss (nội dung được review tổng hợp)

- Loss chỉ xuất hiện dưới dạng khuyến nghị (focal / class-weighted) cho mất cân bằng (mục 5.1, tr. 25). Không có tổng hợp loss hồi quy.
- Transfer learning: [125] D'Incecco và cộng sự (IEEE TSG 11(2), Saleem ghi năm 2019) đề xuất *appliance transfer* và *cross-domain transfer* cho seq2point; [126] DANN để tăng khái quát; [130] transformer + transfer learning cải thiện MAE và “normalized signal aggregate error” (mục 2.2.3, tr. 13–14; mục 6.8, tr. 29).

## 5. Bộ dữ liệu và thiết lập (mức review)

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Bộ dữ liệu | REDD, UK-DALE, REFIT, WHITED, Wikienergy, PLAID, BLUED, AMPds… là các bộ nổi bật; Bảng 4 nêu ứng dụng, hạn chế, đặc điểm | Mục 3.4.1–3.4.2, tr. 20; Bảng 4, tr. 20 |
| Phân tích theo bộ dữ liệu | Hình 6: mô hình có F1 cao nhất theo bộ/hộ (giá trị chưa trích) | Mục 3.4.2, tr. 20–21; Hình 6, tr. 21 |
| Thước đo dùng để so sánh | F1 và thời gian suy luận/tính toán | Mục 1.2, tr. 3–4; mục 3.3, tr. 19; Bảng 2–3 |

## 6. Mô hình đối chứng, thước đo và kết quả

Không có thí nghiệm. F1 trong Bảng 2–3 là số tự báo cáo, khác dữ liệu/giao thức (ví dụ SVM + k-means trên REDD hộ 1/2/6: F1 0,803 / 0,8555 / 0,8068, Bảng 2, tr. 6) — không so sánh trực tiếp.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| Thước đo NILM không nhất quán, cản trở so sánh | Lời tác giả | Mục 5.2, tr. 26 | Trung bình (lời tác giả) |
| Đánh giá tập trung vào vài hộ (REDD hộ 1, UK-DALE hộ 2); thiếu kiểm chứng trên hộ/bộ khác | Lời tác giả, dựa trên Hình 6 | Mục 3.4.2, tr. 20 | Trung bình |
| Nhiễu dữ liệu NILM chưa được nghiên cứu kỹ | Lời tác giả | Mục 5.1, tr. 25 | Trung bình |
| Focal / class-weighted loss là hướng xử lý mất cân bằng | **Khuyến nghị**, không có thực nghiệm | Mục 5.1, tr. 25 | Thấp (đề xuất) |
| Hiệu năng giảm khi đổi môi trường/thiết bị | Lời tác giả | Mục 5.2, tr. 26; mục 6.5, tr. 28 | Trung bình (thứ cấp) |
| Không bàn ràng buộc vật lý, không phân tích loss hồi quy, không nêu chiến lược tìm | Tìm toàn văn tr. 1–29 | Toàn bài | Cao (vắng mặt trong review này) |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

ML/DL đạt độ chính xác cao trong NILM; CNN được dùng nhiều nhất và “là tương lai” của NILM tự động (mục 3.2, tr. 19); thách thức còn lại ở dữ liệu (nhiễu, nhãn, mất cân bằng, thiếu chuẩn), mô hình (khái quát, giải thích, siêu tham số) và triển khai (tính toán, riêng tư, mở rộng) (mục 5, tr. 25–26).

### Thí nghiệm thực sự chứng minh gì?

Không có thí nghiệm. Các so sánh F1 là tự báo cáo.

### Bài báo chưa giải quyết gì?

- Không mô tả quy trình tìm/chọn bài → không đánh giá được độ bao phủ.
- Không đề cập ràng buộc vật lý, không phân tích loss hồi quy.
- Thiên về F1 nên ít thông tin về sai số công suất.

## 9. Hạn chế và khả năng tái lập

Không áp dụng. Các dòng của Bảng 2–3 và giá trị Hình 3–7 chưa trích; nhận định ở ghi chú này chỉ dựa trên phần lời và cấu trúc bảng.

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc:**

- Review 2025 vẫn **không** đưa ra bằng chứng so sánh loss có kiểm soát hay đo vi phạm vật lý → không mâu thuẫn với khoảng trống Huber 2021 nêu (đến 11/2020), nhưng chỉ là “không thấy trong review này”, không phải bằng chứng vắng mặt trong toàn lĩnh vực.
- Nhánh “độ vững và khái quát” (Hình 2) và mục 6.5 cung cấp danh sách lá cho chủ đề 4 (DANN [126], DA tổng hợp→thực [212], source-free DA [213]).
- Focal/class-weighted loss nên được xem là **ứng viên** loss cho mất cân bằng; cần nguồn lá có thực nghiệm trước khi đưa vào benchmark.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Trích dòng Bảng 2–3 và Hình 3–6 nếu cần thống kê xu hướng mô hình theo năm/bộ dữ liệu.
- Tra [212] Hao và cộng sự 2024 (IEEE TIM, DA tổng hợp→thực), [213] Zhong và cộng sự 2024 (IEEE TIM, source-free DA), [197] Yin và cộng sự 2024 (UDA, IEEE TII), các bài transfer [126], [130], [131], [133].

## 12. Trích dẫn

```bibtex
@article{saleem2025review,
    title   = {A comprehensive review of machine learning and deep learning models for non-intrusive load monitoring: performance, analyses, practical insights, and emerging trends},
    author  = {Saleem, Muhammad Hammad and Taha, Muhammad and Rehmani, Muhammad Asif Ali and Tito, Shafiqur Rahman and Soltic, Snjezana and Nieuwoudt, Pieter and Pandey, Neel and Ahmed, Mollah Daud},
    journal = {Applied Intelligence},
    volume  = {55},
    number  = {15},
    pages   = {1020},
    year    = {2025},
    doi     = {10.1007/s10489-025-06921-4}
}
```
