from rest_framework.routers import SimpleRouter
from .views.client import ClientViewSet
from .views.seller import SellerViewSet


router_user = SimpleRouter()

router_user.register('clients', ClientViewSet),
router_user.register('clients/<int:pk>', ClientViewSet),
router_user.register('sellers', SellerViewSet),
router_user.register('sellers/<int:pk>', SellerViewSet)