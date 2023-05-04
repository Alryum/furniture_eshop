from django.urls import path
from .views import CartAddApi, CartDeleteApi, CartDetailApiView


urlpatterns = [
    path('cart/', CartDetailApiView.as_view(), name='cart_detail_api'),
    path('cart/add/<int:pk>', CartAddApi.as_view(), name='cart_add_api'),
    path('cart/remove/<int:pk>', CartDeleteApi.as_view(), name='cart_remove_api'),
]
