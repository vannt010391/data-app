from django.contrib import admin
from .models import Ward, Bieu1KQ2025, Bieu2KH2026, Bieu3KH20262030, Bieu4CTThanhPho


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['stt', 'don_vi', 'loai']
    search_fields = ['don_vi']


@admin.register(Bieu1KQ2025)
class Bieu1Admin(admin.ModelAdmin):
    list_display = ['ward', 'ten_truong', 'cap_hoc', 'loai_cong_nhan', 'source']
    list_filter = ['source', 'loai_cong_nhan', 'cap_hoc']
    search_fields = ['ward__don_vi', 'ten_truong']


@admin.register(Bieu2KH2026)
class Bieu2Admin(admin.ModelAdmin):
    list_display = ['ward', 'ten_truong', 'cap_hoc', 'loai_cong_nhan', 'source']
    list_filter = ['source', 'loai_cong_nhan', 'cap_hoc']
    search_fields = ['ward__don_vi', 'ten_truong']


@admin.register(Bieu3KH20262030)
class Bieu3Admin(admin.ModelAdmin):
    list_display = ['ward', 'ten_truong', 'cap_hoc', 'source']
    list_filter = ['source', 'cap_hoc']
    search_fields = ['ward__don_vi', 'ten_truong']


@admin.register(Bieu4CTThanhPho)
class Bieu4Admin(admin.ModelAdmin):
    list_display = ['stt', 'don_vi', 'cong_nhan_moi', 'cong_nhan_lai', 'loai']
    list_filter = ['loai']
    search_fields = ['don_vi']
