# https://docs.djangoproject.com/en/3.0/topics/http/urls/
#
#

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'app'
# https://youtu.be/w4nrT7emiVc?t=4766

urlpatterns = [
    path('', views.home_view, name='home'),
    path('production/', views.production, name='production'),
    path('management/', views.management, name='management'),
    # path('engineering/', views.engineering, name='engineering'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('production/<int:project_number>/', views.project_view, name='project_view'),
    path('production/<int:project_number>/<str:release_title>/', views.release_view, name='release_view'),
    path('production/<int:project_number>/<str:release_title>/<str:panel_title>', views.panel_info, name='panel_info'),
    # path('pdf', views.pdf_view, name='pdf'),
    # re_path(r' *.pdf$', views.pdf, name='pdf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
