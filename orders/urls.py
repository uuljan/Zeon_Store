from django.urls import path, include
from rest_framework import routers
from .views import OrderView

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('orders', OrderView, basename='Order')

urlpatterns = [
    path('', include(router.urls)),

]