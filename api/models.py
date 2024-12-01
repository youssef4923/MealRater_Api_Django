from django.db import models
from django.db.models import Index
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.




class Meal(models.Model):
    title = models.CharField(max_length=32, default=True)
    description = models.TextField(max_length=360, default=True)

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