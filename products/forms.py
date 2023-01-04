from django import forms
from .models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductForm(forms.ModelForm):
    OPACITY_CHOICES = (
        (1, ("3%")),
        (2, ("5%")),
        (3, ("10%")),
        (4, ("20%")),
        (5, ("Blackout"))
    )
    DIAMETER_CHOICES = (
        (1, ("Inside")),
        (2, ("Outside"))
    )
    COLOR_CHOICES = (
        (1, ("")),
        (2, ("")),
        (3, ("")),
        (4, ("")),
        (5, (""))
    )

    color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLOR_CHOICES, required=True)
    opacity = forms.ChoiceField(choices=OPACITY_CHOICES, required=True)
    height = forms.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], label="Height (Inches)", required=True)
    width = forms.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)], label="Width (Inches)", required=True)
    diameter = forms.ChoiceField(choices=DIAMETER_CHOICES, required=True)
    quantity = forms.IntegerField(validators=[MinValueValidator(0)], required=True)

    class Meta:
        model = Product
        fields = ['color', 'opacity', 'height', 'width', 'diameter', 'quantity']
