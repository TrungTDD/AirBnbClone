from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models
import math

# Create your models here.


class Review(core_models.AbstractTimeStamp):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        room_models.Room, on_delete=models.SET_NULL, null=True, related_name="reviews"
    )

    def avg_review(self):
        review_points = [
            self.accuracy,
            self.communication,
            self.cleanliness,
            self.location,
            self.value,
        ]
        return sum(review_points) / len(review_points)
