# Troubles with this assignment

- hard to visualize the models layout
    1. I am not completely sure if I can just pass in the models.User fields
        as keyword arguments, or if it would fail to instantiate a User Object.
        It says I have access, but do I really? (I know it's inheritance, but I hate the impliceteness of it)
    
    2. Other than that, how should I connect my models? A user can have listing, comments, and bids on items.

    3. An AuctionListing has a title, description, image url, category, and now comments too?

    4. The requiremens stated there should be a model for comments, so maintain separate from AuctionListing class we created

    5. Ok, now that we can see user id's, we can better visualize the connection between things.


# I need a user as my foreign key to auction listings, bids, and commments

- One issue I was having, was Django admin stopped working
- I think its because I did not apply any of the migrations, so that's why I wasn't even able to view an empty page.
- I applied migrations, and the tables were empty as expected, since I haven't simulated a user creating comments, and listings
- Get a user, such as the superuser that I created.
- Once you have the user object gotten by u = User.objects.all() (gives you back list of users QuerySet), use u = u.first() to get the only user lol
- Pass in the User Object to auction Listing, and any required parameters I have (maybe I should add this requirement in the HTML)
- example: a = AuctionListing(user=u, auction_title="User 3 title", auction_description="User 3 attempt to describe some item", starting_bid=12.22)
- a.save()
- See if it works in the django admin page
- Ok it works, auction listings are updating in Django, now implement functionality in Views
- Need a user, to be able to create a listing