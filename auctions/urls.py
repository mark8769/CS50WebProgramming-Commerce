from django.urls import path

from . import views as view_routes

urlpatterns = [
    path("", view_routes.index, name="index"),
    path("login", view_routes.login_view, name="login"),
    path("logout", view_routes.logout_view, name="logout"),
    path("register", view_routes.register, name="register"),
    path("create_listing", view_routes.create_listing, name="create_listing"),
    # if were going to look at a certain listing, we need to at least know the listing id
    # can't remember syntax, so fine to look at notes
    path("listing_page/<int:auction_id>", view_routes.listing_page, name="listing_page"),
    path("listing_page/<int:auction_id>/add_watchlist", view_routes.add_watchlist, name="add_watchlist"),
    path('listing_page/<int:auction_id>/new_bid', view_routes.new_bid, name="new_bid"),
    # Consider removeing listing_page/ from other url paths if not needed, I did for bottom two.
    path("watchlist", view_routes.watchlist, name="watchlist"),
    path("categories", view_routes.categories, name="categories"),
    path("categories/<str:category>", view_routes.category, name="category"),
    path("cancel/<int:auction_id>", view_routes.cancel, name="cancel"),
    path("comment/<int:auction_id>", view_routes.comment, name="comment")
    # path("listing_page/<int:auction_id>/comment", view_routes.listing_page_comment, name="listing_page_comment")
]
