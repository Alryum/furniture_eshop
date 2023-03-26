from django.urls import path
from .views import index, cart_detail, cart_remove, cart_add, ProductListView, DetailProductView


urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>', cart_add, name='cart_add'),
    path('cart/remove/<int:pk>', cart_remove, name='cart_remove'),
    path('shop/', ProductListView.as_view(), name='shop'),
    path('product/<int:pk>/', DetailProductView.as_view(), name='detail_product'),
]
