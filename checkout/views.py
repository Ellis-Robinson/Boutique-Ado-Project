from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51K47v3KmEBOEpD6dkQZKI2hNhghd6eLGvkdELOuUln1LG3YYExV2zFRn1LVUE2h2Iy4rxT9eziiX7tFjXSYdEvGz00JijRs8Gw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)