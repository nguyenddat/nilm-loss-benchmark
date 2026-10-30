---
type: method
title: "Tối ưu tổ hợp (CO)"
aliases: [Combinatorial Optimization]
tags: [nilm, methodology, baseline]
evidence_status: extracted
---

# Tối ưu tổ hợp (CO)

Tối ưu hóa tổ hợp tìm tập trạng thái thiết bị sao cho tổng công suất dự đoán gần nhất với công suất tổng quan sát, dựa trên mô hình thiết bị đã học. Mỗi thời điểm được tối ưu riêng nên các thời điểm được xem độc lập trong cách trình bày của bài. (Batra và cộng sự, mục 3.5, công thức 2, PDF tr. 5; [@NILMTK].)

Bài báo mô tả độ phức tạp là `O(TK^N)` với `T` lát thời gian, `N` thiết bị và `K` trạng thái mỗi thiết bị; tìm kiếm tổ hợp tăng theo hàm mũ theo số thiết bị. (Batra và cộng sự, mục 3.5, PDF tr. 5.)

Trong bài NILMTK, CO dùng hai trạng thái cho mỗi thiết bị trong ví dụ liên bộ dữ liệu; tác giả nói thí nghiệm nhằm so sánh công bằng hai thuật toán đối chứng, không phải phiên bản tối ưu hóa đầy đủ của từng phương pháp. (Batra và cộng sự, mục 4.4, PDF tr. 9; [@NILMTK].)

CO là mô hình đối chứng phân rã tải, không phải một hàm mất mát trong đánh giá đối chiếu học sâu. Bảng kết quả của các bài nguồn không thể so trực tiếp nếu khác dữ liệu, cách chia và thước đo.

## Liên kết

- [[notes/NILM-methodology/Mô hình ẩn Markov giai thừa (FHMM)|Mô hình ẩn Markov giai thừa (FHMM)]]
- So sánh công bằng giữa hàm mất mát và mô hình (kế hoạch: `synthesis/NILM-Questions/So sánh công bằng giữa hàm mất mát và mô hình`)
