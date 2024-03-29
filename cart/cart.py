from django.contrib import messages

from products.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """

        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        adding product to cart
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
            messages.success(self.request, 'Product successfully updated.')
        else:
            self.cart[product_id]['quantity'] += quantity
            messages.success(self.request, 'Product successfully added to cart.')

        self.save()

    def remove(self, product):
        """
        remove product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, 'product removed successfully')
            self.save()

    def save(self):
        """
        save changes
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        """
        returning the number of products when called
        """
        return len(self.cart.keys())

    def clear(self):
        """
        delete cart
        """
        del self.session['cart']
        self.save()

    def get_total_price(self):
        """calculating total price"""

        return sum(item['quantity'] * item['product_obj'].price for item in self.cart.values())





