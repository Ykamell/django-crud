# Generated by Django 3.2.10 on 2022-06-27 04:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0013_auto_20220625_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Cedula',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Cellphone',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Lastname',
            field=models.TextField(max_length=45, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='users',
            name='Name',
            field=models.TextField(max_length=45, verbose_name='Nombre'),
        ),
    ]
