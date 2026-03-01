from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('add-category/', views.add_category, name='add_category'),
]