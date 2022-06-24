from django.urls import path, include
from rest_framework import routers

from cart.views import CartInfoView, CartView

router = routers.DefaultRouter()
router.register('cart', CartView, basename='CartItem')
router.register('cart_info', CartInfoView, basename='CartInfo')

urlpatterns = [
    path('', include(router.urls)),

]