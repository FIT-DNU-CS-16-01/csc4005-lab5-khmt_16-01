# RUBRIC_LAB6 – CSC4005 Lab 5: Vision Transformer for Smart Campus Scene Classification

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Học phần | CSC4005 – Học sâu |
| Lab | Lab 5 |
| Chủ đề | Vision Transformer cho phân loại ngữ cảnh không gian Smart Campus |
| Dataset | MIT Indoor Scenes 67 – subset 5 lớp |
| Công cụ bắt buộc | GitHub, W&B, PyTorch/Torchvision |
| Tổng điểm | 10 điểm |

Lab này đánh giá năng lực triển khai một pipeline học sâu hoàn chỉnh với Vision Transformer: chuẩn bị dữ liệu, huấn luyện mô hình, theo dõi thí nghiệm bằng W&B, đánh giá kết quả, phân tích lỗi và liên hệ với lý thuyết Transformers/ViT.

---

## 2. Yêu cầu đầu ra bắt buộc

Sinh viên cần nộp đầy đủ các minh chứng sau trong repo GitHub:

```text
README.md hoặc báo cáo theo REPORT_TEMPLATE.md
outputs/<run_name>/metrics.json
outputs/<run_name>/history.csv
outputs/<run_name>/curves.png
outputs/<run_name>/confusion_matrix.png
outputs/<run_name>/class_to_idx.json
Link W&B dashboard hoặc W&B run
Code đã hoàn thiện trong thư mục src/
```

Lưu ý:

- Không commit dataset ảnh gốc lên GitHub.
- Không commit file model quá lớn nếu không được yêu cầu.
- Link W&B cần mở được hoặc có ảnh chụp minh chứng trong báo cáo.
- Kết quả cần có khả năng tái lập ở mức cơ bản thông qua lệnh chạy được mô tả trong README hoặc báo cáo.

---

## 3. Thang điểm tổng quát

| Thành phần đánh giá | Điểm |
|---|---:|
| A. Chuẩn bị dữ liệu MIT Indoor Scenes 67 subset | 1.5 |
| B. Cài đặt và chạy pipeline ViT | 2.0 |
| C. Sử dụng W&B để theo dõi thí nghiệm | 1.5 |
| D. Đánh giá mô hình và lưu artefact | 1.5 |
| E. Phân tích lỗi và nhận xét kết quả | 1.5 |
| F. Liên hệ lý thuyết Transformers/ViT | 1.0 |
| G. Tổ chức repo, tái lập và trình bày | 1.0 |
| **Tổng** | **10** |

---

## 4. Rubric chi tiết

### A. Chuẩn bị dữ liệu MIT Indoor Scenes 67 subset – 1.5 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Chuẩn bị đúng subset 5 lớp `classroom`, `computerroom`, `library`, `corridor`, `office`; cấu trúc thư mục rõ ràng; số lượng ảnh mỗi lớp được thống kê; không commit dữ liệu lên GitHub; có mô tả nguồn dữ liệu và cách chuẩn bị. | 1.3–1.5 |
| Đạt | Chuẩn bị được phần lớn subset 5 lớp; cấu trúc dữ liệu chạy được; có mô tả ngắn nhưng chưa thống kê đầy đủ hoặc chưa giải thích rõ quy trình chuẩn bị. | 0.9–1.2 |
| Chưa đạt | Dữ liệu thiếu lớp, sai cấu trúc, không chạy được ngay; chưa nêu nguồn dữ liệu hoặc chưa giải thích cách tạo subset. | 0.4–0.8 |
| Không đạt | Không chuẩn bị được dữ liệu hoặc dùng dataset không đúng yêu cầu. | 0–0.3 |

Minh chứng cần có:

```text
class_to_idx.json
mô tả dataset trong báo cáo
số ảnh từng lớp
lệnh prepare_subset hoặc mô tả thủ công
```

---

### B. Cài đặt và chạy pipeline ViT – 2.0 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Chạy được pipeline huấn luyện ViT hoàn chỉnh; dùng đúng `vit_b_16` hoặc model ViT tương đương; chạy được chế độ `head_only`; biết điều chỉnh batch size, learning rate, epoch; code rõ ràng và không phá cấu trúc starter. | 1.7–2.0 |
| Đạt | Chạy được baseline ViT; có kết quả train/validation/test; một số tham số chưa tối ưu nhưng pipeline cơ bản hoạt động. | 1.2–1.6 |
| Chưa đạt | Code còn lỗi nhỏ hoặc chỉ chạy được một phần; kết quả chưa đầy đủ; chưa hiểu rõ `head_only` và `finetune`. | 0.6–1.1 |
| Không đạt | Không chạy được mô hình hoặc không dùng ViT. | 0–0.5 |

Minh chứng cần có:

```text
lệnh chạy trong README hoặc báo cáo
outputs/<run_name>/best_model.pt hoặc mô tả nơi lưu model
outputs/<run_name>/config.json
history.csv
metrics.json
```

Gợi ý kiểm tra:

```bash
python -m src.train \
  --data_dir /path/to/mit_indoor_smartcampus_5 \
  --run_name vit_b16_head_only \
  --train_mode head_only \
  --use_wandb
```

---

### C. Sử dụng W&B để theo dõi thí nghiệm – 1.5 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Có W&B project/run rõ ràng; log đầy đủ train loss, validation loss, accuracy, macro-F1, learning rate, epoch time; có cấu hình hyperparameter; dashboard hoặc link run được đưa vào báo cáo. | 1.3–1.5 |
| Đạt | Có dùng W&B và log được các metric chính; thiếu một vài thông tin như epoch time, trainable parameters hoặc ảnh confusion matrix. | 0.9–1.2 |
| Chưa đạt | Có tạo run W&B nhưng log thiếu nhiều, khó theo dõi quá trình huấn luyện hoặc link không rõ ràng. | 0.4–0.8 |
| Không đạt | Không dùng W&B hoặc không có minh chứng W&B. | 0–0.3 |

Metric tối thiểu cần log:

```text
train_loss
val_loss
train_acc
val_acc
val_macro_f1
lr
epoch_time_sec
```

Thông tin cuối run nên có:

```text
test_acc
test_macro_f1
best_val_acc hoặc best_val_macro_f1
total_params
trainable_params
trainable_ratio
```

---

### D. Đánh giá mô hình và lưu artefact – 1.5 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Có đầy đủ accuracy, macro-F1, learning curves, confusion matrix; kết quả được lưu đúng thư mục `outputs/<run_name>/`; báo cáo đọc được kết quả và nêu nhận xét dựa trên số liệu. | 1.3–1.5 |
| Đạt | Có metric chính và ít nhất một biểu đồ; kết quả lưu được nhưng tổ chức chưa thật rõ hoặc nhận xét còn ngắn. | 0.9–1.2 |
| Chưa đạt | Có kết quả nhưng thiếu nhiều artefact quan trọng như confusion matrix hoặc history.csv; khó kiểm chứng. | 0.4–0.8 |
| Không đạt | Không có kết quả đánh giá hoặc chỉ nêu kết quả bằng lời. | 0–0.3 |

Artefact tối thiểu:

```text
metrics.json
history.csv
curves.png
confusion_matrix.png
```

---

### E. Phân tích lỗi và nhận xét kết quả – 1.5 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Phân tích được lớp nào dễ đúng, lớp nào dễ nhầm; dùng confusion matrix để giải thích; nêu được nguyên nhân có thể từ dữ liệu, bối cảnh ảnh, số lượng mẫu, augmentation hoặc giới hạn của mô hình; đề xuất cải thiện hợp lý. | 1.3–1.5 |
| Đạt | Có nhận xét kết quả và nêu được một số lỗi chính; phân tích còn đơn giản nhưng dựa trên số liệu. | 0.9–1.2 |
| Chưa đạt | Nhận xét chung chung, ít liên hệ với confusion matrix hoặc không giải thích nguyên nhân. | 0.4–0.8 |
| Không đạt | Không có phần phân tích lỗi. | 0–0.3 |

Câu hỏi gợi ý:

1. Lớp nào có accuracy tốt nhất?
2. Lớp nào bị nhầm nhiều nhất?
3. `corridor` có bị nhầm với `office` hoặc `classroom` không? Vì sao?
4. Ảnh trong lớp nào có độ đa dạng cao nhất?
5. Nếu cải thiện, nên tăng dữ liệu, đổi augmentation, fine-tune toàn bộ hay đổi mô hình?

---

### F. Liên hệ lý thuyết Transformers/ViT – 1.0 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Giải thích đúng mối liên hệ giữa ảnh, patch, patch embedding, positional embedding, transformer encoder và classification head; phân biệt được `head_only` và `finetune`; liên hệ được vì sao pretrained ViT hữu ích với dataset nhỏ. | 0.9–1.0 |
| Đạt | Trình bày được các ý chính của ViT nhưng còn thiếu chiều sâu hoặc chưa liên hệ nhiều với kết quả thực nghiệm. | 0.6–0.8 |
| Chưa đạt | Giải thích còn nhầm lẫn, ví dụ nhầm patch embedding với convolution thông thường hoặc chưa hiểu vai trò positional embedding. | 0.3–0.5 |
| Không đạt | Không có phần liên hệ lý thuyết. | 0–0.2 |

Nội dung bắt buộc cần trả lời:

```text
1. Patch embedding là gì?
2. Vì sao ViT cần positional embedding?
3. Classification head làm nhiệm vụ gì?
4. Vì sao head_only train nhanh hơn finetune?
5. Khi nào nên fine-tune toàn bộ mô hình?
```

---

### G. Tổ chức repo, tái lập và trình bày – 1.0 điểm

| Mức đạt | Mô tả | Điểm |
|---|---|---:|
| Tốt | Repo sạch, đúng cấu trúc starter; README/báo cáo có lệnh chạy rõ ràng; không commit file thừa; code dễ đọc; kết quả có thể tái lập; báo cáo trình bày mạch lạc. | 0.9–1.0 |
| Đạt | Repo tương đối đầy đủ; có hướng dẫn chạy; còn một số file thừa hoặc trình bày chưa thật gọn. | 0.6–0.8 |
| Chưa đạt | Repo khó theo dõi; thiếu hướng dẫn chạy; đặt file lộn xộn; kết quả khó tái lập. | 0.3–0.5 |
| Không đạt | Repo thiếu nhiều file chính hoặc không thể kiểm tra. | 0–0.2 |

Có thể kiểm tra nhanh:

```bash
python ci/check_structure.py
```

---

## 5. Điểm cộng khuyến khích

Sinh viên có thể được cộng tối đa **0.5 điểm khuyến khích**, nhưng tổng điểm cuối cùng không vượt quá 10.

| Nội dung cộng điểm | Điểm cộng tối đa |
|---|---:|
| So sánh `head_only` và `finetune` bằng số liệu thực nghiệm | +0.2 |
| Có thêm phân tích trainable parameters và thời gian train | +0.1 |
| Có thử nghiệm augmentation/no augmentation | +0.1 |
| Có phân tích mẫu ảnh bị dự đoán sai kèm hình minh họa | +0.1 |

---

## 6. Các lỗi bị trừ điểm mạnh

| Lỗi | Mức trừ gợi ý |
|---|---:|
| Không dùng W&B | -1.0 đến -1.5 |
| Không dùng ViT | -1.5 đến -2.5 |
| Dùng dataset khác mà không giải thích | -1.0 đến -2.0 |
| Không có confusion matrix | -0.5 đến -1.0 |
| Không có báo cáo hoặc báo cáo quá sơ sài | -1.0 đến -2.0 |
| Commit dataset hoặc file model quá lớn lên GitHub | -0.5 đến -1.5 |
| Code không chạy được do lỗi import/cấu trúc | -1.0 đến -3.0 |
| Sao chép kết quả mà không có minh chứng chạy | -2.0 đến -4.0 |

---

