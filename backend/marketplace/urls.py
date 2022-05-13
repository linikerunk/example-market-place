from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from rest_framework import routers
from .views.sale import SaleViewSet


router = routers.SimpleRouter()
router.register(r'sale', SaleViewSet)

urlpatterns = router.urls + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

