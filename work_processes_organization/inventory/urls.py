from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('table', views.table, name='table'),
    path('material', views.material, name='material'),
    path('equipment', views.equipment, name='equipment'),

]
