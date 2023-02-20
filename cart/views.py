from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product
from django.contrib import messages


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    color = str(request.POST.get('color'))
    opacity = str(request.POST.get('opacity'))
    height = int(request.POST.get('height'))
    width = int(request.POST.get('width'))
    diameter = str(request.POST.get('diameter'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        messages.error(request, f'Sorry, at this time you can only have 1 product variation per order. We are working on this and it will be improved in an upcomming update.')
    else:
        cart[item_id] = {'options': {'quantity': quantity,
                                     'color': color,
                                     'opacity': opacity,
                                     'height': height,
                                     'width': width,
                                     'diameter': diameter,
                                     }}
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id]['options']['quantity'] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["options"]["quantity"]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
