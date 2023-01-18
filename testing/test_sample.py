import pytest
from django.urls import reverse
from products import models
from django import forms
from checkout import models


#def test_category_name(product_category):
#    assert product_category.__str__() == 'django'
#
#
#def test_product_name(product_product):
#    assert product_product.__str__() == 'django'
#
#
#@pytest.mark.django_db
#def test_auth_view(auto_login_user):
#    client, user = auto_login_user()
#    url = reverse('profile')
#    response = client.get(url)
#    assert response.status_code == 200
#
#
#class ExampleForm(forms.Form):
#    name = forms.CharField(required=True)
#    age = forms.IntegerField(min_value=18)
#
#
#@pytest.mark.parametrize(
#    'name, age, validity',
#    [('Hugo', 18, True),
#     ('Egon', 17, False),
#     ('Balder', None, False),
#     ('', 18, False),
#     (None, 18, False),
#     ])
#
#
#def test_example_form(name, age, validity):
#    form = ExampleForm(data={
#        'name': name,
#        'age': age,
#    })
#
#    assert form.is_valid() is validity
#
#class Test_Product_Get_rating:
#
#
#    @pytest.fixture()
#    def product(self):
#        return models.Product()
#
#
#    def test_get_rating_1(self, product):
#        result = product.get_rating()
#
#
#class Test_Order__generate_order_number:
#
#
#    @pytest.fixture()
#    def order(self):
#        return models.Order()
#
#
#    def test__generate_order_number_1(self, order):
#        result = order._generate_order_number()
