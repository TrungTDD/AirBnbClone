from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.


class Conversation(core_models.AbstractTimeStamp):
    participants = models.ManyToManyField(user_models.User, blank=True)

    def __str__(self):
        usernames = []
        for p in self.participants.all():
            usernames.append(p.username)
        return ", ".join(usernames)

    def total_messages(self):
        return self.message_set.count()


class Message(core_models.AbstractTimeStamp):
    message = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.conversation}"
