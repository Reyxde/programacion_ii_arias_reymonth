from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls.categoria_urls')),
    path('libros/', include('catalogo.urls.libro_urls')),
    path('catalogo/home/', include('catalogo.urls.home_urls')),
    path('cuentas/',
         include('catalogo.urls.authentication_urls')),
]