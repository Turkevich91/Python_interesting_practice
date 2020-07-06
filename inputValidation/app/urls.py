# https://docs.djangoproject.com/en/3.0/topics/http/urls/
#
#

from django.urls import path
from . import views

# app_name = "app"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('production/', views.production, name='production'),
    path('manage/', views.management, name='manage'),
    path('engineering/', views.engineering, name='engineering'),
    path('login/', views.login_view, name='login'),
    path('production/<int:project_number>/', views.projects, name='projects'),
    path('production/<int:project_number>/<str:release_title>/', views.releases, name='releases'),
    path('production/<int:project_number>/<str:release_title>/<str:panel_title>', views.panels, name='panels'),
]

