# Ứng dụng Tổng hợp Dữ liệu Phường/Xã

Ứng dụng web Django để tổng hợp dữ liệu từ 126 phường/xã theo 4 biểu mẫu chuẩn hóa.

## Tính năng chính

- **Biểu 1**: Kết quả công nhận mới và công nhận lại trường chuẩn quốc gia năm 2025
- **Biểu 2**: Kế hoạch công nhận mới và công nhận lại trường chuẩn quốc gia năm 2026
- **Biểu 3**: Kế hoạch công nhận mới và công nhận lại trường chuẩn quốc gia giai đoạn 2026-2030
- **Biểu 4**: Chương trình thành phố giao

### Chức năng từng biểu

- Import dữ liệu từ file Excel đơn vị
- Hiển thị và chỉnh sửa dữ liệu tổng hợp trực tiếp trên web
- Xuất file Excel tổng hợp đúng format biểu mẫu gốc

## Cài đặt và Chạy

### Bước 1: Cài đặt thư viện

```bash
cd dataapp
pip install -r requirements.txt
```

### Bước 2: Tạo database và load dữ liệu phường/xã

```bash
python manage.py makemigrations
python manage.py migrate
```

### Bước 3: Import danh sách phường/xã

Tạo file `load_wards.py` trong thư mục `dataapp`:

```python
import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataapp.settings')
django.setup()

from core.models import Ward

# Đọc file CSV
df = pd.read_csv('../ds_phuong_xa.csv')

# Import vào database
for _, row in df.iterrows():
    Ward.objects.get_or_create(
        stt=row['stt'],
        defaults={
            'don_vi': row['don_vi'],
            'loai': row['loai']
        }
    )

print(f"Đã import {Ward.objects.count()} phường/xã")
```

Chạy script:

```bash
python load_wards.py
```

### Bước 4: Tạo tài khoản admin (tùy chọn)

```bash
python manage.py createsuperuser
```

### Bước 5: Chạy ứng dụng

```bash
python manage.py runserver
```

Truy cập: http://localhost:8000

Admin panel: http://localhost:8000/admin

## Cấu trúc thư mục

```
dataapp/
├── dataapp/           # Thư mục cấu hình Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── core/              # App chính
│   ├── models.py      # Models cho 4 biểu và Ward
│   ├── views.py       # Views xử lý logic
│   ├── urls.py        # URL routing
│   ├── admin.py       # Admin configuration
│   └── utils.py       # Import/Export Excel utilities
├── templates/         # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── bieu1_list.html
│   ├── bieu1_import.html
│   ├── bieu2_list.html
│   ├── bieu2_import.html
│   ├── bieu3_list.html
│   ├── bieu3_import.html
│   └── bieu4_list.html
├── manage.py
└── requirements.txt
```

## Hướng dẫn sử dụng

### 1. Import dữ liệu từ đơn vị

- Chọn biểu tương ứng (Biểu 1, 2, hoặc 3)
- Click nút "Import từ Excel"
- Chọn phường/xã
- Chọn file Excel theo mẫu (bieu1-donvi.xlsx, bieu2-donvi.xlsx, bieu3-donvi.xlsx)
- Click "Import dữ liệu"

### 2. Xem và chỉnh sửa dữ liệu tổng hợp

- Truy cập trang biểu tương ứng
- Dữ liệu hiển thị dưới dạng bảng có thể chỉnh sửa
- Sửa trực tiếp vào các ô input
- Click nút "Lưu dữ liệu" để lưu thay đổi

### 3. Xuất Excel tổng hợp

- Tại trang danh sách biểu
- Click nút "Xuất Excel"
- File Excel sẽ được download với format đúng biểu mẫu gốc

## Công nghệ sử dụng

- **Backend**: Django 4.2.7
- **Database**: SQLite
- **Frontend**: HTML + Bootstrap 5
- **Excel Processing**: pandas + openpyxl

## Lưu ý

- File Excel import phải đúng format mẫu
- Dữ liệu tự động tạo cho tất cả 126 phường/xã khi truy cập lần đầu
- Có thể chỉnh sửa trực tiếp trên web, không cần import
- Dữ liệu được lưu với trạng thái: import, manual, adjusted

## Nâng cấp sau này

- Nâng cấp database lên PostgreSQL
- Thêm phân quyền người dùng
- Thêm lịch sử thay đổi dữ liệu
- Thêm validation phức tạp hơn
