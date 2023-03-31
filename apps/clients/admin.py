from django.contrib import admin
from clients.models import Client, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'first_name', 'email', 'phone']
    list_editable = ['first_name',]
    list_display_links = ['cpf',]
    list_per_page = 10
    list_filter = ['first_name',]
    search_fields = ['first_name', 'last_name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'amount']
    list_editable = ['amount',]
    list_display_links = ['client',]
    list_filter = ['client',]
    search_fields = ['product']


admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
