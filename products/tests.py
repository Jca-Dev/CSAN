from django.test import TestCase
import unittest
from .models import Product, Review


class TestProduct(unittest.TestCase):
    """models exist"""
    def test_function_returns_product(self):
        assert (Product({}))

    def test_function_returns_review(self):
        assert (Review({}))


if __name__ == '__main__':
    unittest.main()
