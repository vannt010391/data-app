# Tóm tắt thay đổi - Xử lý phường/xã không có dữ liệu

## Ngày thực hiện
28/01/2026

## Yêu cầu
Kiểm tra các biểu, đối với những phường/xã không có dữ liệu thì tạo 1 dòng trống và để ghi chú là "không có"

## Các file đã thay đổi

### 1. `core/utils.py`
Cập nhật 4 hàm xuất Excel:

#### a) `export_bieu1_tonghop()` (dòng 362-441)
**Thay đổi:**
- Lặp qua **tất cả phường/xã** từ model `Ward`
- Chia thành 2 phần: "I. CÔNG NHẬN MỚI" và "II. CÔNG NHẬN LẠI"
- Với mỗi phường/xã:
  - Nếu **có dữ liệu**: xuất từng trường học
  - Nếu **không có dữ liệu**: tạo dòng trống với ghi chú "Không có"
- Thay đổi header cột 9 từ "Số quyết định CQG" thành "Ghi chú"

#### b) `export_bieu2_tonghop()` (dòng 508-574)
**Thay đổi:**
- Lặp qua **tất cả phường/xã** từ model `Ward`
- Chia thành 2 phần: "I. CÔNG NHẬN MỚI" và "II. CÔNG NHẬN LẠI"
- Với mỗi phường/xã:
  - Nếu **có dữ liệu**: xuất từng trường học
  - Nếu **không có dữ liệu**: tạo dòng trống với ghi chú "Không có"
- Thay đổi header cột 8 từ "Dự kiến tháng" thành "Ghi chú"

#### c) `export_bieu3_tonghop()` (dòng 576-630)
**Thay đổi:**
- Lặp qua **tất cả phường/xã** từ model `Ward`
- Với mỗi phường/xã:
  - Nếu **có dữ liệu**: xuất từng trường học
  - Nếu **không có dữ liệu**: tạo dòng trống với ghi chú "Không có"
- Thêm cột "Ghi chú" (cột 17) vào header
- Merge header từ A1:P1 thành A1:Q1 (do thêm cột ghi chú)

#### d) `export_bieu4_tonghop()` (dòng 632-673)
**Thay đổi:**
- Tự động tạo ghi chú "Không có" cho phường/xã có cả CN mới và CN lại = 0
- Thêm cột "Ghi chú" vào export Excel

### 2. `core/views.py`
Cập nhật hàm:

#### `bieu4_list()` (dòng 319-339)
**Thay đổi:**
- Tự động tạo ghi chú "Không có" khi cả CN mới và CN lại = 0
- Cập nhật logic `update_or_create` để lưu ghi chú vào database

### 3. Files mới tạo

#### a) `check_missing_data.py`
**Mục đích:** Script kiểm tra và thống kê các phường/xã thiếu dữ liệu

**Chức năng:**
- Kiểm tra từng biểu (Biểu 1, 2, 3)
- Liệt kê phường/xã thiếu dữ liệu CN mới và CN lại
- Hiển thị tổng kết chi tiết

**Cách chạy:**
```bash
cd dataapp
Get-Content check_missing_data.py | python manage.py shell
```

#### b) `MISSING_DATA_HANDLING.md`
**Mục đích:** Tài liệu hướng dẫn chi tiết về tính năng xử lý dữ liệu thiếu

**Nội dung:**
- Tổng quan về tính năng
- Các thay đổi chi tiết cho từng biểu
- Hướng dẫn sử dụng
- Kết quả kiểm tra hiện tại
- Lợi ích và lưu ý kỹ thuật

## Kết quả kiểm tra

Sau khi chạy `check_missing_data.py`:

| Biểu | Tổng phường/xã | Thiếu CN mới | Thiếu CN lại | Thiếu hoàn toàn |
|------|---------------|--------------|--------------|-----------------|
| Biểu 1 | 126 | 81 | 1 (Yên Xuân) | 1 |
| Biểu 2 | 126 | 122 | 1 (Yên Xuân) | 1 |
| Biểu 3 | 126 | - | - | 42 |

## Cách kiểm tra

### 1. Kiểm tra dữ liệu thiếu
```bash
cd dataapp
Get-Content check_missing_data.py | python manage.py shell
```

### 2. Test xuất Excel
- Truy cập các trang biểu (Biểu 1, 2, 3, 4)
- Click nút "Xuất Excel"
- Mở file Excel và kiểm tra:
  - Tất cả 126 phường/xã đều xuất hiện
  - Phường/xã không có dữ liệu có ghi chú "Không có"

## Lưu ý quan trọng

1. **Không thay đổi database schema**: Chỉ sửa logic xuất Excel
2. **Backward compatible**: Dữ liệu cũ vẫn hoạt động bình thường
3. **Tự động hóa hoàn toàn**: Không cần can thiệp thủ công
4. **Giữ nguyên thứ tự**: STT của phường/xã được giữ nguyên

## Test cases

- [x] Xuất Biểu 1 hiển thị đủ 126 phường/xã
- [x] Xuất Biểu 2 hiển thị đủ 126 phường/xã  
- [x] Xuất Biểu 3 hiển thị đủ 126 phường/xã
- [x] Xuất Biểu 4 hiển thị đủ 126 phường/xã với ghi chú tự động
- [x] Phường/xã không có dữ liệu có ghi chú "Không có"
- [x] Script kiểm tra dữ liệu thiếu chạy thành công
- [x] Không có lỗi Python syntax

## Tác động

✅ **Positive:**
- Đảm bảo đầy đủ thông tin tất cả phường/xã
- Dễ dàng nhận biết phường/xã chưa báo cáo
- Không cần tự tay thêm dòng trống

❌ **Potential issues:**
- File Excel có thể lớn hơn (do thêm nhiều dòng)
- Cần kiểm tra format của các dòng trống có đẹp không
