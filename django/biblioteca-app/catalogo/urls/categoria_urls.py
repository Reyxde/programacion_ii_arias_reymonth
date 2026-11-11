from django.urls import path 
from catalogo.views.categoria_views import (
    categoria_list, categoria_create, categoria_delete, categoria_update
)

urlpatterns = [
    path('categorias/',
         categoria_list,
         name='categoria_list'),
    path('categorias/nueva/',
         categoria_create,
         name='categoria_create'),
    path('categoria/<int:pk>/editar/',
         categoria_update,
         name='categoria_update'),
    path('categoria/<int:pk>/eliminar/',
         categoria_delete,
         name='categoria_delete'),
]