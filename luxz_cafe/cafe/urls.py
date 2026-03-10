from django.urls import path
from . import views

urlpatterns = [
    # Homepage: Shows categories.
    path('', views.home, name='home'),
    # Category Detail: <int:category_id> captures the ID from the URL to show specific items
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    # Add Category: The page where staff can create new menu sections
    path('add-category/', views.add_category, name='add_category'),
    # Registration: The page for new users to sign up
    path('register/', views.register, name='register'), 
    path('api/categories/', views.CategoryListAPI.as_view(), name='api-categories'),
    # Menu API: View or create individual food/drink items
    path('api/menu/', views.MenuItemListAPI.as_view(), name='api-menu'),
    # Orders API: View or place new orders
    path('api/orders/', views.OrderListAPI.as_view(), name='api-orders'),
]