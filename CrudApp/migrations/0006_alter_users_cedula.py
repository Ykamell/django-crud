# Generated by Django 3.2.10 on 2022-06-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0005_alter_users_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Cedula',
            field=models.BigIntegerField(null=True, verbose_name='Cédula'),
        ),
    ]
