from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .base import Base 


class ProductActivity(Base):
    name = models.CharField(max_length=200)
    is_product = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    commission = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
    )
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name

    @property
    def _get_total_price(self):
        return self.price * self.quantity
    class Meta:
        verbose_name = "ProductActivity"
        verbose_name_plural = "ProductActivitys"