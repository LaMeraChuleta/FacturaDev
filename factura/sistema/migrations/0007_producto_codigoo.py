# Generated by Django 5.1.5 on 2025-01-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_remove_producto_codigoo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigoo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
