from typing import Any
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users.models import User

# Create your models here.


class AbstractItem(core_models.AbstractTimeStamp):

    title = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class RoomType(AbstractItem):

    pass


class Amenity(AbstractItem):
    pass


class Facility(AbstractItem):
    pass


class Rule(AbstractItem):
    pass


class Room(core_models.AbstractTimeStamp):
    title = models.CharField(max_length=255)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=255)
    beds = models.SmallIntegerField()
    baths = models.SmallIntegerField()
    bedrooms = models.SmallIntegerField()
    guests = models.SmallIntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True, related_name="rooms"
    )
    amenities = models.ManyToManyField(Amenity, related_name="rooms")
    facilities = models.ManyToManyField(Facility, related_name="rooms")
    rules = models.ManyToManyField(Rule, related_name="rooms")

    def __str__(self):
        return self.title

    def total_rating(self):
        queryset = self.reviews.all()
        review_point = 0
        for review in queryset:
            review_point += review.avg_review()

        return review_point / len(queryset)


class Photo(core_models.AbstractTimeStamp):
    caption = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to="rooms")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
