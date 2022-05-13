from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from .views.client import ClientView


app_name = "marketplace"

urlpatterns = [
    path('client/', ClientView.as_view(), name="sale"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)