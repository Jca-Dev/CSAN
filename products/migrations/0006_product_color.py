# Generated by Django 3.2 on 2023-01-05 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='white', max_length=255),
        ),
    ]
