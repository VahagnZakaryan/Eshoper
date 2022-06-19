from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product, Slider, Blog


# Create your views here.
class IndexList(ListView):
    template_name = 'main/index.html'
    ordering = ['-id']

    def get(self, request):
        prod = Product.objects.all()
        cat = Category.objects.filter(parent=None)
        slid = Slider.objects.all()
        context = {
            'prod': prod,
            'cat': cat,
            'slid': slid
        }
        return render(request, self.template_name, context)


class ProductDetail(DetailView):
    template_name = 'main/product_detail.html'

    def get(self, request, id):
        det = Product.objects.get(pk=id)
        cat = Category.objects.filter(parent=None)
        return render(request, self.template_name, {'det': det, 'cat': cat})


class CategoryList(ListView):
    template_name = 'main/categoryList.html'

    def get(self, request, slug):
        cat = Category.objects.filter(parent=None)
        prod = Product.objects.filter(category__slug=slug).order_by('-id')
        # products_b = Product.objects.filter(brand__slug=slug).order_by('-id')
        context = {
            'cat': cat,
            'prod': prod,
            # 'products_b': products_b,
        }
        return render(request, self.template_name, context)


class ProductList(ListView):
    template_name = 'main/productList.html'

    def get(self, request):
        prod = Product.objects.all()
        cat = Category.objects.filter(parent=None)
        context = {
            'prod': prod,
            'cat': cat,
        }
        return render(request, self.template_name, context)


class BlogList(ListView):
    template_name = 'main/blog.html'

    def get(self, request):
        blog = Blog.objects.all()
        cat = Category.objects.filter(parent=None)
        context = {
            'blog': blog,
            'cat': cat,
        }
        return render(request, self.template_name, context)


class BlogDetail(DetailView):
    template_name = 'main/blog_detail.html'

    def get(self, request, id):
        blog = Blog.objects.get(pk=id)
        cat = Category.objects.filter(parent=None)
        context = {
            'blog': blog,
            'cat': cat,
        }
        return render(request, self.template_name, context)
