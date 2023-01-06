from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from .forms import ProductForm, AddProductForm
from django.contrib.auth.decorators import login_required


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
    form = ProductForm({'color': 'White'})

    data = {
        'product': product,
        'form': form
    }

    return render(request, 'products/product_detail.html', data)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            print('Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            return redirect(reverse('home'))
    else:
        form = AddProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
