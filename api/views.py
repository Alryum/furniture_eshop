from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response
from shop.cart import Cart
from shop.models import Furniture
from .serializers import FurnitureSerializer, CartItemSerializer


class CartAddApi(APIView):
    '''добавляет товар в корзину по id(pk)'''
    def post(self, request, pk):
        product = get_object_or_404(Furniture, pk=pk)
        quantity = request.data.get('quantity', 1)
        cart = Cart(request)
        cart.add(product=product, quantity=quantity)
        return Response({'message': 'Product added to cart successfully.'})


class CartDeleteApi(APIView):
    '''удаляет товар из корзины по id(pk)'''
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Furniture, pk=pk)
        cart.remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetailApiView(APIView):
    '''отдает всю корзину'''
    '''TODO нужно еще вытянуть общую цену итд, смотри item'''
    def get(self, request):
        cart = Cart(request)
        # cart_items = cart.__iter__()

        cart_items_list = []
        # for item in cart_items:
        for item in cart:
            serializer = FurnitureSerializer(item['product'])
            cart_items_list.append(serializer.data)

        if not cart_items_list:
            return Response({'message': 'cart is empty'})

        return Response(cart_items_list)



class ProductListApiView(APIView):
    '''вывод списка товаров'''
    pass


class DetailProductApiView(APIView):
    '''вывод информации об 1 товаре (detailview)'''
    pass
