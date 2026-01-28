# Tính năng Thêm Dòng Trực tiếp Trên Bảng

## Mô tả
Người dùng có thể thêm dòng dữ liệu mới trực tiếp trên bảng biểu mà không cần phải mở modal form. Chỉ cần click nút "+" ở header của bảng, sẽ tạo một dòng trống mới, nhập thông tin vào các ô (như khi chỉnh sửa), và click "Lưu" để thêm dòng mới vào database.

## Cách sử dụng

### 1. Biểu 1 (Kết quả 2025)
1. Mở trang http://localhost:8000/bieu1/
2. Click nút **"+"** (dấu cộng màu xanh) ở phía bên phải header của bảng
3. Một dòng trống mới sẽ xuất hiện ở cuối bảng với màu xanh nhạt (#e7f3ff)
4. Nhập thông tin:
   - **Phường/Xã**: Chọn từ dropdown (bắt buộc)
   - **Tên trường**: Nhập tên trường (bắt buộc)
   - **Cấp học**: Nhập cấp học (tùy chọn)
   - **CN Mới/CN Lại**: Chọn loại công nhận
   - **Năm đạt**: Nhập năm (tùy chọn)
   - **Mức độ CQG**: Nhập mức độ (tùy chọn)
   - **Số QĐ CQG**: Nhập số quyết định (tùy chọn)
   - **Ghi chú**: Nhập ghi chú (tùy chọn)
5. Click nút **"Lưu"** để lưu dòng mới
   - Nút sẽ hiển thị trạng thái "Đang lưu..."
   - Khi lưu thành công, dòng sẽ có màu xanh nhạt (#d4edda) và trang sẽ reload
6. Click nút **"Hủy"** để xóa dòng mới mà không lưu

### 2. Biểu 2 (Kế hoạch 2026)
Tương tự Biểu 1, nhưng với các trường:
- Phường/Xã (bắt buộc)
- Tên trường (bắt buộc)
- Cấp học
- CN Mới/CN Lại
- Năm đạt CQG
- Đã kiểm tra
- Dự kiến tháng
- Ghi chú

### 3. Biểu 3 (Kế hoạch 2026-2030)
Tương tự Biểu 1, nhưng với thêm các trường năm:
- Phường/Xã (bắt buộc)
- Tên trường (bắt buộc)
- Cấp học
- Loại hình
- Năm đạt CQG
- **Công nhận mới**: 2026, 2027, 2028, 2029, 2030 (5 cột)
- **Công nhận lại**: 2026, 2027, 2028, 2029, 2030 (5 cột)
- Ghi chú

## Thay đổi trong mã nguồn

### 1. Views (core/views.py)
Thêm API endpoint mới:
```python
def api_wards(request):
    """API để lấy danh sách phường/xã (JSON)"""
    wards = Ward.objects.all().order_by('stt')
    data = [{'id': w.id, 'stt': w.stt, 'don_vi': w.don_vi} for w in wards]
    return JsonResponse(data, safe=False)
```

### 2. URLs (core/urls.py)
Thêm route mới:
```python
path('api/wards/', views.api_wards, name='api_wards'),
```

### 3. Templates (bieu1_list.html, bieu2_list.html, bieu3_list.html)

#### Header
Thêm cột "+" ở header:
```html
<th style="width: 40px; text-align: center;">
    <button class="btn btn-sm btn-outline-success" onclick="addNewRow('bieu1-tbody')" title="Thêm dòng trống mới">
        <i class="bi bi-plus"></i>
    </button>
</th>
```

#### Tbody
Thêm ID cho tbody:
```html
<tbody id="bieu1-tbody">
```

#### JavaScript
Thêm 3 hàm JavaScript:
- `addNewRow(tbodyId)`: Tạo dòng trống mới từ API
- `saveNewRow(newRowId)`: Lưu dòng mới vào database
- `cancelNewRow(newRowId)`: Hủy dòng mới mà không lưu

## Công nghệ sử dụng
- **Fetch API**: Lấy danh sách phường/xã từ `/api/wards/` và lưu dòng mới via `/bieu{1-3}/add/`
- **Contenteditable**: Các ô dữ liệu dùng contenteditable="true" để cho phép chỉnh sửa trực tiếp
- **HTML `<select>`**: Dropdown cho phường/xã và loại công nhận
- **CSS Animation**: Màu sắc thay đổi để hiển thị trạng thái (loading, success, cancel)

## Lưu ý
1. **Phường/Xã và Tên trường là bắt buộc** - Nếu không điền, sẽ hiển thị thông báo lỗi
2. **Tự động reload** - Sau khi lưu thành công, trang sẽ tự động reload để hiển thị dòng mới
3. **Ctrl+S** - Khi focus vào ô contenteditable ở dòng mới, có thể nhấn Ctrl+S để lưu
4. **"---"** - Dấu "---" được sử dụng làm placeholder cho các ô trống, sẽ được chuyển thành chuỗi rỗng khi lưu

## So sánh với Modal Form

| Tính năng | Modal Form | Inline Row Addition |
|----------|-----------|-------------------|
| **Tốc độ** | Cần mở modal, điền form, click Thêm | Nhanh hơn - edit trực tiếp trên bảng |
| **Trải nghiệm UX** | Rời khỏi bảng để nhập | Không cần rời khỏi bảng |
| **Thích hợp cho** | Thêm 1-2 dòng | Thêm nhiều dòng liên tục |
| **Validation** | Có validation nội bộ modal | Validation khi click Lưu |

## Troubleshooting

### Lỗi: "Lỗi khi tải danh sách phường/xã"
- Kiểm tra API endpoint `/api/wards/` có hoạt động không
- Đảm bảo server Django đang chạy
- Kiểm tra console F12 để xem chi tiết lỗi

### Dòng mới không lưu được
- Kiểm tra điều kiện validation: Phường/Xã và Tên trường phải được điền
- Xem console F12 để xem response từ server
- Kiểm tra CSRF token có được gửi đúng không

### Trang không reload sau lưu
- Kiểm tra kết nối mạng
- Xem console F12 để xem lỗi fetch API
- Thử lại manual refresh trang

## Future Improvements
- [ ] Inline validation trước khi click Lưu
- [ ] Hiển thị lỗi validation cho từng ô
- [ ] Thêm tính năng Duplicate (copy) dòng hiện tại
- [ ] Multi-select cho các ô ngày/tháng
- [ ] Keyboard navigation giữa các ô
