from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()

    data = {
        'products': products
    }

    return render(request, 'products/products.html', data)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm()

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'products/product_detail.html', context)
