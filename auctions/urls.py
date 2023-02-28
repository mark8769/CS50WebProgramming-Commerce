from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    # if were going to look at a certain listing, we need to at least know the listing id
    # can't remember syntax, so fine to look at notes
    path("listing_page/<int:auction_id>", views.listing_page, name="listing_page"),
    path("listing_page/<int:auction_id>/watchlist", views.watchlist, name="watchlist"),
    path('listing_page/<int:auction_id>/new_bid', views.new_bid, name="new_bid")
    # path("listing_page/<int:auction_id>/comment", views.listing_page_comment, name="listing_page_comment")
]
