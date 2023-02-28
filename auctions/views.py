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

from .models import User, AuctionListing, Watchlist
from .forms import ListingForm

def index(request):
    # need to pass in context for active listings
    return render(request, "auctions/index.html",{
        "listings": AuctionListing.objects.all()
    })


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

# https://docs.djangoproject.com/en/4.0/topics/auth/default/#the-login-required-decorator
@login_required
def create_listing(request):
    
    if request.method == "POST":
        # we submitted our new listing, need to do something here
        # perhaps use the AuctionListing model we created
        # pretty sure we have to save it to the database somehow
        # trying to check notes minimally

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

    auction_listing = AuctionListing.objects.get(id=auction_id)
    is_signedin = request.user.is_authenticated
    is_watching = True

    if is_signedin:

        user_object = User.objects.get(id=request.user.id)
        # Check if record already exists.
        # If it does, update current record.
        # Else make a new record.
        try:
            watchlist_item = Watchlist.objects.get(user=user_object, item=auction_listing)
            
            if request.method == "POST":
                # if watchlist item exists, then we're taking off watchlist
                is_watching = False

        except ObjectDoesNotExist:
            
            if request.method == "POST":
                watchlist_item = Watchlist(user=user_object, item=auction_listing)
            else:
                is_watching = False

    if request.method == "POST":        
        
        # new bid submitted
        # https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it
        new_bid = request.POST.get('new_bid', False)

        if new_bid is not False:

            current_bid = auction_listing.starting_bid
            new_bid = float(request.POST["new_bid"])    
            
            if new_bid > current_bid:

                auction_listing.starting_bid = new_bid
                # only updating one field, recommended for performance improvements
                # could also use listing.save()
                # https://docs.djangoproject.com/en/dev/ref/models/instances/#specifying-which-fields-to-save
                auction_listing.save(update_fields=["starting_bid"])
            
                return render(request, "auctions/listing_page.html",{
                    "is_watching": is_watching,
                    "signed_in": is_signedin,
                    "listing": auction_listing
                })

            else:

                return render(request, "auctions/listing_page.html",{
                    "message": "Bid amount is not greater than current bid!",
                    "is_watching": is_watching,
                    "signed_in": is_signedin,
                    "listing": auction_listing
                })

        # user added item to watchlist
        else:

            if is_watching:
                watchlist_item.save()
            else:    
                watchlist_item.delete()

            return render(request, "auctions/listing_page.html",{
                "is_watching": is_watching,
                "signed_in": is_signedin,
                "listing": auction_listing
            })

    # can either be a user, or not a user. Watchlist button dependent on user being logged in
    return render(request, "auctions/listing_page.html",{
        "listing": auction_listing,
        "is_watching": is_watching,
        "signed_in": is_signedin
    })

def watchlist(request, auction_id):

    auction_listing = AuctionListing.objects.get(id=auction_id)
    user_object = User.objects.get(id=request.user.id)
    is_watching = True

    # Check if record already exists.
    # If it does, update current record.
    # Else make a new record.
    try:
        watchlist_item = Watchlist.objects.get(user=user_object, item=auction_listing)
        
        if request.method == "POST":
            # if watchlist item exists, then we're taking off watchlist
            is_watching = False

    except ObjectDoesNotExist:
        
        if request.method == "POST":
            watchlist_item = Watchlist(user=user_object, item=auction_listing)
        else:
            is_watching = False

    # return HttpResponseRedirect(reverse("listing_page"))
    return redirect('listing_page', auction_id=auction_id)


def new_bid(request, auction_id, bid_amount):

    auction_listing = AuctionListing.objects.get(id=auction_id)
    current_bid = auction_listing.starting_bid
    new_bid = float(request.POST["new_bid"])    
    
    if new_bid > current_bid:

        auction_listing.starting_bid = new_bid
        # only updating one field, recommended for performance improvements
        # could also use listing.save()
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#specifying-which-fields-to-save
        auction_listing.save(update_fields=["starting_bid"])
        
    
