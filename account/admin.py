from django.contrib import admin
from .models import User, Role


class RolesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_permissions']
    list_display_links = ['id', 'name']

    def get_permissions(self, obj):
        return ", ".join([permission.name for permission in obj.permissions.all()])
    get_permissions.short_description = "Boshqaruv"


admin.site.register(Role, RolesAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_roles', 'username', 'first_name', 'last_name', 'created_at']
    list_display_links = ['id', 'username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name']

    def get_roles(self, obj):
        return ", ".join([role.name for role in obj.role.all()])
    get_roles.short_description = "Roles"


admin.site.register(User, UserAdmin)