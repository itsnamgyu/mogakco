from django.urls import path
from . import views

#Create your Urls here.
urlpatterns = [
    path('', views.displayMainPage, name='main'),
    path('search', views.displaySearchPage, name='search'),
    path('result/<slug:keyword>', views.displayResultPage, name='result'),
]
