from .models import Rating, Meal
from rest_framework import serializers





class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description', 'num_of_ratings', 'avg_rating')
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'meal', 'stars')