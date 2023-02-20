from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data, in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        quantity = item_data['options']['quantity']
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'product': product,
            'quantity': quantity,
            'color': item_data['options']['color'],
            'opacity': item_data['options']['opacity'],
            'height': item_data['options']['height'],
            'width': item_data['options']['width'],
            'diameter': item_data['options']['diameter'],
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
