from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('profiles/', include('profiles.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
