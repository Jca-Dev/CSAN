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

    color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLOR_CHOICES, required=True, error_messages={
                    "unique": "Please select a color."
                    })
    opacity = forms.ChoiceField(choices=OPACITY_CHOICES, required=True)
    height = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], label="Height (Inches)", required=True)
    width = forms.IntegerField(label="Width (Inches)", required=True)
    diameter = forms.ChoiceField(choices=DIAMETER_CHOICES, required=True)

    class Meta:
        model = Product
        fields = ['color', 'opacity', 'height', 'width', 'diameter']
