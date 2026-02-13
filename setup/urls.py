from django.contrib import admin
from django.urls import path, include  # Importe o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('escola.urls')),  # Redireciona tudo para o arquivo urls.py da escola
]