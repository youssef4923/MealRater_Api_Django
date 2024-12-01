from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import MealViewSet, RaingViewSet

router = routers.DefaultRouter()
router.register('meal', MealViewSet)
router.register('ratings', RaingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
