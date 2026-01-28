# Quick Start - Thêm dòng trực tiếp trên bảng

## ⚡ Bắt đầu nhanh

### Bước 1: Mở trang Biểu
```
http://localhost:8000/bieu1/  (Biểu 1 - Kết quả 2025)
http://localhost:8000/bieu2/  (Biểu 2 - Kế hoạch 2026)
http://localhost:8000/bieu3/  (Biểu 3 - Kế hoạch 2026-2030)
```

### Bước 2: Tìm nút "+"
Nhìn vào phía bên phải header của bảng, bạn sẽ thấy nút **"+"** (dấu cộng màu xanh).

### Bước 3: Click "+"
Một dòng trống mới sẽ xuất hiện ở cuối bảng với nền **xanh nhạt**.

### Bước 4: Nhập thông tin
- **Phường/Xã**: Click dropdown, chọn phường/xã
- **Tên trường**: Click vào ô, nhập tên trường
- **Các ô khác**: Click vào ô, nhập thông tin (tùy chọn)

### Bước 5: Lưu
Click nút **"Lưu"** (xanh). Trang sẽ reload và dòng mới sẽ xuất hiện trong bảng.

**Hoặc**: Click nút **"Hủy"** (xám) để xóa dòng mới mà không lưu.

---

## 📋 Trường dữ liệu bắt buộc

### Biểu 1, 2, 3 (Giống nhau)
- ✅ **Phường/Xã** - Bắt buộc
- ✅ **Tên trường** - Bắt buộc
- ⭕ Các trường khác - Tùy chọn

### Biểu 3 (Thêm vào)
- ✅ **Phường/Xã** - Bắt buộc
- ✅ **Tên trường** - Bắt buộc
- ⭕ **10 cột năm** (CN Mới 2026-2030, CN Lại 2026-2030) - Tùy chọn

---

## 🎨 Thế nào là thành công?

Khi lưu thành công:
1. Dòng sẽ chuyển sang màu **xanh sáng** (#d4edda)
2. Button lưu sẽ hiển thị **"✓ Đã lưu!"**
3. Trang sẽ **reload tự động** sau 1 giây
4. Dòng mới sẽ **xuất hiện trong bảng** với ID

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: "Vui lòng nhập Tên trường!"
**Nguyên nhân**: Chưa nhập tên trường  
**Giải pháp**: Click vào ô "Tên trường" (sticky column bên trái) và nhập

### Lỗi 2: "Vui lòng chọn Phường/Xã!"
**Nguyên nhân**: Chưa chọn phường/xã từ dropdown  
**Giải pháp**: Click vào dropdown phường/xã (sticky column), chọn từ danh sách

### Lỗi 3: "Lỗi khi tải danh sách phường/xã"
**Nguyên nhân**: Server không chạy hoặc API lỗi  
**Giải pháp**: 
1. Kiểm tra Django server đang chạy: `python manage.py runserver 8000`
2. Kiểm tra endpoint: `http://localhost:8000/api/wards/`

### Lỗi 4: Dòng mới nhưng không hiện khi reload
**Nguyên nhân**: Lỗi validation hoặc kết nối database  
**Giải pháp**: Kiểm tra console F12 (F12 → Console tab) để xem chi tiết lỗi

---

## ⌨️ Keyboard Shortcuts

### Ctrl+S (Windows) / Cmd+S (Mac)
Khi focus vào ô contenteditable trên dòng mới, nhấn **Ctrl+S** để lưu.

---

## 📱 Các loại field

### 1. Select Dropdown (Phần tử `<select>`)
```
Phường/Xã: Click, chọn từ dropdown
Loại công nhận: Click, chọn "CN Mới" hoặc "CN Lại"
```

### 2. Contenteditable (Ô text có thể edit)
```
Tên trường, Cấp học, v.v.: Click, nhập text trực tiếp
- Xóa text: Select all (Ctrl+A), nhấn Delete
- Copy text: Ctrl+C
- Paste text: Ctrl+V
```

---

## 🔍 Tìm nút "+" ở đâu?

### Biểu 1, 2, 3
Nhìn vào **bên phải nhất** của **header row** (dòng tiêu đề):
```
[STT] [Phường/Xã] [Tên trường] ... [Ghi chú] [Hành động] [+]
                                                        ↑
                                                    TẠI ĐÂY
```

Nút "+" có:
- ✅ Màu xanh outline
- ✅ Biểu tượng dấu cộng
- ✅ Tooltip: "Thêm dòng trống mới"

---

## 💡 Tips & Tricks

### Tip 1: Thêm nhiều dòng liên tiếp
```
1. Click "+" → Tạo dòng 1
2. Nhập dữ liệu → Click "Lưu"
3. Page reload → Dòng 1 lưu thành công
4. Click "+" → Tạo dòng 2
5. Nhập dữ liệu → Click "Lưu"
...
```

### Tip 2: Nhanh chóng thoát khỏi ô
```
Nhấn Tab → Chuyển tới ô tiếp theo
Nhấn Shift+Tab → Quay lại ô trước
```

### Tip 3: Hủy dòng mới
```
Click "Hủy" → Dòng fade to red
Đợi 300ms → Dòng xóa khỏi bảng
Không có dữ liệu nào bị lưu
```

### Tip 4: Sử dụng Modal Form (Cách cũ)
```
Nếu thích Modal Form hơn inline:
1. Click "Thêm dòng" (Blue button)
2. Form modal popup
3. Điền form
4. Click "Thêm"
Cách này vẫn hoạt động bình thường!
```

---

## 🆚 Inline vs Modal: Khi nào dùng cái nào?

### Dùng Inline (+) khi:
- ✅ Thêm **nhiều dòng** liên tiếp
- ✅ Muốn **nhanh** mà không mở modal
- ✅ Tiếp tục **nhìn thấy bảng** trong khi nhập
- ✅ Quen với **spreadsheet-style editing** (Excel)

### Dùng Modal khi:
- ✅ Thêm **1-2 dòng** thôi
- ✅ Muốn **form structured** rõ ràng
- ✅ Cần **validation messages** trước khi lưu
- ✅ Quen với **traditional form** submit

---

## 📞 Support

Nếu có lỗi:
1. Mở **F12** → **Console tab**
2. Xem thông báo lỗi chi tiết
3. Check `http://localhost:8000/api/wards/` hoạt động không
4. Kiểm tra Django server đang chạy

Hoặc xem file:
- **INLINE_ROW_ADDITION.md** - Chi tiết kỹ thuật
- **CHANGELOG_PHASE3.md** - Thay đổi đầy đủ
- **README.md** - Tổng quan ứng dụng

---

## ✅ Checklist: Ready to Go!

- [x] Server đang chạy (port 8000)
- [x] API `/api/wards/` hoạt động
- [x] Trang Biểu 1, 2, 3 load được
- [x] Thấy nút "+" ở header bảng
- [x] Biết cách fill required fields
- [x] Sẵn sàng thêm dòng mới!

---

**Happy Data Entry! 🎉**
