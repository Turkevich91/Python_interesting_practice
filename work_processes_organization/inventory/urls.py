from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('material', views.material, name='material'),
    path('machine_equipment', views.machine_equipment, name='machine_equipment'),
    path('personal_equipment', views.personal_equipment, name='personal_equipment'),
    path('table', views.table, name='table'),
]
