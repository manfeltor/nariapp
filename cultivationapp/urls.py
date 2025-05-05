from django.urls import path
from .views import roomsList


urlpatterns = [
    path('userslist/', roomsList, name="roomslist"),
]