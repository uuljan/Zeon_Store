from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='Product')
router.register('collection', CollectionView, basename='Collection')
router.register('favorite', FavoriteView, basename='Favorite')



urlpatterns = [
    path('', include(router.urls)),
    # path('favorite/', FavoriteView.as_view())
]