from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('all_hosts.app.urls')),
    path('help/', include('all_hosts.help.urls')),
]
