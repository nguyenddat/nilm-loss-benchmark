# Hướng dẫn workspace thực nghiệm

## Mục tiêu và phạm vi

Hiện thực và đánh giá benchmark NILM theo đề xuất: mối liên hệ giữa lựa chọn mô hình và hàm mất mát với dự đoán công suất thiết bị, hành vi theo thời gian và tính nhất quán vật lý. Đề xuất hướng tới REFIT và tín hiệu tổng hợp có kiểm soát, các thiết lập có giám sát và chỉ dùng dữ liệu tổng, cùng khả năng bền vững trước nhiễu và thay đổi giữa các hộ. Đây là các hướng đề xuất, chưa phải kết quả hay protocol đã chốt. Trước khi hiện thực, đọc `README.md` tại đây và bản đề xuất, ghi chú đã review, tổng hợp liên quan trong `../nilm-document/`. Nêu rõ mâu thuẫn giữa đề xuất và ghi chú hiện có; không tự ý chốt các lựa chọn nghiên cứu còn mở.

## Thiết kế và hiện thực

- Ghi protocol theo `templates/experiment-protocol.md` trước khi chạy. Xác định câu hỏi, giả thuyết có nguồn, thiết bị mục tiêu, các tổ hợp mô hình–loss áp dụng được, đầu ra chính, phép so sánh và quyết định còn mở.
- Ghi danh tính và phiên bản dataset, điều kiện truy cập và giấy phép, cách chọn thiết bị/hộ, căn chỉnh thời gian, tiền xử lý, lấy mẫu lại và xử lý dữ liệu thiếu. Chia theo hộ hoặc thời gian phù hợp với kết luận về khả năng khái quát. Ngăn cửa sổ chồng lấn và thống kê dẫn xuất rò rỉ giữa các tập; chỉ ước lượng phép biến đổi trên tập huấn luyện và chỉ dùng tập huấn luyện/validation để điều chỉnh.
- Khi ablation loss, giữ cố định kiến trúc, đầu vào, nhãn, cách chia, ngân sách huấn luyện, quy trình điều chỉnh, đánh giá và hậu xử lý nếu áp dụng được. Ghi các tổ hợp mô hình–loss không tương thích. Báo cáo riêng phương pháp có giám sát và phương pháp chỉ dùng dữ liệu tổng, cùng khác biệt về quyền dùng nhãn hoặc thông tin huấn luyện khác. Ngân sách tìm siêu tham số và cách chọn mô hình phải so sánh được và được ghi lại.
- Ghi công thức, đơn vị, phép gộp, tỷ lệ và trọng số của từng loss. Loss tái dựng tổng phải nêu rõ thiết bị không được đo, tải dư và căn chỉnh phép đo; không giả định tổng công suất các thiết bị được chọn bằng đúng công suất tổng. Phân biệt regularizer với ràng buộc cứng; báo cáo riêng hậu xử lý hoặc clipping.
- Định nghĩa chính xác MAE, RMSE, SAE và event F1, gồm cách gộp, đơn vị, xử lý mẫu số bằng hoặc gần 0, ngưỡng trạng thái, định nghĩa sự kiện và dung sai ghép sự kiện. Ghi tập dữ liệu, seed, thiết bị và hộ cho từng điểm số; báo cáo biến thiên giữa seed và các đơn vị phân tích nếu phù hợp.
- Kiểm tra C1 không âm, C2 cận trên thiết bị khi có căn cứ, và C3 bất đẳng thức công suất tổng khi các giả định về tiêu thụ không âm, phát điện, nhiễu và căn chỉnh được thỏa mãn. Ghi dự đoán thô hay sau hậu xử lý, dung sai, số mẫu hợp lệ, mẫu số và đơn vị. Kiểm tra dữ liệu ground truth theo cùng quy tắc C3 để phát hiện bất nhất trong phép đo. Không suy luận có vi phạm vật lý chỉ từ phép đo tổng có nhiễu hoặc lệch thời gian.
- Với REFIT, xác định điều kiện áp dụng C3 cho từng mẫu trước khi đánh giá mô hình: ghi cách căn chỉnh thời điểm đo tổng/thiết bị, mặt nạ cờ chất lượng/bất thường và dữ liệu thiếu, cách xử lý phát điện mặt trời hoặc phép đo công suất ròng, cùng các mẫu bị loại. Mặt nạ phải độc lập với dự đoán mô hình; báo số mẫu bị loại theo lý do và lưu kiểm tra tính nhất quán của ground truth. Tham khảo [tài liệu mô tả dataset REFIT](https://pure.strath.ac.uk/ws/portalfiles/portal/63396371/Murray_etal_SD_2016_An_electrical_load_measurements_dataset_of_United_Kingdom.pdf) và phiên bản dataset cụ thể trước khi quyết định dùng các cờ. Không mặc định C3 đúng với mọi mẫu.
- Nêu mô hình nhiễu, cường độ, vị trí thêm nhiễu và seed; phân biệt phép thử sức chịu đựng trên tín hiệu tổng hợp với bằng chứng về hiệu năng trên dataset thực khác. Định nghĩa cửa sổ chuyển trạng thái và không xem các mẫu thời gian có tương quan là các lần lặp độc lập.

## Cấu trúc mã nguồn

Theo YAGNI: chỉ hiện thực và tạo thư mục mà việc hiện tại cần; không thêm abstraction, registry, pipeline hay lớp cấu hình mang tính dự phòng.

```text
nilm-code/
├── src/
│   ├── core/          # đường dẫn và cấu hình dùng chung (giữ nhỏ)
│   ├── data/<dataset>/ # đọc dữ liệu, manifest/checksum, kiểm tra chất lượng riêng từng dataset
│   └── experiments/eXXX_<mục_tiêu>/   # config.py, run.py, analyze.py
├── data/raw/<dataset>/ # dữ liệu tải về, git bỏ qua; không đặt hay chạy mã ở đây
├── outputs/experiments/<experiment_id>/<run-id>/   # đầu ra gốc và bảng dẫn xuất
├── runs/<run-id>/     # hồ sơ lần chạy (README theo templates/run-record.md, env/, log)
└── docs/              # ghi chú kỹ thuật theo ngày, chỉ tạo khi cần
```

- `src/core/`: đường dẫn suy ra từ vị trí mã (`src/core/paths.py`), không mã hóa cứng đường dẫn tuyệt đối. Không đặt cấu hình riêng của experiment ở đây.
- `src/data/<dataset>/`: mọi logic riêng của dataset (cột, tên tệp, hằng số như hộ có điện mặt trời, ngưỡng làm sạch của nhà cung cấp). Không rải điều kiện riêng của dataset vào experiment.
- `src/experiments/eXXX_<mục_tiêu>/`: mỗi experiment trả lời **một** câu hỏi khoa học cụ thể và được đặt tên theo câu hỏi đó, không theo tên phương pháp (ví dụ `e000_refit_data_audit`). Chỉ chứa phần điều phối riêng: `config.py` (dữ liệu, hộ, tham số, ngưỡng, định nghĩa), `run.py` (phần tốn kém hoặc sinh trạng thái: nạp dữ liệu → áp phương pháp → ghi đầu ra gốc), `analyze.py` (đọc đầu ra đã lưu để tính bảng, so sánh, hình; chạy lại được mà không chạy lại `run.py`). Chỉ tạo tệp thật sự cần.
- `src/methods/` (mô hình, hàm mất mát, hậu xử lý) và `src/metrics/` (MAE, RMSE, SAE, event F1, vi phạm C1–C3) là chỗ dành cho sau này: **chưa tạo** cho tới khi cổng bàn giao cho phép khóa tổ hợp mô hình–loss và thước đo. Khi tạo, mã tái sử dụng nằm ở đó và experiment chỉ import; không sao chép hiện thực vào thư mục experiment.
- Chiều phụ thuộc: `experiments → methods / metrics → data → core`. Module cấp thấp không import experiment; tránh phụ thuộc vòng.
- Tách mã–dữ liệu–đầu ra: không ghi đầu ra vào `src/`, không đặt mã trong `data/`. Mỗi run ghi vào `outputs/experiments/<experiment_id>/<run-id>/` và từ chối ghi đè; hồ sơ `runs/<run-id>/README.md` trỏ tới thư mục đầu ra đó.
- Chạy bằng môi trường `uv` ở gốc repo, từ thư mục `nilm-code/`: `uv run python -m src.experiments.<eXXX>.run --run-id <run-id>` rồi `... .analyze --run-id <run-id>`. Thư viện mới thêm bằng `uv add` ở gốc repo.

## Hồ sơ chạy và bàn giao

Mỗi lần chạy cần một run ID duy nhất và ổn định. Dùng `templates/run-record.md` để lưu cùng nhau dưới `runs/<run-id>/`: cấu hình, phiên bản code và trạng thái thay đổi chưa commit, phiên bản dữ liệu và mã tập chia, lệnh chính xác, môi trường, seed, log, đầu ra thô, metric, lỗi và đường dẫn artifact. Giữ nguyên quan sát thô và ghi lệnh tạo mỗi bảng hoặc hình dẫn xuất. Tuân thủ điều kiện truy cập dataset; không commit dữ liệu thô hoặc artifact lớn khi chưa có chính sách rõ ràng của repo.

Kiểm tra có trọng tâm công thức loss và metric, kích thước tensor, mặt nạ, rò rỉ giữa các tập và phép tính ràng buộc. Một run được xác minh cần có bằng chứng tái lập thành công hoặc kiểm tra độc lập được mô tả rõ, gồm tiêu chí khớp; nếu chưa đạt, ghi là thăm dò, thất bại hoặc chờ xác minh. Không bịa số liệu hoặc tuyên bố đã chạy khi thiếu bằng chứng.

Bàn giao cho `paper` protocol, run ID, cấu hình, đầu ra thô và tổng hợp, bằng chứng xác minh và giới hạn. Nếu thiếu nguồn hoặc kết quả cần thiết, báo agent điều phối; không trình bày thí nghiệm đề xuất như một phát hiện.
