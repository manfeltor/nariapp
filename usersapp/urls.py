from django.contrib import admin
from django.urls import path, include
from .views import usersList, create_eliminate_user_view, CreateEliminateUserView, UserDeleteView

urlpatterns = [
    path('userslist/', usersList, name="userslist"),
    path('createuser/', CreateEliminateUserView.as_view(), name="createuser"),
    path('usuarios/eliminar/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]