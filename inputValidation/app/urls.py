from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('production/', views.production, name='production'),
    path('manage/', views.manage, name='manage'),
    path('engineering/', views.engineering, name='engineering')
    # path('<int:rel_id/>', views.projects, name='Project'),
]