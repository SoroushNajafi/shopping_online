from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from products.models import Product, Category
from cart.cart import Cart
from .models import Order, OrderItem


class OrderDetailPage(TestCase):
    def setUp(self):
        product = Product.objects.create(
            category=Category.objects.create(category='women',
                                             cover='media/category/category_cover/baner-right-image-01.jpg'),
            title='product_title',
            description='sample description',
            price=19.90,
            brand='sample_brand',
            image='media/product/Ada_Jacket.jpg',
        )
        self.product = product

        user = get_user_model().objects.create_user(
            username='sample',
            email='testing@gmail.com',
            password='password123456789',
        )
        self.user = user

        self.client.post('/accounts/login/', {'password': 'password123456789',
                                              'login': 'testing@gmail.com'}, follow=True)

    def test_order_detail_page_url(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1,
                                                                               'inplace': False}, follow=True)

        response = self.client.get('/order/create/')
        self.assertEqual(response.status_code, 200)

    def test_order_detail_page_reverse(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1,
                                                                               'inplace': False}, follow=True)

        response = self.client.get(reverse('order_create'))
        self.assertEqual(response.status_code, 200)

    def test_order_detail_page_content(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1,
                                                                               'inplace': False}, follow=True)

        response = self.client.get(reverse('order_create'))
        self.assertContains(response, 'Order Create')
        self.assertContains(response, self.product.title)

    def test_order_detail_page_template_used(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1,
                                                                               'inplace': False}, follow=True)

        response = self.client.get(reverse('order_create'))
        self.assertTemplateUsed(response, 'orders/order_create.html')

    def test_order_create_view_post(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]), {'quantity': 1,
                                                                               'inplace': False}, follow=True)

        response = self.client.post('/order/create/', {'first_name': 'sample_name',
                                                       'last_name': 'last_name',
                                                       'phone_number': '1232342',
                                                       'address': 'sample_address',
                                                       'order_notes': 'sample_note'}, follow=True)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your order's been submitted successfully.")
        self.assertEqual(Order.objects.all().count(), 1)
        self.assertEqual(Order.objects.all()[0].first_name, 'sample_name')
        self.assertEqual(Order.objects.all()[0].last_name, 'last_name')
        self.assertEqual(OrderItem.objects.all().count(), 1)
        self.assertEqual(OrderItem.objects.all()[0].product.title, self.product.title)
        self.assertEqual(float(OrderItem.objects.all()[0].product.price), self.product.price)
        self.assertEqual(Order.objects.all()[0], OrderItem.objects.all()[0].order)
