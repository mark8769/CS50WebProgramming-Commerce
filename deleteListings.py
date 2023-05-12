# https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
# https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell
from auctions.models import User, AuctionListing,Watchlist, Bid, Categories, Comment

def main():
    auctions = AuctionListing.objects.all()
    auctions.delete()

if __name__ == "__main__":
    main()