from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="nombrex"),
    path('cats/', views.cats, name="catsx"),
    path('items/', views.items, name="itemsx"),
    path('login/', views.login_user, name="login"),
    path('edit_item/<int:pk>', views.edit_items, name="editx"),
    path('add_item', views.add_items, name="addx"),
    path('delete_item/<int:pk>', views.delete_items, name="deletex")
]