# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms
# possible fiels for models
# here is more general information about fields and more
# https://docs.djangoproject.com/en/4.0/ref/models/fields/
# Here is an anchor tag link to all the fiels available to use (REALLY USEFUL)
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

'''
Thing to remember, Django gives each model an
auto-incrementing primary key, so do not have to define ourselves.

https://docs.djangoproject.com/en/4.0/topics/db/models/#automatic-primary-key-fields

So to refer to it, we would use it as a ForeignKey if that makes sense
'''

# https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices
class Categories(models.TextChoices):
    CLOTHING = "Clothing", _('Clothing')
    SHOES = "Shoes", _('Shoes')
    VEHICLES = "Vehicle", _('Vehicle')
    ACCESORIES = "Accesories", _('Accesories')
    WATCHES = "Watches", _('Watches')
    SPORTS = "Sports", _("Sports")
    HOME = "Home", _("Home")
    TOYS = "Toys", _("Toys")
    BUSINESS = "Business", _("Business")
    COSMETICS = "Health & Beauty", _("Health & Beauty")
    PETS = "Pets", _("Pets")
    OTHER = "Other", _("Other")

    def get_categories():
        return ["Clothing", "Shoes", "Vehicle",
                "Watches", "Sports", "Home", "Toys",
                "Business", "Health & Beauty", "Pets", "Other"]

class User(AbstractUser):

    # It is recommended to use Abstract User even if User class
    # is enough, because it is more customizable.
    # Can add additional fields here. (We inherit all fiels from default User class)
    # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/


    def __str__(self):
        # id is autoincremented, and it is suggested not to add the field yourself
        return f"User: {self.username} Id: {self.id}"
    
class AuctionListing(models.Model):

    # pull some ideas 'create listing' specification
    # to create a listing, user should be able to specify
    # title
    # description
    # starting bid price
    # url to picture/image (not required for user)
    # category (not required for user)

    # When user is deleted
    # delete all Auction Listings associated with user
    category = models.CharField(
        max_length=16,
        choices=Categories.choices,
        default=Categories.OTHER,
    )
    # https://stackoverflow.com/questions/41595364/fields-e304-reverse-accessor-clashes-in-django
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="creator")
    # Would run into issues if we allowed user to remove bid, but good for now.
    highest_bidder_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder",null=True, blank=True)
    auction_title = models.CharField(max_length=64)
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2)
    auction_description = models.TextField()
    # https://sentry.io/answers/django-difference-between-null-and-blank/#:~:text=By%20default%20all%20fields%20are,that%20pub_time%20can%20be%20empty.
    image_url = models.URLField(max_length=255, blank=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        user = f"User: {self.user.username}\n"
        title = f"Title: {self.auction_title}\n"
        start_bid = f"Start Bid: {self.starting_bid}\n"
        desc = f"Description: {self.auction_description}\n"
        if len(self.image_url) == 0:
            url = "N/A\n"
        else:
            url = f"Url: {self.image_url}\n"

        if len(self.category) == 0:
            category = "N/A\n"
        else:
            category = f"Category: {self.category}\n"

        return user + title + start_bid + desc + url + category

class Comment(models.Model):
    # comment is placed by logged-in user
    # have user_id associated with comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # have comment field
    comment = models.TextField()
    # https://cs50.harvard.edu/web/2020/notes/4/ (for some examples of how to implement models)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments", blank=True, null=True)
    
    def __str__(self):
        user = f"User: {self.user}\n"
        comment = f"User Comment: {self.comment}\n"
        return user + comment

class Bid(models.Model):
    # bid is places by logged-in user
    # need user_id to associate with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # have item key to associate bid
    auction_id = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    # need a bid_price as float
    # DecimalField has two required arguments
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        user = f"User: {self.user}\n"
        auction_id = f"Auction ID: {self.auction_id}\n"
        bid_price = f"Bid Price: {self.bid_price}\n"
        return user + auction_id + bid_price

class Watchlist(models.Model):
    # if user is ever deleted, delete any associated watchlists rows
    # given a User, gives us a way to look at any watchlist item associated with our user (related name)
    # This lets us retrieve all the users with a specific item as their watchlist
    # we want the opposite effect.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_items")
    # if Auction Listing item is removed, delete from watchlist
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        user = f"Username: {self.user.username}\n"
        item = f"Item: {self.item.auction_title}\n"
        return user + item

