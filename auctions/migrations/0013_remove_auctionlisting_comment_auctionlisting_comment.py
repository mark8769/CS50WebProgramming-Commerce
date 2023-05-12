# Generated by Django 4.1.3 on 2023-05-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0012_auctionlisting_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="comment",
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="comment",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="comments", to="auctions.comment"
            ),
        ),
    ]