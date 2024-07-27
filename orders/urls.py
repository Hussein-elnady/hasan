# orders/urls.py
from django.urls import path
from .views import home, add_order, add_user

urlpatterns = [
    path('', home, name='home'),
    path('add_order/', add_order, name='add_order'),
    path('add_user/', add_user, name='add_user'),
]
