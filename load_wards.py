"""
Script để load dữ liệu phường/xã từ CSV vào database
Chạy: python load_wards.py
"""
import os
import sys
import django
import pandas as pd

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataapp.settings')
django.setup()

from core.models import Ward

def load_wards():
    """Load danh sách phường/xã từ CSV"""
    csv_file = '../ds_phuong_xa.csv'
    
    if not os.path.exists(csv_file):
        print(f"Không tìm thấy file {csv_file}")
        return
    
    # Đọc file CSV
    df = pd.read_csv(csv_file)
    
    print(f"Đọc được {len(df)} dòng từ file CSV")
    
    # Import vào database
    count_created = 0
    count_updated = 0
    
    for _, row in df.iterrows():
        obj, created = Ward.objects.update_or_create(
            stt=row['stt'],
            defaults={
                'don_vi': row['don_vi'],
                'loai': row['loai']
            }
        )
        
        if created:
            count_created += 1
        else:
            count_updated += 1
    
    print(f"\nKết quả:")
    print(f"- Tạo mới: {count_created} phường/xã")
    print(f"- Cập nhật: {count_updated} phường/xã")
    print(f"- Tổng: {Ward.objects.count()} phường/xã trong database")

if __name__ == '__main__':
    load_wards()
