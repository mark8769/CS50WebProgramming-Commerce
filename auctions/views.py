from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# https://docs.djangoproject.com/en/4.1/ref/exceptions/#django.core.exceptions.ObjectDoesNotExist
# https://docs.djangoproject.com/en/4.1/ref/models/class/#django.db.models.Model.DoesNotExist
from django.core.exceptions import ObjectDoesNotExist
# making querys for django SQL statements
# https://docs.djangoproject.com/en/4.1/topics/db/queries/

from .models import User, AuctionListing, Watchlist, Bid
from .forms import ListingForm

def index(request):
    '''
    Route to serve homepage of 
    website, displays all available 
    listings on ecommerce site.
    '''
    return render(request, "auctions/index.html",{
        "listings": AuctionListing.objects.all()
    })

def login_view(request):
    '''
    Route to serve login page, 
    or accept login information if already on page.
    '''
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
    '''
    Route to handle logout request. 
    Returns user to index page.    
    '''
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    '''
    Route to handle register request. 
    '''
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

# https://docs.djangoproject.com/en/4.0/topics/auth/default/#the-login-required-decorator
@login_required
def create_listing(request):
    '''
    Route to handle the create listing nav link.
    '''
    if request.method == "POST":
        # we can access our request arguments
        # through
        # post["title"]
        # post["description"]
        # post["starting_bid"]
        # post["url"]

        # create our AuctionListing object
        # then save? AuctionListing.save()
        # we should check that listing does not exist either
        # we also need a user for our auction listing
        # I think I saw this on stack overflow during my search,
        # but this one is off the top of the head remembering

        # form = ListingForm(request.POST)
        # should be doing if form.is_valid() for error checking, doesnt seem to be useful here though.

        user_id = request.user.id
        user = User.objects.get(id=user_id)
        title = request.POST["auction_title"]
        desc = request.POST["auction_description"]
        bid = float(request.POST["starting_bid"])
        url = request.POST["image_url"]
        category = request.POST["category"]

        user_listing = AuctionListing(user=user,
                                    auction_title=title,
                                    starting_bid=bid,
                                    auction_description=desc,
                                    image_url=url,
                                    category=category
        )
        # pass in a message that listing title is taken
        # https://forum.djangoproject.com/t/userpreference-matching-query-does-not-exist/6845
        # Django will return does not exist if objects.get does not exist

        try:
            AuctionListing.objects.get(auction_title=title)
        
        # if title does not exist, catch the error
        # save title, and redirect to index since we haven't implemented Listings yet
        except ObjectDoesNotExist:
            user_listing.save()
            # pass in a view name to go to, django will handle finding the base url
            # return HttpResponseRedirect(reverse("index"))
            return render(request, "auctions/index.html",{
                "created_listing": True,
                # we should be letting the index view handle this
                # but how can we pass context using HttpResponseRedirect? Doesn't seem possible.
                "listings": AuctionListing.objects.all()
            })
        
        return render(request, "auctions/create_listing.html",{
            "message": "Sorry title already taken, pick another one.",
            "form": ListingForm()
        })

    else:
        # this is basically done, have form how I want it
        return render(request, "auctions/create_listing.html",{
            "form": ListingForm()
        })

def listing_page(request, auction_id):
    '''
    GET route that returns listing page 
    of an auction listing that has been clicked.
    '''
    # Get auction listing.
    auction_listing = AuctionListing.objects.get(id=auction_id)
    is_signedin = request.user.is_authenticated
    is_watching = None

    if is_signedin:
        # Get current signed in user.
        user_object = User.objects.get(id=request.user.id)
        try:
            watchlist_item = Watchlist.objects.get(user=user_object, item=auction_listing)
            is_watching = True
        # If watchlist item does not exist.
        except ObjectDoesNotExist:
            is_watching = False

    return render(request, "auctions/listing_page.html",{
        "is_watching": is_watching,
        "signed_in": is_signedin,
        "listing": auction_listing
    })

def watchlist(request, auction_id):
    '''
    POST route to handle user adding a listing
    to their watchlist.
    '''
    auction_listing = AuctionListing.objects.get(id=auction_id)
    user_object = User.objects.get(id=request.user.id)

    try:
        # If item already on watchlist then delete.
        watchlist_item = Watchlist.objects.get(user=user_object, item=auction_listing)
        watchlist_item.delete()

    except ObjectDoesNotExist:
        # If item not on watchlist then save.
        watchlist_item = Watchlist(user=user_object, item=auction_listing)
        watchlist_item.save()

    # return HttpResponseRedirect(reverse("listing_page"))
    return redirect('listing_page', auction_id=auction_id)


# TODO: Attach a bid to a user. 5/8/23
def new_bid(request, auction_id):
    '''
    POST route to handle a user adding
    a new on an auction listing.
    '''
    new_bid = float(request.POST["new_bid"])
    auction_listing = AuctionListing.objects.get(id=auction_id)
    current_bid = auction_listing.starting_bid
    current_user = User.objects.get(id=request.user.id)
    is_signedin = request.user.is_authenticated

    if new_bid > current_bid:
        # only updating one field, recommended for performance improvements
        # could also use listing.save()
        auction_listing.starting_bid = new_bid
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#specifying-which-fields-to-save
        auction_listing.save(update_fields=["starting_bid"])
        # check if bid on item already exists
        user_bid_on_item = Bid(user=current_user,
                            auction_id=auction_listing,
                            bid_price=new_bid)
        user_bid_on_item.save()

    return render(request, "auctions/listing_page.html",{
        "signed_in": is_signedin,
        "listing": auction_listing
    })


        
    
