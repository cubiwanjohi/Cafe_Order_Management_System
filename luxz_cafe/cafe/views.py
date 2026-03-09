from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework import generics
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer

from .models import Category, MenuItem, Order 
from .forms import CategoryForm 

def home(request):
    """Fetches all food categories and displays them on the homepage."""
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_items(request, category_id):
    """Shows all menu items belonging to a specific category (e.g., all 'Drinks')."""
    category = get_object_or_404(Category, id=category_id)
    items = MenuItem.objects.filter(category=category)
    return render(request, 'category_items.html', {'category': category, 'items': items})

@staff_member_required 
def add_category(request):
    """Allows staff to add new categories."""
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def register(request):
    """Handles new user registration using Django's built-in auth form."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/register.html', {'form': UserCreationForm()})

class CategoryListAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemListAPI(generics.ListCreateAPIView):
    """views all categories or create a new one."""
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderListAPI(generics.ListCreateAPIView):
    """customer views or places orders."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer