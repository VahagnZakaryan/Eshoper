from django.urls import path
from .views import IndexList, ProductDetail

urlpatterns = [
    path('', IndexList.as_view(), name='home'),
    path('prod/<str:id>/', ProductDetail.as_view(), name = 'prod')
]
