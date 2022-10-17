from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
import random
from django.contrib import messages

from products.models import Category

from .forms import SubscribeForm, ContactUsForm


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class ContactUsPageView(TemplateView):
    template_name = 'pages/contactus.html'


def subscribe_form_view(request):
    subscribe_form = SubscribeForm(request.POST)

    if subscribe_form.is_valid():
        cleaned_date = subscribe_form.cleaned_data
        sent_email = cleaned_date['email']
        sent_name = cleaned_date['name']
        n = random.randint(10000, 99999)
        send_mail(
            'Successfully Subscribed',
            f'Hi {sent_name}, you have subscribed to our newsletter, your voucher code is: {n}\nEnjoy :-)',
            None,
            [sent_email],
            fail_silently=False,
        )
        messages.success(request, 'Subscribed Successfully, Check your E-mail please.')
        subscribe_form.save()
        return redirect('home')

    subscribe_form_errors = subscribe_form.errors
    return render(request, 'pages/home.html', {'subscribe_form_errors': subscribe_form_errors})


def contact_us_from_view(request):
    contact_us_form = ContactUsForm(request.POST)

    if contact_us_form.is_valid():
        cleaned_date = contact_us_form.cleaned_data
        sent_email = cleaned_date['email']
        sent_name = cleaned_date['name']
        send_mail(
            'Thank you for contacting us',
            f'Hi {sent_name}, you have sent a message to our team, we will reach back to you soon, :-)',
            None,
            [sent_email],
            fail_silently=False,
        )
        messages.success(request, 'Your message is sent successfully.')
        contact_us_form.save()
        redirect('home')
    form_errors = contact_us_form.errors
    return render(request, 'pages/contactus.html', {'form_errors': form_errors})
