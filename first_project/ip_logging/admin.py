from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    ordering = ("email",)

    list_display = ("email", "role", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
            )
        }),
        ("Role", {"fields": ("role",)}),
    )

    add_fieldsets = (
        (None, {
            "fields": (
                "email",
                "password1",
                "password2",
                "role",
                "is_staff",
                "is_active",
            ),
        }),
    )