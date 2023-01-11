from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.TextField()
    sku = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1020, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=4)
    content = models.CharField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
