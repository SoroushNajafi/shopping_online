from django.test import TestCase
from django.shortcuts import reverse

from .models import Product, Category, Comment

from accounts.models import CustomUser


class ProductsListTest(TestCase):

    def setUp(self):
        category = Category.objects.create(category='women')
        product = Product.objects.create(
            category=category,
            title='Sample title',
            description='sample description',
            brand='sample brand',
            price=19.99,
        )
        self.product = product

    def test_products_list_page_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_list_page_reverse(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_products_list_content(self):
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, 'Products list')
        self.assertContains(response, self.product.title)
        self.assertContains(response, self.product.price)

    def test_products_list_template_used(self):
        response = self.client.get(reverse('product_list'))
        self.assertTemplateUsed(response, 'products/product_list.html')


class ProductDetailTest(TestCase):
    def setUp(self):
        category = Category.objects.create(category='women')
        product = Product.objects.create(
            category=category,
            title='Sample title',
            description='sample description',
            brand='sample brand',
            price=19.99,
        )
        self.product = product

    def test_product_detail_by_url(self):
        product_id = self.product.id
        response = self.client.get(f'/products/{product_id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_reverse(self):
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_content(self):
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertContains(response, self.product.title)
        self.assertContains(response, self.product.category)
        self.assertContains(response, self.product.description)

    def test_product_detail_template_used(self):
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertTemplateUsed(response, 'products/product_detail.html')


class ProductsByCategory(TestCase):
    def setUp(self):
        category = Category.objects.create(category='women')
        product = Product.objects.create(
            category=category,
            title='Sample title',
            description='sample description',
            brand='sample brand',
            price=19.99,
        )
        self.product = product
        self.category = category

    def test_products_by_category_url(self):
        response = self.client.get(f'/products/category/{self.category.id}/')
        self.assertEqual(response.status_code, 200)

    def test_products_by_category_reverse(self):
        response = self.client.get(reverse('by_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_products_by_category_content(self):
        response = self.client.get(reverse('by_category', args=[self.category.id]))
        self.assertContains(response, self.category)
        self.assertContains(response, self.product.title)
        self.assertContains(response, self.product.price)

    def test_products_by_category_template_used(self):
        response = self.client.get(reverse('by_category', args=[self.category.id]))
        self.assertTemplateUsed(response, 'products/products_by_category.html')


class CommentTest(TestCase):
    def setUp(self):
        category = Category.objects.create(category='women')
        product = Product.objects.create(category=category, title='Sample title',
                                         description='sample description',
                                         brand='sample brand',
                                         price=19.99,)

        user = CustomUser.objects.create_user(
            username='sample',
            email='sample@email.com',
            password='test1234567password'
        )

        self.client.post('/accounts/login/', {'password': 'test1234567password',
                                              'login': 'sample@email.com'})

        # self.client.force_login(user) inam ye rah baraye login kardane

        self.product = product
        self.user = user

    def test_comment_create(self):
        product_id = self.product.id
        response = self.client.post(f'/products/comment/{product_id}/', {'body': 'sample body',
                                                                                   'stars': '5'})

        last_comment = Comment.objects.last()
        self.assertEqual(last_comment.body, 'sample body')
        self.assertEqual(last_comment.stars, '5')
        self.assertEqual(last_comment.author, self.user)
        self.assertEqual(last_comment.product, self.product)
