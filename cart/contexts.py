from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from events.models import Event, EventInstance

def cart_contents(request):

    cart_items = []
    total = 0
    entries_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        event = get_object_or_404(EventInstance, pk=item_id)
        total += quantity * event.price
        entries_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'event': event,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'entries_count': entries_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context