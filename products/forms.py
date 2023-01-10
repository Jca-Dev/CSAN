from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Product
        fields = ['quantity']


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)
