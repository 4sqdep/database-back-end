from django.contrib import admin
from .models import Categories, SubCategories, Projects, Files


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


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'subcategories', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


admin.site.register(Projects, ProjectsAdmin)


class FilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_code', 'user', 'created_at']
    list_display_links = ['id', 'file_code']
    search_fields = ['id', 'file_code']


admin.site.register(Files, FilesAdmin)
