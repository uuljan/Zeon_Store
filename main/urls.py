from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('bestseller', BestsellerView, basename='Bestseller')
router.register('slider', SliderView, basename='Slider')

urlpatterns = [
    path('', include(router.urls)),
]