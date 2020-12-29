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
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Products")
    active=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"
    
class watchlist(models.Model):
    item = models.ForeignKey(Listing,on_delete=models.CASCADE,unique=True,related_name="watchlist" )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="watchlists" ,default="0")
    def __str__(self):
        return f"{self.item}"

class bidding(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,unique=True,related_name="bidding")
    bidded_user = models.ManyToManyField(User,blank=True,related_name='bidding')
    bid=models.IntegerField(default=0)

    def __str__(self):
         return f"{self.bidded_user.first().username} bid {self.bid}"

