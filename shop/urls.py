from django.urls import path
from .views import index, ProductListView, DetailProductView


urlpatterns = [
    path('', index, name='index'),
    path('shop/', ProductListView.as_view(), name='shop'),
    path('product/<int:pk>', DetailProductView.as_view(), name='detail_product'),
]
