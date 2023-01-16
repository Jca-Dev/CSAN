from django.test import TestCase
import unittest
from .models import Product, Review


class ProductModelTest(unittest.TestCase):

    def test_item_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_item_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


class ReviewModelTest(unittest.TestCase):

    def test_created_by_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('created_by').verbose_name
        self.assertEqual(field_label, 'created by')

    def test_rating_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')

    def test_item_name_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('content').max_length
        self.assertEqual(max_length, 500)
