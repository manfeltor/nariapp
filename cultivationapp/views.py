from django.shortcuts import render
from .models import PlantRoom

# Create your views here.
def roomsList(request):
    rooms = PlantRoom.objects.all()  # Retrieve all users
    return render(request, 'list_rooms.html', {'rooms': rooms})
