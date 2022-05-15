from django.db import models
from marketplace.models.sale import Sale
from marketplace.models.product_activity import ProductActivity
from .base import Base


class SaleProductActivity(Base):
    sale = models.ForeignKey(Sale, related_name='sales', on_delete=models.DO_NOTHING)
    product_activity = models.ForeignKey(
        ProductActivity,
        related_name='product_activity',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.__class__

    class Meta:
        verbose_name = "SaleProductActivity"
        verbose_name_plural = "SaleProductActivitys"