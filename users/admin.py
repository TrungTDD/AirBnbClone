from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomerAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "gender",
        "birthdate",
        "language",
        "currency",
        "superhost",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost", "currency")
