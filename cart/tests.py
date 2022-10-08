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
                                         price=19.50, )

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

    def test_add_to_cart(self):
        response0 = self.client.post(reverse('cart:add_to_cart', args=[self.product.id]))
        self.assertEqual(response0.status_code, 302)
        response = self.client.get(reverse('cart:cart_detail'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, self.product.price)
        self.assertContains(response, self.product.title)
        # request = response.wsgi_request
        # cart = Cart(request)
        # self.assertEqual(len(cart), 1)
        # with open('output.html', 'w') as f:
        #     f.write(response.content.decode('utf-8'))

        # messages = list(response.context['messages'])
        # self.assertEqual(len(messages), 1)
        # self.assertEqual(str(messages[0]), 'Product successfully added to cart')

    def test_remove_cart_by_url(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]))
        response = self.client.post(f'/cart/remove/{self.product.id}/')
        self.assertEqual(response.status_code, 302)

    def test_remove_cart_reverse(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]))
        response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

    def test_remove_cart_redirect(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]))
        response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]))
        self.assertRedirects(response, reverse('cart:cart_detail'))

    def test_remove_cart_content(self):
        self.client.post(reverse('cart:add_to_cart', args=[self.product.id]))
        response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]), follow=True)
        # self.assertNotContains(response, self.product.title)
        # self.assertNotContains(response, self.product.price)
        self.assertNotContains(response, self.product.id)



