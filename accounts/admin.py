from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Дополнительно", {"fields": ("display_name", "date_of_birth")}),
    )
    
    list_display = ("username", "email", "display_name", "is_staff", "is_superuser")
    search_fields = ("username", "email", "display_name")

admin.site.register(User, UserAdmin)