from django.contrib import admin
from .models import Sale, ProductService, SaleProductService


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display =  ['client', 'seller', 'operation_date']


@admin.register(ProductService)
class ProductServiceAdmin(admin.ModelAdmin):
    list_display =  ['name', 'is_product', 'price', 'commission']


@admin.register(SaleProductService)
class SaleProductServiceAdmin(admin.ModelAdmin):
    list_display =  ['sale', 'product_service', 'quantity']