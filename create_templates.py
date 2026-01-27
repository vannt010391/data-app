"""Script tạo templates đơn giản cho các biểu"""

# Biểu 1
bieu1_list = """{% extends 'base.html' %}
{% block title %}Biểu 1 - KQ 2025{% endblock %}
{% block content %}
<h2>Biểu 1 - KẾT QUẢ CÔNG NHẬN MỚI và CÔNG NHẬN LẠI TRƯỜNG CHUẨN QUỐC GIA NĂM 2025</h2>
<p>Tổng: {{ records.count }} trường</p>
<a href="{% url 'bieu1_import' %}" class="btn btn-primary">Import</a>
<a href="{% url 'bieu1_export' %}" class="btn btn-success">Xuất Excel</a>
<table class="table table-bordered mt-3">
<thead><tr><th>STT</th><th>Phường/Xã</th><th>Tên trường</th><th>Cấp học</th><th>Loại</th><th>Năm</th><th>Mức độ</th><th>Số QĐ</th><th>Ghi chú</th></tr></thead>
<tbody>
{% for r in records %}
<tr><td>{{ r.ward.stt }}</td><td>{{ r.ward.don_vi }}</td><td>{{ r.ten_truong }}</td><td>{{ r.cap_hoc }}</td>
<td>{% if r.loai_cong_nhan == 'CN_MOI' %}CN Mới{% else %}CN Lại{% endif %}</td>
<td>{{ r.nam_dat_chuan_gan_nhat|default:'' }}</td><td>{{ r.muc_do_cqg|default:'' }}</td><td>{{ r.so_quyet_dinh_cqg|default:'' }}</td><td>{{ r.ghi_chu|default:'' }}</td></tr>
{% empty %}<tr><td colspan="9" class="text-center">Chưa có dữ liệu</td></tr>{% endfor %}
</tbody>
</table>
{% endblock %}"""

bieu1_import = """{% extends 'base.html' %}
{% block title %}Import Biểu 1{% endblock %}
{% block content %}
<h2>Import Biểu 1 từ Excel</h2>
<form method="post" enctype="multipart/form-data">
{% csrf_token %}
<div class="mb-3">
<label>Chọn phường/xã</label>
<select class="form-select" name="ward_id" required>
<option value="">-- Chọn --</option>
{% for ward in wards %}<option value="{{ ward.id }}">{{ ward.stt }}. {{ ward.don_vi }}</option>{% endfor %}
</select>
</div>
<div class="mb-3">
<label>File Excel</label>
<input type="file" class="form-control" name="excel_file" accept=".xlsx,.xls" required>
</div>
<button type="submit" class="btn btn-primary">Import</button>
<a href="{% url 'bieu1_list' %}" class="btn btn-secondary">Quay lại</a>
</form>
{% endblock %}"""

# Biểu 2
bieu2_list = """{% extends 'base.html' %}
{% block title %}Biểu 2 - KH 2026{% endblock %}
{% block content %}
<h2>Biểu 2 - KẾ HOẠCH CÔNG NHẬN MỚI VÀ CÔNG NHẬN LẠI NĂM 2026</h2>
<p>Tổng: {{ records.count }} trường</p>
<a href="{% url 'bieu2_import' %}" class="btn btn-primary">Import</a>
<a href="{% url 'bieu2_export' %}" class="btn btn-success">Xuất Excel</a>
<table class="table table-bordered mt-3">
<thead><tr><th>STT</th><th>Phường/Xã</th><th>Tên trường</th><th>Cấp học</th><th>Loại</th><th>Năm đạt</th><th>Đã kiểm tra</th><th>Dự kiến</th><th>Ghi chú</th></tr></thead>
<tbody>
{% for r in records %}
<tr><td>{{ r.ward.stt }}</td><td>{{ r.ward.don_vi }}</td><td>{{ r.ten_truong }}</td><td>{{ r.cap_hoc }}</td>
<td>{% if r.loai_cong_nhan == 'CN_MOI' %}CN Mới{% else %}CN Lại{% endif %}</td>
<td>{{ r.nam_dat_cqg_gan_nhat|default:'' }}</td><td>{{ r.phuong_xa_da_kiem_tra|default:'' }}</td><td>{{ r.du_kien_thang|default:'' }}</td><td>{{ r.ghi_chu|default:'' }}</td></tr>
{% empty %}<tr><td colspan="9" class="text-center">Chưa có dữ liệu</td></tr>{% endfor %}
</tbody>
</table>
{% endblock %}"""

bieu2_import = """{% extends 'base.html' %}
{% block title %}Import Biểu 2{% endblock %}
{% block content %}
<h2>Import Biểu 2 từ Excel</h2>
<form method="post" enctype="multipart/form-data">
{% csrf_token %}
<div class="mb-3">
<label>Chọn phường/xã</label>
<select class="form-select" name="ward_id" required>
<option value="">-- Chọn --</option>
{% for ward in wards %}<option value="{{ ward.id }}">{{ ward.stt }}. {{ ward.don_vi }}</option>{% endfor %}
</select>
</div>
<div class="mb-3">
<label>File Excel</label>
<input type="file" class="form-control" name="excel_file" accept=".xlsx,.xls" required>
</div>
<button type="submit" class="btn btn-primary">Import</button>
<a href="{% url 'bieu2_list' %}" class="btn btn-secondary">Quay lại</a>
</form>
{% endblock %}"""

# Biểu 3
bieu3_list = """{% extends 'base.html' %}
{% block title %}Biểu 3 - KH 2026-2030{% endblock %}
{% block content %}
<h2>Biểu 3 - KẾ HOẠCH 2026-2030</h2>
<p>Tổng: {{ records.count }} trường</p>
<a href="{% url 'bieu3_import' %}" class="btn btn-primary">Import</a>
<a href="{% url 'bieu3_export' %}" class="btn btn-success">Xuất Excel</a>
<table class="table table-bordered mt-3">
<thead><tr><th>STT</th><th>Phường/Xã</th><th>Tên trường</th><th>Cấp</th><th>CN mới 26-30</th><th>CN lại 26-30</th><th>Ghi chú</th></tr></thead>
<tbody>
{% for r in records %}
<tr><td>{{ r.ward.stt }}</td><td>{{ r.ward.don_vi }}</td><td>{{ r.ten_truong }}</td><td>{{ r.cap_hoc }}</td>
<td>{{ r.cn_moi_2026|default:'' }} {{ r.cn_moi_2027|default:'' }} {{ r.cn_moi_2028|default:'' }} {{ r.cn_moi_2029|default:'' }} {{ r.cn_moi_2030|default:'' }}</td>
<td>{{ r.cn_lai_2026|default:'' }} {{ r.cn_lai_2027|default:'' }} {{ r.cn_lai_2028|default:'' }} {{ r.cn_lai_2029|default:'' }} {{ r.cn_lai_2030|default:'' }}</td>
<td>{{ r.ghi_chu|default:'' }}</td></tr>
{% empty %}<tr><td colspan="7" class="text-center">Chưa có dữ liệu</td></tr>{% endfor %}
</tbody>
</table>
{% endblock %}"""

bieu3_import = """{% extends 'base.html' %}
{% block title %}Import Biểu 3{% endblock %}
{% block content %}
<h2>Import Biểu 3 từ Excel</h2>
<form method="post" enctype="multipart/form-data">
{% csrf_token %}
<div class="mb-3">
<label>Chọn phường/xã</label>
<select class="form-select" name="ward_id" required>
<option value="">-- Chọn --</option>
{% for ward in wards %}<option value="{{ ward.id }}">{{ ward.stt }}. {{ ward.don_vi }}</option>{% endfor %}
</select>
</div>
<div class="mb-3">
<label>File Excel</label>
<input type="file" class="form-control" name="excel_file" accept=".xlsx,.xls" required>
</div>
<button type="submit" class="btn btn-primary">Import</button>
<a href="{% url 'bieu3_list' %}" class="btn btn-secondary">Quay lại</a>
</form>
{% endblock %}"""

# Biểu 4
bieu4_list = """{% extends 'base.html' %}
{% block title %}Biểu 4 - CT TP{% endblock %}
{% block content %}
<h2>Biểu 4 - CHƯƠNG TRÌNH THÀNH PHỐ GIAO</h2>
<p>Tự động tính từ Biểu 1</p>
<a href="{% url 'bieu4_export' %}" class="btn btn-success">Xuất Excel</a>
<table class="table table-bordered mt-3">
<thead><tr><th>STT</th><th>Đơn vị</th><th>Công nhận mới</th><th>Công nhận lại</th><th>Loại</th></tr></thead>
<tbody>
{% for r in records %}
<tr><td>{{ r.stt }}</td><td>{{ r.don_vi }}</td><td>{{ r.cong_nhan_moi }}</td><td>{{ r.cong_nhan_lai }}</td><td>{{ r.loai }}</td></tr>
{% endfor %}
</tbody>
</table>
{% endblock %}"""

# Ghi file
import os

templates_dir = 'templates'

files = {
    f'{templates_dir}/bieu1_list.html': bieu1_list,
    f'{templates_dir}/bieu1_import.html': bieu1_import,
    f'{templates_dir}/bieu2_list.html': bieu2_list,
    f'{templates_dir}/bieu2_import.html': bieu2_import,
    f'{templates_dir}/bieu3_list.html': bieu3_list,
    f'{templates_dir}/bieu3_import.html': bieu3_import,
    f'{templates_dir}/bieu4_list.html': bieu4_list,
}

for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {filepath}')

print('\nĐã tạo xong templates!')
