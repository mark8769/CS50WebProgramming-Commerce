# Generated by Django 4.1.3 on 2023-05-10 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0010_alter_auctionlisting_highest_bidder_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="is_open",
            field=models.BooleanField(default=True),
        ),
    ]