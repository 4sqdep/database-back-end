from django.contrib import admin
from .models import Categories, SubCategories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


admin.site.register(Categories, CategoriesAdmin)


class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'categories', 'parent', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


admin.site.register(SubCategories, SubCategoriesAdmin)
