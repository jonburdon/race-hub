from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified event to the shopping cart """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    which_athlete = request.POST.get('which_athlete')
    print(which_athlete)
    cart = request.session.get('cart', {})

    
    if item_id in list(cart.keys()):
        if which_athlete in cart[item_id]['items_by_athlete'].keys():
            # Add error here to refuse to add another entry for the same athlete
            # cart[item_id]['items_by_athlete'][which_athlete] += quantity
            print (which_athlete)
        else:
            cart[item_id]['items_by_athlete'][which_athlete] = quantity
    else:
        cart[item_id] = {'items_by_athlete': {which_athlete: quantity}}


    # if item_id in list(cart.keys()):
     #   cart[item_id] += quantity
    #else:
    #    cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        which_athlete = None
        if 'which_athlete' in request.POST:
            athlete = request.POST['which_athlete']
        cart = request.session.get('cart', {})

        if athlete:
            del cart[item_id]['which_athlete'][athlete]
            if not cart[item_id]['which_athlete']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)