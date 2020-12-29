from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from.forms import *



def index(request):
    context = {"listing":Listing.objects.all()}
    return render(request, "auctions/index.html",context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def Categories(request):
    context={}
    return render(request, "auctions/categories.html" ,context)
def Watchlist(request):
 
    
    context ={"watchlists": watchlist.objects.filter(user=request.user.id)}
    return render(request,"auctions/watchlist.html",context)
def create_listing(request):
    
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    
    return render(request,"auctions/create_listing.html",{
        'form':form
    })
def listing_page(request,list_id):
    product = Listing.objects.get(id=list_id)
    form = ListingForm(instance=product)
    
    if len(watchlist.objects.filter(item_id=list_id,user=request.user.id))==1:
   
        blob=True
        if request.method=="POST" and  'watchlist' in request.POST:
            item = watchlist.objects.filter(item_id=list_id)
            item.delete()
            return HttpResponseRedirect(reverse("listing_page",args=(list_id,)))
    else:
        blob=False
        if request.method=="POST" and 'watchlist' in request.POST:
            b = watchlist(item = Listing.objects.get(pk=list_id),user=User.objects.get(pk=request.user.id))
            b.save()

            return HttpResponseRedirect(reverse("listing_page",args=(list_id,)))

    
    error=""
    if request.method=="POST" and  'watchlist' not in request.POST:
        
        
        if int(request.POST['starting_bid']) <= Listing.objects.get(id=list_id).starting_bid:
            error="NOT enough money"
          
            
        else:
            product.starting_bid = request.POST['starting_bid']
            user = User.objects.get(id=request.user.id)
            hello=bidding.objects.create(listing=product,bid=request.POST['starting_bid'])
            hello.bidded_user.add(user)
            hello.save()
            product.save()
            return HttpResponseRedirect(reverse("listing_page",args=(list_id,)))
    

                
        
  
    if request.user.id == Listing.objects.get(id=list_id).user.id:
        owner=True
    else:
        owner=False
    return render(request,"auctions/listing_page.html",{
        "list":Listing.objects.get(pk=list_id),
        "in_watchlist":blob,
        "form": form,
        'owner':owner,
        "error":error
     
    })

def specific_category(request, category):
    context={"items":Listing.objects.filter(category=category)}
    return render(request,"auctions/category.html",context)