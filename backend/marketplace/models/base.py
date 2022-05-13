from django.db import models


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualização', auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
