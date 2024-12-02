from django.db import models
from django.db.models import Index
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.




class Meal(models.Model):
    title = models.CharField(max_length=32, default=True)
    description = models.TextField(max_length=360, default=True)
    
    def num_of_ratings(self):
        rating = Rating.objects.filter(meal=self)
        return len(rating)
    
    #  def num_of_ratings(self):
        # return Rating.objects.filter(meal=self).count()
    
    
    def avg_rating(self):
        rating = Rating.objects.filter(meal=self)
        
        summ = 0
        if len(rating) == 0:
            return 0
        
        for x in rating:
            summ += x.stars
            
        return summ / len(rating)
    
    
    # def avg_rating(self):
    #     ratings = Rating.objects.filter(meal=self)
    #     return sum(r.rating for r in ratings) / len(ratings) if ratings.exists() else 0
    

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = (('user', 'meal'),)
        indexes = [
            Index(fields=['user', 'meal']),
        ]