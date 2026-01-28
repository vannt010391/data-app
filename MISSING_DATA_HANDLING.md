# Hướng dẫn: Xử lý phường/xã không có dữ liệu

## Tổng quan

Hệ thống đã được cập nhật để **tự động hiển thị tất cả phường/xã** khi xuất báo cáo, kể cả những phường/xã không có dữ liệu. Đối với những phường/xã không có dữ liệu, hệ thống sẽ tự động tạo một dòng trống và ghi chú là **"Không có"**.

## Các thay đổi chính

### 1. Biểu 1 - Kết quả công nhận mới và công nhận lại năm 2025

Khi xuất Excel Biểu 1, hệ thống sẽ:
- Hiển thị đầy đủ tất cả 126 phường/xã
- Chia thành 2 phần: **I. CÔNG NHẬN MỚI** và **II. CÔNG NHẬN LẠI**
- Đối với phường/xã không có dữ liệu:
  - Hiển thị STT và tên phường/xã
  - Cột "Ghi chú" ghi: **"Không có"**
  - Các cột khác để trống

### 2. Biểu 2 - Kế hoạch công nhận mới và công nhận lại năm 2026

Khi xuất Excel Biểu 2, hệ thống sẽ:
- Hiển thị đầy đủ tất cả 126 phường/xã
- Chia thành 2 phần: **I. CÔNG NHẬN MỚI** và **II. CÔNG NHẬN LẠI**
- Đối với phường/xã không có dữ liệu:
  - Hiển thị STT và tên phường/xã
  - Cột "Ghi chú" ghi: **"Không có"**
  - Các cột khác để trống

### 3. Biểu 3 - Kế hoạch công nhận giai đoạn 2026-2030

Khi xuất Excel Biểu 3, hệ thống sẽ:
- Hiển thị đầy đủ tất cả 126 phường/xã
- Đối với phường/xã không có dữ liệu:
  - Hiển thị STT và tên phường/xã
  - Cột "Ghi chú" ghi: **"Không có"**
  - Các cột khác để trống

### 4. Biểu 4 - Chương trình thành phố giao

Khi xem hoặc xuất Excel Biểu 4, hệ thống sẽ:
- Tự động tính toán từ dữ liệu Biểu 1
- Hiển thị đầy đủ tất cả 126 phường/xã
- Đối với phường/xã không có dữ liệu (cả CN mới và CN lại đều = 0):
  - Cột "Ghi chú" tự động ghi: **"Không có"**

## Cách sử dụng

### Kiểm tra dữ liệu thiếu

Chạy script kiểm tra để xem có bao nhiêu phường/xã chưa có dữ liệu:

```bash
cd dataapp
Get-Content check_missing_data.py | python manage.py shell
```

Script sẽ hiển thị:
- Số lượng phường/xã thiếu dữ liệu cho mỗi biểu
- Danh sách 5 phường/xã đầu tiên thiếu dữ liệu
- Tổng kết chi tiết

### Xuất báo cáo Excel

Khi xuất Excel từ các biểu, hệ thống sẽ tự động:
1. Lấy danh sách tất cả phường/xã từ database
2. Kiểm tra từng phường/xã có dữ liệu không
3. Nếu có: xuất đầy đủ thông tin các trường học
4. Nếu không có: tạo dòng trống với ghi chú "Không có"

## Kết quả kiểm tra hiện tại

Tính đến thời điểm kiểm tra:

| Biểu | Tổng phường/xã | Có dữ liệu | Thiếu CN mới | Thiếu CN lại | Thiếu hoàn toàn |
|------|---------------|------------|--------------|--------------|-----------------|
| Biểu 1 | 126 | 125 | 81 | 1 | 1 |
| Biểu 2 | 126 | 125 | 122 | 1 | 1 |
| Biểu 3 | 126 | 84 | - | - | 42 |
| Biểu 4 | 126 | tự động | tự động | tự động | tự động |

**Ghi chú:** 
- Biểu 4 tự động tính từ Biểu 1, nên không có dữ liệu thiếu
- Phường/xã "Yên Xuân" là đơn vị duy nhất thiếu cả 2 loại dữ liệu trong Biểu 1 và 2

## Lợi ích

1. **Đầy đủ**: Đảm bảo không bỏ sót bất kỳ phường/xã nào trong báo cáo
2. **Rõ ràng**: Dễ dàng nhận biết phường/xã nào chưa có dữ liệu qua ghi chú "Không có"
3. **Tiện lợi**: Không cần tự tay thêm các dòng trống khi xuất báo cáo
4. **Chính xác**: Đảm bảo thứ tự STT của tất cả phường/xã được giữ nguyên

## Lưu ý kỹ thuật

- Hệ thống sử dụng model `Ward` để lấy danh sách đầy đủ các phường/xã
- Mỗi biểu được kiểm tra riêng biệt
- Biểu 1 và 2 được chia thành 2 phần (CN mới và CN lại), mỗi phần đều hiển thị đầy đủ tất cả phường/xã
- Ghi chú "Không có" chỉ xuất hiện ở cột Ghi chú, các cột khác để trống
