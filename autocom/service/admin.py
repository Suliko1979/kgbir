from django.contrib import admin
from .models import Category, Model


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'active', 'sort', 'price')
    list_display_links = ['category', 'name', 'active']
    list_filter = ['category', 'active',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Model, ModelAdmin)
