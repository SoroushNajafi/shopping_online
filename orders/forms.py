from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'order_notes': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Any extra notes here'}),
        } # in widgets faghat baraye zahere form e, mituni cosumize koni
