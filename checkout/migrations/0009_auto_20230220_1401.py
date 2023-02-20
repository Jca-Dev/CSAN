# Generated by Django 3.2 on 2023-02-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_alter_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='color',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='diameter',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='height',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='opacity',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='width',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
