# Hướng dẫn: Thêm dòng dữ liệu trực tiếp trên biểu

## Giới thiệu
Bạn có thể thêm dòng dữ liệu mới trực tiếp từ giao diện web mà không cần phải tạo file Excel và import. Tính năng này có sẵn cho tất cả 3 biểu (Biểu 1, 2, 3).

## Các bước thêm dòng

### 1. Biểu 1 - Kết quả công nhận năm 2025

#### Bước 1: Truy cập trang Biểu 1
- Nhấp vào **"Biểu 1"** từ menu hoặc truy cập `/bieu1/`

#### Bước 2: Tìm button "Thêm dòng"
- Ở thanh công cụ (bên phải), bạn sẽ thấy button xanh lá cây: **"➕ Thêm dòng"**
- Nằm bên cạnh các button Import, Xuất Excel, Xóa đã chọn

#### Bước 3: Nhấp button "Thêm dòng"
- Modal form sẽ hiển thị
- Form có 9 trường:
  1. **Phường/Xã** ⭐ (bắt buộc) - Chọn từ dropdown
  2. **Tên trường** ⭐ (bắt buộc) - Nhập tên trường học
  3. **Cấp học** - VD: Tiểu học, THCS, THPT
  4. **Loại hình** - VD: CL, CLHQ, DL
  5. **Loại công nhận** - Chọn "Công nhận mới" hoặc "Công nhận lại"
  6. **Năm đạt chuẩn** - Năm được công nhận (VD: 2023, 2024, 2025)
  7. **Mức độ CQG** - VD: Cơ bản, Tốt, Xuất sắc
  8. **Số QĐ CQG** - Số quyết định công nhận
  9. **Ghi chú** - Thêm ghi chú nếu cần

#### Bước 4: Điền dữ liệu
- **Bắt buộc**: Phường/Xã và Tên trường
- **Tùy chọn**: Các trường khác có thể để trống

#### Bước 5: Nhấp button "Thêm"
- Button sẽ hiển thị "Đang thêm..." trong khi xử lý
- Nếu thành công: Trang sẽ tự động reload
- Dòng mới sẽ xuất hiện trong bảng (nhóm CÔNG NHẬN MỚI hoặc CÔNG NHẬN LẠI tùy theo lựa chọn)

### 2. Biểu 2 - Kế hoạch công nhận năm 2026

#### Quá trình tương tự Biểu 1
- Nhấp **"Biểu 2"** → **"Thêm dòng"**
- Form có 9 trường (khác một chút):
  1. **Phường/Xã** ⭐
  2. **Tên trường** ⭐
  3. **Cấp học**
  4. **Loại hình**
  5. **Loại công nhận** (CN mới / CN lại)
  6. **Năm đạt CQG**
  7. **Đã kiểm tra** - Có hay không
  8. **Dự kiến tháng** - Tháng dự kiến đánh giá (VD: 3, 5, 9)
  9. **Ghi chú**

### 3. Biểu 3 - Kế hoạch công nhận 2026-2030

#### Quá trình tương tự
- Nhấp **"Biểu 3"** → **"Thêm dòng"**
- Form chia thành 4 phần:

**Phần I: Thông tin cơ bản**
- Phường/Xã ⭐
- Tên trường ⭐
- Cấp học
- Loại hình
- Năm đạt CQG

**Phần II: Công nhận mới 2026-2030** (5 năm)
- Năm 2026
- Năm 2027
- Năm 2028
- Năm 2029
- Năm 2030

**Phần III: Công nhận lại 2026-2030** (5 năm)
- Năm 2026
- Năm 2027
- Năm 2028
- Năm 2029
- Năm 2030

**Phần IV: Ghi chú**
- Ghi chú tự do

## Mẹo sử dụng

### ✅ Cách thêm nhanh
1. Mở modal form
2. Chọn Phường/Xã
3. Nhập Tên trường
4. Nhấp "Thêm" ngay
5. (Các field khác có thể để trống)

### ✅ Khi có lỗi?
- **Quên Phường/Xã hoặc Tên trường**: Sẽ xuất hiện thông báo "Vui lòng nhập Phường/Xã và Tên trường"
- **Lỗi kết nối**: Có thể server không hoạt động, kiểm tra lại kết nối mạng
- **Phường/Xã không có**: Phải chọn từ dropdown, không được nhập tự do

### ✅ Hủy thêm dòng
- Nhấp button **"Hủy"** hoặc **"✕"** để đóng modal
- Dữ liệu nhập sẽ bị xóa (không lưu)
- Khi mở lại modal, form sẽ được reset

### ✅ Có thể edit sau không?
**Có!** Sau khi thêm dòng:
1. Dòng mới sẽ xuất hiện trong bảng
2. Bạn có thể **nhấp vào ô bất kỳ** để sửa (những ô có màu vàng khi hover)
3. Nhấp button **"Lưu"** để lưu thay đổi
4. Hoặc nhấp **"Xóa"** để xóa dòng

## Từ điển thuật ngữ

| Thuật ngữ | Nghĩa |
|-----------|-------|
| CN mới | Công nhận mới - Trường chưa từng được công nhận |
| CN lại | Công nhận lại - Trường đã được công nhận trước đó |
| CQG | Chuẩn Quốc Gia |
| Phường/Xã | Đơn vị hành chính cấp 3 |
| Cấp học | Mầm non, Tiểu học, THCS, THPT |
| Loại hình | CL=Công lập, DL=Dân lập, CLHQ=CL có Hỗ trợ |
| Ghi chú | Thông tin bổ sung, lưu ý |

## Câu hỏi thường gặp

**Q: Có thể thêm nhiều dòng cùng lúc không?**
A: Hiện tại không, phải thêm từng dòng. Có thể dùng tính năng Import nếu có file Excel có nhiều dòng.

**Q: Dữ liệu thêm trực tiếp có khác gì so với import?**
A: Giống nhau hoàn toàn. Hệ thống chỉ theo dõi nguồn ("manual" vs "import") để biết từ đâu.

**Q: Có thể thêm dòng trống (ghi chú "Không có") không?**
A: Không cần, hệ thống tự động thêm ghi chú "Không có" khi xuất Excel nếu phường/xã không có dữ liệu.

**Q: Có phải lưu riêng sau khi thêm không?**
A: Không, trang sẽ tự động reload sau khi thêm thành công. Dữ liệu đã được lưu vào database.

**Q: Có thể hủy lệnh thêm không?**
A: Sau khi nhấp "Thêm", nếu có lỗi sẽ hiển thị ngay. Nếu thành công rồi, có thể xóa dòng bằng button "Xóa".

**Q: Phần "Ghi chú" dùng để làm gì?**
A: Ghi thêm thông tin như: "Kiến nghị từ phòng GD", "Chờ bổ sung hồ sơ", v.v.

## Troubleshooting

### Problem: Modal không hiển thị
- **Giải pháp**: Kiểm tra xem có JavaScript error không (F12 → Console tab)
- **Thử**: Reload trang, xóa cache browser

### Problem: Không thể chọn Phường/Xã
- **Giải pháp**: Dropdown có thể chưa load xong, đợi một chút
- **Thử**: Refresh trang rồi thử lại

### Problem: Lỗi "Lỗi kết nối"
- **Giải pháp**: Server Django có thể không chạy
- **Thử**: Kiểm tra server có chạy: `python manage.py runserver`

### Problem: Sau khi thêm, dòng không xuất hiện
- **Giải pháp**: Trang reload nhưng có thể cần scroll hoặc filter
- **Thử**: Scroll lên/xuống, kiểm tra filter Phường/Xã

## Liên hệ hỗ trợ

Nếu có vấn đề, vui lòng:
1. Kiểm tra lại các bước theo hướng dẫn
2. Xem phần "Troubleshooting" ở trên
3. Kiểm tra console (F12) có error gì không
4. Liên hệ người quản trị hệ thống
