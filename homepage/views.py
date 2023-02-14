from django.shortcuts import render
from .forms import TestimonialForm
from .models import Testimonial
from django.contrib import messages


def index(request):
    tform = TestimonialForm
    testimonials = Testimonial.objects.all()

    data = {
        'tform': tform,
        'testimonials': testimonials
    }
    return render(request, 'homepage/index.html', data)


def returns(request):
    return render(request, 'homepage/returns.html')


def customer_service(request):
    return render(request, 'homepage/customer_service.html')
