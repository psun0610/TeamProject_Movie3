from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write, name='write'),
    path('write_sec', views.write_sec, name='write_sec'),
    path('content/<int:pk>', views.content, name='content'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('edit_sec/<int:pk>', views.edit_sec, name='edit_sec'),
    path('delete/<int:pk>', views.delete, name='delete'),
]