from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from shop.cart import Cart
from shop.models import Furniture
from .serializers import FurnitureSerializer


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



class ProductListApiView(ListAPIView):
    '''вывод списка товаров'''
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

class DetailProductApiView(RetrieveAPIView):
    '''вывод информации об 1 товаре (detailview) по id (pk)'''
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
