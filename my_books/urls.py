from django.contrib import admin
from django.urls import path, include # <--- Importante añadir 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')), # <--- Esto conecta con el archivo anterior
]