from django.urls import path, include

urlpatterns = [
    path('meta/', include('cultivationapp.urls.meta')),
    path('rooms/', include('cultivationapp.urls.rooms')),
]
