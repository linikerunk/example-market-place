from django.contrib import admin
from .models import Client, Seller


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display =  ['name']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display =  ['name']