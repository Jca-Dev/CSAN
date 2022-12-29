from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    OPACITY_CHOICES = (
        (1, ("3%")),
        (2, ("5%")),
        (3, ("7%")),
        (4, ("20%")),
        (5, ("Blackout"))
    )
    DIAMETER_CHOICES = (
        (1, ("Inside")),
        (2, ("Outside"))
    )
    COLOUR_CHOICES = (
        (1, ("")),
        (2, (""))
    )
    colour = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=COLOUR_CHOICES,)
    opacity = forms.ChoiceField(choices=OPACITY_CHOICES)
    height = forms.IntegerField(label="Height (Inches)")
    width = forms.IntegerField(label="Height (Inches)")
    diameter = forms.ChoiceField(choices=DIAMETER_CHOICES)

    class Meta:
        model = Product
        fields = ['colour', 'opacity', 'height', 'width', 'diameter']
