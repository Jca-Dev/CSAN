from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    category = request.GET.get('category')

    if category is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)

    categories = Category.objects.all()

    data = {
        'products': products,
        'categories': categories
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
