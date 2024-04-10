from django.db import models
from users.models import User
from restaurants.models import *
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)
    
class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField()

