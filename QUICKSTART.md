# Hướng dẫn cài đặt và chạy ứng dụng nhanh

## Bước 1: Cài đặt thư viện
```bash
pip install -r requirements.txt
```

## Bước 2: Tạo database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Bước 3: Load dữ liệu phường/xã
```bash
python load_wards.py
```

## Bước 4: Chạy ứng dụng
```bash
python manage.py runserver
```

Truy cập: http://localhost:8000

---

## Hoặc chạy nhanh bằng file start.bat (Windows):
```bash
start.bat
```
