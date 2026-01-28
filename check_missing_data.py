"""
Script kiểm tra các phường/xã thiếu dữ liệu
Chạy: python manage.py shell < check_missing_data.py
hoặc: python manage.py shell
>>> exec(open('check_missing_data.py').read())
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataapp.settings')
django.setup()

from core.models import Ward, Bieu1KQ2025, Bieu2KH2026, Bieu3KH20262030

def check_missing_data():
    """Kiểm tra các phường/xã thiếu dữ liệu"""
    
    all_wards = Ward.objects.all().order_by('stt')
    total_wards = all_wards.count()
    
    print("=" * 80)
    print(f"TỔNG SỐ PHƯỜNG/XÃ: {total_wards}")
    print("=" * 80)
    
    # Kiểm tra Biểu 1
    print("\n📋 BIỂU 1 - KẾT QUẢ CÔNG NHẬN MỚI VÀ CÔNG NHẬN LẠI NĂM 2025")
    print("-" * 80)
    
    missing_bieu1_cn_moi = []
    missing_bieu1_cn_lai = []
    
    for ward in all_wards:
        # Kiểm tra CN mới
        has_cn_moi = Bieu1KQ2025.objects.filter(ward=ward, loai_cong_nhan='CN_MOI').exists()
        if not has_cn_moi:
            missing_bieu1_cn_moi.append(ward)
        
        # Kiểm tra CN lại
        has_cn_lai = Bieu1KQ2025.objects.filter(ward=ward, loai_cong_nhan='CN_LAI').exists()
        if not has_cn_lai:
            missing_bieu1_cn_lai.append(ward)
    
    print(f"Số phường/xã KHÔNG CÓ dữ liệu CÔNG NHẬN MỚI: {len(missing_bieu1_cn_moi)}")
    if missing_bieu1_cn_moi:
        for ward in missing_bieu1_cn_moi[:5]:  # Hiển thị 5 cái đầu
            print(f"  - {ward.stt}. {ward.don_vi}")
        if len(missing_bieu1_cn_moi) > 5:
            print(f"  ... và {len(missing_bieu1_cn_moi) - 5} phường/xã khác")
    
    print(f"\nSố phường/xã KHÔNG CÓ dữ liệu CÔNG NHẬN LẠI: {len(missing_bieu1_cn_lai)}")
    if missing_bieu1_cn_lai:
        for ward in missing_bieu1_cn_lai[:5]:
            print(f"  - {ward.stt}. {ward.don_vi}")
        if len(missing_bieu1_cn_lai) > 5:
            print(f"  ... và {len(missing_bieu1_cn_lai) - 5} phường/xã khác")
    
    # Kiểm tra Biểu 2
    print("\n📋 BIỂU 2 - KẾ HOẠCH CÔNG NHẬN MỚI VÀ CÔNG NHẬN LẠI NĂM 2026")
    print("-" * 80)
    
    missing_bieu2_cn_moi = []
    missing_bieu2_cn_lai = []
    
    for ward in all_wards:
        # Kiểm tra CN mới
        has_cn_moi = Bieu2KH2026.objects.filter(ward=ward, loai_cong_nhan='CN_MOI').exists()
        if not has_cn_moi:
            missing_bieu2_cn_moi.append(ward)
        
        # Kiểm tra CN lại
        has_cn_lai = Bieu2KH2026.objects.filter(ward=ward, loai_cong_nhan='CN_LAI').exists()
        if not has_cn_lai:
            missing_bieu2_cn_lai.append(ward)
    
    print(f"Số phường/xã KHÔNG CÓ dữ liệu CÔNG NHẬN MỚI: {len(missing_bieu2_cn_moi)}")
    if missing_bieu2_cn_moi:
        for ward in missing_bieu2_cn_moi[:5]:
            print(f"  - {ward.stt}. {ward.don_vi}")
        if len(missing_bieu2_cn_moi) > 5:
            print(f"  ... và {len(missing_bieu2_cn_moi) - 5} phường/xã khác")
    
    print(f"\nSố phường/xã KHÔNG CÓ dữ liệu CÔNG NHẬN LẠI: {len(missing_bieu2_cn_lai)}")
    if missing_bieu2_cn_lai:
        for ward in missing_bieu2_cn_lai[:5]:
            print(f"  - {ward.stt}. {ward.don_vi}")
        if len(missing_bieu2_cn_lai) > 5:
            print(f"  ... và {len(missing_bieu2_cn_lai) - 5} phường/xã khác")
    
    # Kiểm tra Biểu 3
    print("\n📋 BIỂU 3 - KẾ HOẠCH CÔNG NHẬN MỚI VÀ CÔNG NHẬN LẠI GIAI ĐOẠN 2026-2030")
    print("-" * 80)
    
    missing_bieu3 = []
    for ward in all_wards:
        has_data = Bieu3KH20262030.objects.filter(ward=ward).exists()
        if not has_data:
            missing_bieu3.append(ward)
    
    print(f"Số phường/xã KHÔNG CÓ dữ liệu: {len(missing_bieu3)}")
    if missing_bieu3:
        for ward in missing_bieu3[:5]:
            print(f"  - {ward.stt}. {ward.don_vi}")
        if len(missing_bieu3) > 5:
            print(f"  ... và {len(missing_bieu3) - 5} phường/xã khác")
    
    # Tổng kết
    print("\n" + "=" * 80)
    print("📊 TỔNG KẾT")
    print("=" * 80)
    print(f"Tổng số phường/xã: {total_wards}")
    print(f"\nBiểu 1:")
    print(f"  - Có ít nhất 1 loại dữ liệu: {total_wards - len([w for w in all_wards if w in missing_bieu1_cn_moi and w in missing_bieu1_cn_lai])}")
    print(f"  - Thiếu cả 2 loại: {len([w for w in missing_bieu1_cn_moi if w in missing_bieu1_cn_lai])}")
    print(f"\nBiểu 2:")
    print(f"  - Có ít nhất 1 loại dữ liệu: {total_wards - len([w for w in all_wards if w in missing_bieu2_cn_moi and w in missing_bieu2_cn_lai])}")
    print(f"  - Thiếu cả 2 loại: {len([w for w in missing_bieu2_cn_moi if w in missing_bieu2_cn_lai])}")
    print(f"\nBiểu 3:")
    print(f"  - Có dữ liệu: {total_wards - len(missing_bieu3)}")
    print(f"  - Không có dữ liệu: {len(missing_bieu3)}")
    print("=" * 80)

if __name__ == '__main__':
    check_missing_data()
