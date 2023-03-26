from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from .cart import Cart
from .forms import CartAddProductForm
from .models import Furniture


def index(request):
    return render(request, 'shop/index.html')


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Furniture, id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Furniture, id=pk)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})


class ProductListView(ListView):
    model = Furniture
    template_name = 'shop/products_list.html'
    context_object_name = 'furniture'
    paginate_by = 10


class DetailProductView(DetailView):
    model = Furniture
    template_name = 'shop/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
