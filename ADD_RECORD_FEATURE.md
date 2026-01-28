# Tính năng: Thêm dòng dữ liệu trực tiếp trên biểu

## Mô tả
Người dùng có thể thêm dòng dữ liệu mới trực tiếp từ giao diện web mà không cần phải import từ file Excel. Tính năng này được cập nhật cho tất cả 3 biểu chính (Biểu 1, Biểu 2, Biểu 3).

## Các thay đổi

### 1. Backend (Views)

#### File: `core/views.py`

**Thêm 2 hàm mới:**

- **`bieu2_add(request)`** (dòng ~175)
  - Xử lý yêu cầu thêm dòng mới cho Biểu 2
  - Nhận POST request với dữ liệu JSON
  - Tạo record mới trong database
  - Trả về JSON response với status 'success'

- **`bieu3_add(request)`** (dòng ~290)
  - Xử lý yêu cầu thêm dòng mới cho Biểu 3
  - Nhận POST request với dữ liệu JSON
  - Tạo record mới với tất cả 10 năm (CN mới 2026-2030 + CN lại 2026-2030)
  - Trả về JSON response với status 'success'

**Hàm `bieu1_add()` đã tồn tại (dòng 92)**

### 2. URL Routes

#### File: `core/urls.py`

**Thêm 2 route mới:**

```python
path('bieu2/add/', views.bieu2_add, name='bieu2_add'),
path('bieu3/add/', views.bieu3_add, name='bieu3_add'),
```

**Route `bieu1/add/` đã tồn tại**

### 3. Frontend (Templates)

#### File: `templates/bieu1_list.html`

**Thay đổi:**
- Thêm button "Thêm dòng" ở thanh công cụ (bên cạnh button Import)
- Thêm modal form để nhập dữ liệu:
  - Phường/Xã (required, dropdown)
  - Tên trường (required, text)
  - Cấp học (text)
  - Loại hình (text)
  - Loại công nhận (select: CN mới / CN lại)
  - Năm đạt chuẩn (text)
  - Mức độ CQG (text)
  - Số QĐ CQG (text)
  - Ghi chú (textarea)
- Thêm JavaScript function:
  - `openAddModal()` - mở modal form
  - `submitAddBieu1()` - gửi dữ liệu tới server

#### File: `templates/bieu2_list.html`

**Thay đổi tương tự Biểu 1 nhưng form khác:**
- Phường/Xã (required, dropdown)
- Tên trường (required, text)
- Cấp học (text)
- Loại hình (text)
- Loại công nhận (select: CN mới / CN lại)
- Năm đạt CQG (text)
- Đã kiểm tra (text)
- Dự kiến tháng (text)
- Ghi chú (textarea)

#### File: `templates/bieu3_list.html`

**Thay đổi - Modal form cho Biểu 3:**
- Phần I: Thông tin cơ bản
  - Phường/Xã (required)
  - Tên trường (required)
  - Cấp học
  - Loại hình
  - Năm đạt CQG

- Phần II: Công nhận mới (2026-2030)
  - Năm 2026, 2027, 2028, 2029, 2030 (mỗi năm là 1 field)

- Phần III: Công nhận lại (2026-2030)
  - Năm 2026, 2027, 2028, 2029, 2030 (mỗi năm là 1 field)

- Phần IV: Ghi chú (textarea)

## Cách sử dụng

### Thêm dòng trên Biểu 1

1. Truy cập trang **Biểu 1** (`/bieu1/`)
2. Click button **"Thêm dòng"** (màu xanh lá cây)
3. Modal form sẽ hiển thị
4. Nhập các thông tin:
   - Chọn **Phường/Xã** từ dropdown
   - Nhập **Tên trường** (bắt buộc)
   - Nhập các thông tin khác (tùy chọn)
   - Chọn **Loại công nhận** (CN mới hoặc CN lại)
5. Click **"Thêm"** để lưu
6. Trang sẽ reload tự động khi thêm thành công

### Thêm dòng trên Biểu 2

1. Truy cập trang **Biểu 2** (`/bieu2/`)
2. Click button **"Thêm dòng"**
3. Điền form tương tự Biểu 1 nhưng với fields khác
4. Click **"Thêm"**

### Thêm dòng trên Biểu 3

1. Truy cập trang **Biểu 3** (`/bieu3/`)
2. Click button **"Thêm dòng"**
3. Điền thông tin cơ bản (Phường/Xã, Tên trường)
4. Điền số liệu công nhận mới cho 5 năm (nếu có)
5. Điền số liệu công nhận lại cho 5 năm (nếu có)
6. Nhập ghi chú (nếu cần)
7. Click **"Thêm"**

## Kỹ thuật chi tiết

### Flow dữ liệu

1. **User clicks "Thêm dòng" button**
   - Opens modal form with reset fields
   - Display all wards from database

2. **User fills form and clicks "Thêm"**
   - JavaScript validates required fields
   - Collects data from form inputs
   - Sends POST request to `/bieu{X}/add/` endpoint
   - Request body: JSON with all field values

3. **Server processes request**
   - `bieu{X}_add()` function receives request
   - Validates ward_id exists in database
   - Creates new record with `source='manual'`
   - Returns `{'status': 'success'}`

4. **Frontend handles response**
   - On success: Shows message, hides modal, reloads page
   - On error: Shows error alert, keeps modal open
   - Button shows loading state while requesting

### Data validation

**Client-side (Browser):**
- Phường/Xã: Required
- Tên trường: Required

**Server-side:**
- ward_id: Must exist in Ward model
- All other fields: Optional, defaults to empty string

### Database changes

**No schema changes** - sử dụng các trường hiện tại:
- Biểu 1: Sử dụng tất cả fields trong `Bieu1KQ2025` model
- Biểu 2: Sử dụng tất cả fields trong `Bieu2KH2026` model
- Biểu 3: Sử dụng tất cả fields trong `Bieu3KH20262030` model

### Source tracking

Tất cả record thêm trực tiếp được đánh dấu:
```python
source='manual'  # Thêm trực tiếp từ form
```

So sánh với:
- `source='import'` - Import từ Excel
- `source='adjusted'` - Đã chỉnh sửa

## Lợi ích

1. **Tiện lợi**: Không cần phải chuẩn bị file Excel
2. **Nhanh gọn**: Thêm dòng chỉ mất vài giây
3. **Linh hoạt**: Có thể thêm bất cứ lúc nào trực tiếp trên trang
4. **Theo dõi**: Hệ thống theo dõi nguồn dữ liệu (manual/import/adjusted)
5. **Tích hợp**: Dữ liệu thêm trực tiếp được tích hợp ngay với dữ liệu import

## Lưu ý

1. **Validation**: Chỉ yêu cầu Phường/Xã và Tên trường, các field khác có thể để trống
2. **Auto-reload**: Trang sẽ reload sau khi thêm thành công, dòng mới sẽ hiển thị trong bảng
3. **Phường/Xã**: Phải chọn từ dropdown, không được nhập tự do
4. **Modal form**: Các field sẽ được reset khi mở modal
5. **Error handling**: Nếu có lỗi, modal sẽ giữ nguyên data và hiển thị thông báo lỗi

## Test cases

- [x] Thêm dòng Biểu 1 với loại CN mới
- [x] Thêm dòng Biểu 1 với loại CN lại
- [x] Thêm dòng Biểu 2 với loại CN mới
- [x] Thêm dòng Biểu 2 với loại CN lại
- [x] Thêm dòng Biểu 3 với dữ liệu đầy đủ
- [x] Validation: Kiểm tra Phường/Xã và Tên trường bắt buộc
- [x] Validation: Cho phép để trống các field khác
- [x] Modal form reset khi mở lại
- [x] Error handling khi thêm thất bại
- [x] Dòng mới xuất hiện trong bảng sau khi reload

## Files thay đổi

1. `core/urls.py` - Thêm 2 route
2. `core/views.py` - Thêm 2 function
3. `templates/bieu1_list.html` - Thêm button + modal
4. `templates/bieu2_list.html` - Thêm button + modal
5. `templates/bieu3_list.html` - Thêm button + modal
