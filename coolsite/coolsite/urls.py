from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from coolsite import settings
from women.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
handler404 = pageNotFound