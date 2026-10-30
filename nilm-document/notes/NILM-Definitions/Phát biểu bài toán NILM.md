---
type: concept
title: "Phát biểu bài toán NILM"
aliases: [Bài toán phân rã tải không xâm lấn, Phần dư phép đo tổng hợp, Nhiễu và tải chưa đo trong NILM, Hàm mất mát và thước đo đánh giá, Khả năng so sánh trong nghiên cứu NILM, Tính so sánh NILM]
tags: [nilm, concept, definition, measurement, loss, metric, comparability]
evidence_status: extracted
---

## Định nghĩa hoặc phát biểu chính

**Phát biểu chung:** Non-Intrusive Load Monitoring (NILM) ước lượng công suất của từng thiết bị từ phép đo công suất tổng của một hộ hoặc tòa nhà. (Batra và cộng sự, mục 2.5, PDF tr. 4; Klemenjak và cộng sự, mục II, PDF tr. 1; [@NILMTK]; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].) Batra nêu thêm rằng nhiều thuật toán biểu diễn thiết bị bằng trạng thái rời rạc như tắt, bật hoặc trung gian. (Mục 2.5, PDF tr. 4; [@NILMTK].)

Xét $n$ thiết bị tại $T$ thời điểm, $i=1,\ldots,n$, $t=1,\ldots,T$:
- $P_t$: công suất tổng đo được tại thời điểm $t$.
- $p_{i,t}$: công suất thật của thiết bị $i$ tại $t$, có được khi thiết bị có kênh đo riêng.
- $y_{i,t}$: công suất dự đoán của thiết bị $i$ tại $t$.
- $r_t$: phần dư phép đo tổng hợp.

Đầu vào là chuỗi công suất tổng $\mathbf P=[P_1,\ldots,P_T]^\top\in\mathbb R^T$. 
Đầu ra là ma trận dự đoán $Y=[y_{i,t}]\in\mathbb R^{n\times T}$. 

Ký hiệu đầu ra trên $\mathbb R$, không ràng buộc dấu, là lựa chọn có chủ ý của dự án: tính không âm là đại lượng cần đo khi đánh giá ([[notes/NILM-Evaluation/Ràng buộc C1 - không âm|C1]]), không phải giả định của định nghĩa. Lựa chọn này là quy ước dự án, không do nguồn nào quy định.

**Bảng đối chiếu ký hiệu.** Các nguồn dùng cùng chữ cho đại lượng khác nhau; khi trích công thức, đổi về ký hiệu dự án.

| Đại lượng | Dự án | Batra 2014 | Klemenjak 2020 | Seq2Point 2018 |
| --- | --- | --- | --- | --- |
| Công suất tổng | $P_t$ | $\bar y_t$ | $y_t$ | $y_t$ |
| Công suất thật thiết bị | $p_{i,t}$ | $y_t^{(n)}$ | $x_t^{(i)}$ | $x_{it}$ |
| Công suất dự đoán | $y_{i,t}$ | $\hat y_t^{(n)}$ | chưa xác minh | $\hat x_t$ (mỗi thiết bị một mô hình) |
| Phần dư | $r_t$ | không nêu | $\epsilon_t$ | $u_t+\epsilon_t$ |

Nguồn ký hiệu: Batra, mục 2.5, PDF tr. 4 [@NILMTK]; Klemenjak, mục II, phương trình 1, PDF tr. 1 [@klemenjak2020comparabilitynonintrusiveloadmonitoring]; Zhang và cộng sự, mục "Energy disaggregation", arXiv v3 tr. 2 [@zhang2018sequence].

## Phạm vi và điều kiện
### Phần dư phép đo tổng hợp
Viết theo ký hiệu dự án, Klemenjak biểu diễn phép đo tổng là:

$$
P_t=\sum_{i=1}^{n}p_{i,t}+r_t
$$

Phần dư $r_t$ là chênh lệch giữa công suất tổng đo được và tổng tín hiệu các thiết bị có kênh đo:
- Tác giả nêu phần dư gồm nhiễu đo và tải không được đo, không đặt cận hay dấu cố định cho nó. (Mục II, phương trình 1, PDF tr. 1; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].) 
- Seq2Point tách phần dư thành phần thiết bị không quan tâm $u_t$ và nhiễu Gauss trung bình 0, đồng thời giả định công suất tổng và công suất thiết bị thuộc $\mathbb R^+$; đây là giả định mô hình của tác giả. (Mục "Energy disaggregation", arXiv v3 tr. 2; [@zhang2018sequence].)
- Huber và cộng sự cũng tách phần dư thành tải không đo phụ và nhiễu thiết bị đo; theo tác giả, nhiễu đo nhỏ và xấp xỉ phân phối chuẩn, còn tải không đo phụ thường chiếm phần lớn công suất tổng và có phân phối không Gauss — đây là lập luận, không kèm số liệu. (Mục 2.1, phương trình 1, tr. 9; [@huber2021review].) Ngược lại, Kaselimi và cộng sự gộp mọi phần còn lại vào một nhiễu cộng $\epsilon(t)$. (Mục II.A, phương trình 1, arXiv v1 tr. 3; [@kaselimi2022trustworthy].)
- Huber và cộng sự gọi kịch bản có phần tải không đo phụ bằng 0 (công suất tổng tạo bằng cách cộng các kênh thiết bị) là *synthetic* (= denoised), và kịch bản dùng công suất tổng đo thật là *observed* (= noised). (Mục 3.2.1, tr. 11–12; [@huber2021review].) Hệ quả cho [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|C3]] được ghi trong ghi chú đó.

Nguồn không đặt dấu cho $r_t$, không thể suy ra tổng công suất thiết bị dự đoán luôn nhỏ hơn công suất tổng nếu chưa xác định ngữ nghĩa, chiều công suất và điều kiện căn chỉnh dữ liệu. Sai số căn chỉnh thời gian giữa các luồng đo cũng có thể góp vào $r_t$; điều này suy từ mô tả độ lệch thời điểm giữa IAM và công suất tổng trong REFIT, IAM có thể cũ hơn thời điểm ghi công suất tổng đến 7 giây (mục Individual appliance monitors, PDF tr. 5; [@murray2017refit]), không phải lời của Klemenjak. Đây là hệ quả cho cách diễn giải [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|C3]], không phải kết quả kiểm định mô hình.

### Hàm mất mát và thước đo đánh giá
**Định nghĩa:** hàm mất mát là đại lượng tối ưu trong huấn luyện; thước đo đánh giá là đại lượng dùng báo chất lượng dự đoán. 

**Nhóm loss ứng viên (đề xuất, chưa phải kết luận):** đề xuất nghiên cứu liệt kê MSE và MAE ở cấp thiết bị, loss tái tạo công suất tổng, chính quy hóa L1/L2, total variation theo thời gian và một số tổ hợp; MAE, RMSE, SAE và F1 sự kiện là các thước đo dự kiến. (Đề xuất nghiên cứu, mục 3.1 và 3.3; kế hoạch: `synthesis/research-proposal`.) Vai trò của từng thành phần, chẳng hạn L1 có làm nghiệm thưa hay không, chưa được nguồn đã rà soát nào xác nhận trong bối cảnh NILM; danh sách sẽ được điều chỉnh theo tổng quan tài liệu.

**Điều hai bài nguồn cùng không khảo sát:** NILMTK và Klemenjak đều không so sánh loss huấn luyện hoặc làm ablation loss. (Batra và cộng sự, mục 3.5–3.7, PDF tr. 5–7, và mục 4.4–4.5, PDF tr. 9–10; Klemenjak và cộng sự, toàn bài, PDF tr. 1–5; [@NILMTK]; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].) RMSE trong nghiên cứu trường hợp của Klemenjak là thước đo đánh giá, không phải bằng chứng loss huấn luyện nào tốt hơn. (Mục IV.C, PDF tr. 4–5; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

**Loss trong tài liệu DNN-NILM (theo một review):** Huber và cộng sự viết rằng đa số công trình DNN-NILM tần số thấp dùng MAE hoặc MSE cho ước lượng công suất và cross-entropy cho bật/tắt; một số dùng quantile regression, loss GAN hoặc loss ghép nhiều thành phần; và “theo hiểu biết của tác giả” chưa có so sánh có hệ thống các loss cho DNN-NILM. Phạm vi: tài liệu DNN-NILM tần số thấp đến cuối 11/2020. (Mục 1.3, tr. 9; mục 3.4.2, tr. 16; [@huber2021review].) Kaselimi và cộng sự (2022) và Saleem và cộng sự (2025) không có mục tổng hợp loss hồi quy; Saleem chỉ khuyến nghị focal loss hoặc loss có trọng số lớp cho mất cân bằng, không kèm thực nghiệm. (Toàn bài, arXiv v1 tr. 1–16; [@kaselimi2022trustworthy]; mục 5.1, tr. 25; [@saleem2025review].)

**Cùng tên SAE nhưng khác mẫu số:** Zhong và cộng sự định nghĩa SAE là trung bình theo thiết bị của sai lệch tổng năng lượng chia cho tổng công suất tổng (phương trình 9, tr. 6; [@zhong2014signal]); Seq2Point định nghĩa SAE cho từng thiết bị là sai lệch tổng năng lượng chia cho năng lượng thật của thiết bị đó trên một ngày (mục "Performance evaluation", arXiv v3 tr. 5; [@zhang2018sequence]). Không so sánh số SAE giữa hai định nghĩa.

**Cùng tên NDE nhưng khác về căn bậc hai:** Kolter & Jaakkola định nghĩa normalized disaggregation error là căn bậc hai của tỉ số tổng bình phương sai số trên tổng bình phương tín hiệu thật (phương trình 16, tr. 1477; [@kolter2012approximate]); Zhong và cộng sự dùng cùng tỉ số nhưng không lấy căn (phương trình 8, tr. 5; [@zhong2014signal]). Không so sánh số NDE giữa hai định nghĩa.

**Total variation và Huber trong AFAMAP không áp lên đầu ra thiết bị:** Kolter & Jaakkola đặt prior total variation lên thành phần $z_t$ giải thích phần công suất tổng không thuộc thiết bị nào được mô hình hóa (mục 2.2, phương trình 3–4, tr. 1474). Trong mô hình hiệu, ở các bước không chuỗi nào đổi trạng thái, sai số bình phương cộng phạt ℓ1 trên $\Delta z_t$ tối ưu giải tích thành hàm Huber trên tín hiệu hiệu đã chuẩn hóa; đây là mục tiêu suy luận không giám sát, không phải loss huấn luyện mạng. (Mục 3.2, phương trình 14, tr. 1476; Phụ lục B, phương trình 33–35, tr. 1481–1482; [@kolter2012approximate].)

### Khả năng so sánh kết quả
**Điểm chung:** NILMTK và Klemenjak cùng nêu rằng khác biệt về dữ liệu, thuật toán đối chứng và thước đo cản trở việc diễn giải kết quả NILM cạnh nhau. (Batra và cộng sự, Giới thiệu, PDF tr. 1–2; Klemenjak và cộng sự, mục I, PDF tr. 1; [@NILMTK]; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

**Phần Klemenjak mở rộng:** bài phân tích thêm độ bao phủ tập kiểm tra và mức nhiễu. Ví dụ REDD nhà 6 cho thấy RMSE đổi theo tỷ lệ tập kiểm tra; DRED nhà 1 cho thấy RMSE khác nhau giữa công suất tổng thực và tổng các kênh thiết bị đo. (Mục IV.A, PDF tr. 3; mục IV.C, Bảng II–III, PDF tr. 4–5; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

## Bằng chứng nguồn

| Nhận định                                                                         | Nguồn và vị trí chính xác                                                                                                            | Điều kiện / giới hạn                                                       |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| NILM ước lượng công suất thiết bị từ công suất tổng                               | [@NILMTK], mục 2.5, PDF tr. 4; [@klemenjak2020comparabilitynonintrusiveloadmonitoring], mục II, PDF tr. 1                            | Ký hiệu khác nhau giữa hai bài; Batra nêu thêm trạng thái rời rạc          |
| Công suất tổng = tổng thiết bị có kênh đo + phần dư gồm nhiễu đo và tải chưa đo   | [@klemenjak2020comparabilitynonintrusiveloadmonitoring], mục II, phương trình 1, PDF tr. 1                                           | Không đặt cận hay dấu cho phần dư                                          |
| Phần dư tách thành tải không quan tâm và nhiễu Gauss; công suất giả định không âm | [@zhang2018sequence], mục "Energy disaggregation", arXiv v3 tr. 2                                                                    | Giả định mô hình; chưa đối chiếu bản AAAI                                  |
| Tải không đo phụ tách khỏi nhiễu đo; tải không đo phụ lớn, không Gauss | [@huber2021review], mục 2.1, phương trình 1, tr. 9 | Lập luận tác giả, không số liệu; Kaselimi gộp vào một nhiễu cộng ([@kaselimi2022trustworthy], mục II.A, arXiv v1 tr. 3) |
| Kịch bản synthetic (= denoised) vs observed (= noised) | [@huber2021review], mục 3.2.1, tr. 11–12 | Định nghĩa của Huber |
| MAE/MSE + cross-entropy phổ biến; chưa có so sánh loss có hệ thống | [@huber2021review], mục 3.4.2, tr. 16 | DNN-NILM tần số thấp đến 11/2020; theo hiểu biết tác giả |
| NILMTK và Klemenjak không so sánh loss huấn luyện                                 | [@NILMTK], mục 3.5–3.7, PDF tr. 5–7, mục 4.4–4.5, PDF tr. 9–10; [@klemenjak2020comparabilitynonintrusiveloadmonitoring], PDF tr. 1–5 | Chỉ nói về hai bài này                                                     |
| SAE có hai mẫu số khác nhau                                                       | [@zhong2014signal], phương trình 9, tr. 6; [@zhang2018sequence], arXiv v3 tr. 5                                                      | Không so sánh số giữa hai định nghĩa                                       |
| NDE có căn (Kolter) và không căn (Zhong)                                          | [@kolter2012approximate], phương trình 16, tr. 1477; [@zhong2014signal], phương trình 8, tr. 5                                       | Không so sánh số giữa hai định nghĩa                                       |
| TV đặt lên phần dư $z_t$; Huber là mục tiêu suy luận trên $\Delta z_t$            | [@kolter2012approximate], mục 2.2, phương trình 3–4, tr. 1474; mục 3.2, phương trình 14, tr. 1476; phương trình 33–35, tr. 1481–1482 | Suy luận AFHMM không giám sát, không phải loss huấn luyện mạng             |
| Khác biệt dữ liệu, đối chứng và thước đo cản trở so sánh                          | [@NILMTK], Giới thiệu, PDF tr. 1–2; [@klemenjak2020comparabilitynonintrusiveloadmonitoring], mục I, PDF tr. 1                        | Phát biểu chung của tác giả                                                |
| RMSE đổi theo độ bao phủ tập kiểm tra và theo loại tín hiệu tổng                  | [@klemenjak2020comparabilitynonintrusiveloadmonitoring], mục IV.A, PDF tr. 3; mục IV.C, Bảng II–III, PDF tr. 4–5                     | REDD nhà 6, DRED nhà 1; mỗi cấu hình một kết quả; Bảng II không ghi đơn vị |

## Liên kết

- [[notes/README|Bản đồ ghi chú kiến thức NILM]]
- [[notes/NILM-Evaluation/Ràng buộc C1 - không âm|Ràng buộc C1 - không âm]]
- [[notes/NILM-Evaluation/Ràng buộc C2 - công suất cực đại thiết bị|Ràng buộc C2 - công suất cực đại thiết bị]]
- [[notes/NILM-Evaluation/Ràng buộc C3 - giới hạn công suất tổng|Ràng buộc C3 - giới hạn công suất tổng]]
- [[notes/NILM-Evaluation/NAR - tỷ lệ phần dư công suất tổng|NAR - tỷ lệ phần dư công suất tổng]]
- [[notes/NILM-Evaluation/TSR và EVR - độ bao phủ tập kiểm tra|TSR và EVR - độ bao phủ tập kiểm tra]]
- [[notes/NILM-Evaluation/F-score theo lát thời gian và event-F1|F-score theo lát thời gian và event-F1]]
- [[notes/NILM-methodology/README|Các phương pháp giải bài toán]]
- [[notes/NILM-Datasets/README|Các bộ dữ liệu dùng để đánh giá]]
- So sánh công bằng giữa hàm mất mát và mô hình (kế hoạch: `synthesis/NILM-Questions/So sánh công bằng giữa hàm mất mát và mô hình`)
