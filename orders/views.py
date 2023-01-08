from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'You can not proceed to "Checkout" because Your cart is empty.')
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_form_obj = order_form.save(commit=False)
            order_form_obj.user = request.user
            order_form_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_form_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )
            cart.clear()
            messages.success(request, "Your order's been submitted successfully.")

            request.user.first_name = order_form_obj.first_name
            request.user.last_name = order_form_obj.last_name
            request.user.save()
            return redirect('home')

    return render(request, 'orders/order_create.html', {'order_form': order_form})
