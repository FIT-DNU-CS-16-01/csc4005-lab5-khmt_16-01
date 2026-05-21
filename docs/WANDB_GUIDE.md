# W&B Guide

## 1. Đăng nhập W&B

```bash
wandb login
```

Sau đó dán API key từ tài khoản W&B.

## 2. Project thống nhất

Tất cả sinh viên dùng cùng tên project:

```text
csc4005-lab6-mit-indoor-vit
```

## 3. Chạy với W&B

```bash
python -m src.train \
  --data_dir /path/to/mit_indoor_smartcampus_5 \
  --project csc4005-lab5-mit-indoor-vit \
  --run_name vit_b16_head_only \
  --train_mode head_only \
  --use_wandb
```

## 4. Metric cần log

Mỗi epoch:

```text
train_loss
val_loss
train_acc
val_acc
val_macro_f1
lr
epoch_time_sec
```

Cuối run:

```text
test_acc
test_macro_f1
best_val_acc
best_val_macro_f1
total_params
trainable_params
trainable_ratio
```

## 5. Evidence khi nộp bài

Trong báo cáo, sinh viên cần dán:

- link W&B project hoặc run;
- screenshot learning curves;
- bảng hyperparameter chính;
- nhận xét kết quả.
