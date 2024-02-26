from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from core import models as core_models
from users import models as user_models
from rooms import models as room_models

# Create your models here.


class Reservation(core_models.AbstractTimeStamp):
    STATUS_PENDING = "Pending"
    STATUS_CANCEL = "Cancel"
    STATUS_CONFIRM = "Confirm"

    STATUSES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CANCEL, "Cancel"),
        (STATUS_CONFIRM, "Confirm"),
    ]

    status = models.CharField(max_length=80, choices=STATUSES)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return self.check_in < now < self.check_out
    
    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return self.check_out < now

    is_finished.boolean = True