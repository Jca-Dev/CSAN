from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    OPACITY_CHOICES = (
        ("3%", ("3%")),
        ("5%", ("5%")),
        ("10%", ("10%")),
        ("20%", ("20%")),
        ("Blackout", ("Blackout"))
    )
    DIAMETER_CHOICES = (
        ("Inside", ("Inside")),
        ("Outside", ("Outside"))
    )
    COLOR_CHOICES = (
        ("Black", ("")),
        ("White", ("")),
        ("Blue", ("")),
        ("Red", ("")),
        ("Green", (""))
    )

    color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLOR_CHOICES, required=True)
    opacity = forms.ChoiceField(choices=OPACITY_CHOICES, required=True)
    height = forms.DecimalField(label="Height (Inches)", min_value=1, max_value=200, required=True)
    width = forms.DecimalField(label="Width (Inches)", min_value=1, max_value=120, required=True)
    diameter = forms.ChoiceField(choices=DIAMETER_CHOICES, required=True)
    quantity = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Product
        fields = ['color', 'opacity', 'height', 'width', 'diameter', 'quantity']
        widgets = {
            'color': forms.RadioSelect(attrs={"required": "required"}),
        }


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)
