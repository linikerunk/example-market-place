# Generated by Django 4.0.4 on 2022-05-15 03:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_alter_productactivity_commission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleproductactivity',
            name='quantity',
        ),
        migrations.AddField(
            model_name='productactivity',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productactivity',
            name='commission',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
