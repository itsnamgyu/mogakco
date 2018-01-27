from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('cafe/index', views.index, name='index'),
    path('cafe/create', views.create, name='create'),
    path('cafe/submit_cafe', views.submit_cafe, name='submit_cafe'),
    path('cafe/<int:cafe_pk>/add_review', views.add_review, name='add_review'),
    path('cafe/<int:cafe_pk>/add_prices', views.add_prices, name='add_prices'),
    path('cafe/<int:cafe_pk>/submit_review', views.submit_review, name='submit_review'),
    path('cafe/<int:cafe_pk>/submit_prices', views.submit_prices, name='submit_prices'),
]
