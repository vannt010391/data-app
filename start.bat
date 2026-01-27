@echo off
echo ===============================================
echo HUONG DAN CHAY UNG DUNG
echo ===============================================
echo.

echo Buoc 1: Cai dat thu vien
pip install -r requirements.txt

echo.
echo Buoc 2: Tao database
python manage.py makemigrations
python manage.py migrate

echo.
echo Buoc 3: Load du lieu phuong/xa
python load_wards.py

echo.
echo Buoc 4: Tao tai khoan admin (tuy chon)
echo Nhan Ctrl+C de bo qua hoac nhap thong tin:
python manage.py createsuperuser

echo.
echo Buoc 5: Chay ung dung
echo Truy cap: http://localhost:8000
python manage.py runserver

pause
