from pipes import Template
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormView
from .models import *
from .forms import NewUserForm, CommentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request, 'main/register.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'main/login.html', context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'ou have successfully logged out.')
    return redirect('home')


class IndexList(ListView):
    template_name = 'main/index.html'
    ordering = ['-id']

    def get(self, request):
        prod = Product.objects.all()
        cat = Category.objects.filter(parent=None)
        slid = Slider.objects.all()
        super_slid = SupterSlider.objects.all()
        context = {
            'prod': prod,
            'cat': cat,
            'slid': slid,
            'super_slid': super_slid
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


class ContactsList(ListView):
    template_name = 'main/contacts.html'

    def get(self, reqest):
        cont = Contacts.objects.all()
        return render(reqest, self.template_name, {'cont': cont})


# class CommentView(TemplateView):
#     template_name = 'main/product_detail.html'

#     def get(self, request):
#         comment = CommentForm()
#         comments = Comment.objects.all()
#         args = {'comment' : comment, 'comments': comments}
#         return render(request, self.template_name, args)
    
#     def post(self, request):
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             comment = comment.save(commit = False)
#             comment.user = request.user
#             comment.save()

#             text = comment.cleaned_data['post']
#             comment = CommentForm()
#             return redirect('main/product_detail.html')
    
#         args = {'comment': comment, 'text': text}
#         return render(request, self.template_name, args)

class CommentView(FormView):
    template_name = 'main/product_detail.html'
    form_class = CommentForm
    success_url = 'main/product_detail.html'