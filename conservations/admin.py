from django.contrib import admin
from .models import Conversation, Message


# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
