# Generated by Django 3.2.4 on 2021-06-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carDearlership', '0003_alter_car_carcondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='sellerNumber',
            field=models.CharField(max_length=30),
        ),
    ]
