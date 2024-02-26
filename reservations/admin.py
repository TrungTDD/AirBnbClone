from django.contrib import admin
from .models import Reservation


# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "check_in",
        "check_out",
        "room",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status", )
