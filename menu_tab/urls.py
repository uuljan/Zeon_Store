from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('offer', OfferView, basename='Offer')
router.register('about', AboutView, basename='AboutUs')
router.register('news', NewsView, basename='News')
router.register('help', ImageQuestionView, basename='Questions')
router.register('footer_one', FooterOneView, basename='Footer1')
router.register('footer_two', FooterTwoView, basename='Footer2')

urlpatterns = [
    path('', include(router.urls)),

]
