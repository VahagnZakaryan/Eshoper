from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product, Brend


# Create your views here.
class IndexList(ListView):
    template_name = 'main/index.html'
    ordering = ['-id']

    def get(self, request):
        prod = Product.objects.all()
        brend = Brend.objects.all()
        cat = Category.objects.filter(parent=None)
        context = {
            'prod': prod,
            'brend': brend,
            'cat': cat,
        }
        return render(request, self.template_name, context)


class ProductDetail(DetailView):
    template_name = 'main/product_detail.html'

    def get(self, request, id):
        det = Product.objects.get(pk=id)
        brend = Brend.objects.all()
        cat = Category.objects.filter(parent=None)
        return render(request, self.template_name, {'det': det, 'brend': brend,'cat': cat})
