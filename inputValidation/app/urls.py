from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:rel_id/>', views.projects, name='Project'),
]