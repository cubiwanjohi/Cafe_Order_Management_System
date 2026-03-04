from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('add-category/', views.add_category, name='add_category'),

    path('api/categories/', views.CategoryListAPI.as_view(), name='api-categories'),
    path('api/menu/', views.MenuItemListAPI.as_view(), name='api-menu'),
    path('api/orders/', views.OrderListAPI.as_view(), name='api-orders'),
]