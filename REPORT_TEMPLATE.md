# CSC4005 Lab 5 Report – Vision Transformer for Smart Campus Scene Classification

## 1. Thông tin nhóm/cá nhân

- Họ tên:
- Mã sinh viên:
- Lớp:
- Link GitHub repo:
- Link W&B dashboard:

## 2. Mô tả bài toán

Viết ngắn gọn 5–7 dòng:

- Bài toán cần giải quyết là gì?
- Vì sao bài toán này phù hợp với bối cảnh Smart Campus?
- Các lớp cần phân loại là gì?

## 3. Dữ liệu

| Nội dung | Mô tả |
|---|---|
| Dataset gốc | MIT Indoor Scenes 67 |
| Subset sử dụng | classroom, computerroom, library, corridor, office |
| Số ảnh mỗi lớp | ... |
| Train/Val/Test split | ... |
| Tiền xử lý | resize, normalization, augmentation |

## 4. Mô hình ViT

Mô tả ngắn gọn kiến trúc:

```text
image → patch embedding → positional embedding → transformer encoder → classification head
```

Điền thông số:

| Thành phần | Giá trị |
|---|---|
| model_name | ... |
| train_mode | head_only / finetune |
| img_size | ... |
| batch size | ... |
| số epoch | ... |
| learning rate | ... |
| optimizer | ... |
| total params | ... |
| trainable params | ... |
| trainable ratio | ... |

## 5. Kết quả

| Metric | Validation | Test |
|---|---:|---:|
| Accuracy | ... | ... |
| Macro-F1 | ... | ... |
| Best epoch | ... | ... |

Chèn ảnh:

- Learning curves
- Confusion matrix

## 6. Phân tích lỗi

Trả lời:

1. Lớp nào mô hình dự đoán tốt nhất?
2. Lớp nào dễ bị nhầm nhất?
3. Cặp lớp nào dễ nhầm với nhau? Vì sao?
4. Dữ liệu có mất cân bằng không?
5. Augmentation có giúp cải thiện không?

## 7. Liên hệ với lý thuyết ViT

Trả lời ngắn gọn:

1. Patch embedding trong ViT tương tự bước nào trong NLP?
2. Vì sao ViT cần positional embedding?
3. Vì sao `head_only` train nhanh hơn `finetune`?
4. Khi nào nên fine-tune toàn bộ backbone?

## 8. W&B evidence

- Link run:
- Screenshot dashboard:
- Các hyperparameter chính:
- Các metric được log:

## 9. Kết luận

Viết 5–8 dòng:

- Mô hình đạt kết quả như thế nào?
- ViT có ưu/nhược điểm gì trên dataset nhỏ?
- Nếu cải thiện, bạn sẽ cải thiện dữ liệu, mô hình hay quy trình huấn luyện?
