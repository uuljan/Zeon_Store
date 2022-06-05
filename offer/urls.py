from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('offer', OfferView, basename='Offer')



urlpatterns = [
    path('', include(router.urls)),

]