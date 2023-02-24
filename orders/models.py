from django.db import models
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)

    is_paid = models.BooleanField(default=False)
    order_notes = models.CharField(max_length=500, blank=True)

    zarinpal_authority = models.CharField(max_length=250, blank=True)
    zarinpal_ref_id = models.CharField(max_length=250, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id} of Order {self.order.id}: {self.product} x {self.quantity} (price: {self.price})'
