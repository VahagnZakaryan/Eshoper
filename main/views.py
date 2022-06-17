from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product, Brend, Slider


# Create your views here.
class IndexList(ListView):
    template_name = 'main/index.html'
    ordering = ['-id']

    def get(self, request):
        prod = Product.objects.all()
        brend = Brend.objects.all()
        cat = Category.objects.filter(parent=None)
        slid = Slider.objects.all()
        context = {
            'prod': prod,
            'brend': brend,
            'cat': cat,
            'slid': slid
        }
        return render(request, self.template_name, context)


class ProductDetail(DetailView):
    template_name = 'main/product_detail.html'

    def get(self, request, id):
        det = Product.objects.get(pk=id)
        brend = Brend.objects.all()
        cat = Category.objects.filter(parent=None)
        return render(request, self.template_name, {'det': det, 'brend': brend, 'cat': cat})


class CategoryList(ListView):
    template_name = 'categoryList.thml'

    def get(self, request, slug):
        categories = Category.objects.filter(parent=None)
        brends = Brend.objects.all()
        products = Product.objects.filter(category__slug=slug).order_by('-id')
        products_b = Product.objects.filter(brand__slug=slug).order_by('-id')
        context = {
            'categories': categories,
            'brends': brends,
            'products': products,
            'products_b': products_b,
        }
        return render(request, self.template_name, context)