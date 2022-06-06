from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('offer', OfferView, basename='Offer')
router.register('about', AboutView, basename='AboutUs')
router.register('news', NewsView, basename='News')
router.register('questions', QuestionView, basename='questions')

urlpatterns = [
    path('', include(router.urls)),

]
