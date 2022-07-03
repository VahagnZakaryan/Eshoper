from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexList.as_view(), name='home'),
    path('allblogs', BlogList.as_view(), name='allblogs'),
    path('blog/<str:id>', BlogDetail.as_view(), name='blogDetail'),
    path('products', ProductList.as_view(), name='products'),
    path('prod/<str:id>/', ProductDetail.as_view(), name='prod'),
    path('category/<str:slug>', CategoryList.as_view(), name='category'),
    path("register", register_request, name='register'),
    path("login", login_request, name='login'),
    path("logout", logout_request, name='logout'),
    path("add_comment", CreateView.as_view(), name = 'comment'),
]

