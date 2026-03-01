from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required 
from .models import Category, MenuItem 
from .forms import CategoryForm 

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = MenuItem.objects.filter(category=category)
    return render(request, 'category_items.html', {
        'category': category, 
        'items': items
    })

@staff_member_required 
def add_category(request):
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})