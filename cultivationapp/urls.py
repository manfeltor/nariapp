from django.urls import path
from .views import roomsList, create_room_view


urlpatterns = [
    path('roomslist/', roomsList, name="roomslist"),
    path('createroom/', create_room_view, name="createroom"),
]