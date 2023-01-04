from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'image',
    )

    ordering = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
