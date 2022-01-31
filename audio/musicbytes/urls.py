from django.urls import path
from . import views

app_name = 'musicbytes'
urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:alb_id>/', views.details, name='albumdetails'),
    path('update/', views.upload, name='upload'),
    path('edit/<int:a_id>/', views.edit, name='edit'),
    path('delete/<int:a_id>/', views.delete, name='delete')
]
