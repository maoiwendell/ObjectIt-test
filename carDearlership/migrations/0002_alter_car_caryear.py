# Generated by Django 3.2.4 on 2021-06-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carDearlership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carYear',
            field=models.CharField(max_length=4),
        ),
    ]
