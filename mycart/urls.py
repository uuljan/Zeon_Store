from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('cart', CartViewSet, basename='Cart')

urlpatterns = [
    path('', include(router.urls)),

]
