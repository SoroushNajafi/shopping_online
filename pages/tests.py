from django.test import TestCase
from django.urls import reverse

from .models import Contact, Subscribe


class HomePageTest(TestCase):

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_reverse(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home')

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/home.html')


class AboutUsTest(TestCase):

    def test_about_us_page_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_url_reverse(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us')

    def test_about_us_page_template_used(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')


class ContactUsPageTest(TestCase):
    def test_contact_us_page_url(self):
        response = self.client.get('/contactus/')
        self.assertEqual(response.status_code, 200)

    def test_contact_us_page_reverse(self):
        response = self.client.get(reverse('contactus'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_page_content(self):
        response = self.client.get(reverse('contactus'))
        self.assertContains(response, 'Contact Us')

    def test_contact_us_page_template_used(self):
        response = self.client.get(reverse('contactus'))
        self.assertTemplateUsed(response, 'pages/contactus.html')

    def test_contact_us_form(self):
        response = self.client.post('/contactus/', {'name': 'sample',
                                                    'email': 'sample@email.com',
                                                    'message': 'sample_message'}, follow=True)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your message is sent successfully.')
        self.assertEqual(Contact.objects.all().count(), 1)
        self.assertEqual(response.status_code, 200)


class SubscribeFormTest(TestCase):
    def test_subscribe_form(self):
        response = self.client.post('/subscribe/', {'name': 'sample',
                                                    'email': 'sample@email.com'}, follow=True)

        self.assertEqual(Subscribe.objects.all()[0].name, 'sample')
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Subscribed Successfully, Check your E-mail please.')
        self.assertEqual(response.status_code, 200)
