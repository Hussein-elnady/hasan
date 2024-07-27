# orders/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, OrderForm
from .models import User, Order

@login_required
def home(request):
    if request.user.role == 'admin':
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/home.html', {'orders': orders})

@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'orders/add_order.html', {'form': form})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'orders/add_user.html', {'form': form})
