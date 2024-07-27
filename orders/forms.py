from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'product_name', 'recipient_name', 'phone', 'alternative_phone',
            'governorate', 'route', 'address', 'shipping_price', 'price', 'notes'
        ]
