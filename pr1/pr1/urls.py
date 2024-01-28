# pr1/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinique/', include('clinique.urls')),  # Inclusion des URLs de l'application clinique
]
