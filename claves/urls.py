from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="nombrex"),
    path('cats/', views.cats, name="catsx"),
    path('items/', views.items, name="itemsx"),
    path('contactos/', views.contactos, name="contactosx"),
    path('login/', views.login_user, name="login"),
    path('edit_item/<int:pk>', views.edit_items, name="editx"),
    path('edit_contacto/<int:pk>', views.edit_contactos, name="editconx"),
    path('add_item', views.add_items, name="addx"),
    path('add_contacto', views.add_contactos, name="addconx"),
    path('delete_item/<int:pk>', views.delete_items, name="deletex"),
    path('delete_contacto/<int:pk>', views.delete_contactos, name="deleteconx"),
    path('logout/', views.logout_user, name="logoutx"),
    path('qrcode/', views.generate_qr_code, name="qrcodex"), 
]