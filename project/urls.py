import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]


if settings.DEBUG:
    urlpatterns += static('node_modules', document_root=os.path.join(settings.BASE_DIR, 'node_modules'))
