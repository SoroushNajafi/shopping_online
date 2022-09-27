from django.urls import path, include

from .views import HomePageView, AboutUsPageView, ContactUsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('aboutus/', AboutUsPageView.as_view(), name='aboutus'),
    path('contactus/', ContactUsPageView.as_view(), name='contactus'),
]
