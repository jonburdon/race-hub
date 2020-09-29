from django.shortcuts import render, redirect

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
            cart[item_id]['items_by_athlete'][which_athlete] += quantity
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