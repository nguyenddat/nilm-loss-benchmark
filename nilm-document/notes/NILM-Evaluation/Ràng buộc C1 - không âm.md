---
type: constraint
title: "Ràng buộc C1 - không âm"
tags: [nilm, physical-constraint, evaluation]
evidence_status: proposed
---

# Ràng buộc C1 — công suất dự đoán không âm

Đề xuất đặt C1 là $\hat{y}_{i,t}\ge 0$ cho công suất dự đoán của từng thiết bị. Đây là yêu cầu đánh giá dự kiến của đề tài, không phải kết quả đã được các bài NILMTK, bài về khả năng so sánh hay REFIT xác lập. (Đề xuất nghiên cứu, mục 3.2; đề xuất (kế hoạch: `synthesis/research-proposal`).)

Khi đánh giá, cần ghi rõ đại lượng, đơn vị, cách tính tần suất và độ lớn phần âm. Nếu mô hình đã áp đặt không âm ở đầu ra, vẫn cần nêu phép đo và cách kiểm tra.

## Bằng chứng từ tài liệu (nguồn đã rà soát theo PDF; Seq2Point theo arXiv v3)

**Không âm là giả định mô hình, không phải ràng buộc được kiểm tra:** hai bài cùng nhóm tác giả viết công suất thiết bị thuộc $\mathbb{R}^+$ trong phương trình mô hình đo, nhưng không đo hay báo cáo đầu ra âm. (Zhong và cộng sự, mục 3, phương trình 1, tr. 2; [@zhong2014signal]. Zhang và cộng sự, mục "Energy disaggregation", arXiv v3 tr. 2; [@zhang2018sequence].)

**Đầu ra tuyến tính của Seq2Point:** lớp Dense cuối của seq2point và seq2seq dùng kích hoạt tuyến tính, nên kiến trúc gốc không chặn giá trị âm. (Hình 1, arXiv v3 tr. 3; [@zhang2018sequence].)

**Suy luận của dự án:** vì vậy C1 có thể là thước đo có thông tin với kiến trúc gốc; nếu dự án thêm ReLU/softplus hoặc kẹp đầu ra, cần coi đó là biến kiến trúc/hậu xử lý riêng, không gộp vào hiệu ứng của loss. Chưa có nguồn nào trong vault báo tần suất đầu ra âm của mô hình NILM.
