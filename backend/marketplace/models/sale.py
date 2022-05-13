from django.db import models
from django.utils import timezone
from .base import Base
from user.models.client import Client
from user.models.seller import Seller


class Sale(Base):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    operation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.__class__

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"