from django.contrib import admin
from .models import Conversation, Message


# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "total_messages")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "conversation")
