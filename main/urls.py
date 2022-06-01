from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('bestseller', BestsellerView, basename='Bestseller')
router.register('slider', SliderView, basename='Slider')
router.register('noveltie', NoveltieView, basename='Noveltie')
router.register('collection', CollectionView, basename='Collection')
router.register('advantage', AdvantageView, basename='Advantage')

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]