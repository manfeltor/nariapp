from django.shortcuts import render, redirect
from ..models import PlantRoom
from django.contrib.auth.decorators import login_required
from ..forms.rooms import PlantRoomForm


# Create your views here.
def roomsList(request):
    rooms = PlantRoom.objects.all()  # Retrieve all users
    return render(request, 'list_rooms.html', {'rooms': rooms})

@login_required
def create_room_view(request):
    # if not request.user.is_superuser:
    #     return redirect('unauthorized')

    if request.method == 'POST':
        form = PlantRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roomslist')
    else:
        form = PlantRoomForm()

    return render(request, 'create_room.html', {'form': form})
