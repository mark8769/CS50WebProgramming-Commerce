# Generated by Django 3.2.16 on 2022-12-31 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20221230_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='auction_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='auction_title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Vehicle', 'Vehicle'), ('Accesories', 'Accesories'), ('Watches', 'Watches'), ('Sports', 'Sports'), ('Home', 'Home'), ('Toys', 'Toys'), ('Business', 'Business'), ('Health & Beauty', 'Health & Beauty'), ('Pets', 'Pets'), ('Other', 'Other')], default='Other', max_length=16),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='image_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
