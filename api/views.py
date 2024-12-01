from django.shortcuts import render
from .serializers import RatingSerializer, MealSerializer
from .models import Rating, Meal
from rest_framework import viewsets

# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    
    
class RaingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer