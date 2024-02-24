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
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    rules = models.ManyToManyField(Rule)

    def __str__(self):
        return self.title


class Photo(core_models.AbstractTimeStamp):
    caption = models.CharField(max_length=255)
    image_file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
