from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(watchlist)
admin.site.register(bidding)
admin.site.register(product_won)
admin.site.register(product_comments)