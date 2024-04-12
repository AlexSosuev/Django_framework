from django.contrib import admin
from .models import Client, Product, OrderItem, Order


class HWAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'added_date']
    ordering = ['name', '-price']
    list_filter = ['added_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'

admin.site.register(Client)
admin.site.register(Product, HWAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)