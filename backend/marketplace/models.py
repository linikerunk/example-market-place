from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from user.models import Seller, Client


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualização', auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Sale(Base):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    operation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.__class__

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"


class ProductService(Base):
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
        verbose_name = "ProductService"
        verbose_name_plural = "ProductServices"


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
