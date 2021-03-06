# Generated by Django 3.2.4 on 2021-06-25 16:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carDearlership', '0006_rename_carmaker_car_carmake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carCondition',
            field=models.CharField(choices=[('poor', 'Poor'), ('fair', 'Fair'), ('good', 'Good'), ('excellent', 'Excellent')], max_length=10, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='car',
            name='carMake',
            field=models.CharField(max_length=30, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='car',
            name='carModel',
            field=models.CharField(max_length=30, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='carPrice',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1000)], verbose_name='Asking Price'),
        ),
        migrations.AlterField(
            model_name='car',
            name='carYear',
            field=models.CharField(max_length=4, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='car',
            name='sellerName',
            field=models.CharField(max_length=30, verbose_name='Seller name'),
        ),
        migrations.AlterField(
            model_name='car',
            name='sellerNumber',
            field=models.CharField(max_length=30, verbose_name='Seller mobile'),
        ),
    ]
