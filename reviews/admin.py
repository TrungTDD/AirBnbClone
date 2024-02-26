from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "review",
        "accuracy",
        "communication",
        "cleanliness",
        "location",
        "check_in",
        "value",
        "user",
        "room",
        "avg_review",
    )
