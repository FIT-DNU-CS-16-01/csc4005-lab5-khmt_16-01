# Dataset Guide – MIT Indoor Scenes 67 subset

## 1. Dataset gốc

Dataset được sử dụng: **MIT Indoor Scenes 67**.

Sinh viên cần tải dataset từ nguồn chính thức của MIT Indoor Scenes 67, sau đó giải nén về máy cá nhân. Repo này không lưu dữ liệu ảnh để tránh dung lượng lớn và vấn đề bản quyền/phân phối lại.

## 2. Subset 5 lớp

Lab sử dụng 5 lớp gần với bối cảnh đại học:

```text
classroom
computerroom
library
corridor
office
```

Ý nghĩa trong Smart Campus:

| Lớp | Ý nghĩa |
|---|---|
| classroom | Phòng học |
| computerroom | Phòng máy |
| library | Thư viện |
| corridor | Hành lang |
| office | Văn phòng/khu làm việc |

## 3. Chuẩn bị subset bằng script

Ví dụ:

```bash
python -m src.prepare_subset \
  --source_dir /path/to/indoorCVPR_09/Images \
  --output_dir /path/to/mit_indoor_smartcampus_5 \
  --classes classroom computerroom library corridor office \
  --max_per_class 400
```

Sau khi chạy, cấu trúc nên là:

```text
mit_indoor_smartcampus_5/
├── classroom/
├── computerroom/
├── library/
├── corridor/
└── office/
```

## 4. Lưu ý

- Không commit thư mục ảnh vào GitHub.
- Không đổi tên lớp nếu không cần thiết.
- Nếu số ảnh mỗi lớp quá lệch, nên dùng `--max_per_class` để cân bằng tương đối.
- Nếu gặp lớp không tồn tại, kiểm tra lại tên thư mục trong dataset gốc.
