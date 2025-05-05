from django.urls import path
from .views import base, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('base', base, name="base"),
    path('logout', LogoutView.as_view(), name='logout'),
]