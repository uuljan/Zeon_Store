from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from .cart import Cart
from .form import CartAddProductForm
from rest_framework.response import Response
from rest_framework import status

from .serializers import CartSerializer
from .models import Cart as CartModel

class CartViewSet(ModelViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        cart = CartModel.objects.all()
        return cart
    def get_serializer_context(self):
        return {
            'request': self.request
        }
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    @require_POST
    def cart_add(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        # return redirect('cart:cart_detail')
        return Response(status=status.HTTP_200_OK, data={'cart_details': cart})

    def cart_remove(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        # return redirect('cart:cart_detail')
        return Response(status=status.HTTP_200_OK, data={'cart_details': cart})

    def cart_detail(request):
        cart = Cart(request)
        # return render(request, 'cart/detail.html', {'cart': cart})
        return Response(status=status.HTTP_200_OK, data={'cart': cart})
