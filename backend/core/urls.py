from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from marketplace.urls import router_marketplace
from user.urls import router_user
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('painel/', admin.site.urls),
    path('api/v1/', include(router_marketplace.urls)),
    path('api/v1/', include(router_user.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain_token'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
