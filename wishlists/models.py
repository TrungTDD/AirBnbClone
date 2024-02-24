from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


# Create your models here.
class Wishlist(core_models.AbstractTimeStamp):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(room_models.Room, blank=True)

    def __str__(self):
        return self.name
