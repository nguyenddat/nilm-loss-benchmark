---
type: paper
status: extracted
title: "Subtask Gated Networks for Non-Intrusive Load Monitoring"
authors: [Changho Shin, Sunghwan Joo, Jaeryun Yim, Hyoseop Lee, Taesup Moon, Wonjong Rhee]
year: 2019
venue: "Proceedings of the AAAI Conference on Artificial Intelligence, 33(01):1150–1157 (AAAI-19)"
doi: "10.1609/aaai.v33i01.33011150"
source_url: "https://arxiv.org/abs/1811.06692"
citation_key: "shin2019subtask"
read_date: 2026-10-30
tags: [nilm, literature, deep-learning, loss, multi-task, on-off, ablation]
---

# Subtask Gated Networks — Shin và cộng sự (2019)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Shin, C., Joo, S., Yim, J., Lee, H., Moon, T., Rhee, W. "Subtask Gated Networks for Non-Intrusive Load Monitoring." Proceedings of the AAAI Conference on Artificial Intelligence 33(01):1150–1157, 2019. DOI `10.1609/aaai.v33i01.33011150` (đối chiếu Crossref 2026-10-30: tiêu đề, sáu tác giả, tập/số/trang).
- Toàn văn / phiên bản: **arXiv:1811.06692v1 [cs.LG], 16/11/2018**, 11 trang PDF: tr. 1–8 bài chính (định dạng AAAI, có dòng bản quyền AAAI 2019 ở tr. 1), tr. 10–11 phụ lục A–C. Bản AAAI chính thức **chưa đối chiếu**; phụ lục có thể không nằm trong bản kỷ yếu.
- Tệp nguồn cục bộ: `papers/Subtask Gated Networks for Non-Intrusive Load Monitoring (arXiv 1811.06692v1).pdf`. Locator theo trang PDF arXiv v1; bài không đánh số mục nên dùng tiêu đề mục.
- Mục tiêu đọc / RQ liên quan: chủ đề 2 (loss tổ hợp hồi quy + phân loại bật/tắt, ablation bỏ thành phần loss), chủ đề 3 (đầu ra có bị ràng buộc không âm không); RQ1, RQ2, RQ3.
- Chất lượng trích xuất: văn bản trích bằng PyMuPDF; phương trình 4–8 (tr. 3), Bảng 2 (tr. 5), Bảng 3 (tr. 6) và bảng phụ lục C (tr. 11) đã đối chiếu trên ảnh render trang. Chưa rà soát độc lập.

## 2. Tóm tắt điều hành

- SGN gồm hai mạng con cùng đầu vào: mạng hồi quy cho công suất `p̂` và mạng phân loại cho xác suất bật `ô`; đầu ra cuối là tích từng phần tử `p̂ ⊙ ô` (phương trình 6, tr. 3).
- Loss huấn luyện: `L = L_output + L_on` với `L_output` là MSE trung bình theo thời gian của đầu ra sau cổng và `L_on` là cross-entropy nhị phân **cộng dồn** (không chia T) của mạng phân loại (phương trình 7a, 7c, 8, tr. 3). Trọng số giữa hai thành phần không được tinh chỉnh (mục “Experiment results”, tr. 5).
- Có một ablation loss có kiểm soát trong cùng kiến trúc và cùng thiết lập: huấn luyện chỉ với `L_output` cho kết quả trung bình kém hơn `L_output + L_on` ở cả 16 cặp (4 biến thể × 2 thước đo × 2 bộ dữ liệu) khi người đọc đối chiếu Bảng 2–3 với bảng phụ lục C (tr. 5–6, 11). Tác giả chỉ viết “generally” (tr. 10).
- Mạng hồi quy không có hàm kích hoạt ở lớp cuối (“None”, phụ lục A, tr. 10), dù phương trình 3 khai báo miền đích `R^s_+` (tr. 3). Suy luận của người đọc: đầu ra `p̂ ⊙ ô` có thể âm; bài không đo hay báo cáo giá trị âm.
- Chia theo hộ như Seq2Point: REDD huấn luyện hộ 2–6, kiểm tra hộ 1; UK-DALE huấn luyện hộ 1, 3–5, kiểm tra hộ 2 (mục “Datasets”, tr. 4).
- Bài không đo vi phạm C1/C2/C3, không báo số lần chạy hay độ biến thiên giữa seed.

## 3. Bài toán, động lực và đóng góp

Tác giả cho rằng các mô hình học sâu NILM trước chưa khai thác tường minh tính chất bật/tắt của thiết bị và đề xuất dùng phân loại bật/tắt làm “cổng” cho hồi quy; khác học đa nhiệm thông thường (chỉ chia sẻ tham số), SGN nhân đầu ra hồi quy với xác suất phân loại và thêm “gating loss” dùng nhãn trạng thái (Tóm tắt, tr. 1; mục “Gating mechanism”, tr. 2). Tác giả nêu SGN giảm lỗi trung bình 15–30% so với state of the art trên REDD và UK-DALE (tr. 1, tr. 5).

Mô hình đo: `x_t = Σ_i y^i_t + u_t + ε_t`, với `u_t` là công suất thiết bị không quan tâm và `ε_t` nhiễu Gauss trung bình 0 (phương trình 1–2, tr. 2). Bài không nêu dấu hay cận cho `u_t`.

## 4. Phương pháp và loss

- **Kiến trúc / đầu vào / đầu ra:** mỗi thiết bị một mô hình; đầu vào cửa sổ `x̃_t` dài `s + 2w`, đầu ra chuỗi dài `s` (seq2seq ngắn). Hai mạng con dùng kiến trúc CNN Seq2Seq của Zhang và cộng sự (2018): 6 lớp conv + 2 lớp fully connected; lớp cuối mạng phân loại dùng sigmoid, lớp cuối mạng hồi quy không có kích hoạt (Hình 3, tr. 5; phụ lục A, tr. 10). REDD: w = 400, s = 64; UK-DALE: w = 200, s = 32 (tr. 5).
- **Nhãn trạng thái:** `o^i_t = 1` nếu `y^i_t > threshold`, ngưỡng 15 W (phương trình 4, tr. 3; tr. 4).
- **Công thức loss (đã đối chiếu ảnh render tr. 3):**

$$
\mathcal{L}^i_{output}=\frac{1}{T}\sum_{t=1}^{T}\left(y^i_t-\hat p^i_t\hat o^i_t\right)^2,\quad
\mathcal{L}^i_{power}=\frac{1}{T}\sum_{t=1}^{T}\left(y^i_t-\hat p^i_t\right)^2,
$$

$$
\mathcal{L}^i_{on}=-\sum_{t=1}^{T}\left(o^i_t\log\hat o^i_t+(1-o^i_t)\log(1-\hat o^i_t)\right),\qquad
\mathcal{L}=\mathcal{L}^i_{output}+\mathcal{L}^i_{on}.
\tag{7a–8}
$$

  `L_power` là loss mà Kelly & Knottenbelt (2015) và Zhang và cộng sự (2018) dùng (theo tác giả, tr. 3); SGN **không** dùng `L_power` trong loss huấn luyện (phương trình 8).
- **Reduction / đơn vị:** `L_output` chia T, `L_on` không chia T (phương trình 7a, 7c). Dữ liệu tổng và thiết bị được chia cho độ lệch chuẩn của công suất tổng trước khi huấn luyện (mục “Data Preprocessing”, tr. 4), nên MSE tính trên thang đã chuẩn hóa. Suy luận của người đọc: tỷ trọng thực của hai thành phần phụ thuộc T và thang chuẩn hóa; “không tinh chỉnh trọng số” không có nghĩa hai thành phần cân bằng.
- **Gradient:** tác giả lưu ý mạng hồi quy chỉ học khi mạng phân loại cho xác suất bật khác 0; nếu mạng phân loại bão hòa ở 0, gradient tới mạng hồi quy bằng 0 (tr. 3–4). Ký hiệu trong hai đạo hàm ở tr. 3 dùng `ŷ` lẫn với `p̂`; chưa rõ là lỗi chính tả hay ký hiệu riêng.
- **Biến thể:** SGN-sp thêm công suất chờ học được `b` (phương trình 9; Bảng 1 công suất chờ trung bình theo thiết bị, tr. 4); Hard SGN dùng cổng 0/1 tại ngưỡng 0,5 (phương trình 10–11, tr. 4), `L_on` vẫn tính trên `ô`.
- **Mất cân bằng bật/tắt:** không có trọng số lớp hay lấy mẫu lại; tác giả xem cổng phân loại là cách lọc giá trị nhiễu nhỏ ở trạng thái tắt (Hình 4, tr. 6).

## 5. Bộ dữ liệu và thiết lập thực nghiệm

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Bộ dữ liệu / phiên bản / thiết bị / hộ | REDD: lò vi sóng, tủ lạnh, máy rửa bát, máy giặt; UK-DALE: thêm ấm đun. UK-DALE dùng “last week data” từ gói tiền xử lý của Kelly (NeuralNILM_data.zip) | “Datasets”, tr. 4; chú thích 1 |
| Tần suất lấy mẫu / tiền xử lý / cửa sổ | REDD tổng 1 s, thiết bị 3 s; tách chuỗi để khoảng thiếu < 20 s, lấp ngược, chỉ giữ chuỗi con > 1 ngày; UK-DALE 6 s, dùng nguyên bản tiền xử lý của Kelly; chia cho độ lệch chuẩn công suất tổng | “Data Preprocessing”, tr. 4 |
| Tập huấn luyện / kiểm tra, rò rỉ | Chia theo hộ (REDD test hộ 1; UK-DALE test hộ 2); tập xác thực: không nêu | tr. 4 |
| Hạt giống / số lần chạy | Không nêu | — |
| Siêu tham số / tìm kiếm | lr 1e-4, batch 16, Adam, He init; không tinh chỉnh kiến trúc/siêu tham số/trọng số loss; số epoch: không nêu | tr. 4–5 |
| Phần cứng | NVIDIA GTX 1080Ti, TensorFlow 1.8 | tr. 4 |

## 6. Mô hình đối chứng, thước đo và kết quả

| Thiết lập / bộ dữ liệu / cách chia | Mô hình đối chứng / loss | Thước đo / định nghĩa / đơn vị / chiều tốt hơn | Kết quả / độ biến thiên | Vị trí nguồn |
| --- | --- | --- | --- | --- |
| REDD, test hộ 1 | FHMM, DAE, Seq2Seq (Zhang) so với SGN và biến thể | MAE (W, thấp hơn tốt hơn); SAE_δ với δ = 1 giờ, chuẩn hóa theo thời gian chứ không theo năng lượng thật | MAE trung bình: Seq2Seq 23,10; SGN 19,09; SGN-sp 18,86. SAE_δ trung bình: Seq2Seq 16,71; SGN 11,97 | Bảng 2, tr. 5 |
| UK-DALE, test hộ 2 | như trên | như trên | MAE trung bình: Seq2Seq 14,55; SGN 11,39; SGN-sp 10,89. SAE_δ: Seq2Seq 9,36; SGN 7,66; Hard SGN-sp 9,73 (kém Seq2Seq, “−3,95%”) | Bảng 3, tr. 6 |
| Ablation loss: chỉ `L_output` | Cùng kiến trúc và thiết lập, bỏ `L_on` | MAE / SAE_δ trung bình | REDD: SGN 24,09 / 20,16; SGN-sp 24,99 / 20,05. UK-DALE: SGN 17,17 / 14,12; SGN-sp 12,64 / 8,81 | Phụ lục C, bảng 1–2, tr. 11 |

Điều kiện: một lần chạy cho mỗi cấu hình (số lần chạy không nêu; không có độ lệch chuẩn giữa lần chạy). “Average” là trung bình không trọng số qua thiết bị. SAE_δ khác SAE của Zhang 2018 (tác giả tự nêu, tr. 5) nên không so trực tiếp với số SAE của Seq2Point.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| Loss huấn luyện SGN là MSE đầu ra sau cổng + BCE trạng thái, trọng số 1:1 danh nghĩa | Phương trình 7a, 7c, 8; BCE không chia T | tr. 3 | Cao (đã đối chiếu ảnh) |
| Bỏ `L_on` làm kết quả trung bình kém hơn | 16/16 giá trị trung bình kém hơn so với Bảng 2–3; một lần chạy, không báo biến thiên | tr. 5–6, 11 | Trung bình: có kiểm soát kiến trúc nhưng không có lặp seed |
| Không có `L_on`, mạng phân loại trở thành hệ số tỉ lệ và mạng hồi quy ước lượng quá ở trạng thái bật | Minh họa định tính một ví dụ tủ lạnh UK-DALE | Hình 6, tr. 7; văn bản tr. 6 | Thấp–trung bình (một ví dụ) |
| Đầu ra hồi quy không bị chặn dưới bởi kiến trúc | Lớp cuối mạng hồi quy “None”; nhưng phương trình 3 ghi miền `R^s_+` | Phụ lục A, tr. 10; tr. 3 | Trung bình: mâu thuẫn ký hiệu/kiến trúc; chưa kiểm tra mã |
| Không tinh chỉnh trọng số loss/siêu tham số | Lời tác giả | tr. 5 | Cao (lời tác giả) |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

SGN và SGN-sp giảm lỗi 15–30% so với state of the art; `L_on` giúp mạng phân loại hoạt động như cổng bật/tắt và cho hiệu năng tốt hơn; SGN hữu ích cho mọi bài toán có trạng thái bật/tắt (Tóm tắt, tr. 1; tr. 3, 5–6; phụ lục C, tr. 10).

### Thí nghiệm thực sự chứng minh gì?

Trên REDD (test hộ 1) và UK-DALE (test hộ 2, một tuần dữ liệu đã tiền xử lý), với một lần chạy mỗi cấu hình và ngân sách không tinh chỉnh, SGN có MAE/SAE_δ trung bình thấp hơn các đối chứng được tác giả tự cài lại; bỏ `L_on` làm trung bình kém hơn trong cùng thiết lập. Không có kiểm định thống kê, không có lặp seed, nên không tách được hiệu ứng loss khỏi phương sai huấn luyện (Bảng 2–3, tr. 5–6; phụ lục C, tr. 11).

### Bài báo chưa giải quyết gì?

- Không so sánh loss hồi quy khác nhau (MAE, Huber, quantile…) cho cùng cổng; ablation chỉ là bật/tắt `L_on`.
- Không có ablation `L_power + L_on` (đa nhiệm không cổng) để tách hiệu ứng của cổng khỏi hiệu ứng của nhãn trạng thái — suy luận của người đọc.
- Không đo C1/C2/C3; không báo tỷ lệ đầu ra âm hay tổng dự đoán vượt công suất tổng.
- Không có tập xác thực/tiêu chí dừng được nêu; ngưỡng 15 W không được phân tích độ nhạy.

## 9. Hạn chế và khả năng tái lập

- Mã nguồn / dữ liệu: bài không dẫn kho mã trong bản arXiv v1; UK-DALE dùng gói NeuralNILM_data.zip của Kelly (URL ở chú thích 1, tr. 4; chưa kiểm tra còn truy cập được).
- Lệnh tái lập: không nêu.
- Rủi ro hợp lệ: một tuần dữ liệu UK-DALE; đối chứng tự cài lại; một lần chạy; reduction lệch giữa hai thành phần loss.
- Đã tự chạy lại chưa? Chưa.

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc (chưa phải kết quả):**

- Có thể dùng trực tiếp: định nghĩa loss có cổng (7a, 7c, 8) là một ứng viên “loss tổ hợp hồi quy + phân loại” có công thức rõ; ablation bỏ `L_on` là ví dụ mẫu cho thiết kế “cùng kiến trúc, đổi loss”.
- Cần điều chỉnh: nếu đưa vào benchmark, phải cố định reduction (chia T hay không) và báo cáo trọng số hiệu dụng; cần lặp nhiều seed; nên tách “cổng kiến trúc” khỏi “nhãn trạng thái trong loss” bằng ablation `L_power + L_on`.
- C1: kiến trúc này không đảm bảo không âm; nếu benchmark đo C1, SGN là trường hợp cần đo tần suất giá trị âm. Cổng xác suất có thể làm giảm biên độ giá trị âm ở trạng thái tắt nhưng không loại bỏ — giả thuyết, chưa kiểm chứng.
- Khoảng trống nghiên cứu: bài cho thấy lựa chọn loss làm thay đổi hành vi theo trạng thái (Hình 6) nhưng không đo nhất quán vật lý.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Đối chiếu bản AAAI chính thức: phụ lục C có trong bản kỷ yếu không; phương trình 7c có chia T không.
- Kiểm tra mã công khai (nếu có) để xác nhận lớp cuối mạng hồi quy tuyến tính.
- Thí nghiệm có thể: cùng kiến trúc SGN, so `L_output + L_on`, `L_output`, `L_power + L_on`, với ≥ 3 seed, đo thêm tỷ lệ đầu ra âm (C1) — đề xuất, chưa chốt.

## 12. Trích dẫn

```bibtex
@inproceedings{shin2019subtask,
    title     = {Subtask Gated Networks for Non-Intrusive Load Monitoring},
    author    = {Shin, Changho and Joo, Sunghwan and Yim, Jaeryun and Lee, Hyoseop and Moon, Taesup and Rhee, Wonjong},
    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
    volume    = {33},
    number    = {01},
    pages     = {1150--1157},
    year      = {2019},
    doi       = {10.1609/aaai.v33i01.33011150},
    note      = {Bản đã đọc: arXiv:1811.06692v1}
}
```
