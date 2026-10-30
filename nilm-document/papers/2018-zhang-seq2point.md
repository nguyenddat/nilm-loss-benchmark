---
type: paper
status: reviewed
title: "Sequence-to-Point Learning With Neural Networks for Non-Intrusive Load Monitoring"
authors: [Chaoyun Zhang, Mingjun Zhong, Zongzuo Wang, Nigel Goddard, Charles Sutton]
year: 2018
venue: "Proceedings of the AAAI Conference on Artificial Intelligence, vol. 32, no. 1 (AAAI-18)"
doi: "10.1609/aaai.v32i1.11873"
source_url: "https://arxiv.org/abs/1612.09106"
citation_key: "zhang2018sequence"
read_date: 2026-10-30
tags: [nilm, literature, deep-learning, seq2point, loss, baseline]
---

# Sequence-to-point — Zhang và cộng sự (2018)

## 1. Thông tin thư mục và nguồn

- Trích dẫn đầy đủ: Zhang, C., Zhong, M., Wang, Z., Goddard, N., Sutton, C. "Sequence-to-Point Learning With Neural Networks for Non-Intrusive Load Monitoring." AAAI 2018, 32(1). DOI `10.1609/aaai.v32i1.11873`. Tác giả, tiêu đề, tập/số khớp `ref.bib` (`zhang2018sequence`). Số trang kỷ yếu: chưa xác minh (không có trên bản arXiv).
- Toàn văn / phiên bản: **arXiv:1612.09106v3 [stat.AP], 18/09/2017**, 8 trang PDF (6 trang nội dung, tr. 7 tài liệu tham khảo, tr. 8 Hình 3). Trang 1 có dòng “Copyright © 2018, Association for the Advancement of Artificial Intelligence”, tức bản định dạng AAAI. Bản AAAI chính thức (ojs.aaai.org) **chưa đối chiếu**: lần thử truy cập 2026-10-30 không tải được trang. Không giả định hai bản giống hệt.
- Tệp nguồn cục bộ: `papers/Sequence-to-point learning with neural networks for non-intrusive load monitoring (arXiv 1612.09106v3).pdf`. Locator theo số trang PDF arXiv v3; bài không đánh số mục nên locator dùng tiêu đề mục.
- Mục tiêu đọc / RQ liên quan: chủ đề 2 (loss của mô hình nơ-ron nền tảng), chủ đề 3 (mô hình đo có phần dư, đầu ra có bị ràng buộc không âm không), chủ đề 5 (đối chứng có giám sát); RQ1, RQ2, RQ3.
- Trạng thái `reviewed` (rà soát 2026-10-30) **theo arXiv v3**: đối chiếu phương trình 1–2, Hình 1, Bảng 1–3 và locator trên PDF (ảnh render trang 3 cho phương trình 2). Đã sửa: τ = t + ⌊W/2⌋ và đệm ⌈W/2⌉; giả định Gauss chỉ được nêu tường minh cho seq2seq; bài không nêu Maximum power dùng ở bước nào; ý nghĩa “±” (đã tính lại); số lần chạy không nêu. Mọi locator và số liệu chỉ có giá trị cho bản arXiv v3 cho tới khi đối chiếu bản AAAI.

## 2. Tóm tắt điều hành

- Seq2point: đầu vào là một cửa sổ công suất tổng, đầu ra là **một điểm** (điểm giữa) công suất thiết bị mục tiêu; mỗi thiết bị một mạng. (Tóm tắt, tr. 1; mục “Sequence-to-point learning”, tr. 2–3.)
- Mô hình đo: `y_t = Σ_{i=1}^I x_it + u_t + ε_t`, với `y_t, x_it ∈ R+` (W), `u_t` là phần thiết bị không quan tâm, ε Gauss trung bình 0, phương sai σ². (Mục “Energy disaggregation”, tr. 2.) Đây là giả định mô hình.
- Hàm mục tiêu: tổng log-likelihood của điểm giữa `L_p = Σ_{t=1}^{T−W+1} log p(x_τ | Y_{t:t+W−1}, θ_p)` (phương trình 2, tr. 3). Bài không gọi tên MSE; dạng phân phối của p cho seq2point không được viết tường minh (xem mục 4).
- Đầu ra mạng là lớp Dense **kích hoạt tuyến tính** (Hình 1, tr. 3) → đầu ra không bị ràng buộc không âm về kiến trúc.
- Bảng 1 có hàng “Maximum power” và “On power threshold” cho từng thiết bị (ví dụ ấm đun 3948 W và 2000 W); bài không nêu nguồn của các giá trị và không nêu chúng được dùng ở bước nào; chỉ “Mean on power” và “Standard deviation on power” được dẫn chiếu khi chuẩn hóa (Bảng 1, tr. 4; mục “Data preprocessing”, tr. 4).
- Chia theo hộ: UK-DALE huấn luyện hộ 1, 3, 4, 5, kiểm tra hộ 2; REDD huấn luyện hộ 2–6, kiểm tra hộ 1. (Mục “Data sets”, tr. 4.)
- Kết quả “Overall” UK-DALE: MAE seq2point 15,472 ± 7,718 W so với seq2seq 17,999 ± 9,063, seq2seq(Kelly) 93,488 ± 91,112, AFHMM 82,79 ± 64,50 (Bảng 2, tr. 5). “Overall” khớp trung bình ± độ lệch chuẩn tổng thể qua các thiết bị (người rà soát tính lại; bài không nói).

## 3. Bài toán, động lực và đóng góp

NILM là tách nguồn mù một kênh, không định danh được; các phương pháp trước đưa tri thức miền vào thủ công (đặc trưng cục bộ như mức công suất, chuyển ON–OFF, thời lượng; hoặc thông tin toàn cục như tổng số chu kỳ, tổng năng lượng). Seq2seq dùng cửa sổ trượt nên mỗi điểm có nhiều dự đoán phải lấy trung bình, làm mượt cạnh. Seq2point dự đoán một điểm duy nhất cho mỗi cửa sổ. (Phần mở đầu, tr. 1–2; mục “Energy disaggregation”, tr. 2.) Đóng góp tác giả nêu: đề xuất seq2point; chứng minh (Định lý 1) seq2point cho xấp xỉ chặt hơn theo KL so với seq2seq khi cùng kiến trúc; thực nghiệm trên UK-DALE và REDD; trực quan hóa đặc trưng mạng học được. (Phần mở đầu, tr. 2; mục “Posterior distribution estimators”, tr. 3–4.)

## 4. Phương pháp và loss

- Kiến trúc / đầu vào / đầu ra: 5 lớp tích chập 1D (bộ lọc kích thước 10, 8, 6, 5, 5; số bộ lọc 30, 30, 40, 50, 50; stride 1; ReLU) + Dense 1024 (ReLU) + Dense đầu ra **tuyến tính** (1 đơn vị cho seq2point, 599 cho seq2seq). Cửa sổ 599 điểm cho mọi thiết bị. (Hình 1, tr. 3; Bảng 1, tr. 4.)
- Công thức loss: seq2seq `L_s = Σ_{t=1}^{T−W+1} log p(X_{t:t+W−1} | Y_{t:t+W−1}, θ_s)` với mô hình `X_{t:t+W−1} = F_s(Y_{t:t+W−1}) + ε`, ε là nhiễu Gauss W chiều (phương trình 1, tr. 2); seq2point `L_p = Σ_{t=1}^{T−W+1} log p(x_τ | Y_{t:t+W−1}, θ_p)`, với `x_τ = F_p(Y_{t:t+W−1}) + ε`, τ = t + ⌊W/2⌋ (phương trình 2, tr. 3). Bài không nói tường minh ε của seq2point là Gauss; trong phần lý thuyết, seq2seq được giả định `p(X|Y,θ) = N(μ(θ), cI)` với c hằng (tr. 3). **Suy luận của người rà soát:** nếu ε của seq2point cũng Gauss phương sai hằng thì cực đại L_p tương đương cực tiểu MSE trên mục tiêu đã chuẩn hóa; bài không nêu bộ tối ưu hay hàm loss trong mã.
- Reduction / trọng số / đơn vị: tổng theo cửa sổ; không có trọng số theo trạng thái; đầu vào và mục tiêu được trừ trung bình, chia độ lệch chuẩn theo tham số trong Bảng 1 (bài không nói rõ mains dùng tham số nào). (Mục “Data preprocessing”, tr. 4.)
- Mất cân bằng / bật-tắt: bài không dùng trọng số hay loss riêng cho trạng thái; “On power threshold” trong Bảng 1 không được giải thích công dụng.
- Biên: đệm ⌈W/2⌉ số 0 ở đầu và cuối chuỗi. (Mục “Sequence-to-point learning”, tr. 3.)
- Mẫu huấn luyện: mọi cửa sổ trượt từng bước cho cả seq2seq và seq2point; seq2seq(Kelly) dùng cửa sổ chọn lọc và dữ liệu tăng cường theo Kelly & Knottenbelt 2015a. (Mục “Architectures”, tr. 3; mục “Experiments”, tr. 4.)

## 5. Bộ dữ liệu và thiết lập thực nghiệm

| Thành phần | Thông tin trong nguồn | Vị trí trích dẫn |
| --- | --- | --- |
| Bộ dữ liệu / phiên bản / thiết bị / hộ | UK-DALE (5 hộ, 6 giây, 11/2012–01/2015): ấm đun, lò vi sóng, tủ lạnh, máy rửa bát, máy giặt. REDD (6 hộ; thiết bị 3 giây, mains 1 giây): lò vi sóng, tủ lạnh, máy rửa bát, máy giặt. Phiên bản dữ liệu không nêu | Mục “Data sets”, tr. 4 |
| Tần suất lấy mẫu / tiền xử lý / cửa sổ | Cửa sổ 599; trượt từng bước; chuẩn hóa bằng tham số Bảng 1; cách căn mains 1 s với thiết bị 3 s ở REDD: không nêu | Mục “Data preprocessing”, tr. 4; Bảng 1, tr. 4 |
| Tập huấn luyện / xác thực / kiểm tra | UK-DALE: train hộ 1, 3, 4, 5, test hộ 2 (vì chỉ hộ 1 và 2 có đủ năm thiết bị); tác giả gọi là thiết lập transfer learning giữa các hộ. REDD: train hộ 2–6, test hộ 1. Tập xác thực, khoảng thời gian dùng: không nêu | Mục “Data sets”, tr. 4 |
| Hạt giống ngẫu nhiên / số lần chạy | Không nêu | — |
| Siêu tham số / tìm kiếm / ngân sách | Bộ tối ưu, tốc độ học, batch, số epoch, dừng sớm: không nêu trong arXiv v3 | — |
| Phần cứng / thời gian chạy | Python, TensorFlow; GPU NVIDIA GTX 970 và GTX TITAN X; thời gian không nêu | Mục “Experiments”, tr. 4 |

## 6. Mô hình đối chứng, thước đo và kết quả

Thước đo (mục “Performance evaluation”, tr. 5):

- MAE = `(1/T) Σ_t |x̂_t − x_t|`, W, thấp hơn tốt hơn.
- SAE = `|r̂ − r| / r`, với `r = Σ_t x_t`, `r̂ = Σ_t x̂_t` là tổng năng lượng thật/dự đoán của **một thiết bị** trên một khoảng (tác giả nêu “in this case, one day”). Khác SAE của Zhong et al. 2014 (chuẩn hóa theo tổng công suất tổng).

| Thiết lập / bộ dữ liệu / cách chia | Mô hình đối chứng / loss | Thước đo / định nghĩa / đơn vị / chiều tốt hơn | Kết quả Overall | Vị trí nguồn |
| --- | --- | --- | --- | --- |
| UK-DALE, test hộ 2, 5 thiết bị | AFHMM; seq2seq(Kelly); seq2seq; seq2point | MAE (W) | 82,79 ± 64,50; 93,488 ± 91,112; 17,999 ± 9,063; 15,472 ± 7,718 | Bảng 2, tr. 5 |
| Như trên | Như trên | SAE | 3,17 ± 2,88; 4,001 ± 5,124; 0,423 ± 0,194; 0,321 ± 0,217 | Bảng 2, tr. 5 |
| REDD, test hộ 1, 4 thiết bị | seq2seq; seq2point | MAE (W) | 26,552 ± 5,610; 23,693 ± 4,494 | Bảng 3, tr. 5 |
| Như trên | Như trên | SAE | 0,355 ± 0,183; 0,270 ± 0,187 | Bảng 3, tr. 5 |

Theo thiết bị, seq2point UK-DALE có MAE (W): ấm đun 7,439; lò vi sóng 8,661; tủ lạnh 20,894; máy rửa bát 27,704; máy giặt 12,663 (Bảng 2, tr. 5).

Ý nghĩa của “±”: bài không định nghĩa. **Kiểm tra số học của người rà soát:** với các hàng đã thử (MAE seq2point/seq2seq/seq2seq(Kelly)/AFHMM UK-DALE, SAE seq2point UK-DALE, MAE seq2point và SAE seq2seq REDD), “Overall” trùng trung bình và độ lệch chuẩn tổng thể (chia n) của các giá trị theo thiết bị, sai khác ở chữ số làm tròn cuối. Vì vậy “±” là độ phân tán **giữa các thiết bị**, không phải độ bất định qua seed.

Tác giả báo seq2point giảm MAE 84% và SAE 92% so với seq2seq(Kelly) trên UK-DALE; seq2seq của bài giảm 81% và 89%; trên REDD seq2point cải thiện MAE 11% và SAE 24% so với seq2seq (mục “Experimental results”, tr. 5). Phần mở đầu nêu “as much as 83% reduction in error” (tr. 2). Tác giả viết seq2point tốt hơn seq2seq “in three out of four appliances” trên UK-DALE (tr. 5), trong khi Bảng 2 có năm thiết bị và MAE seq2point thấp hơn ở 4/5 (cao hơn ở máy giặt), SAE thấp hơn ở 4/5 (cao hơn ở lò vi sóng) — câu này không khớp trực tiếp với bảng. Seq2seq(Kelly) dùng cách lấy mẫu huấn luyện và kiến trúc khác (tr. 4), nên so sánh 84%/92% gộp cả khác biệt kiến trúc và dữ liệu huấn luyện. So sánh seq2seq và seq2point của chính bài dùng cùng kiến trúc và cùng mẫu huấn luyện. Các loss **không** được thay đổi giữa các mô hình.

## 7. Bảng bằng chứng

| Nhận định | Bằng chứng / điều kiện | Vị trí nguồn | Mức chắc chắn |
| --- | --- | --- | --- |
| Mô hình đo gồm phần thiết bị không quan tâm `u_t` và nhiễu | `y_t = Σ x_it + u_t + ε_t` | Mục “Energy disaggregation”, tr. 2 | Giả định của tác giả; cao |
| Mục tiêu huấn luyện là log-likelihood của điểm giữa | Phương trình 2 | Mục “Sequence-to-point learning”, tr. 3 | Cao (văn bản); dạng Gauss/tương đương MSE là suy luận của người đọc |
| Đầu ra không bị ràng buộc không âm bởi kiến trúc | Dense đầu ra kích hoạt tuyến tính | Hình 1, tr. 3 | Cao |
| Có giá trị “Maximum power” theo thiết bị nhưng không nêu nguồn và công dụng | Bảng 1 | tr. 4 | Cao về sự tồn tại; nguồn gốc và công dụng không nêu |
| Seq2point tốt hơn seq2seq cùng kiến trúc trên MAE/SAE Overall | UK-DALE hộ 2; REDD hộ 1; số lần chạy và seed không nêu | Bảng 2–3, tr. 5 | Quan sát trong giao thức này; không có độ bất định qua seed |
| Seq2point xấp xỉ posterior điểm giữa chặt hơn seq2seq | Định lý 1 (theo KL), giả định cùng kiến trúc và hàm φ_w như nhau | Mục “Posterior distribution estimators”, tr. 4 | Kết quả lý thuyết dưới giả định của tác giả |

## 8. Phân biệt kết luận

### Tác giả tuyên bố gì?

Seq2point đạt hiệu năng state-of-the-art, cải thiện hai thước đo 84% và 92%, và CNN tự học đặc trưng thiết bị (điểm thay đổi, mức công suất, thời lượng). (Tóm tắt, tr. 1; mục “Visualization of latent features”, tr. 5–6; mục “Conclusions”, tr. 6; Hình 3, tr. 8.)

### Thí nghiệm thực sự chứng minh gì?

Với một hộ kiểm tra mỗi bộ dữ liệu và cùng một hàm mục tiêu log-likelihood, seq2point có MAE/SAE Overall thấp hơn seq2seq cùng kiến trúc (Bảng 2–3, tr. 5). Không nêu số lần chạy, không có kiểm định thống kê, không có ablation loss. Phần trực quan hóa chỉ xét ấm đun với các cửa sổ được chỉnh tay (Hình 3, tr. 8).

### Bài báo chưa giải quyết gì?

- Không so sánh loss; không có thành phần tái tạo công suất tổng hay ràng buộc vật lý trong mục tiêu.
- Không báo tần suất đầu ra âm hoặc vượt công suất tổng, dù đầu ra tuyến tính cho phép điều đó (suy luận của người đọc).
- Không nêu siêu tham số tối ưu và tập xác thực trong arXiv v3.

## 9. Hạn chế và khả năng tái lập

- Mã nguồn / dữ liệu / giấy phép / phiên bản hoặc mã commit: arXiv v3 không nêu kho mã; triển khai trong NILMTK-contrib (Batra et al. 2019) là nguồn cần kiểm tra riêng.
- Lệnh tái lập do tác giả cung cấp: không nêu.
- Chi tiết còn thiếu / nguy cơ ảnh hưởng tính hợp lệ: bộ tối ưu, tốc độ học, epoch, tập xác thực, khoảng thời gian dữ liệu, cách căn REDD 1 s/3 s, tham số chuẩn hóa mains, nguồn và công dụng của “Maximum power”/“On power threshold”.
- Đã tự chạy lại chưa? Chưa.

## 10. Liên hệ với bộ đánh giá so sánh hàm mất mát NILM

**Suy luận / đề xuất của người đọc:**

- Có thể dùng trực tiếp: seq2point là kiến trúc có giám sát được dẫn nhiều, dùng làm khung cố định khi thay loss; mục tiêu gốc là log-likelihood (thường hiểu là Gauss, tương đương MSE trên mục tiêu chuẩn hóa — chưa xác minh từ mã) — điểm tham chiếu cho RQ1/RQ2.
- Cần điều chỉnh: vì đầu ra tuyến tính, C1 (không âm) có thể bị vi phạm khi đánh giá; nếu dự án thêm ReLU/softplus/kẹp đầu ra thì đó là thay đổi kiến trúc/hậu xử lý, cần tách khỏi so sánh loss.
- Cần điều chỉnh: không dùng “Maximum power” của Bảng 1 làm `P_i^max` cho C2 khi chưa biết nguồn (có thể là cực đại quan sát trong dữ liệu — chưa xác minh).
- Cần điều chỉnh: báo cáo SAE phải nêu định nghĩa; SAE của bài này khác Zhong et al. 2014. Khi báo “Overall ± ”, nêu rõ là phân tán qua thiết bị hay qua seed.
- Khoảng trống nghiên cứu: không có bằng chứng về ảnh hưởng của loss lên vi phạm C1–C3.

## 11. Câu hỏi đọc lại và thí nghiệm tiếp theo

- Đối chiếu bản AAAI chính thức với arXiv v3 (số trang kỷ yếu, bảng, thước đo, siêu tham số).
- Tìm nguồn của “Maximum power”, “On power threshold” (có thể theo Kelly & Knottenbelt 2015a — chưa xác minh).
- Câu hỏi thí nghiệm (đề xuất): trên seq2point với đầu ra tuyến tính, tỷ lệ mẫu âm và tỷ lệ mẫu vượt công suất tổng thay đổi thế nào khi đổi MSE sang MAE/Huber hoặc thêm thành phần tái tạo tổng?

## 12. Trích dẫn

Khóa BibTeX `zhang2018sequence` trong `ref.bib`. Zhang, C., Zhong, M., Wang, Z., Goddard, N., & Sutton, C. (2018). Sequence-to-Point Learning With Neural Networks for Non-Intrusive Load Monitoring. *Proceedings of the AAAI Conference on Artificial Intelligence*, 32(1). https://doi.org/10.1609/aaai.v32i1.11873 (nội dung đã đọc: arXiv:1612.09106v3).
