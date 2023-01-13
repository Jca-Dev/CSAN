from django import forms
from .models import Product, Review


class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, max_value=99, required=True)

    class Meta:
        model = Product
        fields = ['quantity']


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)


class ReviewForm(forms.ModelForm):
    REVIEW_CHOICES = (
        ("1", ("1")),
        ("2", ("2")),
        ("3", ("3")),
        ("4", ("4")),
        ("5", ("5"))
    )
    rating = forms.ChoiceField(choices=REVIEW_CHOICES, required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 40}), label="Comment")

    class Meta:
        model = Review
        fields = ['rating', 'content',]
