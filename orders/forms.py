# orders/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'recipient_name', 'phone', 'alternate_phone', 'governorate', 'route', 'address', 'shipping_price', 'price', 'notes']
