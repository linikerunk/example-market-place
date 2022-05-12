from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
    
    def __str__(self):
        return self.name