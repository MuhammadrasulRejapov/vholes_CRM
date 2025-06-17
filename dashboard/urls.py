from django.urls import path
from . import views
from .views import (
    ProductListView, ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView, CategoryListView,
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView
)

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
