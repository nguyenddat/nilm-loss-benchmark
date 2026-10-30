---
type: constraint
title: "Ràng buộc C3 - giới hạn công suất tổng"
tags: [nilm, physical-constraint, evaluation]
evidence_status: proposed
---

# Ràng buộc C3 — tổng dự đoán không vượt công suất tổng

Đề xuất nêu $\sum_i\hat{y}_{i,t}\le P_t$. Chỉ đánh giá C3 khi tổng đo biểu thị tiêu thụ không âm, các kênh được căn thời gian và có giả định phù hợp về tải chưa đo, nhiễu và phát điện. Đây là điều kiện cần chốt, không phải kết quả hiện có. (Đề xuất nghiên cứu, mục 3.2; đề xuất (kế hoạch: `synthesis/research-proposal`).)

**Hệ quả từ mô hình đo:** phương trình NILM của Klemenjak có phần dư chứa tải chưa đo và nhiễu, không nêu dấu/cận cho phần dư; do đó không suy ra C3 vô điều kiện. (Mục II, phương trình 1, PDF tr. 1; [@klemenjak2020comparabilitynonintrusiveloadmonitoring].)

**Điều kiện riêng của REFIT:** bài dataset ghi nhận IAM có thể lệch thời điểm, một số hộ bị ảnh hưởng bởi điện mặt trời và bản sạch đánh dấu mẫu tổng IAM vượt công suất tổng. Đây là vấn đề phép đo cần xét khi lập mặt nạ C3. (Murray và cộng sự, Household aggregate, PDF tr. 4; IAM, PDF tr. 5; Technical Validation, PDF tr. 8; [@murray2017refit].)

**Phần dư được mô hình hóa tường minh trong một số phương pháp:** Seq2Point viết công suất tổng bằng tổng các thiết bị quan tâm cộng phần thiết bị còn lại $u_t$ và nhiễu. (Mục "Energy disaggregation", arXiv v3 tr. 2; [@zhang2018sequence].) AFAMAP thêm một thành phần $z_t$ có thể nhận giá trị tùy ý, với prior total variation, để giải thích tín hiệu không thiết bị nào mô hình hóa; năng lượng không gán được coi là hợp lệ. (Mục 2.2, phương trình 3–4, tr. 1474; mục 5, tr. 1478; [@kolter2012approximate].) Không nguồn nào trong hai bài này ràng buộc dấu của phần dư hoặc đo $\sum_i\hat{y}_{i,t}-P_t$.

**Ràng buộc tổng năng lượng theo thiết bị khác C3:** signal aggregate constraints phạt độ lệch giữa tổng năng lượng của **một thiết bị trong cả khoảng thời gian** và giá trị kỳ vọng; đó không phải bất đẳng thức tổng các thiết bị tại từng thời điểm. (Mục 4.2, phương trình 4–5, tr. 3–4; [@zhong2014signal].)

**Công suất tổng observed và synthetic:** Huber và cộng sự phân biệt kịch bản *synthetic* (= denoised), trong đó phần tải không đo phụ bằng 0 vì công suất tổng được tạo bằng cách cộng các kênh thiết bị, chỉ còn nhiễu đo; và kịch bản *observed* (= noised), trong đó phần dư còn chứa các thiết bị không đo riêng. Tác giả coi synthetic là thiết lập “phòng thí nghiệm”, còn dữ liệu thực thường là observed. (Mục 3.2.1, tr. 11–12; [@huber2021review].) Tác giả cũng cho rằng tải không đo phụ thường chiếm phần lớn công suất tổng và không Gauss (mục 2.1, tr. 9; [@huber2021review]).

**Suy luận của dự án:** trên synthetic, nhãn thỏa $\sum_i p_{i,t}\approx P_t$, nên C3 trên dự đoán gần như chặt — mọi ước lượng quá ở một thiết bị phải được bù bằng ước lượng thiếu ở thiết bị khác; trên observed, phần dư tải không đo tạo khoảng trống làm C3 lỏng hơn. Do đó tỷ lệ vi phạm C3 không chuyển trực tiếp giữa hai kịch bản và phải báo riêng.

**Mô hình đơn đích và tổng công suất (nhận định định tính):** Kaselimi và cộng sự cho rằng các mô hình huấn luyện riêng cho từng thiết bị “có thể ước lượng thiếu hoặc quá đáng kể” tổng công suất vì không tối thiểu hóa chênh lệch giữa tổng đo và tổng các ước lượng thiết bị. Đây là lập luận của tác giả, không kèm số đo. (Mục V.A.2, arXiv v1 tr. 8; Hình 3, tr. 7; [@kaselimi2022trustworthy].) **Suy luận của dự án:** khi đo C3, cần ghi rõ tổng dự đoán đến từ nhiều mô hình đơn đích hay một mô hình đa đích; nhận định trên là giả thuyết kiểm được bằng tỷ lệ mẫu $\sum_i\hat{y}_{i,t}>P_t$, chưa có kết quả.

**Ba review không bàn C3:** Huber 2021, Kaselimi 2022 và Saleem 2025 đều không có mục về ràng buộc vật lý trên dự đoán hay thước đo vi phạm; đây là quan sát trên ba review, không phải bằng chứng vắng mặt trong toàn lĩnh vực. (Tìm toàn văn; [@huber2021review]; [@kaselimi2022trustworthy]; [@saleem2025review]; xem [[notes/NILM-methodology/Taxonomy phương pháp NILM|Taxonomy phương pháp NILM]].)

## Phép đo cần định nghĩa

Đề xuất phép vi phạm $v_t=\max(0,\sum_i\hat{y}_{i,t}-P_t)$ trên mặt nạ mẫu đủ điều kiện; báo tỷ lệ mẫu vi phạm và mức vi phạm theo W. Dung sai đo, căn chỉnh thời điểm và mẫu bị loại cần được đặt trước, đồng thời báo độ phủ của mặt nạ. Đây là thiết kế cần kiểm tra, chưa phải giao thức đã chốt.

## Phân biệt với chất lượng dữ liệu

Cờ tổng công tơ thiết bị vượt công suất tổng là quan sát về phép đo/nhãn; nó không chứng minh dự đoán vi phạm C3. NAR là tỷ lệ phần dư dữ liệu, không thay thế phép đo `v_t`. Xem [[notes/NILM-Evaluation/NAR - tỷ lệ phần dư công suất tổng|NAR - tỷ lệ phần dư công suất tổng]] và Audit dữ liệu và mặt nạ C3 (kế hoạch: `synthesis/NILM-Questions/Audit dữ liệu và mặt nạ C3`).
