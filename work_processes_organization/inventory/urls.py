from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('material', views.material, name='material'),
    path('m_equipment', views.m_equipment, name='m_equipment'),
    path('p_equipment', views.p_equipment, name='personal_equipment'),
    path('table', views.table, name='table'),
]
