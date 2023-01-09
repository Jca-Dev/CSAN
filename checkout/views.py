from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        print("There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)