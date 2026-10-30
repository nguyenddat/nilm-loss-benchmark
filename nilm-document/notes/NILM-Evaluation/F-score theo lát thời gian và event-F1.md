---
type: metric-concept
title: "F-score theo lát thời gian và F1 theo sự kiện"
tags: [nilm, metric, event-detection]
evidence_status: extracted
---

# F-score theo lát thời gian và F1 theo sự kiện

F-score của NILMTK trong bài Batra tính precision/recall cho phân loại trạng thái ON/OFF tại từng lát thời gian. Đây không phải F1 theo sự kiện được tính bằng cách ghép thời điểm bật/tắt của sự kiện. (Batra và cộng sự, mục 3.7, công thức 7–15, PDF tr. 6–7; [@NILMTK].)

Đề xuất nêu F1 theo sự kiện nhưng chưa chốt ngưỡng ON/OFF, cách ghép dự đoán với sự kiện thật, dung sai thời gian hay cách tổng hợp theo thiết bị/hộ. Những định nghĩa này cần được quy định trước khi so sánh. (Đề xuất nghiên cứu, mục 3.3; đề xuất (kế hoạch: `synthesis/research-proposal`).)

## Liên kết

- [[notes/NILM-Evaluation/TSR và EVR - độ bao phủ tập kiểm tra|TSR và EVR - độ bao phủ tập kiểm tra]] — đếm sự kiện trong tập tập kiểm tra là độ bao phủ, không phải F1.
- Định nghĩa thước đo và phân tích theo trạng thái (kế hoạch: `synthesis/NILM-Questions/Định nghĩa thước đo và phân tích theo trạng thái`)
