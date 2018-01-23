from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('index', views.list, name='index'),
    path('create', views.create, name='create'),
]
