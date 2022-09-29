from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import Category


class HomePageView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'home.html'
    context_object_name = 'categories'


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class ContactUsPageView(TemplateView):
    template_name = 'pages/contactus.html'
