from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Import tất cả
    path('import-all/', views.import_all_bieu, name='import_all_bieu'),
    
    # Biểu 1
    path('bieu1/', views.bieu1_list, name='bieu1_list'),
    path('bieu1/import/', views.bieu1_import, name='bieu1_import'),
    path('bieu1/add/', views.bieu1_add, name='bieu1_add'),
    path('bieu1/update/<int:pk>/', views.bieu1_update, name='bieu1_update'),
    path('bieu1/delete/<int:pk>/', views.bieu1_delete, name='bieu1_delete'),
    path('bieu1/delete-multiple/', views.bieu1_delete_multiple, name='bieu1_delete_multiple'),
    path('bieu1/export/', views.bieu1_export, name='bieu1_export'),
    
    # Biểu 2
    path('bieu2/', views.bieu2_list, name='bieu2_list'),
    path('bieu2/import/', views.bieu2_import, name='bieu2_import'),
    path('bieu2/add/', views.bieu2_add, name='bieu2_add'),
    path('bieu2/update/<int:pk>/', views.bieu2_update, name='bieu2_update'),
    path('bieu2/delete/<int:pk>/', views.bieu2_delete, name='bieu2_delete'),
    path('bieu2/delete-multiple/', views.bieu2_delete_multiple, name='bieu2_delete_multiple'),
    path('bieu2/export/', views.bieu2_export, name='bieu2_export'),
    
    # Biểu 3
    path('bieu3/', views.bieu3_list, name='bieu3_list'),
    path('bieu3/import/', views.bieu3_import, name='bieu3_import'),
    path('bieu3/add/', views.bieu3_add, name='bieu3_add'),
    path('bieu3/update/<int:pk>/', views.bieu3_update, name='bieu3_update'),
    path('bieu3/delete/<int:pk>/', views.bieu3_delete, name='bieu3_delete'),
    path('bieu3/delete-multiple/', views.bieu3_delete_multiple, name='bieu3_delete_multiple'),
    path('bieu3/export/', views.bieu3_export, name='bieu3_export'),
    
    # Biểu 4
    path('bieu4/', views.bieu4_list, name='bieu4_list'),
    path('bieu4/update/<int:pk>/', views.bieu4_update, name='bieu4_update'),
    path('bieu4/export/', views.bieu4_export, name='bieu4_export'),
    
    # APIs
    path('api/wards/', views.api_wards, name='api_wards'),
]
