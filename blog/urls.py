from django.contrib import admin
from django.urls import include, path
from users.api.router import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/', include('users.api.router')),
]
