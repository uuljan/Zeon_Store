from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from ZeonShopApi import settings
from ZeonShopApi.settings import MEDIA_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
