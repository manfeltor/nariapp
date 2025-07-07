# cultivationapp/urls/meta.py
from django.urls import path
from cultivationapp.views import meta

urlpatterns = [
    path('<str:model_name>/', meta.meta_list_view, name='meta-list'),
    path('<str:model_name>/crear/', meta.meta_create_view, name='meta-create'),
    path('<str:model_name>/editar/<int:pk>/', meta.meta_update_view, name='meta-update'),
    path('<str:model_name>/eliminar/<int:pk>/', meta.meta_delete_view, name='meta-delete'),
]
