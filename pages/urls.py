from django.urls import path, include

from .views import HomePageView, AboutUsPageView, subscribe_form_view, contact_us_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('aboutus/', AboutUsPageView.as_view(), name='aboutus'),
    path('contactus/', contact_us_view, name='contactus'),
    path('subscribe/', subscribe_form_view, name='subscribe'),
]
