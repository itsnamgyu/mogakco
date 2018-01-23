from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('index', views.cafe_list, name='index')
]
