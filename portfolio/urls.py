from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # Include allows app-specific URL configurations.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),  # Include URLs from your app.
]

# Add static and media URL configurations when in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
