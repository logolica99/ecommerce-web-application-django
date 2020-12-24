from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=150)
    starting_bid = models.IntegerField()
    image_link = models.CharField(max_length=400)
    Category = (('Fashion', 'Fashion'),('Toys','Toys'),('Electronics','Electronics'),('Home','Home'),('Health', 'Health'),('Sports','Sports'))
    category = models.CharField(max_length=200,null=True, choices=Category)
    def __str__(self):
        return f"{self.title}"
    
class watchlist(models.Model):
    item = models.ForeignKey(Listing,on_delete=models.CASCADE,unique=True,related_name="watchlist" )
    def __str__(self):
        return f"{self.item}"