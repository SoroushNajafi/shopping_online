from django.test import TestCase
from django.shortcuts import reverse

from products.models import Product, Category
from .cart import Cart


class CartDetailTest(TestCase):

    def setUp(self):
        category = Category.objects.create(category='men', cover='category/category_cover/baner-right-image-01.jpg')

        product = Product.objects.create(category=category, title='sample title',
                                         description='sample description',
                                         brand='sample brand',
                                         price=19.59, )

        self.product = product

    def test_cart_detail_by_url(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_cart_detail_reverse(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)

    def test_cart_detail_template_used(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertTemplateUsed(response, 'cart/cart_detail.html')

    def test_add_to_cart_url(self):
        response0 = self.client.post(f'/cart/add/{self.product.id}/',
                                     {'quantity': 3, 'inplace': False}, follow=True)

        self.assertEqual(response0.status_code, 200)
        self.assertContains(response0, 'Sample title')
        self.assertContains(response0, self.product.price)

        request = response0.wsgi_request
        cart = Cart(request)
        self.assertEqual(len(cart), 1)

        messages = list(response0.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product successfully added to cart.')

    def test_add_to_cart_reverse(self):
        response0 = self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                                     {'quantity': 3, 'inplace': False}, follow=True)

        self.assertEqual(response0.status_code, 200)
        self.assertContains(response0, 'Sample title')
        self.assertContains(response0, self.product.price)

        request = response0.wsgi_request
        cart = Cart(request)
        self.assertEqual(len(cart), 1)

        messages = list(response0.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product successfully added to cart.')

    def test_remove_cart_by_url(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'inplace': False}, follow=True)

        response = self.client.post(f'/cart/remove/{self.product.id}/', follow=True)
        self.assertEqual(response.status_code, 200)
        request = response.wsgi_request
        cart = Cart(request)
        self.assertEqual(len(cart), 0)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'product removed successfully')

    def test_remove_cart_reverse(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'inplace': False}, follow=True)

        response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        request = response.wsgi_request
        cart = Cart(request)
        self.assertEqual(len(cart), 0)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'product removed successfully')

    def test_remove_cart_redirect(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'inplace': False}, follow=True)

        response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]))
        self.assertRedirects(response, reverse('cart:cart_detail'))

    def test_remove_cart_content(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'inplace': False}, follow=True)

        response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]), follow=True)

        self.assertNotContains(response, self.product.title)
        self.assertNotContains(response, self.product.price)

    def test_clear_cart_url(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'inplace': False}, follow=True)

        response = self.client.get('/cart/clear/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.product.title)
        request = response.wsgi_request
        cart = Cart(request)
        self.assertEqual(len(cart), 0)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'cart cleared successfully')

    def test_clear_cart_reverse(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]),
                         {'quantity': 3, 'inplace': False}, follow=True)

        response = self.client.get(reverse('cart:clear_cart'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.product.title)
        request = response.wsgi_request
        cart = Cart(request)
        self.assertEqual(len(cart), 0)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'cart cleared successfully')




