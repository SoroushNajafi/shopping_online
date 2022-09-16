from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class LogInPageTest(TestCase):
    username = 'sample'
    email = 'email@email.com'
    password = 'password123456789'

    def test_login_page_by_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_reverse(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_content(self):
        response = self.client.get(reverse('account_login'))
        self.assertContains(response, 'Log In')

    def test_login_page_template_used(self):
        response = self.client.get(reverse('account_login'))
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_redirect(self):
        user = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
        response = self.client.post('/accounts/login/', {'password': 'password123456789',
                                                         'login': 'email@email.com'})

        self.assertEqual(response.status_code, 302)


class SignUpPageTest(TestCase):

    def test_sign_up_page_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_page_reverse(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_content(self):
        response = self.client.get(reverse('account_signup'))
        self.assertContains(response, 'Sign Up')

    def test_sign_up_template_used(self):
        response = self.client.get(reverse('account_signup'))
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_sign_up_redirect(self):
        response = self.client.post('/accounts/signup/', {'username': 'sample',
                                                          'password1': 'pass1234sample',
                                                          'password2': 'pass1234sample',
                                                          'email': 'sample_email@sample.com'})

        # with open('output.html', 'w') as f:
        #     f.write(response.content.decode('utf-8'))

        self.assertRedirects(response, reverse('home'))


class LogOutPageTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username='sample',
            email='sample@email.com',
            password='test1234567password'
        )
        self.client.post('/accounts/login/', {'password': 'test1234567password',
                                              'login': 'sample@email.com'})

    def test_log_out_page_by_url(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)

    def test_log_out_page_reverse(self):
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 200)

    def test_log_out_page_content(self):
        response = self.client.get(reverse('account_logout'))
        self.assertContains(response, 'Log Out')

    def test_log_out_page_template_used(self):
        response = self.client.get(reverse('account_logout'))
        self.assertTemplateUsed(response, 'account/logout.html')

    def test_log_out_page_redirect(self):
        response = self.client.post('/accounts/logout/', {'password': 'test1234567password',
                                                          'email': 'sample@email.com'})
        self.assertRedirects(response, reverse('home'))

