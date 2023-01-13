from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from products.forms import ProductForm
from django.contrib import messages
from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = Product.objects.filter(user_wishlist=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated successfully')
        else:
            messages.error(request, 'Update failed. Please check the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist': wishlist,
        'ProductForm': ProductForm,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
        messages.info(request, f'Removed {product.name} from your wishlist <a href="/">Go to Wishlist</a>', extra_tags='safe')
    else:
        product.user_wishlist.add(request.user)
        messages.info(request, f'Added {product.name} to your wishlist')

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
