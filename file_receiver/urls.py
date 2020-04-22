from django.urls import path

from . import views

app_name = 'file_receiver'
urlpatterns = [
    path('', views.FileListView.as_view(), name='file_list'),
    path('index/', views.index, name='index'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('delete/<int:pk>', views.delete_file, name='delete_file'),
]