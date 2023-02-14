from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
            'rating',
            'created_by'
        )
    ordering = ('created_by',)

admin.site.register(Testimonial, TestimonialAdmin)
