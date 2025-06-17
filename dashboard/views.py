from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, CategoryForm

@login_required
def home(request):
    """Dashboard home view showing summary statistics"""
    context = {
        'total_products': Product.objects.count(),
        'total_categories': Category.objects.count(),
        'low_stock_products': Product.objects.filter(stock_quantity__lt=10).count(),
        'products': Product.objects.order_by('-created_at')[:5],  # Latest 5 products
    }
    return render(request, 'dashboard/home.html', context)

class ProductListView(LoginRequiredMixin, ListView):
    """View to list all products"""
    model = Product
    template_name = 'dashboard/product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 10

class ProductDetailView(LoginRequiredMixin, DetailView):
    """View to show product details"""
    model = Product
    template_name = 'dashboard/product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    """View to create a new product"""
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/product_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, f'Product has been created!')
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """View to update an existing product"""
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/product_form.html'
    
    def form_valid(self, form):
        messages.success(self.request, f'Product has been updated!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a product"""
    model = Product
    template_name = 'dashboard/product_confirm_delete.html'
    success_url = '/products/'
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f'Product has been deleted!')
        return super().delete(request, *args, **kwargs)

class CategoryListView(LoginRequiredMixin, ListView):
    """View to list all categories"""
    model = Category
    template_name = 'dashboard/category_list.html'
    context_object_name = 'categories'
    ordering = ['name']

class CategoryCreateView(LoginRequiredMixin, CreateView):
    """View to create a new category"""
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/category_form.html'
    success_url = '/categories/'
    
    def form_valid(self, form):
        messages.success(self.request, f'Category has been created!')
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """View to update an existing category"""
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/category_form.html'
    success_url = '/categories/'
    
    def form_valid(self, form):
        messages.success(self.request, f'Category has been updated!')
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a category"""
    model = Category
    template_name = 'dashboard/category_confirm_delete.html'
    success_url = '/categories/'
