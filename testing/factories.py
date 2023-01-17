import factory
from products.models import Category, Product
from profiles.models import UserProfile
from faker import Faker

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'django'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
#        django_get_or_create = ('name',)

    name = 'django'
    price = 1
