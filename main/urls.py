from django.urls import path
from .views import IndexList, ProductDetail, CategoryList, ProductList, BlogList, BlogDetail

urlpatterns = [
    path('', IndexList.as_view(), name='home'),
    path('allblogs', BlogList.as_view(), name='allblogs'),
    path('blog/<str:id>', BlogDetail.as_view(), name='blogDetail'),
    path('products', ProductList.as_view(), name='products'),
    path('prod/<str:id>/', ProductDetail.as_view(), name='prod'),
    path('category/<str:slug>', CategoryList.as_view(), name='category'),
]
