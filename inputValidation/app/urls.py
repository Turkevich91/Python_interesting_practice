from django.urls import path
from . import views

# app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('production/', views.production, name='production'),
    path('manage/', views.management, name='manage'),
    path('engineering/', views.engineering, name='engineering'),
    path('production/<int:project_number/>', views.projects, name='projects'),
]
