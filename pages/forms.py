from django import forms

from .models import Subscribe, Contact


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['name', 'email']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
