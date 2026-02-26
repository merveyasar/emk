from django.contrib import admin
from django.urls import path, include # include eklemeyi unutma
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # core iÃ§indeki urls.py'yi buraya baÄŸladÄ±k
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)