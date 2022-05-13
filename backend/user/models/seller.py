from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
    
    def __str__(self):
        return self.name
