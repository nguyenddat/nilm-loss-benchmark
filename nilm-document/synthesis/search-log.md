---
type: search-log
status: in-progress
title: "Nhật ký tìm kiếm tài liệu"
tags:
  - nilm
  - literature-review
  - search-log
---

# Nhật ký tìm kiếm tài liệu

Ghi lại từng lượt tìm theo mục "Cách tìm và sàng lọc nguồn" của kế hoạch tổng quan tài liệu (kế hoạch: `synthesis/literature-review-plan`). Mỗi lượt ghi ngày, công cụ, truy vấn chính xác, số kết quả đã xem, ứng viên được giữ và lý do loại. Kết quả trong nhật ký chỉ là sàng lọc tiêu đề/tóm tắt/metadata; nội dung chỉ được dùng làm bằng chứng sau khi có ghi chú bài báo với vị trí nguồn.

Quy ước:

- "Số kết quả xem xét" là số mục mà công cụ trả về và đã đọc tiêu đề/đoạn trích, không phải số bài đã đọc toàn văn.
- Công cụ tìm web trả về tóm tắt do máy sinh kèm danh sách liên kết; mọi metadata (tác giả, năm, DOI) chỉ được ghi vào hàng đợi sau khi đối chiếu với Crossref, OpenAlex, arXiv API, trang nhà xuất bản hoặc PDF.
- Nội dung chỉ thấy qua đoạn trích/tóm tắt được gắn nhãn `chưa xác minh`.

## Lượt 1 — 2026-10-30: chủ đề 2 (loss) và chủ đề 3 (ràng buộc vật lý)

**Mục tiêu:** chủ đề 2 và 3 của kế hoạch chưa có nguồn nào; ba nguồn hiện có (REFIT, NILMTK, Comparability) chỉ về dữ liệu/đánh giá. Lượt này tìm nguồn trực tiếp về hàm mục tiêu huấn luyện, tái tạo công suất tổng, chính quy hóa theo thời gian và ràng buộc vật lý trong NILM, rồi truy vết từ các bài nền tảng.

**Công cụ:** WebSearch (công cụ tìm web của môi trường agent, chế độ `standard`); WebFetch tới Crossref REST API (`api.crossref.org`), OpenAlex API (`api.openalex.org`), arXiv API (`export.arxiv.org/api/query`), ML Anthology; tải PDF trực tiếp bằng `curl` rồi trích văn bản bằng `pdftotext`.

### Truy vấn tìm kiếm

| # | Truy vấn chính xác | Cụm | Số kết quả xem xét | Ứng viên giữ lại | Ghi chú / lý do loại |
| --- | --- | --- | --- | --- | --- |
| Q1 | `NILM energy disaggregation loss function comparison deep learning` | NILM × loss | 10 | PB-NILM (Gomes & Pereira 2020); Kelly & Knottenbelt 2015 | Loại: IMG-NILM, các review tổng quát và notebook Zenodo — không so sánh loss có kiểm soát; review chỉ dùng làm nguồn thứ cấp nếu cần. |
| Q2 | `NILM physics-informed energy conservation constraint aggregate consistency loss` | NILM × ràng buộc vật lý | 10 | Không có ứng viên đủ metadata | Kết quả chủ yếu PINN ngoài NILM (cơ học, HVAC, PDE) → loại vì ngoài miền. Hai mục NILM (KFUPM eprint 144059; luận văn METU 11511/113395) chỉ thấy đoạn trích, chưa xác minh tác giả/nội dung → ghi ở mục "Chưa xác minh" bên dưới. |
| Q3 | `energy disaggregation total variation regularization loss non-intrusive load monitoring` | NILM × total variation | 10 | Tang et al. 2014 (SSER, arXiv:1404.1884); Henriet et al. 2019 (IEEE SPL); He et al. 2019 (IEEE TSG) | Loại: trang tác giả paperswithcode/catalyzex (không phải nguồn gốc); review 2207.02009 để dành cho chủ đề tổng quan, chưa sàng lọc. |
| Q4 | `"energy disaggregation" "sum" aggregate reconstruction loss neural network appliance estimates match mains` | NILM × tái tạo công suất tổng | 10 | Zhang et al. 2018 (Seq2Point); Zhang et al. 2021 (Dual-DNN, arXiv:2106.00297) | Loại: trang geosurge.ai (nội dung tổng hợp, không phải nguồn học thuật gốc); VAE 2103.12177 và preprint engrxiv chưa liên quan trực tiếp đến loss tái tạo công suất tổng. |
| Q5 | `non-intrusive load monitoring non-negativity constraint output ReLU appliance power physical constraint deep learning` | NILM × không âm | 10 | Không thêm mới | Kết quả chỉ cho thấy ReLU ở lớp ẩn; không nguồn nào bàn ràng buộc không âm ở đầu ra một cách tường minh. Loại geosurge.ai (không phải nguồn gốc). |
| Q6 | `Kolter Jaakkola 2012 approximate inference additive factorial hidden Markov models energy disaggregation AISTATS` | Truy vết bài nền tảng | 10 | Kolter & Jaakkola 2012 (PMLR v22); Zhong et al. 2014 (SAC, NIPS) | Bản PDF PMLR tải được; đọc toàn văn. |
| Q7 | `BERT4NILM loss function MSE KL divergence soft-margin L1 on-state Yue 2020` | NILM × loss tổ hợp | 10 | Yue et al. 2020 (BERT4NILM) | Thành phần loss chỉ thấy qua bảng của bài thứ cấp → `chưa xác minh`; cần toàn văn. |
| Q8 | `PB-NILM pinball quantile regression loss non-intrusive load monitoring Gomes Pereira IEEE Access 2020 DOI` | NILM × loss | 10 | PB-NILM | Metadata xác minh qua OpenAlex. Toàn văn IEEE (OA, CC-BY) không tải được trong môi trường này (tệp rỗng; trang IEEE trả nội dung rỗng). |
| Q9 | `Zhong Goddard Sutton "Signal Aggregate Constraints" additive factorial HMM NIPS 2014` | NILM × ràng buộc tổng | 10 | Zhong et al. 2014 | URL PDF đúng lấy từ ML Anthology; đọc toàn văn. |
| Q10 | `Kelly Knottenbelt "Neural NILM: Deep neural networks applied to energy disaggregation" BuildSys 2015 doi` | Truy vết bài nền tảng | 10 | Kelly & Knottenbelt 2015 | DOI xác minh qua arXiv API và trang 1 PDF tác giả. PDF arXiv v3 tải được; đã sàng lọc toàn văn phần loss/kiến trúc. |
| Q11 | `Zhang Zhong Wang Goddard Sutton "Sequence-to-point learning" AAAI 2018 doi 10.1609/aaai` | Truy vết bài nền tảng | 10 | Không có kết quả đúng | Toàn bộ 10 kết quả không liên quan. Metadata lấy lại bằng Crossref (xem bảng xác minh). |
| Q12 | `"Towards reproducible state-of-the-art energy disaggregation" NILMTK-contrib BuildSys 2019 doi` | Truy vết bài nền tảng | 10 | Batra et al. 2019 (NILMTK-contrib) | DOI `10.1145/3360322.3360844` chỉ thấy qua đoạn trích tìm kiếm; tiêu đề có hai biến thể → `chưa xác minh` metadata đầy đủ. |
| Q13 | `physics-informed neural network NILM energy disaggregation 2023 2024 constraint loss aggregate` | NILM × ràng buộc vật lý (gần đây) | 10 | Không thêm mới | Kết quả lặp lại Q1/Q10. Không tìm thấy bài NILM 2023–2024 có loss bảo toàn năng lượng trong lượt này. |
| Q14 | `NILM "loss function" study weighted MSE on-off state imbalance comparison energy disaggregation evaluation` | NILM × loss/mất cân bằng | 10 | DualNILM (Wang et al., arXiv:2508.14600); target-weighted RMSE (core.ac.uk 15115668) | Loại: 2204.06767 (federated, MSE cơ bản, không so sánh loss); 1912.00759 (kiến trúc attention). Target-weighted RMSE chưa xác minh metadata. |
| Q15 | `"Refinement" optimization NILM output aggregate constraint IEEE Transactions on Smart Grid 2019 10.1109/TSG.2019.2906012` | NILM × hậu xử lý theo tổng | 10 | He et al. 2019 (TSG); bản workshop 2018 (Strathprints 63678) | He et al. dùng REFIT. Kho Strathprints từ chối kết nối (ECONNREFUSED) → chưa đọc được toàn văn. |
| Q16 | `multi-appliance NILM neural network output sum equals aggregate constraint softmax proportion "energy conservation"` | NILM × bảo toàn năng lượng | 10 | Không thêm mới | Kelly 2015 có từ khóa "energy conservation" nhưng theo nghĩa tiết kiệm năng lượng của hộ, không phải ràng buộc mô hình (xác minh trên PDF, tr. 1). |
| Q17 | `Subtask gated networks non-intrusive load monitoring Shin AAAI 2019 loss classification regression` | NILM × loss tổ hợp hồi quy/phân loại | 10 | Shin et al. 2019 (SGN) | Công thức loss chưa xem; cần toàn văn. |
| Q18 | `arXiv NILM "loss function" ablation transformer energy disaggregation 2022 2023 2024 regression classification combined loss` | NILM × ablation loss | 10 | NILMFormer (Petralia et al. 2025) — chỉ metadata | TransformNILM (EUSIPCO 2022), SAED: chưa xác minh metadata → để lượt sau. Loại 2505.04367 (luận văn tổng hợp, EV). |
| Q19 | `energy disaggregation post-processing projection appliance estimates sum to aggregate power non-negative least squares` | NILM × chiếu lên ràng buộc tổng | 10 | Rahimpour et al. 2017 (NMF sum-to-k) | Không tìm thấy bài dùng NNLS/chiếu simplex tường minh. |

Tổng: 19 truy vấn WebSearch, khoảng 190 mục được xem ở mức tiêu đề/đoạn trích.

### Xác minh metadata và truy cập toàn văn

| Nguồn | Cách xác minh | Kết quả |
| --- | --- | --- |
| Zhang et al. 2018, Seq2Point | Crossref `query.bibliographic`; arXiv API `1612.09106` | DOI `10.1609/aaai.v32i1.11873`, AAAI vol. 32, no. 1; arXiv v3 ghi journal_ref AAAI-18. PDF arXiv v3 tải được. |
| He et al. 2019 | Crossref `works/10.1109/TSG.2019.2906012` | IEEE TSG 10(6):6472–6480, 11/2019. Toàn văn chưa truy cập được. |
| Gomes & Pereira 2020, PB-NILM | OpenAlex `doi:10.1109/ACCESS.2020.2978513` (Crossref trả 429) | IEEE Access 8:48386–48398, gold OA CC-BY. Toàn văn chưa tải được. |
| Yue et al. 2020, BERT4NILM | Crossref `query.bibliographic` | DOI `10.1145/3427771.3429390`, NILM'20 workshop, tr. 89–93. |
| Kelly & Knottenbelt 2015 | arXiv API `1507.06594`; trang 1 PDF | DOI `10.1145/2821650.2821672`, BuildSys'15. |
| Tang et al. 2014 (SSER); Shin et al. 2018/2019 (SGN); Zhang et al. 2021 (Dual-DNN); Wang et al. 2025 (DualNILM) | arXiv API | Tiêu đề/tác giả/ngày xác minh; DualNILM có DOI `10.1145/3744255.3798113`. |
| Rahimpour et al. 2017; Petralia et al. 2025 (NILMFormer) | arXiv API | DOI `10.1109/TPWRS.2017.2660246`; DOI `10.1145/3711896.3737251` (KDD '25). |
| Henriet et al. 2019 | Crossref `query.bibliographic` | DOI `10.1109/LSP.2019.2941428`, IEEE SPL 26(11):1643–1647. |
| Zhong et al. 2014 (SAC) | ML Anthology; PDF NeurIPS | NIPS 2014, tr. 3590–3598; PDF tải được (URL đúng: `bf64575b...-Paper.pdf`). |
| Kolter & Jaakkola 2012 | Trang PMLR v22; PDF | AISTATS 2012, PMLR 22:1472–1482; PDF tải được. |

### Ứng viên chưa xác minh (không đưa vào hàng đợi)

- KFUPM eprint 144059 ("Cloud-Edge Collaborative Framework ... Appliance Consumption Monitoring"): đoạn trích nói có loss vật lý; chưa xác minh tác giả, nơi công bố và công thức.
- Luận văn METU `11511/113395`: đoạn trích nói hậu xử lý để tổng ước lượng khớp công suất tổng; chưa xác minh.
- Target-weighted RMSE (PAKDD 2016 workshop, core.ac.uk 15115668): chưa xác minh metadata.
- TransformNILM (EUSIPCO 2022), SAED: chưa xác minh metadata.

### Loại trừ ở mức sàng lọc

- Các bài PINN ngoài NILM (arXiv 2105.00075, 2302.11002, Oxford ORA ...): ngoài miền; có thể dùng sau làm tài liệu phương pháp chung về ràng buộc mềm/cứng, nhưng không là bằng chứng NILM.
- Trang tổng hợp không phải nguồn gốc (geosurge.ai, paperswithcode, catalyzex, liner.com): không dùng làm nguồn.

### Kết quả lượt 1

- Đọc toàn văn và tạo ghi chú bài báo cho ba nguồn: Kolter & Jaakkola 2012, Zhong et al. 2014, Zhang et al. 2018 (xem danh mục bài báo, `papers/index.md`).
- Kelly & Knottenbelt 2015: đã sàng lọc toàn văn phần loss/kiến trúc (MSE là objective cho mọi mạng, mục 2, PDF arXiv tr. 2–3; lớp ra tuyến tính, mục 4, PDF tr. 5–6); chưa tạo ghi chú riêng.
- Ứng viên còn lại ghi ở hàng đợi đọc (`inbox/reading-queue.md`).

### Khoảng trống sau lượt 1

- Chưa tìm thấy nguồn NILM nào đo **tần suất/mức vi phạm** C1/C2/C3 của dự đoán mạng nơ-ron; các nguồn đã đọc dùng ràng buộc tổng năng lượng theo thiết bị (SAC) hoặc thành phần phần dư, không phải bất đẳng thức theo từng mẫu như C3.
- Chưa có nguồn đọc toàn văn về so sánh loss có kiểm soát (PB-NILM, BERT4NILM, SGN chưa đọc).
- Chưa có nguồn về nguồn gốc giới hạn `P_i^max` độc lập (C2).
- Chưa chạy: tìm trên Google Scholar/IEEE Xplore/Scopus trực tiếp; truy vết trích dẫn xuôi của Zhong 2014 và Kolter 2012; truy vấn về điện mặt trời/net load trong NILM (liên quan C3); truy vấn "soft-DTW", "focal loss", "asymmetric loss" NILM; truy vấn chủ đề 4 (nhiễu, chuyển nhà).

## Lượt 2 — 2026-10-30: chủ đề 4 (độ vững), loss khác, ràng buộc vật lý, PV, trích dẫn xuôi; đổi hướng sang top-down

**Mục tiêu ban đầu:** lấp khoảng trống lượt 1 — chủ đề 4 (chuyển hộ/bộ dữ liệu, nhiễu), loss khác (focal, quantile, soft-DTW, đa nhiệm), ràng buộc vật lý (C1–C3, định mức), điện mặt trời sau công tơ (liên quan C3 với REFIT), truy vết trích dẫn xuôi của Zhong 2014 và Kolter 2012, xử lý các ứng viên lượt 1.

**Quyết định của người dùng (2026-10-30):** bỏ qua PB-NILM (`10.1109/ACCESS.2020.2978513`) và He và cộng sự 2019 (`10.1109/TSG.2019.2906012`) vì không truy cập được toàn văn; không tìm bài thay thế cho riêng hai bài này.

**Đổi hướng giữa lượt (theo yêu cầu người dùng, qua agent chính):** dừng đọc sâu bài lá sau pha A; chuyển sang **top-down**: đọc review/survey → dựng taxonomy → chọn nhánh liên quan → chọn bài lá. Ghi chú lá đã tạo trong pha A được giữ nguyên.

**Công cụ:** WebSearch; Crossref REST API (`query.bibliographic`, `works/<doi>`); OpenAlex API (metadata, OA, trích dẫn xuôi); arXiv API qua `https` (bản `http` trả rỗng); tải PDF bằng `curl` vào thư mục tạm riêng; trích văn bản và render trang bằng PyMuPDF qua `uv run python -I`.

### Pha A — bài lá (trước khi đổi hướng)

| # | Truy vấn chính xác | Cụm | Số kết quả xem xét | Ứng viên giữ lại | Ghi chú / lý do loại |
| --- | --- | --- | --- | --- | --- |
| R1 | `NILM cross-house generalization unseen houses transfer learning deep neural network energy disaggregation` | Chủ đề 4 | ~10 | D'Incecco và cộng sự 2020 (TSG); Murray và cộng sự 2019 (ICASSP) | Các kết quả khác lặp lại hoặc không phải nguồn gốc. |
| R2 | `NILM domain adaptation cross-dataset train UK-DALE test REFIT energy disaggregation` | Chủ đề 4 | ~10 | NILMBench2026; Liu và cộng sự, UDA (TII 2022) | |
| R3 | `non-intrusive load monitoring robustness measurement noise noisy aggregate signal evaluation deep learning` | Chủ đề 4 | ~10 | Klemenjak và cộng sự 2021 (real vs denoised) | |
| R4 | `NILM focal loss OR quantile loss OR asymmetric loss energy disaggregation imbalance appliance` | Loss khác | ~10 | Không thêm mới ngoài PB-NILM (đã bỏ qua) | Đoạn trích không đủ để xác minh bài có focal loss. |
| R5 | `energy disaggregation soft-DTW loss OR dynamic time warping loss neural network appliance` | Loss khác | ~10 | Không | DTW chủ yếu dùng làm đặc trưng/đo tương tự, không làm loss huấn luyện NILM → loại. |
| R6 | `physics-informed non-intrusive load monitoring energy conservation constraint aggregate power sum appliance outputs deep learning` | Ràng buộc vật lý | ~10 | RAPC-Net (Li & Sun 2026, Applied Sciences) | Đoạn trích nói có loss tái tạo aggregate, hinge ước lượng quá và thước đo “Over-ratio” — **chưa xác minh**; MDPI chặn tải tự động. |
| R7 | `NILM sum-to-aggregate loss multi-appliance overestimation constraint predicted sum exceeds mains` | C3 | ~10 | MATNilm (TII 2023); Liu & Fan 2026 (arXiv 2609.18315) | |
| R8 | `non-intrusive load monitoring rated power nameplate appliance maximum power clipping output constraint` | C2 | ~10 | Không | Không có nguồn học thuật nêu P_max độc lập. |
| R9 | `NILM behind-the-meter solar PV net load energy disaggregation household rooftop` | PV / C3 | ~10 | Chen & Ardakanian 2022 (SEGAN); DualNILM (đã có) | |
| R10 | `seq2point weighted loss on/off state low power imbalance regression classification multi-task loss NILM` | Loss đa nhiệm | ~10 | SGN (đã có; đọc toàn văn) | |
| R11 | `"loss functions" comparison NILM MSE MAE Huber empirical study energy disaggregation` | So sánh loss | ~10 | Không | Không thấy so sánh loss có kiểm soát trong NILM. |
| R12 | `unsupervised domain adaptation NILM adversarial energy disaggregation unseen dataset` | Chủ đề 4 | ~10 | Chang và cộng sự KDD'23; Liu UDA TII (lặp) | |
| R13 | `NILM negative power predictions neural network output non-negative ReLU final layer appliance estimate clipped zero` | C1 | ~10 | Không | Không nguồn nào đo tần suất dự đoán âm. |
| R14 | `"NILM Domain Adaptation: When Does It Work" OR "Taming the Domain Shift in Multi-source Learning for Energy Disaggregation"` | Chủ đề 4 | ~10 | Không | Tiêu đề không được Crossref/arXiv xác nhận trong lượt này → không đưa vào hàng đợi. |
| R15 | `NILM evaluation physical consistency metric fraction of time predicted appliance sum exceeds aggregate violation rate` | Thước đo vi phạm | ~10 | RAPC-Net (lặp) | |
| R16 | `NILM REFIT houses with solar panels excluded net metering export negative aggregate preprocessing` | PV / REFIT | ~10 | D'Incecco 2020 (lặp) | |
| R17 | `BERT4NILM bidirectional transformer non-intrusive load monitoring pdf loss function KL divergence soft margin` | Loss ghép | ~10 | BERT4NILM (đã có) | PDF ACM chưa truy cập. |
| R18 | `household appliance rated power database typical maximum power kettle washing machine dishwasher survey measurement UK` | C2 | ~10 | Không (chỉ nguồn xám) | Chỉ có trang phi học thuật (Electrical Safety First) → không dùng làm căn cứ P_max; Household Electricity Survey là ứng viên cần tìm tiếp. |

**Trích dẫn xuôi (OpenAlex):** `api.openalex.org/works?filter=cites:<W>,title_and_abstract.search:<kw>&per_page=50`, với W ∈ {W2115033874 (Zhong 2014), W1138573735 (Kolter 2012)} × kw ∈ {constraint, aggregate, physics, consistency} = 8 truy vấn.

| Bài được trích | constraint | aggregate | physics | consistency | Kết quả |
| --- | --- | --- | --- | --- | --- |
| Zhong 2014 (W2115033874) | 2 | 38 | 0 | 0 | Đã xem tiêu đề; không có nguồn mới đo vi phạm C3. |
| Kolter 2012 (W1138573735) | 23 | 149 (xem 50 đầu) | 0 | 3 | Ghi nhận Cui và cộng sự 2019 (TSG, lọc nền) và “Fundamental limits of NILM” (2014) — metadata chưa xác minh đầy đủ. |

### Pha B — review/survey (sau khi đổi hướng)

**Tiêu chí chọn review:** (1) review/survey về NILM, 2019–2026; (2) phạm vi gồm DNN tần số thấp hoặc chủ đề liên quan (transfer, đánh giá, tin cậy); (3) nơi công bố có bình duyệt; (4) toàn văn truy cập hợp lệ (OA, kho tổ chức hoặc arXiv); (5) ưu tiên review có mục về loss, kịch bản đánh giá, độ vững. **Tiêu chí loại:** chỉ có trên ResearchGate hoặc không xác minh được metadata; toàn văn đóng (giữ trong hàng đợi, không đọc); review chỉ về tần số cao hoặc ứng dụng phi dân dụng.

| # | Truy vấn chính xác | Số kết quả xem xét | Ứng viên giữ lại | Ghi chú |
| --- | --- | --- | --- | --- |
| V1 | `review deep neural networks low-frequency non-intrusive load monitoring survey` | ~10 | Huber và cộng sự 2021 (Energies) | Đọc sâu. |
| V2 | `non-intrusive load monitoring review 2023 2024 2025 deep learning taxonomy challenges` | ~10 | Saleem và cộng sự 2025; Xiang và cộng sự 2026; arXiv 2306.05017; arXiv 2403.06474 | Review “Observability regimes” chỉ thấy trên ResearchGate → loại (chưa xác minh). |
| V3 | `NILM transfer learning generalization review survey cross-domain` | ~10 | Schirmer & Mporas 2023 (TSG) | Toàn văn đóng. |
| V4 | `NILM performance evaluation metrics datasets review survey` | ~10 | Pereira & Nunes 2018 (WIREs); Yan và cộng sự 2026 (RSER) | Pereira & Nunes: metadata chưa xác minh đầy đủ. |
| V5 | `energy disaggregation review physics-informed OR physical constraints OR trustworthy NILM survey` | ~10 | Kaselimi và cộng sự 2022 (Sensors); Angelis 2022 (Energy and Buildings) | Không tìm thấy review chuyên về ràng buộc vật lý trong NILM. |

Đọc sâu: Huber 2021, Kaselimi 2022 (đầy đủ), Saleem 2025 (có chọn lọc). Lý do chọn: ba góc khác nhau (DNN tần số thấp có chiến lược tìm rõ; khung tin cậy/thế lưỡng nan thiết kế; review rộng mới nhất 2025), đều truy cập hợp lệ.

Tổng lượt 2: 23 truy vấn WebSearch (~230 mục ở mức tiêu đề/đoạn trích), 8 truy vấn OpenAlex trích dẫn xuôi, cùng các lần tra Crossref/arXiv/OpenAlex để xác minh.

### Xác minh metadata và truy cập toàn văn (lượt 2)

| Nguồn | Cách xác minh | Kết quả |
| --- | --- | --- |
| Shin và cộng sự 2019, SGN | Crossref; arXiv API 1811.06692 | DOI `10.1609/aaai.v33i01.33011150`, AAAI 33(01):1150–1157. Đọc arXiv v1. |
| Huber và cộng sự 2021 | Crossref; OpenAlex (gold OA) | DOI `10.3390/en14092390`, Energies 14(9):2390. MDPI chặn; đọc bản xuất bản từ kho HSLU. |
| Kaselimi và cộng sự 2022 | Crossref; arXiv API 2207.02009 | DOI `10.3390/s22155872`, Sensors 22(15):5872. Đọc arXiv v1; bản Sensors chưa đối chiếu. |
| Saleem và cộng sự 2025 | Crossref; OpenAlex (hybrid OA) | DOI `10.1007/s10489-025-06921-4`, Applied Intelligence 55(15):1020. PDF Springer tải được. |
| D'Incecco và cộng sự 2020 | Crossref; arXiv API 1902.08835 | DOI `10.1109/tsg.2019.2938068`, TSG 11(2):1419–1429. Đọc arXiv v3. |
| Klemenjak và cộng sự 2021 | Crossref; arXiv API 2008.10985 | DOI `10.1186/s42162-021-00137-9`, Energy Informatics 4(1):3, CC BY. Đọc arXiv v2. |
| Liu & Fan 2026 | arXiv API 2609.18315 | Preprint v1; đã đọc toàn văn. |
| Li & Sun 2026, RAPC-Net | Crossref | DOI `10.3390/app16178866`, Applied Sciences 16(17):8866, CC BY. Toàn văn bị MDPI chặn; **nội dung chưa xác minh**. |
| MATNilm | Crossref | DOI `10.1109/tii.2023.3301026`, TII 20(3):3177–3187. Chỉ sàng lọc. |
| NILMBench2026 | Crossref | DOI `10.1145/3744256.3812587`, CC BY. Chưa đọc. |
| NILMTK-contrib (Batra và cộng sự 2019) | Crossref | DOI `10.1145/3360322.3360844` xác minh, tr. 193–202, 9 tác giả. |
| Chang và cộng sự KDD'23 | Crossref | DOI `10.1145/3580305.3599910`, tr. 3805–3816. |
| Liu và cộng sự, UDA | Crossref | DOI `10.1109/tii.2021.3065934`, TII 18(1):266–277. |
| Murray và cộng sự 2019 | Crossref | DOI `10.1109/icassp.2019.8682486`, ICASSP 2019, tr. 8330–8334. Tải Strathprints thất bại. |
| Bonfigli và cộng sự 2018 | Crossref | DOI `10.1016/j.enbuild.2017.11.054`, Energy & Buildings 158:1461–1474. |
| Chen & Ardakanian 2022 | Crossref; arXiv 2105.08122 | DOI `10.1016/j.segan.2022.100813`, SEGAN 32:100813. |
| Review chưa đọc | Crossref/OpenAlex | Yan 2026 RSER 226:116255 `10.1016/j.rser.2025.116255` (green OA); Schirmer & Mporas 2023 TSG 14(1):769–784 `10.1109/tsg.2022.3189598` (đóng); Angelis 2022 E&B 261:111951 `10.1016/j.enbuild.2022.111951` (đóng); Xiang 2026 Energies 19(8):1883 `10.3390/en19081883` (MDPI chặn); arXiv 2306.05017; arXiv 2403.06474 (đã tải, chưa đọc). |

### Kết quả lượt 2

- Ghi chú bài lá (pha A): `papers/2019-shin-subtask-gated-networks.md` (extracted).
- Đọc toàn văn nhưng chưa tạo ghi chú (dừng theo đổi hướng): D'Incecco 2020, Klemenjak 2021, Liu & Fan 2026 → `screened` trong hàng đợi.
- Ghi chú review (pha B): `papers/2021-huber-dnn-low-frequency-nilm-review.md`, `papers/2022-kaselimi-trustworthy-nilm-review.md`, `papers/2025-saleem-ml-dl-nilm-review.md` (extracted; Saleem đọc có chọn lọc).
- Taxonomy đề xuất: ban đầu ở `synthesis/taxonomy-phuong-phap-nilm.md` (draft); ngày 2026-10-30 chuyển sang `notes/NILM-methodology/Taxonomy phương pháp NILM.md` sau khi rà soát ba review (ba review chuyển `reviewed`).

### Khoảng trống sau lượt 2

- Vẫn chưa đọc toàn văn nguồn nào **đo** vi phạm C1/C2/C3; RAPC-Net là ứng viên duy nhất (chưa xác minh, cần tải thủ công).
- So sánh loss có kiểm soát: chỉ có ablation bỏ L_on của SGN (một lần chạy); Huber 2021 nêu chưa có so sánh có hệ thống đến 11/2020; Kaselimi 2022 và Saleem 2025 không có mục loss.
- Chưa có nguồn học thuật về P_max độc lập (C2).
- Chưa đọc review 2023–2026 ngoài Saleem 2025; chưa tìm trực tiếp trên Scopus/IEEE Xplore.
- MDPI chặn tải tự động (RAPC-Net, Xiang 2026, bản Sensors của Kaselimi) → cần người dùng tải thủ công.
