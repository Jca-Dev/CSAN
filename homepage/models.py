from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Testimonial(models.Model):
    created_by = models.ForeignKey(User, related_name='testimonials', on_delete=models.CASCADE)
    rating = models.CharField(default='Ok', max_length=9)
    head = models.CharField(max_length=26, null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)