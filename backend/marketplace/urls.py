from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from .views.sale import SaleView


app_name = "marketplace"

urlpatterns = [
    path('sale/', SaleView.as_view(), name="sale"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)