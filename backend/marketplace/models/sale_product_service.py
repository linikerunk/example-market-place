from django.db import models
from marketplace.models.sale import Sale
from marketplace.models.product_service import ProductService
from .base import Base


class SaleProductService(Base):
    sale = models.ForeignKey(Sale, on_delete=models.DO_NOTHING)
    product_service = models.ForeignKey(
        ProductService,
        on_delete=models.DO_NOTHING
    )
    quantity = models.IntegerField()

    def __str__(self):
        return self.__class__

    class Meta:
        verbose_name = "SaleProductService"
        verbose_name_plural = "SaleProductServices"