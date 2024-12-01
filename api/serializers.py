from .models import Rating, Meal
from rest_framework import serializers





class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        # fiels = ('id', '  title', 'description')
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        # fiels = ('id', 'user', 'meal', 'stars')