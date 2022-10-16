from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
import random
from django.contrib import messages

from products.models import Category

from .forms import SubscribeForm


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
        messages.success(request, 'Subscribed Successfully')
        subscribe_form.save()

    return redirect('home')
