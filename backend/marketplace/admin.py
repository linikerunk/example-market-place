from django.contrib import admin
from .models.sale import Sale
from .models.product_activity import ProductActivity
from .models.sale_product_activity import SaleProductActivity


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display =  ['client', 'seller', 'operation_date']


@admin.register(ProductActivity)
class ProductActivityAdmin(admin.ModelAdmin):
    list_display =  ['name', 'is_product', 'price', 'commission', 'quantity']


@admin.register(SaleProductActivity)
class SaleProductActivityAdmin(admin.ModelAdmin):
    list_display =  ['sale', 'product_activity']
