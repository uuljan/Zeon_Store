from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('bestseller', BestsellerView, basename='Bestseller')
router.register('slider', SliderView, basename='Slider')
router.register('novelty', NoveltyView, basename='Novelty')

router.register('advantage', AdvantageView, basename='Advantage')

urlpatterns = [
    path('', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]