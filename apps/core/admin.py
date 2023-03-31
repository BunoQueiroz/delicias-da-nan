from django.contrib import admin
from core.models import Dish, Drink

class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'serves', 'category']
    list_editable = ['name', 'description', 'price']
    list_display_links = ['id',]
    list_filter = ['category', 'serves']
    search_fields = ['name', 'description']

class DrinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'category']
    list_editable = ['name', 'description', 'price']
    list_display_links = ['id',]
    list_filter = ['category']
    search_fields = ['name', 'description']

admin.site.register(Dish, DishAdmin)
admin.site.register(Drink, DrinkAdmin)
