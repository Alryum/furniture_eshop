from django.urls import path
from .views import CartAddApi, CartDeleteApi, CartDetailApiView, ProductListApiView, DetailProductApiView


urlpatterns = [
    path('cart/', CartDetailApiView.as_view(), name='cart_detail_api'),
    path('cart/add/<int:pk>', CartAddApi.as_view(), name='cart_add_api'),
    path('cart/remove/<int:pk>', CartDeleteApi.as_view(), name='cart_remove_api'),
    path('shop/', ProductListApiView.as_view(), name='product_list_api'),
    path('shop/<int:pk>', DetailProductApiView.as_view(), name='product_detail_api'),
]
