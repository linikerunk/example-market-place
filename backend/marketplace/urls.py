from rest_framework.routers import SimpleRouter
from .views.product_activity import ProductActivityViewSet
from .views.sale_product_activity import SaleProductActivityViewSet
from .views.sale import SaleViewSet


router_marketplace = SimpleRouter()
router_marketplace.register('sales', SaleViewSet)
router_marketplace.register('sales/<int:pk>/', SaleViewSet)
router_marketplace.register('product_activitys', ProductActivityViewSet)
router_marketplace.register('product_activitys/<int:pk>/', ProductActivityViewSet)
router_marketplace.register('sale_product_activitys/<int:sale_product_activitys_pk>/product_activitys/', ProductActivityViewSet)
router_marketplace.register('sale_product_activitys', SaleProductActivityViewSet)
router_marketplace.register('sale_product_activitys/<int:pk>/', SaleProductActivityViewSet)
