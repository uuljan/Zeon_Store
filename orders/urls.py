from django.urls import path, include
from rest_framework import routers
from .views import OrderView, OrderInfoView

router = routers.DefaultRouter()
router.register('orders', OrderView, basename='Order')
router.register('order_info', OrderInfoView, basename='OrderInfo')

urlpatterns = [
    path('', include(router.urls)),

]