---
type: literature-review-plan
status: planning
title: "Kế hoạch tổng quan tài liệu cho nghiên cứu loss và ràng buộc vật lý trong NILM"
tags:
  - nilm
  - literature-review
  - research-plan
---

# Kế hoạch tổng quan tài liệu

## Mục đích

Đọc và tổng hợp nghiên cứu hiện có trước khi chốt benchmark hoặc viết mã thí nghiệm. Tổng quan cần xác định cách các công trình định nghĩa mục tiêu huấn luyện, giao thức NILM, thước đo hiệu năng và tính nhất quán vật lý; đồng thời chỉ ra phần nào có thể so sánh công bằng.

Đây là kế hoạch tìm đọc, chưa phải tổng quan đã hoàn thành. Chưa có kết luận nào về ưu thế của một loss, mô hình hoặc bộ dữ liệu. Theo dõi tiến độ bằng trạng thái trong hàng đợi đọc, ghi chú theo mẫu ghi chú bài báo, rồi cập nhật ma trận bằng chứng.

## Chủ đề cần bao phủ

### 1. Bộ dữ liệu và giao thức đánh giá NILM

- Đặc tính các bộ dữ liệu có đo tổng và đo thiết bị: độ phân giải thời gian, số hộ, thiết bị, khoảng thiếu, sai lệch cảm biến, cách làm sạch và điều kiện giấy phép.
- Cách chia theo thời gian, theo hộ và giữa các bộ dữ liệu; nguy cơ rò rỉ do chia cửa sổ hoặc chuẩn hóa.
- Quy ước tiền xử lý, lấy mẫu lại, định nghĩa trạng thái thiết bị và cách tổng hợp kết quả giữa thiết bị/hộ.
- Mức độ phù hợp của REFIT với từng câu hỏi, không mặc định một bộ dữ liệu đại diện cho mọi thiết lập.

### 2. Hàm mục tiêu và loss trong NILM

- Hồi quy công suất thiết bị, gồm MSE, MAE và các dạng loss bền vững nếu có bằng chứng phù hợp.
- Loss tái tạo công suất tổng: thông tin nhãn cần dùng, tải dư từ thiết bị không được mô hình hóa, trọng số và cách căn chỉnh phép đo.
- Các thành phần chính quy hóa như L1/L2, làm trơn theo thời gian và total variation; ghi rõ loss nào là mục tiêu huấn luyện, loss nào là hậu xử lý hoặc ràng buộc cứng.
- Các tổ hợp loss, ablation và cách chọn hệ số; ghi nhận quy trình tìm siêu tham số để đánh giá mức độ so sánh được.

### 3. Ràng buộc vật lý và tính nhất quán năng lượng

- Không âm, giới hạn công suất từng thiết bị, tổng công suất và bảo toàn năng lượng: định nghĩa toán học, điều kiện áp dụng và nguồn của giới hạn.
- Khác biệt giữa áp ràng buộc trong huấn luyện, ép đầu ra sau huấn luyện và chỉ đo mức vi phạm khi đánh giá.
- Ảnh hưởng của tải không được đo, phát điện tại chỗ, nhiễu, độ lệch thời điểm cảm biến, sai số công tơ và mẫu dữ liệu bất thường.
- Cách đo tần suất, độ lớn và dung sai vi phạm; liệu ground truth có tự thỏa cùng giả định hay không.

### 4. Độ bền, chuyển trạng thái và dịch chuyển phân phối

- Sai số khi thiết bị bật/tắt, ở vùng công suất thấp và theo loại thiết bị.
- Mô hình nhiễu đo, vị trí thêm nhiễu, mức độ và cách đánh giá độ nhạy.
- Chia hộ huấn luyện/kiểm tra, thích nghi miền và chuyển bộ dữ liệu; phân biệt bằng chứng thực tế với stress test trên dữ liệu tổng hợp.
- Đơn vị thống kê phù hợp: mẫu thời gian, sự kiện, lần chạy, hộ gia đình hay thiết bị; cách biểu diễn độ bất định.

### 5. Họ mô hình và loại thông tin huấn luyện

- Hồi quy hoặc mô hình đối chứng đơn giản, mạng nơ-ron theo thời gian và tối ưu hóa lồi.
- Huấn luyện có giám sát bằng nhãn thiết bị so với phương pháp chỉ quan sát công suất tổng.
- Giả định, thông tin đầu vào/nhãn, mục tiêu và ngân sách khác nhau; không xếp hạng trực tiếp khi hai phương pháp giải bài toán khác nhau.

## Cách tìm và sàng lọc nguồn

1. Ghi ngày tìm, cơ sở dữ liệu/công cụ tìm kiếm và câu truy vấn chính xác cho mỗi lượt vào nhật ký tìm kiếm (kế hoạch: `synthesis/search-log`). Dùng tổ hợp thuật ngữ NILM/energy disaggregation với loss/objective, physical constraint/energy conservation, evaluation/metric, REFIT/dataset, domain shift/noise và supervised/unsupervised.
2. Tìm trong cơ sở dữ liệu học thuật và kho xuất bản phù hợp; ưu tiên bài báo gốc, bài mô tả dữ liệu, bài định nghĩa phương pháp và tài liệu chính thức của bộ dữ liệu. Dùng danh sách tài liệu tham khảo và trích dẫn xuôi/ngược để tìm nguồn liên quan.
3. Ghi từng kết quả ứng viên vào hàng đợi đọc kèm DOI/URL đã kiểm tra, chủ đề và câu hỏi liên quan. Trạng thái `queued` chỉ có nghĩa là cần xem xét, không có nghĩa là đã đọc hay đã xác nhận nội dung.
4. Sàng lọc tiêu đề/tóm tắt để xác định phạm vi sơ bộ; sau đó đọc toàn văn các nguồn có đóng góp trực tiếp cho câu hỏi hoặc quy trình. Ghi lý do loại trừ nếu không liên quan, thiếu thông tin cốt lõi hoặc không phải nguồn đủ tin cậy cho loại nhận định cần dùng.
5. Với mỗi nguồn được chọn, tạo ghi chú từ mẫu ghi chú bài báo. Chỉ chuyển trạng thái sang `reviewed` sau khi kiểm tra trích dẫn, vị trí nguồn, điều kiện thí nghiệm, con số và phần suy luận.
6. Cập nhật ma trận bằng chứng và các quyết định trong câu hỏi nghiên cứu. Nếu hai kết quả không cùng dataset, split, tiền xử lý, đơn vị, metric hoặc ngân sách, ghi rõ và không xếp hạng trực tiếp.

### Chiến lược top-down (áp dụng từ lượt tìm 2, 2026-10-30, theo yêu cầu người dùng)

Đọc theo thứ tự **review → taxonomy → nhánh → lá**:

1. Đọc sâu một số review/survey có tiêu chí chọn ghi trong nhật ký tìm kiếm (năm, phạm vi, bình duyệt, truy cập hợp lệ) để nắm xu hướng và các nhóm phương pháp.
2. Dựng taxonomy đề xuất của dự án (ghi chú tri thức `notes/NILM-methodology/Taxonomy phương pháp NILM.md`, theo mẫu tổng hợp), mỗi nút dẫn review và locator; ghi chỗ các review đồng thuận/mâu thuẫn.
3. Đánh dấu nhánh liên quan bài toán (loss, C1–C3, độ vững) và xếp ưu tiên bài lá trong từng nhánh.
4. Chỉ đọc sâu bài lá theo danh sách ưu tiên đó; bài lá ngoài các nhánh được đánh dấu chỉ sàng lọc. Khi một nhánh liên quan (ví dụ loss nhất quán với aggregate, PV sau công tơ) không được review nào nhắc, ghi rõ nhánh đó được dựng từ bài lá và tìm thêm review để kiểm tra.

### Bài lá ưu tiên theo taxonomy (kế hoạch đọc, cập nhật 2026-10-30)

Cây phân nhóm nằm trong ghi chú tri thức `notes/NILM-methodology/Taxonomy phương pháp NILM.md` (nút A–C). Danh sách dưới đây là **đề xuất ưu tiên đọc** của dự án, không phải kết luận; trạng thái theo hàng đợi đọc (`inbox/reading-queue.md`). Nút đánh dấu [L] là nhánh dựng từ bài lá, chưa review nào xác nhận.

1. **RAPC-Net (Li & Sun 2026, Applied Sciences)** — B2/B4f [L]/C3: loss tái tạo aggregate, hinge ước lượng quá, thước đo “Over-ratio” (chỉ thấy qua đoạn trích, chưa xác minh). Cần tải thủ công (MDPI chặn).
2. **NILMBench2026** — C-b/C-c: benchmark 16 mô hình, T3 REDD↔REFIT; đối chiếu thiết kế giao thức.
3. **Klemenjak và cộng sự 2021 (real vs denoised)** — C-a: đã đọc toàn văn; cần tạo ghi chú (NAR REFIT, ảnh hưởng của phần dư).
4. **D'Incecco và cộng sự 2020** — A4/C-b: REFIT → UK-DALE/REDD; đã đọc toàn văn; cần tạo ghi chú (lưu ý mâu thuẫn về loại nhà 13 có PV).
5. **BERT4NILM (2020)** — B4d: loss ghép; PDF ACM chưa truy cập.
6. **UNet-NILM (Faustine và cộng sự)** — B2/B4b: đa đích + quantile; Huber [46] ghi là NILM'20 workshop; DOI chưa xác minh.
7. **Liu & Fan 2026 (arXiv 2609.18315)** — B1/B4f [L]: L_cons; đã đọc toàn văn; cần tạo ghi chú.
8. **MATNilm 2023 (TII)** — B2: tổng ≤ aggregate qua kiến trúc.
9. **Loss GAN: EnerGAN (Kaselimi và cộng sự, Huber [43]), Pan và cộng sự (Huber [34])** — B4c; metadata chưa xác minh.
10. **Murray 2019, Liu UDA TII 2022, Chang KDD'23, thước đo chuyển giao của Klemenjak (Huber [145]), Shin 2019 về yêu cầu dữ liệu (Huber [75])** — C-b.
11. **Chen & Ardakanian 2022 (PV sau công tơ), DualNILM** — C-e [L]/C3 với REFIT có PV.
12. **Rafiq và cộng sự 2020 (hậu xử lý, Huber [36])** — B5/C1.
13. Review 2023–2026 chưa đọc (Yan 2026, Schirmer & Mporas 2023, Xiang 2026) — để kiểm tra các nhánh [L].

Không đặt hạn ngạch số lượng bài báo. Dừng lượt tìm chính khi các cụm truy vấn và truy vết trích dẫn liên tiếp không còn bổ sung phương pháp, cách đánh giá hay giới hạn mới có ý nghĩa cho câu hỏi; đồng thời ghi rõ chủ đề nào vẫn thiếu bằng chứng. Nếu một RQ còn thiếu nguồn hoặc quy trình có thể kiểm tra, tiếp tục tìm ở chủ đề đó thay vì coi tổng quan đã bão hòa.

## Trường cần trích xuất

Với mỗi nguồn, ghi những trường có liên quan và ghi `không nêu` khi nguồn không cung cấp:

- Thông tin thư mục, phiên bản nguồn và vị trí trích dẫn cụ thể.
- Câu hỏi, loại phương pháp và đóng góp mà tác giả tuyên bố.
- Bộ dữ liệu, thiết bị, hộ, tần suất đo, tiền xử lý, nhãn, cách chia và cách ngăn rò rỉ.
- Mô hình, loss/công thức, reduction, đơn vị, hệ số và nguồn của từng lựa chọn.
- Baseline, thông tin được dùng lúc huấn luyện, ngân sách tinh chỉnh, seed và phần cứng nếu có.
- Metric, công thức, ngưỡng sự kiện, đơn vị, cách gộp, kết quả và biến thiên.
- Ràng buộc vật lý được nêu, điều kiện áp dụng, dung sai, cách đo vi phạm và xử lý phép đo không nhất quán.
- Code/dữ liệu/giấy phép, lệnh tái lập và giới hạn do tác giả nêu.
- Nhận xét của người đọc: khả năng so sánh, nguy cơ sai lệch, điều chưa rõ và câu hỏi cần kiểm tra.

## Mức độ bằng chứng

- **Tuyên bố của tác giả:** nội dung được nêu trong bài; luôn kèm vị trí nguồn.
- **Kết quả được quan sát:** con số hoặc hiện tượng báo cáo từ thí nghiệm; kèm dataset, split, metric và điều kiện.
- **Suy luận của dự án:** diễn giải hoặc giả thuyết rút ra từ nhiều nguồn; gắn nhãn suy luận và không dùng như kết quả đã chứng minh.
- **Chưa xác minh:** thông tin mới thấy ở tiêu đề/tóm tắt, trích dẫn thứ cấp hoặc tài liệu chưa đọc đủ; không dùng làm bằng chứng cho paper hay protocol.

## Sản phẩm tổng hợp

- Ghi chú từng nguồn đã đọc, có vị trí bằng chứng và trạng thái.
- Bảng ma trận so sánh các công trình theo loss, mô hình, dữ liệu, giao thức, metric và ràng buộc.
- Ghi chú tổng hợp theo chủ đề, nêu điểm đồng thuận, khác biệt, giới hạn và khả năng so sánh.
- Bản đồ bằng chứng cho RQ1–RQ4, bao gồm vùng có/thiếu bằng chứng và câu hỏi còn mở.
- Danh sách lựa chọn benchmark được tài liệu hỗ trợ và lựa chọn vẫn cần quyết định hoặc thử nghiệm.

## Cổng bằng chứng trước khi giao cho workspace code

Chưa chốt protocol và chưa chạy benchmark đầy đủ cho đến khi tổng hợp tài liệu đủ để trả lời hoặc ghi rõ giới hạn ở các mục sau:

- Xác định được các lớp loss và baseline liên quan, công thức/nguồn của chúng, cùng tổ hợp nào có thể so sánh công bằng trên cùng kiến trúc.
- Biết các quy ước benchmark trước đây về dữ liệu, chia tập, tiền xử lý, metric và sự kiện; chỉ ra các khác biệt có thể làm thay đổi kết luận.
- Có cơ sở và cách ghi rõ cho C1/C2/C3, bao gồm điều kiện đo lường, giới hạn thiết bị, sai lệch cảm biến và phép hậu xử lý.
- Có thiết kế riêng cho học có giám sát và chỉ dùng công suất tổng, không nhập hai nhóm thành bảng xếp hạng trực tiếp.
- Có định nghĩa khả thi cho độ bền trước nhiễu/chuyển nhà và giới hạn của stress test tổng hợp.
- Đưa ra bản đồ bằng chứng cho từng RQ, danh sách các quyết định đã được nguồn hỗ trợ, các quyết định còn bỏ ngỏ và nguồn cần đọc tiếp.

Khi đạt cổng này, bàn giao cho `nilm-code/` bản tóm tắt có liên kết nguồn, không chỉ danh sách bài báo. Nếu phần quan trọng còn thiếu, báo rõ khoảng trống và thu hẹp câu hỏi hoặc tiếp tục đọc trước khi thiết kế thí nghiệm.

## Trạng thái hiện tại

Đây là kế hoạch tổng quan tài liệu. Bài báo REFIT [@murray2017refit], nhưng README/metadata/tệp dữ liệu định dùng còn phải kiểm tra. Lượt tìm đầu tiên cho chủ đề 2–3 (2026-10-30) đã ghi trong nhật ký tìm kiếm (kế hoạch: `synthesis/search-log`); ba nguồn [@kolter2012approximate], [@zhong2014signal], [@zhang2018sequence] ở trạng thái `extracted`, chưa rà soát, và chưa nguồn nào đo vi phạm C1–C3 hay so sánh loss có kiểm soát. Tổng quan theo các chủ đề loss, ràng buộc vật lý, mô hình và dịch chuyển phân phối chưa hoàn tất; chưa qua cổng bằng chứng và chưa có quy trình benchmark được chốt.

Lượt tìm 2 (2026-10-30, nhật ký: `synthesis/search-log`, mục “Lượt 2”) chuyển sang chiến lược top-down giữa lượt. Trạng thái theo chủ đề sau lượt 2:

| Chủ đề | Trạng thái | Nguồn đã có (trạng thái) | Còn thiếu |
| --- | --- | --- | --- |
| Tổng quan / taxonomy | Ba review đã rà soát; taxonomy bản nháp | [@huber2021review], [@kaselimi2022trustworthy] (theo arXiv v1), [@saleem2025review] (`reviewed`, 2026-10-30); taxonomy `notes/NILM-methodology/Taxonomy phương pháp NILM.md` (draft, locator review đã đối chiếu) | Review 2023–2026 khác (Yan 2026, Schirmer & Mporas 2023, Xiang 2026); rà soát taxonomy |
| 1. Dữ liệu và đánh giá | Một phần | REFIT, NILMTK, Comparability (`reviewed`); Klemenjak 2021 real vs denoised (`screened`, đã đọc toàn văn) | Ghi chú Klemenjak 2021; NILMBench2026; review về tái lập |
| 2. Loss | Mỏng | [@shin2019subtask] (`extracted`; ablation bỏ L_on, một lần chạy); Huber 2021 nêu chưa có so sánh loss có hệ thống đến 11/2020 | So sánh loss có kiểm soát; BERT4NILM, UNet-NILM, loss GAN; PB-NILM đã bị loại theo quyết định người dùng |
| 3. Ràng buộc vật lý | Chưa có nguồn đo vi phạm | Kolter 2012, Zhong 2014 (`reviewed`); Liu & Fan 2026, MATNilm (`screened`) | RAPC-Net (cần tải thủ công; nội dung chưa xác minh); nguồn P_max độc lập cho C2; He et al. 2019 đã bị loại theo quyết định người dùng |
| 4. Độ vững / dịch chuyển | Đã bắt đầu | D'Incecco 2020 (`screened`, đã đọc toàn văn); review nêu cross-domain hiếm (Huber 2021, mục 3.2.1) | Ghi chú D'Incecco; Murray 2019, UDA, Chang KDD'23, thước đo chuyển giao |
| 5. Họ mô hình | Có khung từ review | Seq2Point, SGN; nhóm mô hình theo ba review | Chọn tổ hợp mô hình–loss chưa được thực hiện (chờ rà soát) |
