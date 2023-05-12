# Generated by Django 4.1.3 on 2023-05-10 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0011_auctionlisting_is_open"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="auctions.comment",
            ),
        ),
    ]