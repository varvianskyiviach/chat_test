from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ["groups", "user_permissions", "password"]
    readonly_fields = [
        "id",
        "date_joined",
        "is_superuser",
        "is_staff",
        "is_active",
        "last_login",
    ]
    list_display = ["email", "first_name", "last_name", "is_active"]
    search_fields = ["email"]
