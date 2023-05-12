# https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
# https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell
from auctions.models import User, AuctionListing,Watchlist, Bid, Categories, Comment

def create_users():
    one = User.objects.create_user(username="Mark1231", email="noreply@gmail.com", password="1")
    two = User.objects.create_user(username="JoeTheMan", email="noreply@gmail.com", password="1")
    three = User.objects.create_user(username="ShoeSeller", email="noreply@gmail.com", password="1")
    four = User.objects.create_user(username="GardenDepot", email="noreply@gmail.com", password="1")
    five = User.objects.create_user(username="flowerSeller", email="noreply@gmail.com", password="1")
    six = User.objects.create_user(username="FriendlyNeighborhoodReseller", email="noreply@gmail.com", password="1")
    one.save()
    two.save()
    three.save()
    four.save()
    five.save()
    six.save()
    print("Done creating users.")

def create_listings():
    user_one = User.objects.get(username="Mark1231")
    user_two = User.objects.get(username="JoeTheMan")
    user_three = User.objects.get(username="ShoeSeller")
    user_four = User.objects.get(username="GardenDepot")
    user_five = User.objects.get(username="flowerSeller")
    user_six = User.objects.get(username="FriendlyNeighborhoodReseller")


    one_list = AuctionListing(user=user_one,
                              auction_title="Yeezy 350 Beluga",
                              starting_bid=1000,
                              auction_description="The adidas Yeezy Boost 350 V2 Beluga Reflective builds off of the original Beluga colorway by adding reflective qualities and speckled orange accents to its Primeknit upper. Signature details like a Boost sole and orange side stripe complete it.",
                              image_url="https://hypebeast.com/image/2021/11/adidas-yeezy-boost-350-v2-beluga-reflective-release-date-info-001.jpg",
                              category="Shoes")
    one_list.save()

    two_list = AuctionListing(user=user_two,
                              auction_title="Yeezy 350 Pirate",
                              starting_bid=1200,
                              auction_description="Some would say the adidas Yeezy Boost 350 in 'Pirate Black' is the most popular colorway of the most preferred silhouette from Kanye West's collaboration with adidas. Released on August 22, 2015.",
                              image_url="https://sneakernews.com/wp-content/uploads/2022/08/adidas-yeezy-boost-350-pirate-black-bb5350-0.jpg",
                              category="Shoes")
    two_list.save()

    three_list = AuctionListing(user=user_three,
                                auction_title="Yeezy 350 Zebra",
                                starting_bid=1100,
                                auction_description="Debuted in 2017, the adidas Yeezy Boost 350 V2 Zebra is known as one of the most renowned colorways in the Yeezy line. It features a white and black marbled Primeknit upper with a white side-stripe and red 'SPLY-350' text.",
                                image_url="https://sneakernews.com/wp-content/uploads/2022/04/zebra-yeezys-release-date-2.jpg",
                                category="Shoes")
    three_list.save()

    four_list = AuctionListing(user=user_four,
                   auction_title="Yeezy 350 Turtle Dove",
                   starting_bid=1500,
                   auction_description="Released in 2015, the adidas Yeezy Boost 350 Turtle Dove is the first colorway to kick off Yeezy's expansive 350 line. Composed of a grey and brown patterned Primeknit, the design was one of the most comfort focus Yeezys.",
                   image_url="https://sneakernews.com/wp-content/uploads/2016/02/yeezy-boost-50-turtle-dove-2016-release.jpg",
                   category="Shoes")
    four_list.save()

    five_list = AuctionListing(user=user_five,
                auction_title="Yeezy 350 Blue Tint",
                starting_bid=350,
                auction_description="In a similar pattern to the renowned adidas Yeezy Boost 350 V2 Zebra, the adidas Yeezy Boost 350 V2 Blue Tint features a marbled grey Primeknit upper with a light grey side stripe that is decorated with bright red SPLY-350 text.",
                image_url="https://sneakernews.com/wp-content/uploads/2022/01/adidas-yeezy-boost-350-v2-blue-tint-B37571-2022-release-date-0.jpg",
                category="Shoes")
    five_list.save()

    six_list = AuctionListing(user=user_six,
                auction_title="Bearbrick x CLOT Panda 1000%",
                starting_bid=300,
                auction_description="Following the release of its 'Summer Fruits' BE@RBRICKs last year, CLOT reconnects with Medicom Toy this season for new Panda-inspired figures based off of the brands mascot, Ning Ning. ",
                image_url="https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2022%2F11%2Fclot-medicom-toy-bearbrick-panda-figure-info-001.jpg?q=70&w=1125&cbr=1&fit=max",
                category="Toys")
    six_list.save()

    # have something for watches, home, vehicles, accessories, business, cosmetics, pets, other
    one_2_list = AuctionListing(user=user_one,
                auction_title="Supreme TOYO Steel T-320 Toolbox",
                starting_bid=120,
                auction_description="The Supreme TOYO Steel T 320 Toolbox Red is a classic red steel toolbox that features the Supreme branding embossed at the top. This Steel T 320 Toolbox by Supreme is made in Japan in collaboration with TOYO.",
                image_url="https://www.supremecommunity.com/u/season/fall-winter2022/accessories/7eebc15372e543d1a7e1ef0ebe88428b_sqr.jpg",
                category="Home")
    one_2_list.save()

    two_2_list = AuctionListing(user=user_two,
                auction_title="Supreme Clay Brick",
                starting_bid=300,
                auction_description="The Supreme brick has gone semi-viral and elicited a mixture of reactions memes, sniggers, eye-rolls, lust and derision are merely a few of them. A slab of red moulded clay might seem an odd item for a fashion brand to sell",
                image_url="https://www.highsnobiety.com/static-assets/thumbor/i19CiOdg1nWNFF9C1VtqXhGdalE=/1600x1067/www.highsnobiety.com/static-assets/wp-content/uploads/2016/08/17122514/supreme-brick-1.jpg",
                category="Accesories")
    two_2_list.save()

    three_2_list = AuctionListing(user=user_three,
                auction_title="Hot Wheels x Tesla Cybertruck",
                starting_bid=110,
                auction_description="The Hot Wheels x Tesla Cybertruck 1:10 Scale R/C Car 2021 Version with Cyberquad is the third time Mattel and Elon Musks electric vehicle and clean energy company have collaborated on an R/C version of the Cybertruck by Tesla.",
                image_url="https://media.techeblog.com/images/mattel-hot-wheels-1-10-rc-tesla-cybertruck-cyberquad.jpg",
                category="Vehicle")
    three_2_list.save()

    four_2_list = AuctionListing(user=user_four,
                auction_title="Funko Pop! Games Pokemon Charizard 10-Inch Target Exclusive Figure #851",
                starting_bid=80,
                auction_description="Funko Pop! teamed up with Target to release a limited edition jumbo sized 10inch Charizard Pokémon figure. Charizard was originally introduced in 1996, during the release of the Pokémon Red and Blue Video Game series.",
                image_url="https://funkypriceguide.com/media/collectibles/funko-pop-851-charizard_001_large_aa.jpg",
                category="Pets")
    four_2_list.save()

    five_2_list = AuctionListing(user=user_five,
                auction_title="Rolex Submariner Date",
                starting_bid=10000,
                auction_description="The Oyster Perpetual Submariner Date in Oystersteel with a Cerachrom bezel insert in black ceramic and a black dial with large luminescent hour markers.",
                image_url="https://timeandtidewatches.com/wp-content/uploads/2021/03/Rolex-03.jpg.webp",
                category="Watches")
    five_2_list.save()

    six_2_list = AuctionListing(user=user_six,
                auction_title="Supreme Rawlings Baseball Bat",
                starting_bid=250,
                auction_description="The Supreme Rawlings Baseball Bat was the primary accessory released as a part of Week 2 and includes custom laser engraved and filled logos. This Supreme bat is made from a chromed maple wood and its length is 34 inches.",
                image_url="https://www.supremecommunity.com/u/season/spring-summer2021/accessories/d0854083e62648698657bc2482eb00d0_sqr.jpg",
                category="Sports")
    six_2_list.save()

    any_one = AuctionListing(user=user_one,
                auction_title="Off-White Make Up Pouch",
                starting_bid=150,
                auction_description="Off-White make up pouch.",
                image_url="https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fwp-content%2Fblogs.dir%2F6%2Ffiles%2F2019%2F08%2Foff-white-makeup-pouch-black-travel-bag-001.jpg?q=70&w=750&cbr=1&fit=max",
                category="Health & Beauty")
    any_one.save()

    any_two = AuctionListing(user=user_two,
                auction_title="Goyard Business Card Holder",
                starting_bid=550,
                auction_description="Goyard's Cardholder wallet, a minimalist wallet that is one of the most popular choices in their collection. The wallet itself is fairly standard in design.",
                image_url="https://www.allthewallets.com/wp-content/uploads/2020/10/Goyard-Wallet.jpg",
                category="Business")
    any_two.save()

    any_three = AuctionListing(user=user_three,
                auction_title="Supreme Brooklyn Box Logo Tee",
                starting_bid=300,
                auction_description="The Supreme Brooklyn Box Logo Tee White is a short-sleeve T-shirt that comes in a white base fabric material and features the box logo in a black and yellow camo pattern while the phone number of the shop is emblazoned at the back.",
                image_url="https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2017%2F10%2Fsupreme-brooklyn-box-logo-1.jpg?q=70&w=750&cbr=1&fit=max",
                category="Clothes")
    any_three.save()

    # Highlight. Then Option + Shift + down
    # AuctionListing(user=,
    #             auction_title=,
    #             starting_bid=,
    #             auction_description=,
    #             image_url=,
    #             category=)

def main():
    #create_users()
    #create_listings()
    


if __name__ == "__main__":
    main()