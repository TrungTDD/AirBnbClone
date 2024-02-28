from django.urls import path
from rooms import views as room_views


urlpatterns = [
    path("", room_views.ListRooms.as_view()),
]
