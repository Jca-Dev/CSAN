from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html')


def returns(request):
    return render(request, 'homepage/returns.html')


def customer_service(request):
    return render(request, 'homepage/customer_service.html')
