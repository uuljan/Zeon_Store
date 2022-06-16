from django.urls import path, include
from rest_framework import routers

from cart.views import CartView, CartInfoView, CartItemView

router = routers.DefaultRouter()
router.register('cart', CartView, basename='Cart')
router.register('cart_item', CartItemView, basename='CartItem')
router.register('cart_info', CartInfoView, basename='CartInfo')

urlpatterns = [
    path('', include(router.urls)),

]