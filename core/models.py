from django.db import models


class Ward(models.Model):
    """Danh mục phường/xã"""
    stt = models.IntegerField(unique=True)
    don_vi = models.CharField(max_length=200)
    loai = models.CharField(max_length=50)

    class Meta:
        db_table = 'ward'
        ordering = ['stt']

    def __str__(self):
        return f"{self.stt}. {self.don_vi}"


class Bieu1KQ2025(models.Model):
    """Biểu 1 - KẾT QUẢ CÔNG NHẬN MỚI và CÔNG NHẬN LẠI TRƯỜNG CHUẨN QUỐC GIA NĂM 2025
    Mỗi dòng là một trường học"""
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='bieu1_records')
    quan_huyen = models.CharField(max_length=200, blank=True, null=True, verbose_name='Quận, Huyện')
    phuong_xa = models.CharField(max_length=200, blank=True, null=True, verbose_name='Phường, xã')
    
    # Thông tin trường
    ten_truong = models.CharField(max_length=300, verbose_name='Tên trường')
    cap_hoc = models.CharField(max_length=100, verbose_name='Cấp học')  # Mầm non, Tiểu học, THCS
    loai_hinh = models.CharField(max_length=10, verbose_name='Loại hình')  # 1=CL, 2=CLHQ, 3=DL, 4=TT
    nam_dat_chuan_gan_nhat = models.CharField(max_length=10, blank=True, null=True, verbose_name='Năm đạt chuẩn gần nhất')
    muc_do_cqg = models.CharField(max_length=50, blank=True, null=True, verbose_name='Mức độ CQG')
    so_quyet_dinh_cqg = models.CharField(max_length=200, blank=True, null=True, verbose_name='Số quyết định CQG')
    ghi_chu = models.TextField(blank=True, null=True, verbose_name='Ghi chú')
    
    # Phân loại công nhận mới hay công nhận lại
    loai_cong_nhan = models.CharField(max_length=20, choices=[
        ('CN_MOI', 'Công nhận mới'),
        ('CN_LAI', 'Công nhận lại')
    ], verbose_name='Loại công nhận')
    
    source = models.CharField(max_length=50, default='manual', choices=[
        ('import', 'Import từ Excel'),
        ('manual', 'Nhập thủ công'),
        ('adjusted', 'Đã chỉnh sửa')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bieu1_kq2025'
        ordering = ['ward__stt', 'loai_cong_nhan', 'id']

    def __str__(self):
        return f"{self.ten_truong} - {self.ward.don_vi}"


class Bieu2KH2026(models.Model):
    """Biểu 2 - KẾ HOẠCH CÔNG NHẬN MỚI VÀ CÔNG NHẬN LẠI TRƯỜNG CHUẨN QUỐC GIA NĂM 2026
    Mỗi dòng là một trường học"""
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='bieu2_records')
    phuong_xa = models.CharField(max_length=200, blank=True, null=True, verbose_name='Phường, xã')
    
    # Thông tin trường
    ten_truong = models.CharField(max_length=300, verbose_name='Tên trường')
    cap_hoc = models.CharField(max_length=100, verbose_name='Cấp học')
    loai_hinh = models.CharField(max_length=10, verbose_name='Loại hình')
    nam_dat_cqg_gan_nhat = models.CharField(max_length=10, blank=True, null=True, verbose_name='Năm đạt CQG gần nhất')
    phuong_xa_da_kiem_tra = models.CharField(max_length=10, blank=True, null=True, verbose_name='Phường xã đã kiểm tra')
    du_kien_thang = models.CharField(max_length=100, blank=True, null=True, verbose_name='Dự kiến tháng đề nghị TP đánh giá')
    ghi_chu = models.TextField(blank=True, null=True, verbose_name='Ghi chú')
    
    # Phân loại công nhận mới hay công nhận lại
    loai_cong_nhan = models.CharField(max_length=20, choices=[
        ('CN_MOI', 'Công nhận mới'),
        ('CN_LAI', 'Công nhận lại')
    ], verbose_name='Loại công nhận')
    
    source = models.CharField(max_length=50, default='manual', choices=[
        ('import', 'Import từ Excel'),
        ('manual', 'Nhập thủ công'),
        ('adjusted', 'Đã chỉnh sửa')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bieu2_kh2026'
        ordering = ['ward__stt', 'loai_cong_nhan', 'id']

    def __str__(self):
        return f"{self.ten_truong} - {self.ward.don_vi}"


class Bieu3KH20262030(models.Model):
    """Biểu 3 - KẾ HOẠCH CÔNG NHẬN MỚI VÀ CÔNG NHẬN LẠI TRƯỜNG CHUẨN QUỐC GIA GIAI ĐOẠN 2026-2030
    Mỗi dòng là một trường học"""
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='bieu3_records')
    phuong_xa = models.CharField(max_length=200, blank=True, null=True, verbose_name='Phường, xã')
    
    # Thông tin trường
    ten_truong = models.CharField(max_length=300, verbose_name='Tên trường')
    cap_hoc = models.CharField(max_length=100, verbose_name='Cấp học')
    loai_hinh = models.CharField(max_length=10, verbose_name='Loại hình')
    nam_dat_cqg_gan_nhat = models.CharField(max_length=10, blank=True, null=True, verbose_name='Năm đạt CQG gần nhất')
    
    # Công nhận mới theo năm
    cn_moi_2026 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN mới 2026')
    cn_moi_2027 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN mới 2027')
    cn_moi_2028 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN mới 2028')
    cn_moi_2029 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN mới 2029')
    cn_moi_2030 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN mới 2030')
    
    # Công nhận lại theo năm
    cn_lai_2026 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN lại 2026')
    cn_lai_2027 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN lại 2027')
    cn_lai_2028 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN lại 2028')
    cn_lai_2029 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN lại 2029')
    cn_lai_2030 = models.CharField(max_length=10, blank=True, null=True, verbose_name='CN lại 2030')
    
    ghi_chu = models.TextField(blank=True, null=True, verbose_name='Ghi chú')
    ty_le_dat_cqg = models.CharField(max_length=20, blank=True, null=True, verbose_name='Tỷ lệ đạt CQG hết năm 2030')
    
    source = models.CharField(max_length=50, default='manual', choices=[
        ('import', 'Import từ Excel'),
        ('manual', 'Nhập thủ công'),
        ('adjusted', 'Đã chỉnh sửa')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bieu3_kh2026_2030'
        ordering = ['ward__stt', 'id']

    def __str__(self):
        return f"{self.ten_truong} - {self.ward.don_vi}"


class Bieu4CTThanhPho(models.Model):
    """Biểu 4 - CHƯƠNG TRÌNH THÀNH PHỐ GIAO
    Tổng hợp số lượng công nhận mới và công nhận lại cho từng phường/xã"""
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='bieu4_records', null=True, blank=True)
    stt = models.IntegerField(verbose_name='STT')
    don_vi = models.CharField(max_length=500, verbose_name='Đơn vị')
    
    # Số lượng
    cong_nhan_moi = models.IntegerField(default=0, verbose_name='Công nhận mới')
    cong_nhan_lai = models.IntegerField(default=0, verbose_name='Công nhận lại')
    ghi_chu = models.TextField(blank=True, null=True, verbose_name='Ghi chú')
    
    # Phân loại
    loai = models.CharField(max_length=20, choices=[
        ('THANH_PHO', 'Thành phố'),
        ('PHUONG', 'Phường'),
        ('XA', 'Xã'),
        ('THI_TRAN', 'Thị trấn')
    ], default='PHUONG', verbose_name='Loại')
    
    source = models.CharField(max_length=50, default='manual', choices=[
        ('manual', 'Nhập thủ công'),
        ('adjusted', 'Đã chỉnh sửa')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bieu4_ct_thanh_pho'
        ordering = ['stt']

    def __str__(self):
        return f"Biểu 4 - {self.stt}. {self.don_vi}"
