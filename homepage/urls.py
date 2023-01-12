from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('returns/', views.returns, name='returns'),
    path('customer_service/', views.customer_service, name='customer_service')
]
