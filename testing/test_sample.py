import pytest
from django.urls import reverse

from django import forms


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