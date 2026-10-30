---
type: constraint
title: "Ràng buộc C2 - công suất cực đại thiết bị"
tags: [nilm, physical-constraint, evaluation]
evidence_status: proposed
---

# Ràng buộc C2 — giới hạn công suất cực đại thiết bị

Đề xuất đặt C2 là $\hat{y}_{i,t}\le P_i^{\max}$ khi có giới hạn công suất đáng tin cậy. Các nguồn đang tổng hợp không cung cấp một bảng giới hạn độc lập áp dụng cho mọi thiết bị/hộ. (Đề xuất nghiên cứu, mục 3.2; đề xuất (kế hoạch: `synthesis/research-proposal`).)

Trước khi tính C2, cần truy nguồn cho từng giới hạn, đơn vị và phạm vi áp dụng. Không lấy cực đại trên tập kiểm tra làm $P_i^{\max}$, vì khi đó giới hạn phụ thuộc chính dữ liệu cần đánh giá.

## Bằng chứng từ tài liệu (nguồn đã rà soát theo PDF; Seq2Point theo arXiv v3)

Bảng tham số của Seq2Point có hàng "Maximum power" cho năm thiết bị UK-DALE (ví dụ ấm đun 3948 W, lò vi sóng 3138 W), nhưng bài không nêu giá trị lấy từ đâu hay dùng vào bước nào. (Bảng 1, arXiv v3 tr. 4; [@zhang2018sequence].) Vì nguồn gốc chưa rõ và có thể là cực đại quan sát trong dữ liệu (chưa xác minh), không dùng các giá trị này làm $P_i^{\max}$ độc lập cho REFIT.

Chưa có nguồn nào trong vault cung cấp giới hạn công suất thiết bị độc lập với dữ liệu đánh giá.
