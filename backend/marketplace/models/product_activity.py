from django.db import models
from django.core.exceptions import ValidationError
from .base import Base 


class ProductActivity(Base):
    name = models.CharField(max_length=200)
    is_product = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    commission = models.DecimalField(max_digits=2, decimal_places=2)

    def _commission(self):
        if self.commission > 10 or self.commission < 0:
            raise ValidationError({
                'error': 'Comissão deve estar entre 0 e 10 %'
            })
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ProductActivity"
        verbose_name_plural = "ProductActivitys"