# https://docs.djangoproject.com/en/3.0/topics/http/urls/
#
#

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# app_name = "app"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('production/', views.production, name='production'),
    path('management/', views.management, name='management'),
    # path('engineering/', views.engineering, name='engineering'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('production/<int:project_number>/', views.projects, name='projects'),
    path('production/<int:project_number>/<str:release_title>/', views.releases, name='releases'),
    path('production/<int:project_number>/<str:release_title>/<str:panel_title>', views.panels, name='panels'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)