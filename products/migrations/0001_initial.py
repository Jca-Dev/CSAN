# Generated by Django 3.2 on 2022-12-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sku', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField(blank=True, max_length=1020, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]