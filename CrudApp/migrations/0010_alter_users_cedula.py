# Generated by Django 3.2.10 on 2022-06-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0009_auto_20220625_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Cedula',
            field=models.BigIntegerField(default=None, verbose_name='Cédula'),
        ),
    ]
