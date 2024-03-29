from django import forms
from .models import Product, Review


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

    quantity = forms.IntegerField(min_value=1, max_value=99, required=True)
    color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLOR_CHOICES, initial="White", required=True)
    opacity = forms.ChoiceField(choices=OPACITY_CHOICES, required=True)
    height = forms.DecimalField(label="Height (Inches)", min_value=1, max_value=200, required=True)
    width = forms.DecimalField(label="Width (Inches)", min_value=1, max_value=120, required=True)
    diameter = forms.ChoiceField(choices=DIAMETER_CHOICES, required=True)

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
