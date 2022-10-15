from django import forms


class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
