# Generated by Django 3.2 on 2023-01-05 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_diameter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='diameter',
        ),
    ]
