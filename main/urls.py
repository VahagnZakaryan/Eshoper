from django.urls import path
from .views import IndexList, ProductDetail, CategoryList

urlpatterns = [
    path('', IndexList.as_view(), name='home'),
    path('prod/<str:id>/', ProductDetail.as_view(), name='prod'),
    path('category/<str:slug>', CategoryList.as_view(), name='category'),
]
