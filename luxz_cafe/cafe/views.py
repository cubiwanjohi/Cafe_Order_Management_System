from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework import generics
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer
from .models import Category, MenuItem, Order 
from .forms import CategoryForm 

def home(request):
    """
    Renders the main landing page.
    Fetches all available menu categories to be displayed in the UI.
    """
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_items(request, category_id):
    """
    Filters and displays menu items based on a selected category ID.
    Uses get_object_or_404 to ensure robust error handling if the ID is invalid.
    """
    category = get_object_or_404(Category, id=category_id)
    items = MenuItem.objects.filter(category=category)
    return render(request, 'category_items.html', {'category': category, 'items': items})

@staff_member_required 
def add_category(request):
    """
    Secure view for administrative staff to create new menu categories.
    Handles both the GET (display form) and POST (save data) logic.
    """
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
    """
    Standard user registration portal using Django's built-in UserCreationForm.
    Redirects to the login page upon successful account creation.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    # Re-renders the form with validation errors if the POST was invalid
    return render(request, 'registration/register.html', {'form': UserCreationForm()})

# ==========================================
# API ENDPOINTS (REST Framework)
# ==========================================
class CategoryListAPI(generics.ListCreateAPIView):
    """
    Endpoint for listing categories or creating new ones via JSON.
    Supports GET (List) and POST (Create) methods.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemListAPI(generics.ListCreateAPIView):
    """
    Endpoint for retrieving the full menu or adding new items.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderListAPI(generics.ListCreateAPIView):
    """
    Endpoint for customers to view order history or submit new orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer