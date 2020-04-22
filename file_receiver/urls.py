from django.urls import path

from . import views

app_name = 'file_receiver'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
]