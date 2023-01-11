from django.contrib import admin
from .models import Product, Category, Review


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
            'product',
            'rating',
            'content',
            'created_by',
            'created_at',
        )
    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
