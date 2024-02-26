from django.contrib import admin
from django.db.models import Avg, Sum
from django.utils.safestring import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Rule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.all().count()


class PhotoInlineAdmin(admin.TabularInline):
    model = models.Photo


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
        "total_rating",
        "total_photos",
        "count_amenities",
        "total_facilities",
        "total_rules",
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
    inlines = (PhotoInlineAdmin,)

    def count_amenities(self, obj):
        return obj.amenities.all().count()
    
    def total_photos(self, obj):
        return obj.photo_set.all().count()
    
    def total_amenities(self, obj):
        return obj.amenities.all().count()
    
    def total_facilities(self, obj):
        return obj.facilities.all().count()
    
    def total_rules(self, obj):
        return obj.rules.all().count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("caption", "get_thumbnail")

    def get_thumbnail(self, obj):
        # Django prevent to execute the abnormal script which created from customer
        # so in order to do that, they convert to plain text
        # so to execute the html, or script that we knows that it is safe
        # we use `mark_safe`
        return mark_safe(
            f'<img width="50px" height="50px" src="{obj.image_file.url}" />'
        )

    get_thumbnail.short_description = "Thumbnail"
