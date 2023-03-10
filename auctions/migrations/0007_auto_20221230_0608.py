# Generated by Django 3.2.16 on 2022-12-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auctionlisting_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='auction_description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='auction_title',
            field=models.CharField(max_length=64, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Starting Bid'),
        ),
    ]
