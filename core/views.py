from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Ward, Bieu1KQ2025, Bieu2KH2026, Bieu3KH20262030, Bieu4CTThanhPho
from .utils import import_bieu1_donvi, import_bieu2_donvi, import_bieu3_donvi, import_all_bieu_donvi
from .utils import export_bieu1_tonghop, export_bieu2_tonghop, export_bieu3_tonghop, export_bieu4_tonghop
import json


def home(request):
    """Trang chủ - Dashboard"""
    context = {
        'total_wards': Ward.objects.count(),
        'bieu1_count': Bieu1KQ2025.objects.count(),
        'bieu2_count': Bieu2KH2026.objects.count(),
        'bieu3_count': Bieu3KH20262030.objects.count(),
        'bieu4_count': Bieu4CTThanhPho.objects.count(),
    }
    return render(request, 'home.html', context)


# ============= IMPORT TẤT CẢ =============
def import_all_bieu(request):
    """Import tất cả 3 biểu từ 1 file Excel"""
    if request.method == 'POST':
        ward_id = request.POST.get('ward_id')
        excel_file = request.FILES.get('excel_file')
        
        if not ward_id or not excel_file:
            messages.error(request, 'Vui lòng chọn phường/xã và file Excel')
            return redirect('import_all_bieu')
        
        try:
            ward = Ward.objects.get(id=ward_id)
            success, message = import_all_bieu_donvi(ward, excel_file)
            
            if success:
                messages.success(request, message)
            else:
                messages.error(request, message)
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
        
        return redirect('home')
    
    wards = Ward.objects.all()
    return render(request, 'import_all_bieu.html', {'wards': wards})


# ============= BIỂU 1 =============
def bieu1_list(request):
    """Danh sách Biểu 1"""
    records_cn_moi = Bieu1KQ2025.objects.select_related('ward').filter(loai_cong_nhan='CN_MOI').order_by('ward__stt', 'ten_truong')
    records_cn_lai = Bieu1KQ2025.objects.select_related('ward').filter(loai_cong_nhan='CN_LAI').order_by('ward__stt', 'ten_truong')
    wards = Ward.objects.all()
    context = {
        'records_cn_moi': records_cn_moi,
        'records_cn_lai': records_cn_lai,
        'total_count': records_cn_moi.count() + records_cn_lai.count(),
        'wards': wards
    }
    return render(request, 'bieu1_list.html', context)


def bieu1_import(request):
    """Import Biểu 1"""
    if request.method == 'POST':
        ward_id = request.POST.get('ward_id')
        excel_file = request.FILES.get('excel_file')
        
        if not ward_id or not excel_file:
            messages.error(request, 'Vui lòng chọn phường/xã và file Excel')
            return redirect('bieu1_import')
        
        try:
            ward = Ward.objects.get(id=ward_id)
            success, message = import_bieu1_donvi(ward, excel_file)
            
            if success:
                messages.success(request, message)
            else:
                messages.error(request, message)
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
        
        return redirect('bieu1_list')
    
    wards = Ward.objects.all()
    return render(request, 'bieu1_import.html', {'wards': wards})


def bieu1_add(request):
    """Thêm record Biểu 1"""
    if request.method == 'POST':
        data = json.loads(request.body)
        ward = Ward.objects.get(id=data.get('ward_id'))
        
        Bieu1KQ2025.objects.create(
            ward=ward,
            phuong_xa=ward.don_vi,
            ten_truong=data.get('ten_truong', ''),
            cap_hoc=data.get('cap_hoc', ''),
            loai_hinh=data.get('loai_hinh', ''),
            nam_dat_chuan_gan_nhat=data.get('nam_dat_chuan_gan_nhat', ''),
            muc_do_cqg=data.get('muc_do_cqg', ''),
            so_quyet_dinh_cqg=data.get('so_quyet_dinh_cqg', ''),
            ghi_chu=data.get('ghi_chu', ''),
            loai_cong_nhan=data.get('loai_cong_nhan', 'CN_MOI'),
            source='manual'
        )
        return JsonResponse({'status': 'success'})


def bieu1_update(request, pk):
    """Cập nhật Biểu 1"""
    if request.method == 'POST':
        data = json.loads(request.body)
        record = Bieu1KQ2025.objects.get(pk=pk)
        
        record.ten_truong = data.get('ten_truong', '')
        record.cap_hoc = data.get('cap_hoc', '')
        record.loai_hinh = data.get('loai_hinh', '')
        record.nam_dat_chuan_gan_nhat = data.get('nam_dat_chuan_gan_nhat', '')
        record.muc_do_cqg = data.get('muc_do_cqg', '')
        record.so_quyet_dinh_cqg = data.get('so_quyet_dinh_cqg', '')
        record.ghi_chu = data.get('ghi_chu', '')
        record.loai_cong_nhan = data.get('loai_cong_nhan', 'CN_MOI')
        record.source = 'adjusted'
        record.save()
        return JsonResponse({'status': 'success'})


def bieu1_delete(request, pk):
    """Xóa record"""
    if request.method == 'POST':
        Bieu1KQ2025.objects.filter(pk=pk).delete()
        return JsonResponse({'status': 'success'})


def bieu1_delete_multiple(request):
    """Xóa nhiều record Biểu 1"""
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', [])
        Bieu1KQ2025.objects.filter(id__in=ids).delete()
        return JsonResponse({'status': 'success', 'deleted': len(ids)})


def bieu1_export(request):
    """Xuất Excel Biểu 1"""
    return export_bieu1_tonghop()


# ============= BIỂU 2 =============
def bieu2_list(request):
    """Danh sách Biểu 2"""
    records_cn_moi = Bieu2KH2026.objects.select_related('ward').filter(loai_cong_nhan='CN_MOI').order_by('ward__stt', 'ten_truong')
    records_cn_lai = Bieu2KH2026.objects.select_related('ward').filter(loai_cong_nhan='CN_LAI').order_by('ward__stt', 'ten_truong')
    wards = Ward.objects.all()
    context = {
        'records_cn_moi': records_cn_moi,
        'records_cn_lai': records_cn_lai,
        'total_count': records_cn_moi.count() + records_cn_lai.count(),
        'wards': wards
    }
    return render(request, 'bieu2_list.html', context)


def bieu2_import(request):
    if request.method == 'POST':
        ward_id = request.POST.get('ward_id')
        excel_file = request.FILES.get('excel_file')
        
        if not ward_id or not excel_file:
            messages.error(request, 'Vui lòng chọn phường/xã và file Excel')
            return redirect('bieu2_import')
        
        try:
            ward = Ward.objects.get(id=ward_id)
            success, message = import_bieu2_donvi(ward, excel_file)
            
            if success:
                messages.success(request, message)
            else:
                messages.error(request, message)
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
        
        return redirect('bieu2_list')
    
    wards = Ward.objects.all()
    return render(request, 'bieu2_import.html', {'wards': wards})


def bieu2_add(request):
    """Thêm record Biểu 2"""
    if request.method == 'POST':
        data = json.loads(request.body)
        ward = Ward.objects.get(id=data.get('ward_id'))
        
        Bieu2KH2026.objects.create(
            ward=ward,
            phuong_xa=ward.don_vi,
            ten_truong=data.get('ten_truong', ''),
            cap_hoc=data.get('cap_hoc', ''),
            loai_hinh=data.get('loai_hinh', ''),
            nam_dat_cqg_gan_nhat=data.get('nam_dat_cqg_gan_nhat', ''),
            phuong_xa_da_kiem_tra=data.get('phuong_xa_da_kiem_tra', ''),
            du_kien_thang=data.get('du_kien_thang', ''),
            ghi_chu=data.get('ghi_chu', ''),
            loai_cong_nhan=data.get('loai_cong_nhan', 'CN_LAI'),
            source='manual'
        )
        return JsonResponse({'status': 'success'})


def bieu2_update(request, pk):
    """Cập nhật Biểu 2"""
    if request.method == 'POST':
        data = json.loads(request.body)
        record = Bieu2KH2026.objects.get(pk=pk)
        
        record.ten_truong = data.get('ten_truong', '')
        record.cap_hoc = data.get('cap_hoc', '')
        record.loai_hinh = data.get('loai_hinh', '')
        record.nam_dat_cqg_gan_nhat = data.get('nam_dat_cqg_gan_nhat', '')
        record.phuong_xa_da_kiem_tra = data.get('phuong_xa_da_kiem_tra', '')
        record.du_kien_thang = data.get('du_kien_thang', '')
        record.ghi_chu = data.get('ghi_chu', '')
        record.loai_cong_nhan = data.get('loai_cong_nhan', 'CN_LAI')
        record.source = 'adjusted'
        record.save()
        return JsonResponse({'status': 'success'})


def bieu2_delete(request, pk):
    """Xóa record Biểu 2"""
    if request.method == 'POST':
        Bieu2KH2026.objects.filter(pk=pk).delete()
        return JsonResponse({'status': 'success'})


def bieu2_delete_multiple(request):
    """Xóa nhiều record Biểu 2"""
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', [])
        Bieu2KH2026.objects.filter(id__in=ids).delete()
        return JsonResponse({'status': 'success', 'deleted': len(ids)})


def bieu2_export(request):
    return export_bieu2_tonghop()


# ============= BIỂU 3 =============
def bieu3_list(request):
    records = Bieu3KH20262030.objects.select_related('ward').all()
    wards = Ward.objects.all()
    return render(request, 'bieu3_list.html', {'records': records, 'wards': wards})


def bieu3_import(request):
    if request.method == 'POST':
        ward_id = request.POST.get('ward_id')
        excel_file = request.FILES.get('excel_file')
        
        if not ward_id or not excel_file:
            messages.error(request, 'Vui lòng chọn phường/xã và file Excel')
            return redirect('bieu3_import')
        
        try:
            ward = Ward.objects.get(id=ward_id)
            success, message = import_bieu3_donvi(ward, excel_file)
            
            if success:
                messages.success(request, message)
            else:
                messages.error(request, message)
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
        
        return redirect('bieu3_list')
    
    wards = Ward.objects.all()
    return render(request, 'bieu3_import.html', {'wards': wards})


def bieu3_add(request):
    """Thêm record Biểu 3"""
    if request.method == 'POST':
        data = json.loads(request.body)
        ward = Ward.objects.get(id=data.get('ward_id'))
        
        Bieu3KH20262030.objects.create(
            ward=ward,
            phuong_xa=ward.don_vi,
            ten_truong=data.get('ten_truong', ''),
            cap_hoc=data.get('cap_hoc', ''),
            loai_hinh=data.get('loai_hinh', ''),
            nam_dat_cqg_gan_nhat=data.get('nam_dat_cqg_gan_nhat', ''),
            cn_moi_2026=data.get('cn_moi_2026', ''),
            cn_moi_2027=data.get('cn_moi_2027', ''),
            cn_moi_2028=data.get('cn_moi_2028', ''),
            cn_moi_2029=data.get('cn_moi_2029', ''),
            cn_moi_2030=data.get('cn_moi_2030', ''),
            cn_lai_2026=data.get('cn_lai_2026', ''),
            cn_lai_2027=data.get('cn_lai_2027', ''),
            cn_lai_2028=data.get('cn_lai_2028', ''),
            cn_lai_2029=data.get('cn_lai_2029', ''),
            cn_lai_2030=data.get('cn_lai_2030', ''),
            ghi_chu=data.get('ghi_chu', ''),
            source='manual'
        )
        return JsonResponse({'status': 'success'})


def bieu3_update(request, pk):
    """Cập nhật Biểu 3"""
    if request.method == 'POST':
        data = json.loads(request.body)
        record = Bieu3KH20262030.objects.get(pk=pk)
        
        record.ten_truong = data.get('ten_truong', '')
        record.cap_hoc = data.get('cap_hoc', '')
        record.loai_hinh = data.get('loai_hinh', '')
        record.nam_dat_cqg_gan_nhat = data.get('nam_dat_cqg_gan_nhat', '')
        record.cn_moi_2026 = data.get('cn_moi_2026', '')
        record.cn_moi_2027 = data.get('cn_moi_2027', '')
        record.cn_moi_2028 = data.get('cn_moi_2028', '')
        record.cn_moi_2029 = data.get('cn_moi_2029', '')
        record.cn_moi_2030 = data.get('cn_moi_2030', '')
        record.cn_lai_2026 = data.get('cn_lai_2026', '')
        record.cn_lai_2027 = data.get('cn_lai_2027', '')
        record.cn_lai_2028 = data.get('cn_lai_2028', '')
        record.cn_lai_2029 = data.get('cn_lai_2029', '')
        record.cn_lai_2030 = data.get('cn_lai_2030', '')
        record.ghi_chu = data.get('ghi_chu', '')
        record.source = 'adjusted'
        record.save()
        return JsonResponse({'status': 'success'})


def bieu3_delete(request, pk):
    """Xóa record Biểu 3"""
    if request.method == 'POST':
        Bieu3KH20262030.objects.filter(pk=pk).delete()
        return JsonResponse({'status': 'success'})


def bieu3_delete_multiple(request):
    """Xóa nhiều record Biểu 3"""
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', [])
        Bieu3KH20262030.objects.filter(id__in=ids).delete()
        return JsonResponse({'status': 'success', 'deleted': len(ids)})


def bieu3_export(request):
    return export_bieu3_tonghop()


# ============= BIỂU 4 =============
def bieu4_list(request):
    """Biểu 4 - Tự động tính từ Biểu 1"""
    # Tự động tạo/cập nhật
    wards = Ward.objects.all()
    
    for ward in wards:
        cn_moi = Bieu1KQ2025.objects.filter(ward=ward, loai_cong_nhan='CN_MOI').count()
        cn_lai = Bieu1KQ2025.objects.filter(ward=ward, loai_cong_nhan='CN_LAI').count()
        
        # Tạo ghi chú "Không có" nếu không có dữ liệu
        ghi_chu = 'Không có' if (cn_moi == 0 and cn_lai == 0) else ''
        
        Bieu4CTThanhPho.objects.update_or_create(
            ward=ward,
            defaults={
                'stt': ward.stt,
                'don_vi': ward.don_vi,
                'cong_nhan_moi': cn_moi,
                'cong_nhan_lai': cn_lai,
                'ghi_chu': ghi_chu,
                'loai': 'PHUONG' if ward.loai == 'phuong' else 'XA'
            }
        )
    
    records = Bieu4CTThanhPho.objects.select_related('ward').all()
    return render(request, 'bieu4_list.html', {'records': records})


def bieu4_export(request):
    return export_bieu4_tonghop()


# ============= API ENDPOINTS =============
def api_wards(request):
    """API để lấy danh sách phường/xã (JSON)"""
    wards = Ward.objects.all().order_by('stt')
    data = [{'id': w.id, 'stt': w.stt, 'don_vi': w.don_vi} for w in wards]
    return JsonResponse(data, safe=False)
