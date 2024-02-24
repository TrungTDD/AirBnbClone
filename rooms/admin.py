from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rule)
class RuleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "baths",
        "bedrooms",
        "instant_book",
        "count_amenities"
    )
    list_filter = (
        "city",
        "room_type",
        "amenities",
        "facilities",
        "rules__title",
        "instant_book",
        "country",
    )
    filter_horizontal = ("amenities", "facilities", "rules")
    ordering = ("price",)

    def count_amenities(self,obj):
        return obj.amenities.all().count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
