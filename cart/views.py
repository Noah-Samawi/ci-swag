"""Cart Views"""
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')



def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')

    product = get_object_or_404(Product, pk=item_id)

    print(product)

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()) and quantity:
        cart[item_id] += int(quantity)
    elif quantity:
        cart[item_id] = int(quantity)
    else:
        cart[item_id] = 1


    request.session['cart'] = cart
    return redirect(redirect_url)
