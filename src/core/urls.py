from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # main
    path('dashboard/', admin.site.urls),

    # API
    path('auth/accounts/', include("apps.accounts.urls")),
    path('cars-data/', include("apps.cars.urls")),
    path('cars/', include("apps.cars_posts.urls")),
    path('tariffs/', include("apps.tariffs.urls")),
    path('house/', include('apps.house.urls')),
    path('main/', include('apps.main.urls')),
    # swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema')),
] + static('/static/', document_root = settings.STATIC_ROOT) + static('/media/', document_root = settings.MEDIA_ROOT)
