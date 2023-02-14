from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    TESTIMONIAL_CHOICES = (
        ("Very Poor", ("Very Poor")),
        ("Poor", ("Poor")),
        ("Ok", ("Ok")),
        ("Good", ("Good")),
        ("Very Good", ("Very Good"))
    )
    rating = forms.ChoiceField(choices=TESTIMONIAL_CHOICES, required=True)
    head = forms.CharField(widget=forms.Textarea(attrs={"rows": 1, "cols": 40}), required=True, label="Heading")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 40}), required=True, label="Comment")

    class Meta:
        model = Testimonial
        fields = ['rating', 'head', 'content',]
