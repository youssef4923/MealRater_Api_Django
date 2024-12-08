from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import MealViewSet, RaingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('users', UserViewSet)
router.register('ratings', RaingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
