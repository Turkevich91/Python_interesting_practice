from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/material', views.material, name='material'),
    path('inventory/m_equipment', views.m_equipment, name='m_equipment'),
    path('inventory/p_equipment', views.p_equipment, name='personal_equipment'),
]
