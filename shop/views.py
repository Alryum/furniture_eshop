from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from .cart import Cart
from .forms import CartAddProductForm
from .models import Furniture


def index(request):
    return render(request, 'shop/index.html')


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Furniture, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


class ProductListView(ListView):
    model = Furniture
    template_name = 'shop/products_list.html'
    context_object_name = 'furniture'
    paginate_by = 10


class DetailProductView(DetailView):
    model = Furniture
    template_name = 'shop/detail.html'
    context_object_name = 'product'
