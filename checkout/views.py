from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K8BS4Cv3YU8vyKQzXYoxX5bemjcoyDq5SoMI4dp1EsZOB31ie4OmV9Fa9TKC3s0fdDBmoJ8wbe8KpjeW9xQ7oqM00FbS02yNW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)