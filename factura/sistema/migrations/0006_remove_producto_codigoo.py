# Generated by Django 5.1.5 on 2025-01-27 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_rename_codigo_producto_codigoo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='codigoo',
        ),
    ]
