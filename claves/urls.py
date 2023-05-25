from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="nombrex"),
    path('cats/', views.cats, name="catsx"),
    path('items/', views.items, name="itemsx")
]