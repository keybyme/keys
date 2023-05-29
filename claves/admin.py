from django.contrib import admin
from .models import Categoria, Item, Catpeople, Contacto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('desc',)
    search_fields = ('desc',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('url', 'username', 'password', 'categoria', 'remarks')
    search_fields = ('url', 'username', 'remarks')
    list_filter = ('categoria',)

@admin.register(Catpeople)
class CatpeopleAdmin(admin.ModelAdmin):
    list_display = ('catp',)
    search_fields = ('catp',)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'catpeople')
    search_fields = ('name', 'address', 'phone', 'email')
    list_filter = ('catpeople',)
